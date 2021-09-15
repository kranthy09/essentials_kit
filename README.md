# Essentials Kit Management
## _The Last essentails..._


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Kit management will be done when we need essentials that are to be taken care of in need. Here the kits will be rolled out and show the items present in each kit. we can choose the items in each kit and track the delivery according to the kit delivery scheduled date and some times on item availablity

## API Views
##### There are 10 apis developed so far
 
- Users-list (path: /store/users/)
- user-detail (path: /store/user/<user_id:pk>)
- Forms-list (path: /store/forms/)
- Form-detail (path: /store/form/<form_id:pk>)
- Items-list (path: /store/items/)
- Item-detail (path: /store/item/<item_id: pk>)
- Brands-list (path: /store/brands/)
- Brand-detail (path: /store/brands/<brand_id: pk>)
- Product-list (path: /store/products/)
- ItemsBrandsList (path: /store/itembrands/)

Essentials Kit Management project is written in Django and provides apis to communicate with client.


## Tech

uses a number of projects to work properly:

- [Django] - version=3.2.7


## Installation

Create a virtual environment using python

```sh
python3 -m venv kitenv
```

Django can be installed from pip

```sh
pip install Django
```