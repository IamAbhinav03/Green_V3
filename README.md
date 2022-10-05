# Welcome to Green!!

Hi, We are Team Green. Firstly we would like to thank the organizers of the Hack4Earth hackathon for giving us this opportunity to participate in this event. We are deeply thankfull and hope you like our proect as well!

Waste the unwanted burden of society! It is a major cause for panic as it contributes to environmental decay and ecological collapse. Due to the chemicals and solid wastes in landfilles, soil around the landfill is leached of minerals which then makes the area inhospitable to flora and fauna. We have lost hecters of place for landfills and now oceans are also being affected causing more troubles to aquatic life too.

But worry not, we humans have realised our mistakes and started taking critical measures to achieve Zero Waste. As a first step towards this goal, we have designed the 3 R's; **Recyle, Reuse, Reduce**.

## Problem Statement

3 R's is a great initiative but due to our laziness and unwillignes we are not seeing the full potential of the 3 R's. Some of the issues we saw are:
* Lack of reusing
* Lack of motivation to recycle or reuse waste
* Lack of knowledge on 3 R's
* Improper segragation of waste
* Timely collection of waste

## Our Solution
![alt text](https://github.com/IamAbhinav03/Green_V3/blob/main/assets/home.jpg?raw=true)
<!-- https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true -->

Our solution to the above mentioned problems is an all-in-one platform for waste management. We belive that if every person properly segrates the waste they produce and reuse the most of it will make the 3 R's initiative more effective. 

The majour feature of our web app is in the Reuse Tab of our web-app. We have used an **AI**  algorithm which can dectet different materials. A user loged int our web app can use this to scan their waste material and the model predict it. It also give links to articles and videos of reusing that material. An example use case will be. if the user has a paper waste material, ther user can scan it and the model predicts and materials and give links to articles on how to reuse that paper into craft items and etc. We are hoping to educate users about reusing waste materials with this feature. We also belive that this feature wil help users to segraate the materials more efficiently.

We also found that to make reusing more attractive to users, a reward system will be good. So we added a point system where the waste agencies(admin of the web app) can give points to the users.

## Features on Development

* **Empty Trash**
	* We have also noticed that some people dump or burn their waste due to the lack of timely collection of them for recycling. So we have been working on feature that is implemented in the Notify tab of the web-app. Users can go there and notify their waste collection agency or muncipalites that their garbage bin is full.
	>Current implementation just send the notification to the admin.
	
	 With this feature we hope that people will not dump their waste or burn and help the environment a little bit safer.
 
* **Market Place**
	* We are thinking about integrating a marketplace into the web-app where people can sell their reused item. Many of the waste we produce can be reused into usefull items, and by implementing this we will provide users a income source for, further motivating them to reuse. Moreover most of the food waste we create can be converted into fertilizers. Users can make fertlizers out of the food waste they produce and farmers can buy this and provide a good organic manure to crops, helping us to get good and chemical free food. Furthermore we also think that this will be a good place for craftsmen. They can use their creativity to create new and unique products out of waste material and also get a new income source.

## Technical Details.

* **How our web-app is built?**
	* **Backend**
		* Our project is made using the Django framework and currently hosted locally. We chose django for scaling the app easily in the future.
	* **UI/UX**
		* We have made the UI of the app using a online website builder. We then exported those codes and integrated it with the Django Backend.
	*  **Database**
		* Postgress
	* **AI Model**
		* For detecting the waste materials, we have trained a ResNet-50 model, a convolution neural network that classifies images into 6 categories(Paper, plastic, cardboard, metal, glass, organic) using the Pytorch framework. The model was trained on [Garbage classification Dataset](https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification) from kaggle. The current model has an accuracy of 95% on the test dataset.

* **How does it works**
	* The model predicts the waste material in the given image, compares it with the resource list on the web applciation, and picks the correct suggestion. Suggestions in the form of links to articles and videos regarding waste management are also shared by the model. The model can be used as a web application with people from muncipalites(admin) having access to it. Currently it's hosted locally. We are planning to host it in aws in the future.