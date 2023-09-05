# StellarHunt-Backend

Welcome to the Stellar Hunt Flower Shop Backend repository! This Django project serves as the backend for the
Stellar Hunt flower shop website, providing essential functionality for user authentication, inventory management, 
cart handling, and the checkout process.


**Table of Contents**

* Project Overview
* Installation
* Authentication
* Inventory Management
* Cart Handling
* Checkout Process
* Admin User
* Contributing

**Project Overview**
Stellar Hunt is a flower shop backend built using Django and the Django Rest Framework. It serves as the backbone for the Stellar Hunt Flower Shop website. Here's an overview of the key features and components:

**Authentication**
The project includes an authentication app with token-based authentication. Users can create accounts, log in, and access personalized features such as order history and saved addresses.

**Inventory Management**
The inventory_management app manages flower categories, subcategories, and products. It provides APIs for adding, updating, and retrieving product information.

**Cart Handling**
The cart_handler app handles the shopping cart functionality. Users can add products to their cart, adjust quantities, and remove items as needed.

**Checkout Process**
The project supports a seamless checkout process where users can provide shipping information and payment details to complete their flower purchases.

**Admin User**
To get started with administrative tasks, the first admin user needs to be created. This user can access the Django admin panel to manage products, categories, users, and other backend functionalities.

**Installation**
To set up the Stellar Hunt Flower Shop Backend on your local machine, follow these steps:

1. Clone the repository to your local machine:
    ```bash
      git clone https://github.com/WishaEman/Stellar_Hunt.git
    ```
   
2. Navigate to the project directory:
   ```bash
      cd Stellar_Hunt
    ```
   
3. Create a virtual environment:
   ```bash
     python -m venv venv
    ```
   
4. Activate the virtual environment:

   * On Windows:
       ```bash
         venv\Scripts\activate
       ```
   * On macOS and Linux:
      ```bash
         source venv/bin/activate
       ```
  
5. Install the project dependencies:
   ```bash
         pip install -r requirements.txt
   ```
   
6. Apply database migrations:
    ```bash
         python manage.py migrate
    ```

7. Create the first admin user:
   ```bash
        python manage.py createsuperuser
    ```

8. Start the development server:
   ```bash
        python manage.py runserver
    ```
   
You can now access the API endpoints and the Django admin panel.

**Contributing**
If you'd like to contribute, please follow these guidelines:

1. Fork the repository and create a new branch for your feature or bug fix.
2. Make your changes and test thoroughly.
3. Create a pull request with a clear description of your changes.
4. Ensure your code follows best practices and is well-documented.