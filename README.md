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

Set the environment variables by creating .env at the root directory. This project doesn't need high security so I've just pasted the needed environment variable [here](https://pastebin.com/zmx7WxhW) to allow anyone to use the project.

## Local hosting

```
python manage.py migrate
python manage.py collectstatic
python manage.py runserver
```