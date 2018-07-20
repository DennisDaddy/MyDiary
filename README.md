# MyDiary
[![Build Status](https://travis-ci.com/DennisDaddy/MyDiary.svg?branch=data-structures)](https://travis-ci.com/DennisDaddy/MyDiary)
[![Coverage Status](https://coveralls.io/repos/github/DennisDaddy/MyDiary/badge.svg?branch=data-structures)](https://coveralls.io/github/DennisDaddy/MyDiary?branch=data-structures)
[![Maintainability](https://api.codeclimate.com/v1/badges/07809922afad3a74f442/maintainability)](https://codeclimate.com/github/DennisDaddy/MyDiary/maintainability)


MyDiary is an online journal where users can pen down their thoughts and feelings.

## How to use or contribute to the project
Follow the steps below if you're interested in contributing or using this API.
In this part the data is stored in data structures(list and dictionary) not databases.

This API is built on the top of Flask python web framework.

### Heroku link
 
This is the link.. https://madiary.herokuapp.com/

### Setting up the environment

1. Clone the repository

```sh
$ git clone https://github.com/DennisDaddy/MyDiary.git
```

2. Access the cloned application directory

```sh
$ cd MyDiary
```


3. Create the virtual environment and install dependencies(These are required Python, pip and virtual environment):

```sh
$ virtualenv venv
```

4. Activate the virtual environment [Linux]

```sh
$ source  venv/bin/activate
```


5. Install dependencies using pip

```sh
$ pip install -r requirements.txt
```



### Running the API

To run the tests, use `nosetests` or any other test runner of your choice with the name of the test file at the end.

```sh
$ nosetests -v
```

Then run the app

```sh
$ python app.py
```

### API Endpoints

**`GET /`** *Home page*

**`POST /diary/api/v1/auth/register`** *User registration*

**`POST /diary/api/v1/auth/login`** *User login*

**`POST /diary/api/v1/auth/logout`** *User logout*

**`GET /diary/api/v1/account`** *Get user account details*

**`GET /diary/api/v1/entries/`** *Get all the entries*

**`GET /diary/api/v1/entries/<entry_idd>`** *Get single entry*

**`POST /diary/api/v1/entries`** *Create new entry*

**`PUT /diary/api/v1/entries/<entry_id>`** *Update entry details*

**`DELETE /diary/api/v1/entries/<entry_id>`** *Delete entry*

