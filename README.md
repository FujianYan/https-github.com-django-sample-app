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
4. Run `pip install -r requirements/local.txt` under Django-sample-app folder to install required packages.

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

## 4. API Document

Please refer to [here](https://github.com/gywangbruce/django-sample-app/blob/master/API_DOCUMENT.md).

## 5. Development Instruction

Our final product could help companies to manage their hiring pipeline. This sample server give user ability to create/read/update/delete company information and manage the stage level information within the company's hiring pipeline.

There are two simple apps within this server: `companies` and `stages`. They are under the `api` folder. The `companies` app is an example while you need to finish the `stages` app according to our API document. Below is the instruction:

1. The `stage` model is already defined for you. You need to create the `views.py`, `serializers.py` and `tests.py`.
2. Unlike `companies` app, `stages` app has an endpoint to change the order of different stages. This is pretty tricky so please choose any method you are comfortable with to achieve this. A challenging part is how to define the `validate` method in serializer beautifully.
3. `stage` model has a field called `stage_type`. It's saved in database as int but should be rendered as string. Please check API document for detailed example.
4. Remember to write up your unit test in `tests.py`
