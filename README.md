# Module 3 Project - E-commerce API

This API provides a platform for managing users, products, orders, and order-product relationships for an e-commerce application.

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Configuration](#configuration)
- [Database Models](#database-models)
- [API Endpoints](#api-endpoints)

## Project Overview

This project is a RESTful API built using Flask, SQLAlchemy, and Marshmallow. It allows the creation, retrieval, updating, and deletion of users, products, and orders. The API also manages the association between orders and products.

## Technologies Used

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Marshmallow
- Marshmallow-SQLAlchemy
- MySQL
- MySQL Connector Python

## Installation

### Prerequisites

- Python 3.x installed on your system.
- MySQL Server installed and running.

### Steps

1. **Clone the Repository**

    ```bash
    git clone https://github.com/mramessar/module-3-project.git
    cd ecommerce-api
    ```

2. **Create and Activate a Virtual Environment**
    - For Windows:

      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```

    - For Mac/Linux:

      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Database URI**
    - Update the `app.config['SQLALCHEMY_DATABASE_URI']` in `app.py` with your MySQL credentials.

## Configuration

### MySQL Configuration

- Ensure your MySQL server is configured to use `mysql_native_password` as the default authentication plugin. You can set this in your `my.ini` configuration file:

    ```ini
    [mysqld]
    default_authentication_plugin=mysql_native_password
    ```

- Restart your MySQL server after making changes.

### Database Initialization

- Run the following command to create the database tables:

    ```bash
    python app.py
    ```

## Database Models

### User

- `id`: Integer, primary key, auto-increment
- `name`: String
- `address`: String
- `email`: String (must be unique)

### Order

- `id`: Integer, primary key, auto-increment
- `order_date`: DateTime
- `user_id`: Integer, foreign key referencing `User`

### Product

- `id`: Integer, primary key, auto-increment
- `product_name`: String
- `price`: Float

### Order_Product

- `order_id`: Integer, foreign key referencing `Order`
- `product_id`: Integer, foreign key referencing `Product`

## API Endpoints

### Users

- `GET /users`: Retrieve all users
- `POST /users`: Create a new user
- `GET /users/<id>`: Retrieve a single user by ID
- `PUT /users/<id>`: Update a user by ID
- `DELETE /users/<id>`: Delete a user by ID

### Products

- `GET /products`: Retrieve all products
- `POST /products`: Create a new product
- `GET /products/<id>`: Retrieve a single product by ID
- `PUT /products/<id>`: Update a product by ID
- `DELETE /products/<id>`: Delete a product by ID

### Orders

- `GET /orders`: Retrieve all orders
- `POST /orders`: Create a new order
- `GET /orders/<id>`: Retrieve a single order by ID
- `PUT /orders/<id>`: Update an order by ID
- `DELETE /orders/<id>`: Delete an order by ID
