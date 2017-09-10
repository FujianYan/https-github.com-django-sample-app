# Django-sample-app

--------------------------------------------------------------------------------
## 1. Environment Setup

### Postgres

1. Download Docker Community Edition from [Docker Website](https://store.docker.com/search?offering=community&type=edition).
2. Run `docker pull juneng/postgres` to pull postgres docker image.
3. Run `docker run --name postgres -p 5432:5432 -d juneng/postgres` to start postgres docker container.
4. Run `docker start postgres` if the container already exists.

### Anaconda

1. Download Python 3.6 from [Anaconda Website](https://www.continuum.io/downloads).
2. Run `conda create -n entropy python=3.6 anaconda` to create new environment for Django.
3. Run `source activate entropy` to switch your current Python environment.
4. Run `pip install -r requirements/local.txt` under entropy-backend folder to install required packages.

### Pycharm

1. Download and install Pycharm Community Edition from [JetBrains](https://www.jetbrains.com/pycharm/).

## 2. Deployment

1. Run `./reset_database.sh` to clean migrations and database.
2. Run `python manage.py makemigrations` to make migrations.
3. Run `python manage.py migrate` to update database.
4. Run `python manage.py test` to conduct unit test.
5. Run `python manage.py runserver` to start server.

## 3. Unit Test

### Running the tests
To run all the tests for all api:

```
./manage.py test api
```
--------------------------------------------------------------------------------
