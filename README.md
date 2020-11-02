# Jumpcloud Interview Project

This application is meant to demonstrate a proficiency in devops relative to python.

## Points of Interest

* Linting with flake8
* Automatic code formatting with black
* Build in pre-commit script to run linting
* Docker compose environment for development
* Helm chart which is production ready
* Secrets management with sops

## Exclusions

For the sake of time, a number of things were purposefully excluded from this project.
1. Tests. I know tests are important, and are arguably a very important part of devops. Given enough time I would have used PYTest. Note that the app is set up to make this addition seamless.
2. Error handling. There is virtually no error handling in this API. The responses from the jumpcloud API should be parsed and cleaned so that the appropriate error messages are returned.
3. Better logging. Typically I would ensure that logs and errors were formatted in a consistent fashion so they can be easily aggregated.

## Running locally

1. Clone the repository: `git clone https://github.com/cgeene/jumpcloud-interview.git`
2. Optionally create a virtualenv: `virtualenv jumpcloud -p python3 && source jumpcloud/bin/activate`
3. Install: `pip3 install -r requirements.txt`
4. Install [PostgreSQL](https://www.postgresql.org/download/)
5. Configure Postgres:
```bash
sudo -u postgres psql
CREATE ROLE jumpcloud WITH LOGIN SUPERUSER CREATEDB CREATEROLE INHERIT NOREPLICATION CONNECTION LIMIT -1 PASSWORD 'jumpcloud';
CREATE DATABASE jumpcloud OWNER jumpcloud;
```
6. Run (from jumpcloud project directory):
```bash
export FLASK_APP=flaskr
export CONFIG_FILEPATH=$(pwd)/config/dev_config.py
flask init-db
flask run
```

## Run in docker-compose
```bash
make initdb
make buildup
```

## APIs 

#### GET /users
```bash
curl --location --request GET 'localhost:5000/users' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'x-api-key: {api-key}'
```

#### GET /users/:id
```bash
curl --location --request GET 'localhost:8080/users/<id>' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'x-api-key: {api-key}' \
```

#### POST /users
```bash
curl --location --request POST 'localhost:8080/users' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'x-api-key: {api-key}' \
--data-raw '{
    "description": "Test user 2",
    "displayname": "Test Person",
    "email": "test.person@gmail.com",
    "firstname": "test",
    "lastname": "person",
    "username": "tperson"
}'
```

#### PUT /users/:id
```bash
curl --location --request PUT 'localhost:8080/users/<id>' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'x-api-key: {api-key}' \
--data-raw '{
    "description": "Test user 2",
    "displayname": "Test Person",
    "email": "test.person@gmail.com",
    "firstname": "test",
    "lastname": "person",
    "username": "tperson"
}'
```

#### DELETE /users/:id
```bash
curl --location --request DELETE 'localhost:8080/users/<id>' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'x-api-key: {api-key}' \
```

#### GET /users/count
```bash
curl --location --request GET 'localhost:8080/users/count' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'x-api-key: {api-key}' \
```