# Portfolio

This is a little portfolio - construction ongoing.

## Wolf or Husky?

A simple image classifier, which spits out a result if it's more than 90% confident, otherwise professes ignorance (cf. 'Artifical Stupidity', [Vincent Warmerdam at PyData conference 2019](https://pydata.org/london2019/schedule/presentation/10/how-to-constrain-artificial-stupidity/): we shouldn't be extrapolating about things far outside the original training data, even though models let you do so.

Hosted [here](http://kieuk.eu.pythonanywhere.com/wolforhusky/)

[Jupyter notebook](https://colab.research.google.com/drive/1tF7tN7uPPtvqdGFt_OaFYsbpx6LDh7nR) where I trained the model.


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