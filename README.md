# **CI-MS3-Tutti-Fruitti**

Code Institute Milestone Project 3, Data-centric Module

![Am I Responsive](static/documentation/Am-I-responsive.png)

## **Table of Contents**

- [About](#about)
- [Users Experience(UX)](<#users-experience(ux)>)
  - [Project Goals](#project-goals)
  - [Target Audience](#target-audience)
  - [User Stories](#user-stories)
  - [Design](#design)
  - [Wireframe & Mockups](#wireframe&mockups)
    - [Mock-up](#mock-up)
    - [Wireframes](#wireframes)
    - [Database Schema](#database-schema)
- [Features](#Features)
  - [Existing Features](#existing-features)
  - [Features Left to Implement](#features-left-to-implement)
- [Technologies-Used](#Technologies-Used)
- [Testing](#Testing)
- [Deployment](#Deployment)
- [Credit](#Credit)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)

## **About**

Tutti Fruitti is a place for smoothies recipes.

It is a platform for smoothies lovers to explore and share smoothies recipes with one another. The users also have the the option of hoding an account, there they can add, edit and delete the their own recipes.

A live website can be found [here](https://tutti-fruitti.herokuapp.com/).

## **Users Experience (UX)**

### **Project Goals**

The project goal is to provide a platform for users who love smoothies to explore new recipes and also add more recipes to share them with other users. As more and more users starting using the service, the website become a free resource.

### **Target Audience**

Our target audience are anyone who interested in healthy living, who enjoys fruit and veg, or just simply exploring new experiences.

### **Uers Stories**

**_General User Goals_**

As a general user:

- I want to be able to see recipes without having to register an account.

- I want to be able to search recipe with certain ingredients.

- I want to search by specific categories, ie. detox, kids friendly, weight loss etc.

- I want to be able to share my recipe with other people.

- I want to have an account so I can come back, add, edit or delete my recipe.

**_First Time User Goals_**

As a first time user:

- I want to know what the website is about.

- I want to explore around to get to know the place.

- I want to have a little taste about how the recipe looks like, is it something I am looking for.

- I want to know if there is an option to register and hold an account, so I can come back anytime and add recipe if I like.

**_Returning User Goals_**

As a returning user:

- I want to be able to log into my accout.

- I want to share my own recipe.

- I want to add recipe to pre-determined categories.

- I want to have access to the recipe I uploaded.

- I want to be able to edit or delete my own recipe anytime if I want to.

**_Site Owner/Admin Goals_**

As the site owner/admin:

- I want to be able to add new categories to the site.

- I want the new category to be added and displayed as a certain way to go with the flow of the entire site.

- I want to be able to edit the pre-existing categories.

- I want to be able to delete any categories.

### **Design**

**_Overall Feel_**

Considering the nature of Smoothies, ie. "fruit" "vegetables" "summer" "ice" "cold" "fresh". The overall feel of this project will be light, cool, refreshing, clean. The user should feel like they are on holiday, by the beach and having a nice cold fruity drink in their hands.

**_Colour Scheme_**

Take from the above feeling, I decide to use below color palatte. ⬇️

![color palatte](static/documentation/MS3-palette.png)
![color palatte](static/documentation/ms3-palette-2.png)

**_Typography_**

**_Imagery_**

Imagery is the soul of a website, it plays an very important role of user experience. It should be nice and clear, illustrating the site and recipes. The color scheme of the images should interact with the main color scheme.

### **Wireframes & Mockups**

**_Mockups_**

The initial plan of this project is to use a bootstap template, but as the development progress, it turned out a bit messy. So I decided to ditch the original plan and start it again. You can see a photo or a hand-drawing mockup below. ⬇️

![mock-up](static/documentation/ms3-mockup.png)

**_Wireframes_**

All wireframes were designed base on mobile first principle, along side with a tablet and destop view. You can see all wireframes [here](static/documentation/wireframes.md).

**_Database Schema_**

![Database Schema](static/documentation/ms3-database-schema.png)

## **Features**

### **Existing Features**

**_Navigation displayed in all pages_**

All the pages will look identical with the same navigation menu displayed at the very top. Depending if a user is logged in or not, the options correspond accordingly. see the chat below for a clearer view. ⬇️

![navigation menu](static/documentation/ms3-navigation.png)

**_Recipes avaliable to all users_**

All recipes are avaliable to all users, so that all users will get to taste what the website is all about, and what they can experience, then decide if they would like to explore more functionalities of the website.

**_Users can search recipes based on either key words or ingredients_**

For smoothies, most people may not familiar with a specific name. The main ingredient or the main liquid is what people look at when it comes to searching. This feature will meet this particular user need.

**_Slides diplayed on all recipes page to showcase various category of smoothies_**

The slides show the users of different types of smoothies with a tagline explaining what the benefits are.

**_Users can view full recipe_**

Users can access the full recipe page and view the ingredients and method, smoothie category and the username of the recipe creator.

**_Users account management_**

- **Register** Users have the option to create an account.

- **LogIn** registered users can access their account by logging in.

- **LogOut** Once the user finished using the site, they have a option of logging out the website.

**_Users Recipes management_**

A registered user is able to upload their own recipes to the site. All access is shown on my recipes page.

- Upload: users are asked to fill up a form to upload a recipe. The form is validated. It means that the user cannot leave any inputs blank and white spaces.

- Edit: the user can edit their own recipes on my recipes page by hover over the recipe image and click on edit button. They will be shown the form their filled out when they created the recipe, they can make changes and save.

- Delete: the user can delete their own recipes by clicking on the delete button when hovering over the recipe image. A confirmation message modal will pop up to confirm deletion.

**_Pagiantion on all recipes and my recipes pages_**

Pagination is used for all recipes and my recipes pages. It is useful for mobile devices, help reduce loading time. The database is relatively small at the moment, but it will get bigger as more and more users start to use it, it is very important feagure for this purpose.

**_Admin manage categories functionality_**

As a site owner, I can have the option to edit or delete the existing categories if I would like to.

### **Features Left to Implement**

- **Calories calculation**

  can be a nice feature for those who cautious about calorie gaining and weight management.

- **Reviews**

  allow users to leave a review, commenting what they think about the recipe will help other users deciding on whether or not to try the recipe.

- **More secure user authetication system**

  at the moment, the create account only build by username and password. The feature can be improved by adding email and comfrim passwording functionality.

- **Ability to upload an image file**

  by adding a image file instead of relying on a URL.

- **Save Recipes**

  the feature of saving a recipe to my account for future reference.

## **Technologies Used**

### **Languages Used**

- [HTML5](https://en.wikipedia.org/wiki/HTML#:~:text=The%20HyperText%20Markup%20Language%2C%20or,displayed%20in%20a%20web%20browser.)

  - The language used to give the site its main structure and all necessary features.

- [CSS3](https://en.wikipedia.org/wiki/CSS)

  - The language used to give the application its visual effects including the font, color and layout etc.

- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

  - The language used to implement the site's interactive features, allow the users to be interactive and make actions during their visit.

- [Python3](https://www.python.org/downloads/)

  - The language used to implement all backend functionalities.

### **Frameworks & Libraries**

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)

- [Flask-PyMongo](https://pypi.org/project/Flask-PyMongo/)

- [pipenv](https://pipenv.pypa.io/en/latest/)

- [dnspython](https://www.dnspython.org/)

- [jQuery](https://jquery.com/)

- [Flask Paginate](https://pythonhosted.org/Flask-paginate/)

- [ninja](https://jinja.palletsprojects.com/en/3.0.x/)

- [Materialize](https://materializecss.com/)

- [werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/)

### **Other Programs Used**

- [Heroku](https://id.heroku.com/login)

  - Heroku used for hosting the live site.

- [MongoDB](https://www.mongodb.com/)

  - MongoDB used to host database information.

- [VScode](https://code.visualstudio.com/)

  - Visual Studio Code has been used as a local code editor for write and manage all codes and files.

- [Github](https://github.com/)

  - Github is used to create, store and maintain all codes in a repository.

  - Github is also used as the site hosting service for the final website to be published on.

- [Git Version control](https://git-scm.com/)

  - Git 2.31.1 for Mac is used for commit and push codes to Github.

- [Google Fonts](https://fonts.google.com/)

  - The font used on this quiz were chosen from Google fonts.

- [Fontawesome](https://fontawesome.com/)

  - The icons used on this quiz were found in Fontawesome.

- [Balsamiq](https://balsamiq.com/)

  - The wireframes were created using Balsamiq.

- [Random Key Generator](https://randomkeygen.com/)

  - used to create a stronger password for required <SECRET_KEY>.

- [Google DevTools](https://developer.chrome.com/docs/devtools/)

  - Google DevTools was extensively used throughout the project for various styling, testing and debugging purposes.

- [Am I Responsive](http://ami.responsivedesign.is/)

  - Am I responsive has been used to test the responsiveness of the site and also to create the mock-up image presented at the start of this document.

- [W3C Markup Validation service](https://validator.w3.org/)

  - W3C Markup Validation Service has been used to test the HTML codes.

- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

  - W3C CSS Validation Service has been used to test the CSS codes.

- [tinypng.com](https://tinypng.com/)

  - tinypng.com has been used to compress large images.

- [coolors](https://coolors.co/)

  - coolors has been used to decide the color scheme for the site.

- [Light House](https://developers.google.com/web/tools/lighthouse)

  - used for performance report.

- [Responsive Viewer](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb?hl=en)

  - used for testing site responsiveness.

- [Lucidchart](https://www.lucidchart.com/)

  - used for document database schema and visual navigation system.

## **Testing**

Testing information can be found in a seperate file [testing.md](testing.md)

## **Deployment**

### **Heroku Deployment**

I deployed this project to heroku using the following steps:

#### **Create Flask Application**

- Log into Heruko
- Under dashboard, Select "Create New App"
- Choose an app name (it shows in red if the name is already taken)
- select a region base on your location
- click "Create app"

#### **Create Github Repository**

- Log into Github
- Click the green "new" button under the main dashboard
- Choose a name
- Select "Add a README file"
- Click "Create repository"

#### **Environmentals File**

Create an env.py file using the following information:

`import os`

`os.environ.setdefault("IP", "0.0.0.0") os.environ.setdefault("PORT", "5000") os.environ.setdefault("SECRET_KEY", " *unique secret key* ") os.environ.setdefault("MONGO_URI", " *unique uri from mongo.db * ") os.environ.setdefault("MONGO_DB", " *database name* ")`

The unique mongoDB url looks like this
`mongodb+srv://username:password@clustername-qtxun.mongodb.net/databasename?retryWrites=true&w=majorit`

The env.py file contains sensive information, it needs to be added to the '.gitignore' file.

#### **Requirements.txt and Procfile**

Heroku needs to know all the requirements files the app needed for running the app successfully.

- In VScode terminal, use the following command to create a requirements.txt file.

  `pip3 freeze --local > requirements.txt`

- In VScode terminal, type `echo web: python app.py > Procfile` to create a Procifile.

- The Procfile need to contain `web:python app.py` with no additional blank line after it.

- Push these files to Github.

#### **Connecting to GitHub**

- From the heroku dashboard select "Deploy" tab
- In "deployment method" section select "GitHub"
- From the search bar just appeared enter your Github repository name
- When your locate the relative repository, click"Connect"
- Click the "setting" tab in the top bar
- Click"Reveal Config Vars" in the "Config Vars" section
- fill up the form use the following key/value pairs in the env.py file:
- Go back to the "Deploy" tab and click "enable automatic deployment"
- Uderneath, find "Manual Deploy", choose the master branch and click"Deploy Branch"
- It may take a few minutes for the app to build, once it's done, click "Open App" from the top of the page

### **Forking the Repository**

- Log into Github and locate the Github repository
- At the top right corner of the repository, there is a button reads "Fork"
- Once click on the button, you will have a copy of the original repository in your own Github account.

### **Local Clone**

- Log into Github
- Locate the repository
- Under the main navbar there is a button "code" beside the green "Gitpod" button
- Click on "Code" button, you can see the URL of the repository
- Click on the clipboard icon to copy the URL
- Open your local terminal
- Change the current working directory to the location where you want to clone the repository
- Type in CLI the command `git clone`and paste the URL you just copied. It should look like this:
  `$ git clone https://github.com/MelindaZhang2020/CI-MS3-Tutti-Fruitti`
- press enter to create you local clone

Alternatively

- Inside the "code" button, at the buttom click "Download ZIP"
- A zip file will download into you download folder on your device
- Double click on the zip file, it will unzip it for you
- Now you have all the files of the project

NB: In order to work with a clone of this project, you will need to create your own env.py file using your own variables and create your own mongoDB database matching the schema in the [Database Schema](#database-schema) section.

## **Credits**

### **Content**

#### _Code_

- The main structure code has been written followed [Code institute task manager mini project](https://learn.codeinstitute.net/)
- Landing page [neon font] code taken from [code pen](https://codepen.io/FelixRilling/pen/qzfoc)
- Landing page grid images code taken from [W3schools](https://www.w3schools.com/howto/howto_css_image_grid_responsive.asp)
- All recipes page slider taken from [Materialize](https://materializecss.com/carousel.html)
- Recipe display image overlay code taken from [W3schools](https://www.w3schools.com/howto/howto_css_image_overlay_icon.asp)
- Pagination code was taken from [Github](https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9) and [Stack overflow](https://stackoverflow.com/questions/27992413/how-do-i-calculate-the-offsets-for-pagination/27992616)
- Full recipe page go back button code was taken from [W3schools](https://www.w3schools.com/jsref/met_his_back.asp)
- My recipes & manage categories page delete confirmation message modal code was take from [W3schools](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_delete_modal)
- Materialize form validation issue solving code was take from [code institute lecture source code](https://github.com/Code-Institute-Solutions/TaskManagerAuth/tree/main/04-AddingATask-WritingToTheDatabase/02-materialize-select-validation)

#### _Recipes_

All testing recipes are taken from [BBC good food](https://www.bbcgoodfood.com/recipes/collection/smoothie-recipes), [eatthisnotthat!](https://www.eatthis.com/weight-loss-smoothies/) and [allrecipes](http://allrecipes.co.uk/recipes/tag-205/smoothie-recipes.aspx)

### **Media**

- Landing page images are downloaded from [shutterstock](https://www.shutterstock.com/home)

- All smoothies images in all recipes pages represent each category are downloaded from[unsplash](https://unsplash.com/)

- Logo icon, favicon and all the icons in create recipe form are downloaded from [ICON8](https://icons8.com/)

### **Acknowledgements**

I would like to thank:

- My mentor Antonio Rodriguez for his patience generosity with his times.

- Help and support from fellow students in the Slack community.

- Tutor support and student care team.

- My boyfriend Kevin Hurley's support and help with testing and encouragement.

Should you have any queries please reach me on melinda_hongye@yahoo.com
