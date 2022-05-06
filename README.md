# Adyen Drop-in - Demo Store

This repo contain an implementation of the [Adyen Drop-In API](https://docs.adyen.com/checkout/drop-in-web) on a simple Django webapp.
[You can see the application live on Heroku!](http://adyen-python-store-demo.herokuapp.com/)

The goal was to illustrate the integration of this API. As such it's pretty barebone:
* Selection from 3 countries
* No real cart content
* Fixed amount and currency(15.00€)

`TODO` items are used to note documentation remarks that I had.

## Requirements
* Python 3.8.2
* Packages: `Django`, `Adyen`, `whitenoise` and `gunicorn` to run in on Heroku
* Adyen account, that you can [request it here](https://www.adyen.com/home/discover/test-account-signup#form).

## Installation
Most merchant-specific info are needs to be registered in `base/secrets.py`. A template is provided in `base/secrets_template.py`.
1. Rename `base/secrets_template.py` to `base/secrets.py`.
1. Fill the variable with your merchant information.
1. Don't forget to install required packages: `pip install Adyen Django whitenoise`
1. If you want to deploy the app, update Django configuration with your host in `adyen-python-store-demo/settings.py`, `ALLOWED_HOSTS`

## Usage
1. Collect static files: `manage.py collectstatic`
1. Start the Django app: `manage.py runserver`

## Usages acknowledgment
* [Wikipedia Commons - File:Costa carrot cake (13070325384).jpg](https://commons.wikimedia.org/wiki/File:Costa_carrot_cake_(13070325384).jpg)
* [Wikipedia Commons - File:Mum's lemon meringue pie crop.jpg](https://commons.wikimedia.org/wiki/File:Mum%27s_lemon_meringue_pie_crop.jpg)
* [Wikipedia Commons - File:Chocolate cake.jpg](https://commons.wikimedia.org/wiki/File:Chocolate_cake.jpg)
* [Pixabay - Leovinus icons](https://pixabay.com/users/leovinus-615857/)

## License
The Unlicense - see LICENSE.
Some code extract are coming from [Adyen documentation](https://docs.adyen.com/checkout/drop-in-web).
