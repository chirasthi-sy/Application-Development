# Application-Development
This repository contains all files and documents related to the web application built for a popular pastry shop in Sri Lanka. 

The repository structure is as follows.
* Planning documentation - contains all files created during web application planning
* Order system - contains all files of the web application
   * customer - a module created to hold all views, functions and files necessary for customer point of view of application
   * management - a module created to hold all view, functions and files necessary for management point of view of application
   * order_system - contains all files necessary for the operations of the web application
   * media - contains all image files used in designing the web application
   * static - contains all static files such as css which were used in styling the web application
   * templates - contains all html templates used in creating user authentication interfaces


The main aim of building the web application is to create an online order-taking system for the company. The brief steps taken to complete the project are as follows.
1. Planning the web application functionalities and design.
2. Creating apps/modules for customer and admin interfaces.
3. Creating web pages to suit the needs of each app.
4. Making the necessary changes for backend development.


To log in as an admin user, the following credentials can be used in the management login available in the footer of the web application.
* Username: manager
* Email: manager@sponge.lk
* Password: 12345


The main functionalities created for a customer are as follows.
* View/ browse bakery products
* View more details of products
* Sign up / log in as a customer to place order
* Add products to order
* Provide customer details and receive order confirmation
* Make payments
* Receive confirmation emails for signing up and order confirmation
* View a customer dashboard which displays information such as total orders and total spend
* View individual order details and view shipping status of the order


The main functionalities created for an admin user (manager/employee) are as follows.
* Add / edit / delete bakery categories and products
* Add other employees as users
* View a management dashboard which displays the orders for the day and total revenue earned
* View individuals order details and update order details (eg: Mark an order completed once payment has been received and order is shipped)

