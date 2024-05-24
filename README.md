# Yugen

## Introduction

![Screenshot of homepage]()

[View the live website on Heroku]()

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
[here]()

1. 
2. 
3. 
4. 
5. 
6. 


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

These are the user stories that were completed for the projects first release, by Epic.

1. Initial Django setup
    * []()
    * []()
    * []()

<br>

2. 

<br>

3. 

<br>

4. 

<br>

5. 

<br>

6. 

<br>


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
User Story:

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
