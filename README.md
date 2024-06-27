# Yugen

## Introduction
Yugen is a website built on Django using Python, JavaScript, HTML and CSS. The site is a full B2C ecommerce website for a fictional business. The business sells Japanese inspired artworks, be it for decoration in your office, home or anywhere you want; ranging from Traditional artworks, Modern artworks or Anime artworks. Users of the site can search for products via manual keyword search, filter by category or browse through all products available. They can select differing quantities of products for purchase and add them to their shopping cart, and proceed through a purchase process designed to be simple and with minimal steps. There is also a reviews section for users to review products as well as a favorites option where users can add product to their favorites. Admin are able to add, delete and edit products as well as customise the updates heading in the landing page.


![Screenshot of homepage](documentation/readme-hero.png)

[View the live website on Heroku](https://yugen-319a909ad83d.herokuapp.com/)

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
      + [Social Media Marketing](#social-media-marketing)
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
* To provide an ecommerce solution for a small business selling japanese artworks to consumers - B2C
* To enable business employees to maintain and update the site content in line with their needs easily.
* To provide users with a simple product selection and purchase experience.
* To provide the business owner/manager a degree of control over the site.

<br>

### The Strategy Plane
* Yugen is a business to consumer B2C ecommerce site for users (consumers browsing products and making purchases) to find and purchase selected products, read reviews, whilst for business employees they are able to manage the site content to ensure it is kept upto date with the business needs. The overall design of the site is intended to provide users with a clean and easy to navigate environment whilst providing the level of detail required for the different types of products.

### The Sites Ideal User
* Japanese related enthusiast searching for new products
* Someone looking to buy a new product for decoration
* Someone looking for inspiration for new things they could decorate with

### Site Goals

* To provide users with a place to purchase their pictures for display
* To promote the product range of Yugen
* To promote Yugen as the preferred site for users to purchase japanese inspired decoration

### Epics

10 Epics were created which were then further developed into 31 User Stories. The details on each epic, along with the user stories linked to each one can be found in the project kanban board [here](https://github.com/users/SerJosh/projects/7)

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

8. Checkout [#30](https://github.com/SerJosh/Yugen/issues/30)

   As a **user**, I can **create and maintain an account**, so that **I can order products quickly and easily without having to enter information each time**

   #### Potential User Stories
   1. Create User Profile / Account
   2. Edit User Profile / Account
   3. View User Profile / Account
   4. Delete User Profile / Account

9. Product Management [#35](https://github.com/SerJosh/Yugen/issues/35)

   As a **Site Owner**,  I would like **employees to be able to manage the products on the site easily, so that it is easy to keep the site up to date**

   #### Potential User Stories
   1. Add products
   2. Edit Products
   3. Delete Products

10. Custom Models [#39](https://github.com/SerJosh/Yugen/issues/39)

   As a **user and site owner**, I can **have multiple uses to interact with on the site**, so that **I can customize and engage with the website**

   #### Potential User Stories
   1. Favorites
   2. Reviews
   3. Headline update


### User Stories

|User Stories| | |31|
|----|----|----|----|
|Must Have's| | | 110pts |
|Should Have's| | | 28pts |
|**Total Story Pts**| | |**138pts**|

|Completed Pts| | |Uncompleted Pts|
|----|----|----|----|
|130| | |8 |

From the Epics, 31 User stories were developed. Each story was assigned a classification of Must-Have, Should-Have, Could-Have or Won't Have originally, but throughout the development of the project, not could haves or wont haves were developed. Each story was also assigned user story points, based on my best estimation for the time/difficulty of completing each story. A combination of being new to story estimation, inexperience with Django and time constraints during development left me completing 130 story points from the initial total of 138. The full list of User Stories, seperated by those completed and those incomplete are available on the project [kanban board](https://github.com/users/SerJosh/projects/7).


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

<br>

8. User Profile
    * [US#31](https://github.com/SerJosh/Yugen/issues/31) Create Account - As a **user**, I can **create an account**, so that **I don’t have to enter my details every time I place an order**
    * [US#32](https://github.com/SerJosh/Yugen/issues/32) Edit Account - As a **user**, I can **edit the details/address stored on my account**, so that **If I move, I can change my details**
    * [US#33](https://github.com/SerJosh/Yugen/issues/33) View Account - As a **user**, I can **view the details stored on my account**, so that **I can review what is stored**
    * [US#34](https://github.com/SerJosh/Yugen/issues/34) Delete Account - As a **user**, I can **delete my account**, so that **I have full control over the information that is stored about me**

<br>

9. Product Management
    * [US#36](https://github.com/SerJosh/Yugen/issues/36) Add Products - As an **Store Owner**, I would like **employees to be able to add new products to the site easily**, so that **the site can be kept up to date**
    * [US#37](https://github.com/SerJosh/Yugen/issues/37) Delete Products - As a **Store Owner**, I would like **employees to be able to remove product details from the site**, so that **we can remove no longer available products from the site**
    * [US#38](https://github.com/SerJosh/Yugen/issues/39) Edit Products - As a **Store Owner**, I would **like employees to be able to edit product details on the site easily**, so that **any corrections needed can be carried out when required**

<br>

10. Custom Models
    * [US#40](https://github.com/SerJosh/Yugen/issues/40) Favorites - As a **user**, I can **choose my favorites from the products**, so that **I can buy them later**
    * [US#41](https://github.com/SerJosh/Yugen/issues/41) Reviews - As a **user**, I can **add review to products**, so that **I can give my thoughts on the product**
    * [US#42](https://github.com/SerJosh/Yugen/issues/42) Headline Update - As a **site owner**, I can **edit the text content on the landing page**, so that **I can let user know new information**

### The Scope Plane

<br>

#### Opportunities
Arising from user stories
| Opportunities | Importance | Viability / Feasibility
| ------ | :------: | :------: |
| **Provide users the ability to create an account** | 5 | 5 |
| **Provide users the ability to save address information for easier checkout** | 5 | 5 |
| **Provide users the ability to edit their account** | 5 | 5 |
| **Provide users the ability to delete their account** | 3 | 4 |
| **Provide users the ability to login to their account** | 5 | 5 |
| **Provide users the ability to logout from their account** | 5 | 5 |
| **Provide users the ability to view product summary information** | 5 | 5 |
| **Provide users the ability to view product detailed information** | 5 | 5 |
| **Provide users the ability to add products to their cart** | 5 | 5 |
| **Provide users the ability to edit the quantity of products in their cart** | 5 | 5 |
| **Provide users the ability to remove products from their cart** | 5 | 5 |
| **Provide users the ability to progress to checkout** | 5 | 5 |
| **Provide users the ability to enter their information to checkout** | 5 | 5 |
| **Provide employees the ability to create product** | 4 | 5 |
| **Provide employees the ability to edit product** | 4 | 5 |
| **Provide employees the ability to remove product** | 4 | 5 |
| **Provide employees the ability to edit informative Headings updates** | 3 | 4 |
| **Provide users the ability to create reviews** | 5 | 5 |
| **Provide users the ability to edit reviews** | 5 | 5 |
| **Provide users the ability to view reviews** | 5 | 5 |
| **Provide users the ability to delete reviews** | 5 | 5 |
| **Provide users the ability to save a product to their favorites** | 3 | 5 |
| **Provide users the ability to remove a product from their favorites** | 3 | 5 |
| **Provide users the ability to search the site for products** | 4 | 5 |
| **Provide users the ability to access the site on any device** | 5 | 5 |


**Features planned:**
* User Profile - Create, Read, Update and Delete
* User Address - Create, Read, Update and Delete
* User Wishlist - Create, Read, Update and Delete
* Users can login to their account, email address and delivery address
* Users can reset their password if they forget it
* Users can logout of their account
* Products - Create, Read, Update and Delete
* Product Search - by category and keyword
* Products - View product details or summary information
* Shopping Cart - Add, Update and Remove products from the shopping cart
* Checkout - Enter delivery information and payment information
* Payment Processing - Successfully process payment information and confirm orders
* Order Confirmation - Confirm order information on payment success
* Order Tracking - Users can track order status for individual orders
* Headline Update - Create, Read, Update and Delete
* Reviews - Create, Read, Update and Delete
* Users need to be registered and logged in to access product wishlist, saving addresses, prior order information and the ability to provide reviews.
* Email newsletter subscription - Ability to subscribe to a company newsletter for marketing purposes.
* Responsive Design - the site needs to be fully responsive to cover the wide variety of devices users may use to access it

<br>
<br>

### The Structure Plane

<br>

#### User Story: Django Setup

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

#### User Story: Secure the Keys
   As a Developer, I can setup the Django environment to secure the secret keys, so that I do not expose the keys in an insecure way

   Tasks
   <ul>
   <li>Create an env.py file to store the environment variables needed</li>
   <li>Add the env.py file to the .gitignore file so that it does not get pushed to Github</li>
   </ul>

<br>

#### User Story: Deployment to Heroku
   As a Developer, I want to deploy the app to Heroku, so that I can confirm everything works before development of the site.

   Tasks
   <ul>
   <li>Update code for deployment</li>
   <li>Create new Heroku app</li>
   <li>Connect Heroku to the PostgreSQL database</li>
   <li>Implement and add Secret Key to project and Heroku config var</li>
   </ul>

<br>

#### User Story: Create a User Account
   As a user, I would like to be able to create an account, so that I don’t have to enter my details every time I place an order

   Acceptance Criteria
   <ul>
   <li>Given that I am an unregistered user
And, I am on the user registration page
When I enter my username, email address and password
And, I click on the register button
Then the system creates me an account</li>
   <li>Given that I have an account
And, I have items in my cart
WhenI navigate to checkout
Then I have my address information ready to be used</li>
   </ul>

   Tasks
   <ul>
   <li>Develop ability for users to register for a user account</li>
   <li>Develop a page and button in the nav bar to direct users to the registration page</li>
   <li>Remove the register button from the nav bar when users are logged in</li>
   <li>Create a User Registration form</li>
   </ul>

<br>

#### User Story: Users must confirm their email

   As a developer, I can make users confirm their email, so that I can keep my account secure

   Acceptance Criteria
   <ul>
   <li>Given that a user wants to register
When they fill in the details in the registration page
Then they have to confirm their email</li>
   <li>Given that the user has confirmed their email
When they have confirmed it in their email
Then they will be able to access the site as a registered user</li>
   </ul>

   Tasks
   <ul>
   <li>Develop an automated email platform for users to receive email confirmations</li>
   <li>Include a link to the website to go back once they have confirmed</li>
   <li>Develop the ability to see confirmed users in the admin page</li>
   </ul>


<br>

#### User Story: Users can reset their password

   As a user I can reset my password so that if I forget it I can still access my account

   Acceptance Criteria
   <ul>
   <li>Given that I forgot by password
When I try to login with an incorrect password
Then an option is available to reset my password</li>
   <li>Given that I click on the link to reset my password
When I enter my email address that I used to sign up,
Then I should receive an email with instructions on how to reset my password</li>
<li>Given that I have received the email to reset my password
When I follow the instructions
Then my password should be reset, or I should be able to set a new password of my choosing
And When I do not follow the instructions,
Then my password should not be reset</li>
   </ul>

   Tasks
   <ul>
   <li>Develop a link on the login page to take users to a reset password page</li>
   <li>Develop a form for users to enter their email address in order to reset their password</li>
   <li>Develop an email containing a link to reset the user password</li>
   <li>Ensure form for user to enter email address, validates the email address as belonging to current user</li>
   </ul>

<br>

#### User Story: User Account Login / Logout

   As a User, I can login or logout of my account, so that I can keep my account secure

   Acceptance Criteria
   <ul>
   <li>Given that I am a registered user, who is not logged in
When I navigate to the sign in page
And, I enter my credentials correctly and press sign in
Then I am signed into my account</li>
   <li>Given that I am a registered user, who is currently logged in
When I click on the sign out link
Then I am signed out of my account</li>
<li>Given that I am a registered user, who has signed out of my account
When I use the browser navigation buttons such as back button
Then I can not access information which requires me to be signed in</li>
   </ul>

   Tasks
   <ul>
   <li>Develop the ability for users to sign into their account</li>
   <li> Develop a sign in form to capture user sign in details</li>
   <li>Develop form validation to ensure the data is correct</li>
   <li>Develop a link for users to sign out of their account – should be accessible from all pages (nav bar), user account section</li>
   <li>Develop a redirect so if a user signs out whilst on a page requiring a user to be logged in, it redirects them appropriately</li>
   </ul>

<br>

#### User Story: Add to Cart

   As a user, I can add products that I want to buy to my shopping cart, so that I can proceed to purchase them

   Acceptance Criteria
   <ul>
   <li>Given That I am an unregistered user
When I find a product I want to purchase
And, I click on add to cart
Then the product is added to my shopping cart, ready for me to purchase</li>
   <li>Given that I am a User,
When I click add to cart on a product I have previously added to my cart
Then The quantity of that product in my cart increases by the amount I just added</li>
   </ul>

   Tasks
   <ul>
   <li>Develop a shopping cart functionality to track products users want to purchase.</li>
   <li> Enable the cart to be utilized when a user is logged in or not</li>
   <li>Develop check on add to cart functionality for product already existing in cart – if product exists, increase quantity appropriately</li>
   </ul>

<br>

#### User Story: Create nav-bar with relevant content for navigation

   As a user, I can access and see the necessary content on the nav-bar, so that it is easily reachable and have control on every page

   Acceptance Criteria
   <ul>
   <li>Given That I am a user on the website
When I want to see my account information
Then I can access it on the nav-bar on every page</li>
   <li>Given That I am a user on the website
When I want to see if I am logged in or not
Then I can see it on the nav-bar</li>
<li>Given That I am a user on the website
When I am on any page
Then I can access all the necessary content for a e-commerce website
</li>
   </ul>

   Tasks
   <ul>
   <li>Create an account option with the necessary content</li>
   <li> Display the username as logged in and "you are not logged in" if not</li>
   <li>Display content required for filtering or links to all products</li>
   <li>Display Facebook link for Facebook page</li>
   <li>Display shopping cart to link to added products to shopping cart and add features to it (eg amount)</li>
   </ul>

<br>

#### User Story: View Product Details

   As a user, I can view the full details for a product, so that I can make an informed purchase decision

   Acceptance Criteria
   <ul>
   <li>Given That I am a user on the site
When I navigate to a product listing
Then the full details of the product are available</li>
   <li>Given That I am a user on the all products page
When click on a product summary card
Then I am taken to a page with the full details on the product</li>
   </ul>

   Tasks
   <ul>
   <li>Develop a product full details page template</li>
   <li>Develop product card template</li>
   <li>Link product card with product detail page</li>
   </ul>

<br>

#### User Story: Product Search

   As a user, I can search for products, so that I can find the product I am looking for easily

   Acceptance Criteria
   <ul>
   <li>Given That I am a User
When I am on the site
Then I have easy access to search functionality</li>
   <li>Given That I am a User
When I search for a product by name
Then the product appears in the search result</li>
<li>Given That I am a User
When I search for a product by category
Then all the products in that category appear</li>
   </ul>

   Tasks
   <ul>
   <li>Develop search bar functionality that is easy to access on every page</li>
   <li>Develop search query filter to search by product name</li>
   <li>Develop search query filter to search by any keyword</li>
   </ul>

<br>

#### User Story: View Products by Category

   As a user, view all products belonging to a set category capability, so that I can compare those products easily with each other and see what options are available

   Acceptance Criteria
   <ul>
   <li>Given that I am a user,
When I want to quickly look at all product in a given category
Then there is a link in the navigation bar to quickly access them</li>
   <li>Given that I am a user,
When click on the category link
Then all the products related to that category are displayed</li>
   </ul>

   Tasks
   <ul>
   <li>Develop navigation links for each category of product</li>
   <li>Develop query for each link to automatically apply filter to product results for each category to be used for the nav links.</li>
   </ul>

<br>

#### User Story: Edit Cart Contents

   As a user, I can adjust quantity of items in my cart, so that I can only proceed with the correct amount of products that I want to buy

   Acceptance Criteria
   <ul>
   <li>Given That I am a User
And, I have added products to my cart
When I view the cart
Then I can adjust the quantity of each item individually</li>
   <li>Given That I am a User
When I view the items in my cart
Then have the ability to remove an item completely.</li>
   </ul>

   Tasks
   <ul>
   <li>Develop the ability to adjust the item quantity within the shopping cart</li>
   <li>Develop the ability to remove items from the shopping cart</li>
   </ul>

<br>

#### User Story: View Cart

   As a user, I can view the contents of my shopping cart, so that I can confirm the details prior to proceeding to purchase

   Acceptance Criteria
   <ul>
   <li>Given That I am a User
When I click on my shopping cart
Then I am taken to a page with the details of all the products I have within my cart</li>
   <li>Given That I am a user
When I add a product to my cart
Then I have a visual confirmation that the product is now in my cart</li>
   </ul>

   Tasks
   <ul>
   <li> Develop template page for viewing the shopping cart</li>
   <li>Develop temporary preview of shopping cart to display when adding products to the cart</li>
   </ul>

<br>

#### User Story: Proceed to Checkout

   As a user, I can progress to purchasing my items, so that I can complete my transaction

   Acceptance Criteria
   <ul>
   <li>Given That I am a user
When I have reviewed my shopping cart
Then I have the option to proceed to purchase them</li>
   <li>Given That I am a user
When I have added products to my shopping cart
Then I have the option to proceed to purchase, without having to confirm the details of the products within my cart</li>
   </ul>

   Tasks
   <ul>
   <li>Develop checkout link on shopping cart page</li>
   <li>Develop checkout link on shopping cart preview</li>
   </ul>

<br>

#### User Story: Fill out address details for checkout

   As a user, I can provide my details, so that I can complete my order

   Acceptance Criteria
   <ul>
   <li>Given that I am a User,
When I proceed to checkout
Then I am asked to enter my delivery and billing address</li>
   <li>Given that I am a user,
When I enter my billing address
Then I can use the same address for delivery without having to fill it out twic</li>
<li>Given that I am a logged in user,
When I enter my address details,
Then have the option to save the details I entered to my account</li>
<li>Given that I am a logged in user,
WhenI get to the enter billing and delivery address screen
Then I have the option to use previously saved address(es) details</li>
<li>Given hat I am a registered user, not logged in
When I progress to enter the address information – I have the ability to login
Then return to the same screen and use previously saved address details.</li>
   </ul>

   Tasks
   <ul>
   <li>Develop checkout page to collect billing and delivery address details</li>
   <li>Enable option to use billing address for delivery address</li>
   <li>Enable option for users to save address details to their account</li>
   <li>Enable logged in users to select previously saved addresses instead of manual completion of the form</li>
   </ul>

<br>

#### User Story: Payment

   As a user, I can use my credit card to make the purchase, so that I can pay for the purchase easily

   Acceptance Criteria
   <ul>
   <li>Given that I am a user
When purchasing my items
Then I have the ability to enter my credit card details on a secure form</li>
   <li>Given that I am a user
When I enter my card details to pay for the transaction
Then the system will process the payment</li>
<li>Given that I am a user
When I process the payment using my card details
Then I am kept informed as to the status as it progresses</li>
<li>Given that I am a user
WhenMy payment fails
Then I am returned to the checkout page without losing all the inputted information</li>
<li>Given that I am a user
When I checkout and my payment is successful
Then I am taken to a confirmation page</li>
   </ul>

   Tasks
   <ul>
   <li>Develop secure form to capture credit card details</li>
   <li>Develop link to payment processor</li>
   <li>Develop message system to keep customer informed of processing status</li>
   <li>Develop redirect to appropriate page depending on payment outcome</li>
   </ul>

<br>

#### User Story: Order Confirmation

   As a user, I can be taken to a confirmation page when my order is completed, so that it is clear my order has gone through

   Acceptance Criteria
   <ul>
   <li>Given that I am a user
When I complete a checkout form and my payment is processed
Then I can see confirmation of my order details</li>
   <li>Given that I am a user
When I complete a checkout form and my payment is processed
Then I receive an email with the confirmation details</li>
<li>Given that I am a user
When I complete a checkout form and my payment is processed
Then an order number is generated with which I can retrieve the order details</li>
<li>Given That I am a registered user, logged in when I placed my order
When I I have successfully completed my order
Then the order appears in my orders of my account</li>
   </ul>

   Tasks
   <ul>
   <li>Develop an order confirmation page that the user redirects to on order completion.</li>
   <li>Develop automated email confirming order – email to include link to order details page for that order and order number</li>
   </ul>

<br>

#### User Story: Create Account

   As a user, I can create an account, so that I don’t have to enter my details every time I place an order

   Acceptance Criteria
   <ul>
   <li>Given that I am an unregistered user
And, I am on the user registration page
When I enter my email address and password
And, I click on the register button
Then the system creates me an account
And, it tells me that my account has been created</li>
   <li>Giventhat I have an account
And, I have items in my cart
WhenI navigate to checkout
Then I have my address information ready to be used</li>
   </ul>

   Tasks
   <ul>
   <li>Develop the ability for users to register for an account</li>
   <li>Develop ability for users to save details to their account such as address</li>
   </ul>

<br>

#### User Story: Edit Account

   As a user, I can edit the details/address stored on my account, so that If I move, I can change my details

   Acceptance Criteria
   <ul>
   <li>Given that I have a user profile,
And, I am logged into my profile
When I navigate to my profile
Then I have the ability to edit my address on my account</li>
   <li>Given that I have a user profile,
And, I am logged into my profile
When I navigate to my profile
Then I have the option to delete the address’s</li>
   </ul>

   Tasks
   <ul>
   <li>Develop the ability for users to save addresses to their profile</li>
   <li>Develop the ability for users to edit the addresses on their profile</li>
   <li>Develop the ability for users to delete the addresses on their profile</li>
   </ul>

<br>

#### User Story: View Account

   As a user, I can view the details stored on my account, so that I can review what is stored

   Acceptance Criteria
   <ul>
   <li>Given that I have a user account
When I am logged into my account
Then I have an option to view my account</li>
   <li>Given that I have a user account
And, I am logged in
When I navigate to view my details
Then everything that is stored within my account is available to be viewed</li>
   </ul>

   Tasks
   <ul>
   <li>Develop a link in the menu that takes logged in users to their profile</li>
   <li>Develop a link within the user profile page that they can use to view all other information associated with the account – previous orders, address details, etc.</li>
   </ul>

<br>

#### User Story: Implementation of Responsive Design

   As a user, I can easily navigate and view content, so that I can use any device, no matter what the screen size

   Acceptance Criteria
   <ul>
   <li>Giventhat the user is visiting the site
Whenthe user is using a different device
Then the website automatically adjusts its content to accommodate for the screen size</li>
   </ul>

   Tasks
   <ul>
   <li>Use media queries to make content responsive up to 325px</li>
   <li>when needed use bootstrap to make content responsive</li>
   <li>test responsive content on mobile phone</li>
   </ul>

<br>

#### User Story: Enhance the design of each page of the project

   As a user, I can engage the content on each page of the website, so that I can understand the content on each page with it being easy on the eye

   Acceptance Criteria
   <ul>
   <li>Given That I am a user and on a certain page
When I am on that page looking at the content
Then That it is easily readable and engaging</li>
   </ul>

   Tasks
   <ul>
   <li>Enhance the design of allauth pages</li>
   <li>Enhance the design of the home page</li>
   <li>Enhance the design of the pictures/products/gallery pages</li>
   <li>Enhance the design of the bag page</li>
   <li>Enhance the design of the checkout pages</li>
   <li>Enhance the design of the profile page</li>
   </ul>

<br>

#### User Story: Add Products

   As an Store Owner, I would like employees to be able to add new products to the site easily, so that the site can be kept up to date

   Acceptance Criteria
   <ul>
   <li>Given That I am an employee
When I log into the site
Then I should have additional stock management options available</li>
   <li>Given That I am a logged in employee
When I go to product management
Then I should be directed to a form that allows me to add a new product to the site</li>
<li>Given That I am a logged in employee And, I have completed the form to add a product
When I submit the form
Then the new product should appear on the site</li>
   </ul>

   Tasks
   <ul>
   <li>Develop a separate navigation bar for employee users to allow access to other site area</li>
   <li>Develop a form for employees to add products to the site</li>
   <li>Develop validation to ensure that product information is completed correctly</li>
   </ul>

<br>

#### User Story: Delete Products

   As a Store Owner, I would like employees to be able to remove product details from the site, so thatwe can remove no longer available products from the site

   Acceptance Criteria
   <ul>
   <li>Given that I am an employee
When I select a product to edit,
Then I should have the option to remove it from yugen</li>
   <li>Given that I am an employee
When select a product to remove from the store
Then I should also have the option to delete the product entirely</li>
<li>Given that I am an employee
When I have selected to delete a product entirely
Then the product is removed from the database</li>
   </ul>

   Tasks
   <ul>
   <li>Develop an option in the product management to remove the product from the store</li>
   <li>Restrict access to the option to employees only</li>
   </ul>

<br>

#### User Story: Edit Products

   As a Store Owner, I would like employees to be able to edit product details on the site easily, so that any corrections needed can be carried out when required

   Acceptance Criteria
   <ul>
   <li>Given That I am an employee
When I log into the site
Then I should have the option to edit a product</li>
   <li>Given That I am a logged in employee
When I select which product to edit
Then I am directed to a form from which I can edit the existing product data</li>
<li>Given That I am a logged in employee
When I edit product details within the form and submit the changes
Then the changes I made appear on the site</li>
   </ul>

   Tasks
   <ul>
   <li>Develop the option for employees to edit products</li>
   <li>Develop validation for the form to ensure product information is complete</li>
   <li>Develop a form for employees to edit the product data</li>
   </ul>

<br>

#### User Story: Favorites

   As a user, I can choose my favorites from the products, so that I can buy them later

   Acceptance Criteria
   <ul>
   <li>Given That i am a user
When I see the list of products
Then I can choose which one i want to put as favorites</li>
   <li>Given That i am a user
When I want to see my list of products
Then I can go to a page to see my favorite</li>
<li>Given That i am a user
When I want to remove a product from my favorites
Then There is a button letting me do so</li>
   </ul>

   Tasks
   <ul>
   <li>Implement a favorites page</li>
   <li>Make each product with add to favorites/added to favorites</li>
   <li>Develop function to delete product</li>
   </ul>

<br>

#### User Story: Delete Account

   As a user, I can delete my account, so that I have full control over the information that is stored about me

   Acceptance Criteria
   <ul>
   <li>Given that I have a user account
When I view my account details whilst logged in
Then I have the option to delete my account.</li>
   <li>Given that I have a user account
And, I am on my account details page
When I select to delete my account
And, I confirm the deletion request
Then My account is deleted.</li>
   </ul>

   Tasks
   <ul>
   <li>On the user profile page provide an option to delete account</li>
   <li> require a second confirmation for account deletion</li>
   <li>develop method to delete the account when the user requests it to be deleted – will need to keep order history separately for company records</li>
   </ul>

<br>

#### User Story: home page content

   As a user, I would like to see an engaging landing page, with an attractive hero image and a bigger picture of what the website has to offer, so that I can make more informative decisions in an engaging way

   Acceptance Criteria
   <ul>
   <li>Given That I am on the landing page
When I enter the site
Then An enterprising and engaging image is displayed</li>
   <li>Given That I am on the landing page
When I enter the site
Then I know immediately what I can do as it is displayed simply and descriptivel</li>
<li>Given that I am on the landing page
When I look into the landing page
Then I know where I can go and what I can do</li>
   </ul>

   Tasks
   <ul>
   <li>Add Hero image and a shop now button for immediate action</li>
   <li>Add niche product sections (divs) to give some insight into that particular product</li>
   <li>Add necessary Information regarding the site that is display immediately(free delivery, sales, etc.)</li>
   </ul>

<br>

#### User Story: Reviews

   As a user, I can add review to products, so that I can give my thoughts on the product

   Acceptance Criteria
   <ul>
   <li>Given That i am a user
When I click add a review
Then I can add text content to give a review.</li>
   <li>Given That i am a user
When I want to delete my review
Then I have the ability to by clicking on delete</li>
<li>Given That i am a user
When I want to edit my comment
Then I have the ability to by clicking on edit</li>
   </ul>

   Tasks
   <ul>
   <li>Add a reviews section under the product</li>
   <li> Add Create/Edit/Delete functionality</li>
   </ul>

<br>

#### User Story: Headline Update

   As a site owner, I can edit the text content on the landing page, so that I can let user know new information

   Acceptance Criteria
   <ul>
   <li>Given that i am a site owner
When There is a notification/news i want users to know
Then It is displayed on the home page</li>
   <li>Given that i am a site owner
When I want to edit the text content
Then I can go to a page and edit it</li>
   </ul>

   Tasks
   <ul>
   <li>Implement a form to edit the content</li>
   <li>Add a section in the landing page to edit content</li>
   <li>Restrict the size of the content</li>
   </ul>


<br>
<br>

## The Skeleton Plane
### Wireframe mock-ups
Wireframes were produced for the major pages including the landing page, the display of products, the details of the products and the checkout page. Through the creation of the project, some aspects of the wireframes have been changed.

<br>

Primary Landing Page
<br>
![Primary landing page](documentation/yugen-primary-landing.png)
<br>
Alternative Landing Page
<br>
![Alternative landing page](documentation/yugen-alternative-landing.png)
<br>
Products Page
<br>
![Products Page](documentation/wf-products.png)
<br>
Product Details Page
<br>
![Product Details Page](documentation/wf-detail.png)
<br>
Checkout Page
<br>
![Checkout Page](documentation/wf-checkout.png)
<br>


### Social Media Marketing

Facebook was used as an extension for social media marketing for this website, if still active this is the facbook business page [Yugen](https://www.facebook.com/profile.php?id=61561504131258)

Here are the screenshots of the page.

![FaceBook page 1](documentation/fb-2.png)

<br>

![FaceBook page 2](documentation/fb-1.png)

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

#### Keywords
These are the keywords implemented into the project. From this research a refined keyword list was cultivated for use with the short-tail keywords within the head meta tags and for content through out the site.
<br>

* japanese-artworks

<br>

* japanese-merchandise 

<br>

* japanese-inspired-gifts

<br>

* japanese-gifts

<br>

* anime-artworks 

<br>

* modern-japanese-artworks

<br>

* traditional-japanese-arworks 

<br>

* anime-decoration

<br>

* buy-japanese-artwork-decoration

<br>

* gifts-for-anime-lovers

<br>

#### Content Strategy


## The Surface Plane

### Design

The simpicity of a clear white background was user with dark fonts and borders over containers and text, this was to not take away from the colour of the images displayed. The Header, Footer and Reviews section implemented a light gray color (rgba(211, 211, 211, 0.5)) to represet the use of watercolours used in jaanese paintings. Dark text and borders were also used over this background colour for overall effect. Buttons implemented a bark or light hover to represent the action of what is happeneing more clearly.

<br>

### Typography 

Two different fonts were utilised for the site. The main headings font of Sedan SC and the smaller text font of Urbanist were selected for their Elegant and clear (Sedan SC) feel and simple and clear (Urbanist) feel whilst sans-serif was chosen a backup if the other fonts are not displayed.


##### Images

Product and background images were acquired from free image sites [Pixabay](https://pixabay.com/), [UPicjumbo](https://picjumbo.com/) and [Google](https://www.google.com/).


## Features

### Landing Page
This is the landing page of the website, where users are introduced to brief yet insightfull information of the site, as the user scrolls down, the user can see the categories displayed via images (Traditional, modern, anime) where there is a shop now button to see products of that category. The last section is the mailchimp section where users can sign up to the newsletter. 
<br>

![Landing Page](documentation/landing.png)

<br>

![Landing Page traditonal](documentation/traditional.png)

<br>

![Landing Page modern](documentation/modern.png)

<br>

![Landing Page anime](documentation/anime.png)

<br>

![Landing Page mailchimp](documentation/mailchimp.png)

<br>

<br>

### Products
This page displays an array of prducts, where users can filter through product by name, price and category, where the range alters according to the filter, cliccking on the image will take you to the product details page.
<br>

![Products](documentation/products.png)

<br>

### Shoping bag
The shopping bag gives a list of all the products selected in the store, and giving the option to change the quantity or remove items. It also gives the grand total at the bottom and a button to proceed to checkout.
<br>

![Shoping bag](documentation/bag.png)

<br>

### Checkout
The checkout is where users can pay for their items using the checkout form, if details are edited or saved in the profile, these changes will show up on this page too.
<br>

![Checkout](documentation/checkout.png)

<br>

### Product-deatil
A detailed explaination of the product, from its name, category, price and description where users can also click on the image to open another page to get a bigger look at the product. It also give the option to add to favorites, increase or decrease the quantity desired.
<br>

![Product-deatil](documentation/detail.png)

<br>

### Product-review
A section on the product-detail page where users can leave reviews of products and delete their own reviews.
<br>

![Product-review](documentation/review.png)

<br>

### Favorites
A feature where users can bookmark or make some products their favorites and it is kept on this page where they have access to it in their account
<br>

![Favorites](documentation/favorites.png)

<br>

### Product-management
A page in the site when admin can add, edit or delete products in yugen to keep everything up to date.
<br>

![Product-management](documentation/product-management.png)

<br>

### Update-management
A page when admin of the site can change the update text in the homw page to let users know of more or useful information about the store, products or anything related to yugen
<br>

![Update-management](documentation/update-management.png)

<br>

### Profile
A users profile details of their billing address and past history purchases
<br>

![Profile](documentation/profile.png)

<br>

### Order-confirmation
A detailed summary of their details and orders after purchasing an item or items.
<br>

![Order-confirmation](documentation/orderconfirm.png)

<br>

### sign in
Users can sign in via the sign in form if signed out
<br>

![sign in](documentation/signin.png)

<br>

### sign-out
Users can sign out via the sign out form when they are signed in
<br>

![sign-out](documentation/signout.png)

<br>

### sign-up
Users can create an account via the sign up form
<br>

![sign-up](documentation/signup.png)

<br>

### password
There is a reset password option if a user has forgotten their password, which lets the user reset their password via email confirmation
<br>

![password](documentation/password.png)

<br>

### Header
The header displays most of the sites functionality, from searching, access to the shopping bag page, the dropdown menu for the user accounts, the filter search of traditional, modern and anime and the Logo, which when clicked takes you back to the home page.
<br>

![Header](documentation/header.png)

<br>

### Footer
The footer displays links to facebook and github. The footer is at the bottom of every page.
<br>

![Footer](documentation/footer.png)

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
* The walkthrough project Botuiqe Ado, from Code Institue for the overall and general layout of code and how to go about an Ecommerce Website.
* The walkthrough project Codestar, from Code Institue for ways to go about doing the Reviews section.
* [Druid](https://github.com/MattBCoding/druid-pp5) by Matt Bodden, for inspiration of how to go about the project, the Kanban Board and Readme file.
* [Wordsmith](https://github.com/SerJosh/wordsmith) by myself Joshua Ronan, for guidlines on how to go about the implementation of django-allauth and other parts of the project.
* [Djando-simple-blog-app](https://github.com/veryacademy/YT-Django-Simple-Blog-App-Part10-User-Favourties-Save) by very academy, for guidelines on how to go about favorites and reviews.
 


### Acknowledgements

I'd like to thank the following:
* 
* 
