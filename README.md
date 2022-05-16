# greenbox

An inventory management web app developed in Python using Django and SQLite. 
But since I used Django, PostgreSQL, MariaDB, MySQL, and Oracle can be used as well.

## Run on Replit
Navigate to https://replit.com/@andyt19/greenbox#.replit and click the run button

## Run Locally
Install the latest version of Python https://www.python.org/

Clone the project

```bash
  git clone https://github.com/andyt19/greenbox
```

Go to the project directory

```bash
  cd greenbox
```

Install requirements

```bash
  pip install -r requirements.txt
```

Start the server

```bash
   python manage.py runserver
```

Open a web browser and type 127.0.0.1:8000 into the web address

## Usage
Add new warehouse - Takes user to form for adding a warehouse to the Warehouses database. Address, postal code, city, and province fields are required.

Add new product - Takes user to form for adding a product to the Products database. Product name, stock, warehouse ID (select from existing warehouses), and description fields are required.

Upon deleting a warehouse, the products associated with that warehouse will also be deleted.

When running the app, remember that you must have at least one warehouse before adding new products.

## Demo

![Demo of the viewall page](https://i.imgur.com/xWq3GPU.png)

![Demo of the addproduct page](https://i.imgur.com/pQr6pp9.png)
