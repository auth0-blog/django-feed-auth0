This application is based on [this Django authentication tutorial](https://auth0.com/blog/django-authentication/) where you learn how to create a public feed application, add authentication, and add moderator permissions.

![Django public feed app](https://cdn.auth0.com/blog/django-authentication/django-public-feed.png)

## Running the application

First, clone the application:

```bash
git clone git@github.com:auth0-blog/django-feed-auth0.git
cd django-feed-auth0
```

Next, install the dependencies:

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Then, you need to update your `settings.py` file with your own Auth0 values. You can [sign up for a free Auth0 account here](https://auth0.com/signup) if you don't have one already.

You can find the location of those values in your Auth0 dashboard. For more details, please see the ["Adding Authentication" section of the tutorial](https://auth0.com/blog/django-authentication#adding-authentication).


Migrate the application:

```shell script
cd feed
python manage.py migrate
```

Create a superuser:

```shell script
python manage.py createsuperuser
```

Finally, run the application:

```bash
python manage.py runserver
```
