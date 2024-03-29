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
6. As a website user, I can see a list of markets the business takes part so that I can easily find them in town.(Markets #6)

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
2. As a website user, I can adjust a number of meals in different quantities to my basket so that I can easily make changes before I purchase(Adjust Number of Items #20)
3. As a website user, I can add the quantity of individual meals in my basket so that I can complete the purchase.(Add items to the basket #21)
4. As a website user, I can view the contents of my basket at any time so that I can see what is included and the total cost.(View Basket #22)
5. As a website user, I can view an order confirmation after checkout and receive an email confirmation of my order so that I know my purchase was successful.(Order confirmation message and email #23)

5.EPIC: Admin, Marketing & Store Management
- USER STORIES:
1. As a website Superuser, I can create and publish a new dish so that I can update my menu.(Menu Management #26)
2. As a website Superuser I can provide  the opportunity for the user to register for a newsletter so that I can build a stronger and more personal relationship with customers.(Create a Newsletter subscription #31)

**Strategy**

For the development of the website the Agile methodology was taken using GitHub functions which are issues, milestones, iterations and Kanban board.

1. Milestones were used to create Epics with a custom template.

2. Issues were used to create User Stories with a custom template. Eash user story has been mapped out using the Kanban board format. Each one has acceptance criteria and tasks.
Each user story was linked to an Epic.

**Web Marketing Strategy**
- - -

- Email Marketing: MailChimp Newsletter 
In order to increase engagement with the site and build a stronger relationship with its customers, the Sushi Go Team partnered with MailChimp. This is a free service to collect customers email addresses and share news, services and special offers with customers and potential customers. The feature is located on the Footer, visible in every page. The customers have the opportunity to enter their address to subscribe and get a success message once the subscription is completed. No registration to the Sushi Go website is required to benefit of this service.
Below is a screenshot of the Sushi Go - Mailchimp dashboard.

![Alternate text](/static/images/newsletter.png)

- Social Media Marketing: Facebook Page
In order to increase traffic to the website, the Sushi Go Team has created a Facebook Business Page for organic social media marketing. The decision was taken considering the impact of the social media platform on the Irish people. We can see that in 2023 3.51 millions of irish out of 5.1 is using Facebook, and for this reason it's still considered a great option to promote the business online.

![Alternate text](/static/images/stats.png)

Below we can see the Facebook Page created for this project.

![Alternate text](/static/images/facebook.png)

- Search Engine Optimization(SEO)
The meta keywords and description in the site's base.html have been chosen after a keywords research conducted through [Ubersuggest](https://neilpatel.com/ubersuggest/) by Neil Patel, a SEO and content marketing tool.
For SEO purposes, a sitemap.xml and robots.txt file were included to the website's root directory to improve the quality of the website and to ensure that search engines are able to understand its structure.

**Structure**

The users will first see the Home Page, where they can find a call to action button to start exploring the menu. A navbar is also available and give access to all the necessary info.

Both registered and unregistered users can place their own order and complete the checkout process, but only registered users can interact with the page by creating their personal wish list, leaving a feedback or updating their own profile details.

Simply by clicking on "View details" more information about the dish will be revealed and a "Add to basket" button will also be available.

The "Wish list" page is accessible only for registered users. This page can be accessed by clicking the 'Wish list' button in the navigation bar, which is only visible for a registered user. After completing the log in, the user will see a "Add to wish list" button on the menu page, right under the "View details" button and the picture of the dish. Users are then able to edit their own wish list as they like.

**WIREFRAMES**
- - -

**Home Page**

![Alternate text](/static/images/home2.png)

**Menu Page**

![Alternate text](/static/images/menu2.png)

**Menu Page: Logged in view**

![Alternate text](/static/images/logged.png)

**Food Details Page**

![Alternate text](/static/images/detail.png)

**Check Out Page**

![Alternate text](/static/images/checkout2.png)

**Basket Page**

![Alternate text](/static/images/basket2.png)

**Contact Page**

![Alternate text](/static/images/contact2.png)

**Testimonials Page**

![Alternate text](/static/images/testimonials2.png)

**Markets Page**

![Alternate text](/static/images/markets2.png)



**FEATURES**
- - -

- NavBar.
 
The navigation menu is clear and consistent throughout the site to provide the users an easy navigation. Links to the Menu Page, Testimonials Page, Contact Page, Markets Page, Privacy Policy, Basket Page, Search bar, Register and Sign In/Out buttons are available. If the user is not signed in the Sign in and Register links are visible in the navbar. If the user is signed in the Sign In and Register links are replaced by a Sign Out, Profile and a Wish List link. While the Account and Basket icons will always be displayed in any screen, the other links that the user can find in the bar, will switch to hamburger on tablets and mobiles.

![Alternate text](/static/images/navbar.png)

- Footer.

At the bottom of the page we can find the footer with the newsletter signup form and links to direct the user to the Facebook, Instagram, LinkedIn and Twitter pages. The name of the Company and the address is also visible. The footer is available on all site pages.
 
![Alternate text](/static/images/footer.png)

- Home Page.

A background image is displayed at the center, between the Navbar and the footer, with a Call to action button also available.

![Alternate Text](/static/images/homepage.png)

- Menu section
 
When clicking the 'Menu' link in the navbar the dropdown menu will show all the different categories including 'Nigiri', 'Osomaki','Sashimi', 'Temaki', 'Tempura', 'Okura Special Roll', 'Noodles' and 'Side dishes'. There is also the option to select 'All' and see the whole menu displayed.
Each card shows an image of the dish, its title, rating and price.
If the user is a superuser, edit and delete buttons will be available at the bottom of the card.

![Alternate text](/static/images/menu.png)

- Food detail page
 
By clicking on an individual card the user get access to the Food detail page, which provides additional information about the dish.
The quantity buttons are located right under the description and can be used to add items to the basket.
The plus and minus buttons increase and decrease the input value.
Clicking the 'Add to Basket' button adds that amount of food selected to the basket.
Clicking the 'Back to Menu' button takes the user back to the Menu page.

![Alternate text](/static/images/fooddetail.png)
 
- Basket Page
 
The Basket Page allows the user to view a summary of the items in the basket and their total prices.
Users can change the quantity of the food in the basket or remove it entirely, before proceeding to the secure checkout page. Underneath the grand total a message will be displayed, informing the users of how much more they need to spend in order to receive free delivery if they haven't already met the free delivery threshold (€30). Also a button to enable the users to go "Back to Menu' and add further items to their basket is available. 

![Alternate text](/static/images/basket.png)

- Checkout Page

To place an order and complete the checkout process, there's no need to be registered with Sushi Go.
However, only registered users can save their info for future orders, if they wish so.
The checkout page is simple and easy to use. It also allows the user to take a look at the "Order Summary" before submit their credit card details.

![Alternate text](/static/images/checkout.png)

- Checkout Success Page

Once the order has been processed, a checkout success page is loaded to inform the user the order was successful.
An email with the order confirmation is also sent to the user.

![Alternate text](/static/images/checkout_success.png)

- Wish List

By clicking on the 'Account' link in the navbar, if signed in, a user can benefit of the wish list feature. Thanks to it the user will have the opportunity to add a dish to the wish list for a future purchase. An option to remove the dishes selected from the wish list is also available.

![Alternate text](/static/images/wishlist.png)

- Testimonials

By clicking on the link in the NavBar, the user will access to the Testimonials page. Unregistered users will be able to read all the reviews left by others, while registered users will also be able to create their own review and see it displayed with their username and the date of submission.

![Alternate text](/static/images/testimonials.png)

- Add Review Page

In the Testimonials page users will find a "Add your review" button. If not signed a Sign In page will display. If signed a form opens and the user can enter all the fields to add a review which will be displayed on the website.

![Alternate text](/static/images/add_review.png)

- Edit Review Page

The Edit review page is accessed by the Edit button, made available beside the review itself and visible only to its owner, so that it can only be edited by its own user or by superuser. If the user confirms the changes made to the review, will be redirected to the Testimonials page and a message will show below the navbar to inform that the review was succesfully edited.

![Alternate text](/static/images/edit_review.png)

- Delete Review Page

The owner of the review also have another button available, which is the Delete button. If the user clicks on it a Delete Review page displays and asks the user for confirmation to delete the review. Users can either click on "Delete" or cancel and go back to the Testimonials Page. 
If the user confirms to delete the review, will be redirected to the Testimonials Page and a message will show below the navbar to inform that the review was deleted.

![Alternate text](/static/images/delete_review.png)

- Register Page

This page can be opened from the register button in the navigation bar. New visitors are asked to enter username, email, email confirmation, password and password confirmation to register. Once successfully registered, users will be asked to check their email to confirm their registration and have access to all the features available for registered users.

![Alternate text](/static/images/register.png)

- Sign In Page

The Sign In button can be accessed to login. Username and password will be required. On successful login, users will be redirected to the Home Page and a message to inform them that they logged in successfully will be displayed under the navigation bar.

![Alternate text](/static/images/signin.png)

- Sign Out Page

Once a user is logged in, the Sign In button in the navigation bar will be replaced with the Sign Out button. If they want to sign out all they need to do is simply click this button and confirm their decision. Once again, users will be redirected to the Home Page and a message to inform them that they sign out successfully will be displayed under the navigation bar.

![Alternate text](/static/images/signout.png)

- Markets Page

By clicking on the "About" button in the NavBar, the user has the opportunity to select the Markets page and see all the local markets Sushi Go collaborate with. This is an opportunity for the user to know where to find in town their favourite sushi, while around. Each card contains the name of the market, a picture of it and a link to its official page with all the important info.

![Alternate text](/static/images/markets.png)

- Contact Us Page

By clicking on the "About" button in the NavBar, the user has the opportunity to select the "Contact Us" feature. Registered and not registered users can benefit of this option.
If the user is logged in, the email field is prepopulated with the user's email address.
The form contains all the fields required to submit the contact request. If any of these fields are left blank or with just whitespace then an error message will appear on that particular field, notifying the user of the issue.
Once the form is submitted, the user receives an email confirmation of their request so that they have a record of it.

![Alternate text](/static/images/contact_us.png)

- Privacy Policy

The "About" button also contains a link to the Sushi Go Privacy Policy, to ensure that the website is compliant with the European Privacy Policy Rules.

![Alternate text](/static/images/privacy_policy.png)

- User Profile

The 'Account' link in the navbar, allows the signed in users to acces their own profile and update their saved delivery details and view order history. Each transaction contains all the necessary info. The 'Order Number' can be clicked to open the order confirmation page.

![Alternate text](/static/images/profile.png)

- Admin - Menu Management

If logged in, super users can access to the "Menu Management" page via the "Account" button. Thanks to this feature the Admin can update the menu selection by adding new dishes to the offer, without accessing to the admin area. Once logged in, the Admin can also edit or delete a dish within the Food Details page, thanks to the specific 'Edit' or 'Delete' buttons.

![Alternate text](/static/images/menu_management.png)

- Page 404 - Page Not Found

In case of any typing URL error or if the page the user is looking for doesn't exist, this Error page will be displayed and a link to the Home page will be available to allow the user to get back to the Sushi Go website.

![Alternate text](/static/images/error_page.png)


**TECHNOLOGIES USED**
- - -

- HTML: HTML has been used to give structure and content to the website.
- CSS: In order to style the content created with HTML, and give responsiveness to the pages, the CSS language has been used.
- Java Script: JS was used with Bootstrap to provide interaction on the front-end.
- Python: It was used to code the back end of the project.
- Pixabay: I used this platform for the background image displayed on the Home page.
- Bootstrap: Bootstrap was used to style the website, add responsiveness and interactivity.
- AWS: Amazon Web Services was used for hosting static and media files for the website.
- Balsamiq Wireframes: I used it to produce low fidelity wireframes to organise the structure of the pages.
- Mailchimp: To create the newsletter signup form.
- Stripe: To process all online and credit card purchases on the website.
- Font Awesome: was used for all the icons on the website.
- Compressor - was used to compress images.
- Gitpod was used to develop the project.
- GitHub was used to host repository.
- Heroku was used to deploy the website.
- ElephantSQL was used to provide a configured and optimized PostgreSQL database.
- Django was used as the main python framework for the development of the project.
- Django AllAuth was used to provide user account management functionality.
- Google Chrome Dev Tools was used to check reponsiveness.


**TESTING**
- - - 
Manual testing was carried out to ensure the site works as intended.

All the pages of the website have ben tested using the developer tools in Google Chrome. The code had to be changed along the process in order to achieve the responsiveness required for the project. The preview from Gitpod helped to constantly check all the changes made.

Testing was performed using a MacBook Air (M1, 2020) on macOS Monterey with the following browsers:
- Google Chrome 111.0.5563.110
- Safari 15.3
- Mozilla Firefox 111.0.1 

After testing the website I can confirm the project it's responsive in its all pages and works properly on all standard screen sizes.

The forms are working in each section of the project.
- The users can add, edit and delete their own reviews.
- The users can utilise the Contact form and get a confirmation email.
- The users can update their profile details on their personal account.
- The users can fill the checkout form to complete their order.
- The admin can add, edit and delete items from the menu.
All the internal links are working and bring the user to the right page on the website.
All the external links are working and bring the user to the right page by opening a new browser tab.
The Signup, Signin and Signout features have no issues and are working properly.

* VALIDATOR TESTING

Testing results can be found [here](/TESTING.md)


**DEPLOYMENT**
- - -
The site was deployed via Heroku. These are the steps I followed:

- In the Heroku dashboard, click "New" and then "Create new app". After that enter the app name and specify the region.

- In the Heroku dashboard click on the Resources tab
Scroll down to Add-Ons, search for and select 'Heroku Postgres'.

- In the setting tab, click on Reveal Config Vars button then copy the value for DATABASE_URL key.

- Install 2 more requirements: 
1. pip3 install dj_databse_url
2. pip3 install psycopg2-binary

- Create requirements.txt file by typing pip3 freeze --local > requirements.txt

- In Gitpod create a new env.py file and import the os library. Heroku Config vars need to be set accordingly including DATABASE_URL and SECRET_KEY.

- In settings.py file import dj_database_url, comment out the default configurations within database settings and add the following:

1. DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

- Create an if statement in settings.py to run the postgres database when using the app on heroku or sqlite if not
    1. if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
    }


- Create requirements.txt file by typing pip3 freeze --local > requirements.txt

- Create a file named "Procfile" in the main directory and add the following: web: gunicorn project-name.wsgi:application

- Add Heroku to the ALLOWED_HOSTS list in settings.py in the format ['app_name.heroku.com', 'localhost']

- Add the following Config Vars in Heroku:
1. A new record with SECRET_KEY
2. A new record with the AWS_ACCESS_KEY_ID
3. A new record with the AWS_SECRET_ACCESS_KEY
4. A new record with the EMAIL_HOST_PASS
5. A new record with the EMAIL_HOST_USER
6. A new record with the STRIPE_PUBLIC_KEY
7. A new record with the STRIPE_SECRET_KEY
8. A new record with the STRIPE_WH_SECRET
9. A new record with the DISABLE_COLLECTSTATIC = 1 (this must be removed for final deployment)
10. A new record with the USE_AWS

- On Heroku click on the Deploy tab, connect to GitHub and search for the repository then Connect.
- Scroll to the bottom of the deploy page and click Enable Automatic Deploys for automatic deploys.
- Click on Deploy Branch. When the app is deployed a message 'Your app was successfully deployed' will be shown. Click 'view' to see the deployed app in the browser.

The url for this website can be found [here](https://sushi-go.herokuapp.com/).

* AWS Set Up

AWS has been used for hosting the images. To implement this you will need and AWS account and to create an S3 Bucket and User Profile.
To serve the images you will need to add the following config to your settings.py file.

if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'lucadp07-sushi-go'
    AWS_S3_REGION_NAME = "eu-west-1"
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'


**CREDITS**
- - - 

**Content**

- [Code Institute - Boutique Ado Walkthrough Project](https://github.com/Code-Institute-Solutions/boutique_ado_v1).

- [CODEMY](https://www.youtube.com/@Codemycom).

- [Very Academy](https://www.youtube.com/@veryacademy).

- [Stack Overflow](https://stackoverflow.com/).

- [Am I responsive](https://ui.dev/amiresponsive).

- [Pixabay](https://pixabay.com/).

- [Ubersuggest](https://neilpatel.com/ubersuggest/).

- [Balsamiq Wireframes](https://balsamiq.com/wireframes/).