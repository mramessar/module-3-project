# E-Commerce API (Flask + MySQL)

This project is a fully functional RESTful API for managing users, products, and orders.
Built with **Flask**, **SQLAlchemy**, and **Marshmallow**, backed by a **MySQL** database.

---

## Features

* Create, update, delete, and fetch users and products
* Place orders linked to users
* Associate products with orders (many-to-many)
* Get all orders by a user, or all products in an order

---

## Setup Instructions

1. Clone this repository

2. Set up your MySQL database:

```sql
CREATE DATABASE ecommerce_api;
```

3. Create a virtual environment and install dependencies:

```bash
python -m venv venv
./venv/Scripts/activate   # On Windows
pip install -r requirements.txt
```

4. Set your MySQL password as an environment variable:

```bash
$env:MYSQL_PASSWORD="your_password_here"   # PowerShell (Windows)
```

5. Run the Flask app:

```bash
python app.py
```

---

## API Endpoints

### Users

* `GET /users`
* `GET /users/<id>`
* `POST /users`
* `PUT /users/<id>`
* `DELETE /users/<id>`

### Products

* `GET /products`
* `GET /products/<id>`
* `POST /products`
* `PUT /products/<id>`
* `DELETE /products/<id>`

### Orders

* `POST /orders`
* `PUT /orders/<order_id>/add_product/<product_id>`
* `DELETE /orders/<order_id>/remove_product/<product_id>`
* `GET /orders/user/<user_id>`
* `GET /orders/<order_id>/products`

---

## Postman Testing

This repo includes a **Postman collection** (`ecommerce_api_collection.json`) with all routes preloaded for easy testing.

---

## Developer Notes

> You'll notice a lot of `print()` statements in the code — that was intentional.
> I had to do a *ton* of debugging around MySQL, foreign keys, and server setup,
> so those log statements helped me trace what was happening during startup.

---

## Technologies Used

* Flask
* SQLAlchemy
* Marshmallow
* MySQL
* Postman
