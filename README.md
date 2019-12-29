# Market
An app that lists all the available items.


**Setup Build Environment**

Create a virtual environment:

```virtualenv .```

Clone this repository:

```git clone <url>```

```cd Market```

Install requirements:

```pip install -r requirements.txt```

Create Migrations:

```python manage.py makemigrations```

```python manage.py migrate```

Load Products and Users:

`python manage.py loaddata fixtures/products.json --app products.Products`
`python manage.py loaddata fixtures/users.json --app accounts.User`


Create a superuser or Admin:

`python manage.py createsuperuser`



**Run**

```python manage.py runserver```

Open `localhost:8000` on your browser to view.

 
