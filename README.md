## Project setup guide
```
create virtualenv
activate your virtualenv.
cd to the directory where requirements.txt is located.

run : 
$ pip install -r requirements.txt

Create and set Database Name, User and and User's Password in settings.py.
$ python manage.py migrate 
$ python manage.py loaddata db.json -> To import the initial data (Fixture)

Check it by starting the server with 
$ python manage.py runserver
```

## API Documentation
-----------------

## i. Create Square or Regular Pizza

* #### Endpoint 	: /api/pizza-create

* #### Request Type 	: POST

* #### Request Params 	: **Required** - type(value), size(id), toppings(ids)

* #### Request Sample  :

```
{
	"type": "regular",
	"size":3,
	"toppings":[4,5]
}

```

## ii. Get Pizza List


* #### Endpoint 	: /api/pizza-list

* #### Request Type 	: GET

* #### Request Params 	: **Optional (To  filter the list of pizza based on Size and Type of Pizza. )** -size and type


* #### Request Sample  :

```
{
	"type": "regular",
	"size":3
}

```
### For Endpoints iii to v (mentioned below ) you need to append pizza objects's id to the request url.	
## iii. View Pizza detail

* #### Endpoint 	: /api/pizzas/{id}

* #### Request Type 	: GET

* #### Request Params 	: We don’t need to pass any params for this request

## iv. Update Pizza
* #### Endpoint 	: /api/pizzas/{id}
* #### Request Type 	: POST
* #### Request Params 	: **Required** - type(value), size(id), toppings(ids)
* #### Request Sample  :

```
{
	"type": "square",
	"size":3,
	"toppings":[5,6]
}

```
## v. Delete Pizza

* #### Endpoint 	: /api/pizzas/{id}

* #### Request Type 	: DELETE

* #### Request Params 	: We don’t need to pass any params for this request


## vi. Add Topping

* #### Endpoint 	: /api/pizza-topping

* #### Request Type 	: POST

* #### Request Params 	: name(required)
* #### Request Sample  :

```
{
	"name": "onion"
}

```

## vii. Get Toppings List

* #### Endpoint 	: /api/pizza-topping
* #### Request Type 	: GET
* #### Request Params 	: We don’t need to pass any params for this request

## viii. Add Pizza Size

* #### Endpoint 	: /api/pizza-size

* #### Request Type 	: POST

* #### Request Params 	: name(required)
* #### Request Sample  :

```
{
	"name": "Extra-Large"
}

```
## ix. Get Pizza sizes List

* #### Endpoint 	: /api/pizza-size
* #### Request Type 	: GET
* #### Request Params 	: We don’t need to pass any params for this request


# --------------------------------------------------------------------------
