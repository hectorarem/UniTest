# FireDevs test

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/hectorarem/UniTest.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv venv
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py migrate
(env)$ python manage.py seeds
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.


## Project description

The project is created with Python, Django, Django Rest Framework, Bootstrap, Jquery mainly.
It presents a couple of basic CRUDs with their validations.
The Select2 and Toast plugins are used, one for the searchable selectors in the student form,
and the other to inform the user of their actions.
The application has a command to carry out an initial load 'python manage.py seeds'.
The table offered by the template was used, as an adaptation, but using a DataTable,
it would be much better.
Besides, a simple application is built for a Rest API. With the purpose, mainly,
of future consumption of the information from another interface.
Currently it also allows both CRUD to be carried out.
Finally, you can view a report view of the number of users by groups.
