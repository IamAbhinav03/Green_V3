from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from pathlib import Path
from .forms import PredictionForm
import os
from pathlib import Path
import torch
import torchvision.models as models
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
import base64
from PIL import Image
from pathlib import Path

# classes = ['paper', 'metal', 'cardboard', 'organic', 'glass', 'plastic']
classes = ['cardboard', 'glass', 'metal', 'organic', 'paper', 'plastic']
# Function to find accuracy
def accuracy(outputs, labels):
    _, preds = torch.max(outputs, dim=1)
    return torch.tensor(torch.sum(preds == labels).item() / len(preds))

class ImageClassificationBase(nn.Module):
    
    def training_step(self, batch):
        images, labels = batch 
        out = self(images)                  # Generate predictions
        loss = F.cross_entropy(out, labels) # Calculate loss
        return loss
    
    def validation_step(self, batch):
        images, labels = batch 
        out = self(images)                    # Generate predictions
        loss = F.cross_entropy(out, labels)   # Calculate loss
        acc = accuracy(out, labels)           # Calculate accuracy
        return {'val_loss': loss.detach(), 'val_acc': acc}
        
    def validation_epoch_end(self, outputs):
        batch_losses = [x['val_loss'] for x in outputs]
        epoch_loss = torch.stack(batch_losses).mean()   # Combine losses
        batch_accs = [x['val_acc'] for x in outputs]
        epoch_acc = torch.stack(batch_accs).mean()      # Combine accuracies
        return {'val_loss': epoch_loss.item(), 'val_acc': epoch_acc.item()}
    
    def epoch_end(self, epoch, result):
        print("Epoch {}: train_loss: {:.4f}, val_loss: {:.4f}, val_acc: {:.4f}".format(
            epoch+1, result['train_loss'], result['val_loss'], result['val_acc']))

class ResNet(ImageClassificationBase):
	def __init__(self):
		super().__init__()

		# Use a pretrained model
		self.network = models.resnet50(pretrained=True)
		
		# Repace last layer
		num_ftrs = self.network.fc.in_features
		self.network.fc = nn.Linear(num_ftrs, 6)

	def forward(self, xb):
		return torch.sigmoid(self.network(xb))


# PATH = '/Users/abhinav/Dev/Untitled Folder/weight.pt' #mac
# PATH = 'C:/Users/ASUS/Downloads/Project-20210618T214132Z-001/Project/weight.pt'
PATH = Path("static/weight.pt")
device = torch.device('cpu')
model = ResNet()
model.load_state_dict(torch.load(PATH, map_location=device))
model.eval()

#===================================================================================================================================================
# TESTING
#testing model accuracy after loading to check if it's the saved model
# from torch.utils.data.dataloader import DataLoader
# from torchvision.datasets import ImageFolder
# from torch.utils.data import random_split

# data_dir  = '/Users/abhinav/Dev/Untitled Folder/archive/Garbage classification/Garbage classification'
# transformations = transforms.Compose([transforms.Resize((256, 256)), transforms.ToTensor])
# dataset = ImageFolder(data_dir, transform=transformations)
# random_seed = 42
# torch.manual_seed(random_seed)
# train_data, val_data, test_data = random_split(dataset, [1845, 461, 577])

# val_dataLoader = DataLoader(val_data, 32*2, num_workers=4, pin_memory=True)

# def get_default_device():
    
#     """Pick GPU if available, else CPU"""
#     if torch.cuda.is_available():
#         return torch.device('cuda')
#     else:
#         return torch.device('cpu')
    
# def to_device(data, device):
#     """Move tensor(s) to chosen device"""
#     if isinstance(data, (list,tuple)):
#         return [to_device(x, device) for x in data]
#     return data.to(device, non_blocking=True)

# class DeviceDataLoader():
#     """Wrap a dataloader to move data to a device"""
#     def __init__(self, dl, device):
#         self.dl = dl
#         self.device = device
        
#     def __iter__(self):
#         """Yield a batch of data after moving it to device"""
#         for b in self.dl: 
#             yield to_device(b, self.device)

#     def __len__(self):
#         """Number of batches"""
#         return len(self.dl)
		
# val_dl = DeviceDataLoader(val_dataLoader, device)

# def evaluate(model, val_loader):
# 	model.eval()
# 	outputs = [model.validation_step(batch) for batch in val_loader]
# 	return model.validation_epock_end(outputs)

# evaluate(model, val_dl)
#===================================================================================================================================================
# PREDICTION
def predict(file_path):

	image_path = Path(file_path)
	image = Image.open(image_path)

	print("[INFO]: TRANSFORMING...")
	transform = transforms.Compose([transforms.Resize((256, 256)), transforms.ToTensor()])
	image = transform(image)
	
	xb = torch.unsqueeze(image, 0)
	print("[INFO]: GIVEN IMAGE TO MODEL..")
	# try:
	# 	yb = model(xb)
	# 	prob, preds = torch.max(yb, dim=1)
	# 	return classes[preds[0].item()]
	# except:
	# 	return None
	yb = model(xb)
	prob, preds = torch.max(yb, dim=1)
	print(preds)
	return classes[preds[0].item()]

def convert_uri_jpg(uri, filepath):
	decodeit = open(filepath, 'wb')
	decodeit.write(base64.b64decode(uri))
	decodeit.close()

@login_required()
def reuse(request):
	
	if request.method == 'POST':
		form = PredictionForm(request.POST)
		if form.is_valid():
			image_uri = form.cleaned_data['image']
			image_uri = image_uri[23:]
			TARGET_DIR = settings.MEDIA_ROOT
			print(TARGET_DIR)
			n = sum(1 for f in os.listdir(TARGET_DIR) if os.path.isfile(os.path.join(TARGET_DIR, f)))
			print(n)
			file_name = "Test_{}".format(n+1)
			print(file_name)
			file_path = "{}/{}.jpg".format(TARGET_DIR, file_name)
			convert_uri_jpg(image_uri, file_path)
			file_name = '/media/{}.jpg'.format(file_name)
			print(file_name)
			print("[INFO]: PREDICTING...")
			result = predict(file_path)

			if result == 'paper':
				resources = [
				'www.youtube.com/paper', 
				'www.youtube.com/paper', 
				'www.youtube.com/paper', 
				'www.youtube.com/paper']
			elif result == 'metal':
				resources = [
				'www.youtube.com/metal', 
				'www.youtube.com/metal', 
				'www.youtube.com/metal', 
				'www.youtube.com/metal']
			elif result == 'cardboard':
				resources = [
				'www.foxmovingnashville.com/blog/after-you-move/16-clever-ways-repurpose-cardboard-boxes/',
				'www.bobvilla.com/slidewho/17-creative-ways-to-reuse-cardboard-boxes-47420',
				'www.colorado.edu/ecenter/2021/02/09/ways-reuse-cardboard-and-why-it-important',
				'www.youtube.com/watch?v=Rlvd-dIAHCE'
				 ]
			elif result == 'organic':
				resources = [
				'If treated well organic waste is very usefull. You can make compost with and can be used grow more plants in your home. We also collect the compost your made and awards you green coins', 
				'www.conserve-energy-future.com/smart-ways-recycle-food-waste.php', 
				'www.epa.gov/recycle/composting-home', 
				'www.nrdc.org/stories/composting-101c']
			elif result == 'glass':
				resources = [
				'www.youtube.com/glass', 
				'www.youtube.com/glass', 
				'www.youtube.com/glass', 
				'www.youtube.com/glass']
			elif result == 'plastic':
				resources = [
				'www.budgetdumpster.com/blog/diy-plastic-bottles-recycling/', 
				'www.plasticsmakeitpossible.com/plastics-at-home/the-ultimate-guide-to-recycling-reusing-and-repurposing-plastic-items/', 
				'www.thebetterindia.com/207259/how-to-reuse-plastic-bottles-at-home-10-innovative-ideas/', 
				'www.centerforecotechnology.org/plastic-pollution/']
			else:
				resources = [
				'www.youtube.com/test', 
				'www.youtube.com/test', 
				'www.youtube.com/test', 
				'www.youtube.com/test']
			print(resources)
			context = {
				'result': result,
				'resources': resources,
				'image_file_name': file_name,
			}

			return render(request, 'result.html', context)
		else:
			return HttpResponse("Form not valid")
	else:
		form = PredictionForm()
		print(form)
		return render(request, 'Reuse.html', {'form': form})