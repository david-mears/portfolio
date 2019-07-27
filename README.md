# Portfolio

This is a little portfolio - construction ongoing.

## Local Installation

Git clone this repo, and cd into it.

Create and activate your favourite virtual environment for Python.

At least on Windows, pytorch must be installed before fastai. Choose the correct installation [here](https://pytorch.org/get-started/locally/)

Then:

```
pip install -r requirements.txt
```

## Local hosting

```
python manage.py migrate
python manage.py collectstatic
python manage.py runserver
```