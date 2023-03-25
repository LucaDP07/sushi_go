# Sushi Go

**SITE OVERVIEW**
- - - 

Sushi Go is a small sushi bar serving fresh sushi to the city of Cork. The site is targeted towards users who are sushi lovers or simply want to try something tasty and delicious and see it delivered at their door.
Users can browse and choose a range of selected sushi and place their own order which will be delivered where they want in town. They can also drop their feedback and help the site admin to improve the service. The website utilises Stripe as the payment processor. The website has also an elegant appearance, providing a clear and easy navigation.


![Alternate text](/static/images/responsive.png)

You can view the deployed website [here](https://sushi-go.herokuapp.com/).

**UX**
- - -

**User Goals**

- Easily find the dishes they like.
- A smooth navigation and an easy checkout experience.
- The opportunity to have a personal area where to store personal details and create a wish list.

**Site Owners goals**

- Menu can be managed through a dedicated personal area.
- Non registered users are not able to leave a review of the service.
- Reviews can be controlled through the admin area to avoid an inappropriate use of the website.

**Epic and User Stories**

There are 5 EPICS and 21 USER STORIES.

1.EPIC: Viewing and Navigation
- USER STORIES: 
1. As a website user I can navigate around the site so that I can find the desired content.(Site Browsing #1)
2. As a website user I can View a list of dishes so that I can choose accordingly.(Products #2)
3. As a website user, I can view a specific category of dishes so I can browse the type of meal I'm looking for.(Category #3)
4. As a website user, I can Click on a dish to read and view the full details so that I understand what I can get.(Food Details #4)
5. As a website user, I can read reviews left by others so I see the feedback provided.(View Reviews #5)
6. As a website user, I can see a list of markets the business takes part so that I can **easily find them in town".(Markets #6)

2.EPIC: User Account and Profile
- USER STORIES:
1. As a website user, I can Register for an account so that I can benefit from the services offered to members.(Account Registration #7)
2. As a logged in user, I can Save my personal details in my profile so that I do not have to fill them out for future orders.(Save personal details in User Profile #8)
3. As a logged in user, I can login and logout from the website so that I can keep my account secure.(Login & Logout #19)

3.EPIC: User Interaction
- USER STORIES:
1. As a logged in user, I can create my personal wish list on my personal account so that I can remember my favourite dishes.(Wishlist #9)
2. As a logged in user, I can Review the service purchased so that I can inform potential customers of what they might expect.(CRUD Reviews #10)
3. As a logged in user, I can View my order history so that I can remember what purchases I've made.(Order History #13)
4. As a website user, I can send a message to the business so that I can ask questions or share my opinion about the service with the site’s owner.(Contact Us Page #15)
5. As a website user, I can sign up for the website's newsletter so that I can keep up to date with new promotions.(Newsletter Sign-Up #17)

4.EPIC: Purchasing
- USER STORIES:
1. As a website user, I can Make an order by using the website checkout system so that I can complete my purchase.(Checkout #18)
2. As a logged in user, I can adjust a number of meals in different quantities to my basket so that I can easily make changes before I purchase(Adjust Number of Items #20)
3. As a website user, I can add the quantity of individual meals in my basket so that I can complete the purchase when I am ready.(Add items to the basket #21)
4. As a website user, I can view the contents of my basket at any time so that I can see what is included and the total cost.(View Basket #22)
5. As a website user, I can view an order confirmation after checkout and receive an email confirmation of my order so that I know my purchase was successful.(Order confirmation message and email #23)

5.EPIC: Admin, Marketing & Store Management
- USER STORIES:
1. As a website Superuser, I can create and publish a new dish so that I can update my menu.(Menu Management #26)
2. As a website Superuser I can provide  the opportunity for the user to register for a newsletter so that I can build a stronger and more personal relationship with customers.(Create a Newsletter subscription #31)

**Strategy**

For the development of the website the Agile methodology was taken using GitHub functions which are issues, milestones, iterations and Kanban board.

1.Milestones were used to create Epics with a custom template.

2.Issues were used to create User Stories with a custom template. Eash user story has been mapped out using the Kanban board format. Each one has acceptance criteria and tasks.
Each user story was linked to an Epic.

**Web Marketing Strategy**
- - -

- Email Marketing: MailChimp Newsletter 
In order to increase engagement with the site and build a stronger relationship with its customers, the Sushi Go Team partnered with MailChimp. This is a free service to collect customers email addresses and share news, services and special offers with customers and potential customers. The feature is located on the Footer, visible in every page. The customers have the opportunity to enter their address to subscribe and get a success message once the subscription is completed. No registration to the Sushi Go website is required to benefit of this service.
Below is a screenshot of the Sushi Go - Mailchimp dashboard.

- Social Media Marketing: Facebook Page
In order to increase traffic to the website, the Sushi Go Team has created a Facebook Business Page for organic social media marketing. The decision was taken considering the impact of the social media platform on the Irish people. We can see that in 2023 3.51 millions of irish out of 5.1 is using Facebook, and for this reason it's still considered a great option to promote the business online.

- Search Engine Optimization(SEO)
The meta keywords and description in the site's base.html have been chosen after a keywords research conducted through Ubersuggest by Neil Patel, a SEO and content marketing tool.
For SEO purposes, a sitemap.xml and robots.txt file were included to the website's root directory to improve the quality of the website and to ensure that search engines are able to understand its structure.

**Structure**

The users will first see the Home Page, where they can find a call to action button to start exploring the menu. A navbar is also available and give access to all the necessary info.

Both registered and unregistered users can place their own order and complete the checkout process, but only registered users can interact with the page by creating their personal wish list, leaving a feedback or updating their own profile details.

Simply by clicking on "View details" more information about the dish will be revealed and a "Add to basket" button will also be available.

The "Wish list" page is accessible only for registered users. This page can be accessed by clicking the 'Wish list' button in the navigation bar, which is only visible for a registered user. After completing the log in, the user will see a "Add to wish list" button on the menu page, right under the "View details" button and the picture of the dish. Users are then able to edit their own wish list as they like.

**WIREFRAMES**
- - -

**Home Page: Desktop - Not logged in view**

![Alternate text](/static/images/Home%20-%20Desktop%20-%201.png)

**Second Page: Desktop - Not logged in view**

![Alternate text](/static/images/Second%20page%20-%20Desktop.png)

**Home Page: Desktop - Logged in view**

![Alternate text](/static/images/Home-Desktop%20-%202.png)

**Post Page: Desktop - Not logged in view**

![Alternate text](/static/images/Article%20Page%20-%20Desktop%20-%201.png)

**Post Page: Desktop - Logged in view**

![Alternate text](/static/images/Article%20Page%20-%20Desktop%20-%202.png)

**Add Trip Form: Desktop**

![Alternate text](/static/images/Add%20trip%20form.png)

**Home Page: Mobile**

![Alternate text](/static/images/Home%20-%20Mobile.png)


**FEATURES**
- - -

 - NavBar and SearchBar
 
 The navigation menu is clear and consistent throughout the site to provide the users an easy navigation. Links to the Menu Page, Testimonials Page, Contact Page, Markets Page, Privacy Policy, Basket Page, Search bar, Register and Sign In/Out are available. If the user is not signed in the Sign in and Register links are visible in the navbar. If the user is signed in the Sign In and Register links are replaced by a Sign Out, Profile and a Wish List link. While the Account and Basket icons will be always displayed in any screen, the other links that the user can find in the bar, will switch to hamburger on tablets and mobiles.

 ![Alternate text](/static/images/navbar.png)

 - Footer

At the bottom of the page we can find the footer with the links to direct the user to the Facebook, Instagram, LinkedIn and Twitter pages. The name of the Company and the address is also visible. The footer is available on all site pages.
 
 ![Alternate text](/static/images/footer.png)

 - Home Page

 A background image is displayed at the center, between the Navbar and the footer, with a Call to action button also available.

![Alternate Text](/static/images/home_page.png)

- Menu section
 
When clicking the 'Menu' link in the navbar the dropdown menu will show all the different categories including 'Nigiri', 'Osomaki','Sashimi', 'Temaki', 'Tempura', 'Okura Special Roll', 'Noodles' and 'Side dishes'. There is also the option to select 'All' and see the whole menu displayed.
Each card shows an image of the dish, its title, rating and price.
If the user is a superuser, edit and delete buttons will be available at the bottom of the card.

 ![Alternate text](/static/images/trips_section.png)

 - Food detail
 
By clicking on an individual card the user get access to the Food detail page, which provides additional information about the dish.
The quantity buttons are located right under the description and can be used to add items to the basket.
The plus and minus buttons increase and decrease the input value.
Clicking the 'Add to Basket' button adds that amount of food selected to the basket.
Clicking the 'Back to Menu' button takes the user back to the Menu page.

 ![Alternate text](/static/images/form.png)
 
 - Basket Page
 
The Basket Page allows the user to view a summary of the items in the basket and their total prices.
Users can change the quantity of the food in the basket or remove it entirely, before proceeding to the secure checkout page. Underneath the grand total a message will be displayed, informing the users of how much more they need to spend in order to receive free delivery if they haven't already met the free delivery threshold (€30). Also a button to enable the users to go "Back to Menu' and add further items to their basket is available. 

 ![Alternate text](/static/images/post_detail.png)

 - Checkout Page
In order to complete place an order and complete the checkout process, there's no need to be registered with Sushi Go.
However, only registered users can save their info for future orders, if they wish so.
The checkout page is simple and easy to use. It also allows the user to take a look at the "Order Summary" before submit their credit card details.

 ![Alternate text](/static/images/comments_section.png)

- Checkout Success Page
Once the order has been processed, a checkout success page is loaded to inform the user the order was successful.
An email with the order confirmation is also sent to the user.

 ![Alternate text](/static/images/comments_section.png)

- Wish List
By clicking on the 'Account' link in the navbar, if signed in, a user can benefit of the wish list feature. Thanks to it the user will have the opportunity to add a dish to the wish list for a future purchase. An option to remove the dishes selected from the wish list is also available.

 ![Alternate text](/static/images/comments_section.png)

- Testimonials
By clicking on the link in the NavBar, the user will access to the Testimonials page. Unregistered users will be able to read all the reviews left by others, while registered users will also be able to create their own review and see it displayed with their username and the date of submission.

 ![Alternate text](/static/images/comments_section.png)

 - Add Review Page
 In the Testimonials page users will find a "Add your review" button. If not signed a Sign In page will display. If signed a form opens and the user can enter all the fields to add a review which will be displayed on the website.

 ![Alternate text](/static/images/comments_section.png)

 - Edit Review Page

The Edit review page is accessed by the Edit button, made available beside the review itself and visible only to its owner, so that it can only be edited by its own user or by superuser using the admin page. If the user confirms the changes made to the review, will be redirected to the Testimonials page and a message will show below the navbar to inform that the review was succesfully edited.

 ![Alternate text](/static/images/comments_section.png)

 - Delete Review Page

 The owner of the review also have another button available, which is the Delete button. If the user clicks on it a Delete Review page displays and asks the user for confirmation to delete the review. Users can either click on "Delete" or cancel and go back to the Testimonials Page. 
 If the user confirms to delete the review, will be redirected to the Testimonials Page and a message will show below the navbar to inform that the review was deleted.

 ![Alternate text](/static/images/edit_delete.png)

 - Register Page

 This page can be opened from the register button in the navigation bar. New visitors are asked to enter username, email, email confirmation, password and password confirmation to register. Once successfully registered, users will be asked to check their email to confirm their registration and have access to all the features available for registered users.

 ![Alternate text](/static/images/signup.png)

 - Sign In Page

 The Sign In button can be accessed to login. Username and password will be required. On successful login, users will be redirected to the Home Page and a message to inform them that they logged in successfully will be displayed under the navigation bar.

 ![Alternate text](/static/images/signin.png)

 - Sign Out Page

 Once a user is logged in, the Sign In button in the navigation bar will be replaced with the Sign Out button. If they want to sign out all they need to do is simply click this button and confirm their decision. Once again, users will be redirected to the Home Page and a message to inform them that they sign out successfully will be displayed under the navigation bar.

 ![Alternate text](/static/images/signout.png)

 - Markets Page
By clicking on the "About" button in the NavBar, the user has the opportunity to select the Markets page and see all the local markets Sushi Go collaborate with. This is an opportunity for the user to know where to find in town their favourite sushi, while around. Each card contains the name of the market, a picture of it and a link to its official page with all the important info.

![Alternate text](/static/images/signout.png)

 - Contact Us Page

By clicking on the "About" button in the NavBar, the user has the opportunity to select the "Contact Us" feature. Registered and not registered users can benefit of this option.
If the user is logged in, the email field is prepopulated with the user's email address.
The form contains all the fields required to submit the contact request. If any of these fields are left blank or with just whitespace then an error message will appear on that particular field, notifying the user of the issue.
Once the form is submitted, the user receives an email confirmation of their request so that they have a record of it.

![Alternate text](/static/images/signout.png)

- Privacy Policy
The "About" button also contains a link to the Sushi Go Privacy Policy, to ensure that the website is compliant with the European Privacy Policy Rules.

![Alternate text](/static/images/signout.png)

- User Profile
The 'Account' link in the navbar, allows the signed in users to acces their own profile and update their saved delivery details and view order history. Each transaction contains all the necessary info. The 'Order Number' can be clicked to open the order confirmation page.

![Alternate text](/static/images/signout.png)

- Admin - Menu Management
If logged in, super users can access to the "Menu Management" page via the "Account" button. Thanks to this feature the Admin can update the menu selection by adding new dishes to the offer, without accessing to the admin area. Once logged in, the Admin can also edit or delete a dish within the Food Details page, thanks to the specific 'Edit' or 'Delete' buttons.

![Alternate text](/static/images/signout.png)
 

**TECHNOLOGIES USED**
- - -

- HTML: HTML has been used to give structure and content to the website.
- CSS: In order to style the content created with HTML, and give responsiveness to the pages, the CSS language has been used.
- Java Script: JS was used with Bootstrap to provide interaction on the front-end.
- Python: It was used to code the back end of the project.
- Pixabay: I used this platform for all the images displayed around the website.
- Bootstrap: Bootstrap was used to style the website, add responsiveness and interactivity.
- Cloudinary: Cloudinary was used for hosting the images.
- Balsamiq Wireframes: I used it to produce low fidelity wireframes to organise the structure of the pages.
- Gitpod was used to develop the project.
- GitHub was used to host repository.
- Heroku was used to deploy the website.
- Django was used as the main python framework for the development of the project.
- Django AllAuth was used to provide user account management functionality.
- Google Chrome Dev Tools was used to check reponsiveness.


**TESTING**
- - - 
Manual testing was carried out to ensure the site works as intended.

All the pages of the website have ben tested using the developer tools in Google Chrome. The code had to be changed along the process in order to achieve the responsiveness required for the project. The preview from Gitpod helped to constantly check all the changes made.

Testing was performed using a MacBook Air (M1, 2020) on macOS Monterey with the following browsers:
- Google Chrome 102.0.5005.61
- Safari 15.3
- Mozilla Firefox 101.0.1

After testing the website I can confirm the project it's responsive in its all pages and works properly on all standard screen sizes.

The forms are working in each section of the project.
- The users can add, edit and delete their own posts.
- Comments can be added through the comment form. To be displayed need to be approved by the owner of the website.


* VALIDATOR TESTING

HTML: No errors were returned when passing through the official W3C Validator.

![Alternate text](/static/images/html_responsive.png)

CSS: No errors were returned when passing through the official (Jigsaw) Validator.

![Alternate text](/static/images/css_responsive.png)

All the .py files are validated in the PEP8 online validator replacement provided by Code Institute. No errors detected.

- admin.py

![Alternate text](/static/images/admin.png)

- apps.py

![Alternate text](/static/images/apps.png)

- forms.py

![Alternate text](/static/images/forms.png)

- models.py

![Alternate text](/static/images/models.png)

- urls.py

![Alternate text](/static/images/urls.png)

- views.py

![Alternate text](/static/images/views.png)

 
- UNFIXED BUGS

No unfixed bugs.

**DEPLOYMENT**
- - -
The site was deployed via Heroku. These are the steps I followed:

- In the Heroku dashboard, click "New" and then "Create new app". After that enter the app name and specify the region.

- In the Heroku dashboard click on the Resources tab
Scroll down to Add-Ons, search for and select 'Heroku Postgres'.

- In the setting tab, click on Reveal Config Vars button then copy the value for DATABASE_URL key.

- In Gitpod create a new env.py file and import the os library. Heroku Config vars need to be set accordingly including DATABASE_URL and SECRET_KEY.

- In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url
- Insert the line if os.path.isfile("env.py"): import env
- Remove the insecure secret key that django has in the settings file by default and replace it with SECRET_KEY = os.environ.get('SECRET_KEY')
- Replace the databases section with DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))}
- In the Gitpod terminal, migrate the change by python3 manage.py migrate.
- Login to Cloudinary and copy the API Environment variable and paste in env.py and also Config Vars in Heroku.
- In Heroku config vars add DISABLE_COLLECTSTATIC with value of '1' (this must be removed for final deployment)
- Add Cloudinary libraries to installed apps section of settings.py as per follow:

- - Add 'cloudinary_storage', before 'django.contrib.staticfiles', and 'cloudinary' right after it.

- In the Settings.py file - add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.

- Set TEMPLATES_DIR just below BASE_DIR and insert TEMPLATES_DIR in TEMPLATES array 'DIRS': []

- Set ALLOWED_HOSTS as 'traveldream.herokuapp.com', 'localhost'

- Create Procfile and add the code: web gunicorn traveldream.wsgi
- On GitHub add, commit and push the changed files.
- On Heroku click on the Deploy tab, connect to GitHub and search for the repository then Connect
- Click on Deploy Branch.
- Once the development process is complete, change the debug setting to: DEBUG = False in settings.py.
- Considering for this project the summernote editor was used in Heroku add: X_FRAME_OPTIONS = 'SAMEORIGIN' to settings.py.
- In Heroku settings config vars change the DISABLE_COLLECTSTATIC value to 0.
- Click on Deploy Branch. When the app is deployed a message 'Your app was successfully deployed' will be shown. Click 'view' to see the deployed app in the browser.

During my work to the project, I had to migrate my database from Heroku to ElephantSQL. Here are the stpes I've taken:

- Create and account with ElephantSQL.
- Create New Instance, specify the region, select a data center near my location, click review and click "Create Instance"
- In the ElephantSQL dashboard click on the database instance name for this project(traveldream).
- In the URL section copy the database URL.
- In the env.py file replace the DATABASE_URL variable with the the relevant string from ElephantSQ.
- Run the migration command in the terminal to migrate the database structure to the newly-connected ElephantSQL database.


**CREDITS**
- - - 

**Content**

- The Navigation bar, the comments form and the index were inspired by the [I Think Therefore I Blog](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/fe4299adcd6743328183aab4e7ec5d13/) Project.

- Full CRUD functionality application was achieved thanks to [CODEMY](https://www.youtube.com/@Codemycom).

- Text posts has been taken by [Lonely Planet](https://www.lonelyplanet.com/).


**Media**

- Screenshot under the section "site overview" was created with [Am I responsive](https://ui.dev/amiresponsive).

- Pictures used for the website have been taken from [Pixabay](https://pixabay.com/).

- The wireframes have been created using [Balsamiq Wireframes](https://balsamiq.com/wireframes/).