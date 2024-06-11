# Yugen

## Introduction
Yugen is a website built on Django using Python, JavaScript, HTML and CSS. The site is a full B2C ecommerce website for a fictional business. The business sells Japanese inspired artworks, be it for decoration in your office, home or anywhere you want; ranging from Traditional artworks, Modern artworks or Anime artworks. Users of the site can search for products via manual keyword search, filter by category or browse through all products available. They can select differing quantities of products for purchase and add them to their shopping cart, and proceed through a purchase process designed to be simple and with minimal steps. 

!! Incomplete !!

![Screenshot of homepage]()

[View the live website on Heroku](https://yugen-8b9d8c6f3a88.herokuapp.com/)

Please note: To open any links in this document in a new browser tab, please press CTRL + Click.

## Table of Contents
- [Yugen](#Yugen)
  * [Introduction](#introduction)
  * [Table of Contents](#table-of-contents)
  * [UX](#ux)
    + [Overall Goals](#overall-goals)
    + [The Strategy Plane](#the-strategy-plane)
    + [The Sites Ideal User](#the-sites-ideal-user)
    + [Site Goals](#site-goals)
    + [Epics](#epics)
    + [User Stories](#user-stories)
    + [The Scope Plane](#the-scope-plane)
    + [The Structure Plane](#the-structure-plane)
    + [The Skeleton Plane](#the-skeleton-plane)
      + [Wireframe mock-ups](#wireframe-mock-ups)
      + [Database Schema](#database-schema)
      + [SEO Considerations](#seo-considerations)
  * [The Surface Plane](#the-surface-plane)
  * [Features](#features)
  * [Future Enhancements](#future-enhancements)
  * [Social Media](#social-media-marketing)
  * [Testing](#testing)
  * [Deployment](#deployment)
  * [Credits](#credits)
  * [Acknowledgements](#acknowledgements)

## UX

### Overall Goals
* 
* 
* 
* 

<br>

### The Strategy Plane
* 

### The Sites Ideal User
* 
* 
* 

### Site Goals

* 
* 
* 
* 

### Epics
!!!!!!!!

XX Epics were created which were then further developed into XX User Stories. The details on each epic, along with the user stories linked to each one can be found in the project kanban board [here](https://github.com/users/SerJosh/projects/7)

1. Django Initial Setup [#1](https://github.com/SerJosh/Yugen/issues/1)

    As a **Developer**, I can **setup the Django Environment**, so that **I can initialize the development environment**

   #### Potential User Stories 
   1. Create Django Project
   2. Install required packages
   3. Secure the Keys
   4.  Deploy to Heroku


2. User Login / Logout / Register [#2](https://github.com/SerJosh/Yugen/issues/2)

   As a **User**, I can **register an account or log in and log out of my account**, so that **I can create an account and keep my account secure**

   #### Potential User Stories
   1. User Register
   2. User Login
   3. User Logout
   4. User Email Confirmation
   5.  User Password Reset 

3. Enhancing website design [#10](https://github.com/SerJosh/Yugen/issues/10)

   As a **website owner**, I can **improve the visual appeal and user experience of the website**, so that **visitors are more engaged, are able to use the site on multiple devices and have a clear understanding on what is happening**

   #### Potential User Stories
   1. Implement Responsive Design
   2. Utilize attractive fonts and color schemes
   3. Enhance the design of each page in the project

4. Home page/ Landing page [#14](https://github.com/SerJosh/Yugen/issues/14)

   As a **Site Owner**, I would like **the site to fulfil its general purpose to users on the home page**, so that **it is easy to use for users to navigate to where they want to go **

   #### Potential User Stories
   1. Color Scheme – light/dark mode
   2. Create nav-bar with relevant content for navigation
   3.  home page content
   4.  Art competition form

5. Product Viewing [#17](https://github.com/SerJosh/Yugen/issues/17)

   As a **user**, I can **view different levels of product information**, so that **I can select which amount of detail I want**

   #### Potential User Stories
   1. View product details
   2. Search for a product
   3. View products by category

6. Shopping Cart [#21](https://github.com/SerJosh/Yugen/issues/21)

   As a **user**, I can **add/remove products to my shopping cart**, so that **I can control the list products I am going to purchase**

   #### Potential User Stories
   1. Add product to cart
   2. Edit products in cart
   3. View the products in my cart
   4. Proceed to checkout

7. Checkout [#26](https://github.com/SerJosh/Yugen/issues/26)

   As a **user**, I can **purchase the items I have selected**, so that **I may place my order**

   #### Potential User Stories
   1. Payment
   2. Fill out address details for checkout
   3. Order Confirmation


### User Stories

|User Stories| | ||
|----|----|----|----|
|Must Have's| | |  |
|Should Have's| | | |
|Could Have's| | |  |
|**Total Story Pts**| | |****|

|Completed Pts| | |Uncompleted Pts|
|----|----|----|----|
|| | | |

Explaination

These are the user stories that were completed for the project, by Epic.

1. Initial Django setup
    * [US#3](https://github.com/SerJosh/Yugen/issues/3) Django Setup - As a **Developer**, I can **set up Django and install the supporting libraries needed**, so that **I am ready to start development**
    * [US#4](https://github.com/SerJosh/Yugen/issues/4) Secure the Keys - As a **Developer**, I can **setup the Django environment to secure the secret keys**, so that **I do not expose the keys in an insecure way**
    * [US#5](https://github.com/SerJosh/Yugen/issues/5) Deployment to Heroku - As a **Developer**, I want to **deploy the app to Heroku**, so that **I can confirm everything works before development of the site.**

<br>

2. User Login / Logout / Register
   * [US#6](https://github.com/SerJosh/Yugen/issues/6) Create a User Account - As a **user**, I would like **to be able to create an account**, so that **I don’t have to enter my details every time I place an order**
    * [US#7](https://github.com/SerJosh/Yugen/issues/7) User Account Login / Logout - As a **User**, I can **login or logout of my account**, so that **I can keep my account secure**
    * [US#8](https://github.com/SerJosh/Yugen/issues/8) Users must confirm their email - As a **developer**, I can **make users confirm their email**, so that **I can keep my account secure**
    * [US#9](https://github.com/SerJosh/Yugen/issues/9) Users can reset their password - As a **user** I can **reset my password** so that **if I forget it I can still access my account**
    

<br>

3. Enhancing website design
    * [US#11](https://github.com/SerJosh/Yugen/issues/11) Implementation of Responsive Design - As a **user**, I can **easily navigate and view content**, so that **I can use any device, no matter what the screen size**
    * [US#12](https://github.com/SerJosh/Yugen/issues/12) Utilize attractive fonts and color scheme - As a **user**, I can **visit a website that is enterprising and easy on the eye**, so that **when I interact with the site, it is easy and enjoyable**
    * [US#13](https://github.com/SerJosh/Yugen/issues/13) Enhance the design of each page of the project - As a **user**, I can **engage the content on each page of the website**, so that **I can understand the content on each page with it being easy on the eye**

<br>

4. Home page/ Landing page
    * [US#15](https://github.com/SerJosh/Yugen/issues/15) Create nav-bar with relevant content for navigation - As a **user**, I can **access and see the necessary content on the nav-bar**, so that **it is easily reachable and have control on every page**
    * [US#16](https://github.com/SerJosh/Yugen/issues/16) home page content - As a **user**, I would like to **see an engaging landing page, with an attractive hero image and a bigger picture of what the website has to offer**, so that **I can make more informative decisions in an engaging way**

<br>

5. Product Viewing
    * [US#18](https://github.com/SerJosh/Yugen/issues/18) View Product Details - As a **user**, I can **view the full details for a product**, so that **I can make an informed purchase decision**
    * [US#19](https://github.com/SerJosh/Yugen/issues/19) Product Search - As a **user**, I can **search for products**, so that **I can find the product I am looking for easily**
    * [US#20](https://github.com/SerJosh/Yugen/issues/20) View Products by Category - As a **user**, view all products belonging to a set category **capability**, so that **I can compare those products easily with each other and see what options are available**

<br>

6. Shopping Cart
    * [US#22](https://github.com/SerJosh/Yugen/issues/22) Add to Cart - As a **user**, I can **add products that I want to buy to my shopping cart**, so that **I can proceed to purchase them**
    * [US#23](https://github.com/SerJosh/Yugen/issues/23) Edit Cart Contents - As a **user**, I can **adjust quantity of items in my cart**, so that **I can only proceed with the correct amount of products that I want to buy**
    * [US#24](https://github.com/SerJosh/Yugen/issues/24) View Cart - As a **user**, I can **view the contents of my shopping cart**, so that **I can confirm the details prior to proceeding to purchase**
    * [US#25](https://github.com/SerJosh/Yugen/issues/25) Proceed to Checkout - As a **user**, I can **progress to purchasing my items**, so that **I can complete my transaction**

<br>

7. Checkout
    * [US#27](https://github.com/SerJosh/Yugen/issues/27) Payment - As a **user**, I can **use my credit card to make the purchase**, so that **I can pay for the purchase easily**
    * [US#28](https://github.com/SerJosh/Yugen/issues/28) Fill out address details for checkout - As a **user**, I can **provide my details**, so that **I can complete my order**
    * [US#29](https://github.com/SerJosh/Yugen/issues/29) Order Confirmation - As a **user**, I can **be taken to a confirmation page when my order is completed**, so that **it is clear my order has gone through**



### The Scope Plane

<br>

#### Opportunities
Arising from user stories
| Opportunities | Importance | Viability / Feasibility
| ------ | :------: | :------: |
| **Provide users the ability to** |  |  |
| **Provide users the ability to** |  |  |
| **Provide users the ability to** |  |  |
| **Provide users the ability to** |  |  |
| **Provide users the ability to** |  |  |
| **Provide users the ability to** |  |  |
| **Provide users the ability to** |  |  |
| **Provide users the ability to** |  |  |
| **Provide users the ability to** |  |  |
| **Provide users the ability to** |  |  |


**Features planned:**
* 
* 
* 
* 
* 
* 
* 

<br>
<br>

### The Structure Plane

<br>
User Story: Django Setup

   As a Developer, I can set up Django and install the supporting libraries needed, so that I am ready to start development

   Tasks
   <ul>
   <li>Install Django</li>
   <li>Install dj_database_url psycopg2</li>
   <li>Create a requirements.txt file</li>
   <li>Install django-crispy-forms</li>
   <li>Install Pillow</li>
   <li>Install Django-allauth</li>
   <li>Create new instance in Postgres SQL and connect database to code</li>
   <li>Install Gunicorn</li>
   <li>Create the Django project</li>
   <li>Create the first app</li>
   </ul>

<br>

User Story:

<br>

User Story:

<br>

User Story:

<br>


<br>
<br>

## The Skeleton Plane
### Wireframe mock-ups


<br>

Primary Landing Page
<br>
![Primary landing page](documentation/yugen-primary-landing.png)
<br>
Alternative Landing Page
<br>
![Alternative landing page](documentation/yugen-alternative-landing.png)
<br>
Heading
<br>
![]()
<br>
Heading
<br>
![]()
<br>


### Database Schema

<br>

![Database Schema Diagram]()

<br>
 
<br>

![Model]()

<br>

<br>

![Model]()

<br>

<br>

![Model]()

<br>

<br>

### SEO Considerations

<br>

#### Keyword Research


<br>

[Keyword Research - ]()

<br>

[Keyword Research - ]()

<br>

[Keyword Research - ]()

<br>

[Keyword Research - ]()

<br>

[Keyword Research - ]()

<br>

[Keyword Research - ]()

<br>

[Keyword Research - ]()

<br>


<br>

From this research a refined keyword list was cultivated for use with the short-tail keywords within the head meta tags and for content through out the site. However this only formed a small part of the overall strategy for the sites SEO strategy.

#### Content Strategy


## The Surface Plane

### Design

<br>

![]()

<br>

### Typography 


##### Images


## Features

### Feature
Explaination
<br>

![]()

<br>

### Feature
Explaination
<br>

![]()

<br>


## Testing

!!!! BIG STUFF HERE !!!!


## Deployment

The site was deployed via Heroku, and the live link can be found here - [Yugen]()

To deploy the project through Heroku I followed these steps:
* Sign up / Log in to [Heroku](https://www.heroku.com/)
* From the main Heroku Dashboard page select 'New' and then 'Create New App'
* Give the project a name - I entered Yugen and select a suitable region, then select create app. The name for the app must be unique.
* This will create the app within Heroku and bring you to the deploy tab. From the submenu at the top, navigate to the resources tab.
* Add the database to the app, in the add-ons section search for 'Heroku Postgres', select the package that appears and add 'Heroku Postgres' as the database
* Navigate to the setting tab, within the config vars section copy the DATABASE_URL to the clipboard for use in the Django configuration.
* Within the django app repository create a new file called env.py - within this file import the os library and set the environment variable for the DATABASE_URL pasting in the address copied from Heroku. The line should appear as os.environ["DATABASE_URL"]= "Paste the link in here"
* Add a secret key to the app using os.environ["SECRET_KEY"] = "your secret key goes here"
* Add the secret key just created to the Heroku Config Vars as SECRET_KEY for the KEY value and the secret key value you created as the VALUE
* In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url
* insert the line if os.path.isfile("env.py"): import env
* remove the insecure secret key that django has in the settings file by default and replace it with SECRET_KEY = os.environ.get('SECRET_KEY')
* replace the databases section with DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} ensure the correct indentation for python is used.
* In the terminal migrate the models over to the new database connection
* Navigate in a browser to Amazon AWS, log in, or create an account and log in. 
* Create a new S3 bucket for the site and create a static directory and media directory within the bucket.
* From the dashboard - copy the bucket details into the settings file.
    * you will require the following:
        - Storage Bucket Name
        - Storage Bucket Region Name
        - Access Key ID
        - Secret Access Key
    * configure these settings in the settings file
* in the env.py file created earlier 
    - add os.environ["AWS_ACCESS_KEY_ID"] = "paste in your access key"
    - add os.environ["AWS_SECRET_ACCESS_KEY"] = "paste in your secret access key"
* In Heroku, add the keys and values copied to the clipboard to the config vars
* Also add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars
* this key value pair must be removed prior to final deployment
* Using the requirements.txt file install all of the required packages
* in the Settings.py file - add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
* Link the file to the templates directory in Heroku TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
* Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]
* Add Heroku to the ALLOWED_HOSTS list the format will be the app name given in Heroku when creating the app followed by .herokuapp.com
* In your code editor, create three new top level folders, media, static, templates
* Create a new file on the top level directory - Procfile
* Within the Procfile add the code - web: guincorn PROJECT_NAME.wsgi
* In the terminal, add the changed files, commit and push to GitHub
* In Heroku, navigate to the deployment tab and deploy the branch manually - watch the build logs for any errors.
* Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.
* This project utilises Stripe as a payment platform provider - You can create a stripe account at www.stripe.com you will need a developer account to gain access to the api keys required to run the payment processes.
* Once you have successfully created your stripe account, insert the stripe public key, stripe secret key and stripe webhook key into the env.py file and the heroku config vars. Configure the settings file to point at the variables required. Stripe provide documentation on how to setup stripe within django which is easy to follow. It is available within the stripe developer site.

#### Forking the repository
By forking the GitHub Repository you can make a copy of the original repository to view or change without it effecting the original repository
This can be done by
    * Log into GitHub or create an account.
    * Locate the repository at https://github.com/SerJosh/Yugen .
    * At the top of the repository, on the right side of the page, select "Fork" from the buttons available.
    * A copy of the repository should now be created in your own repository.

#### Create a clone of this repository
Creating a clone enables you to make a copy of the repository at that point in time - this lets you run a copy of the project locally:
This can be done by:
* Navigate to https://github.com/SerJosh/Yugen
* click on the arrow on the green code button at the top of the list of files
* select the clone by https option and copy the URL it provides to the clipboard
* navigate to your code editor of choice and within the terminal change the directory to the location you want to clone the repository to.
* type 'git clone' and paste the https link you copied from github
* press enter and git will clone the repository to your local machine

### Credits
* 
* 
* 


### Acknowledgements

I'd like to thank the following:
* 
* 
