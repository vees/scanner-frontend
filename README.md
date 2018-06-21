    rob@focus:~/Projects$ cd scanner-frontend/
    rob@focus:~/Projects/scanner-frontend$ python3 -m venv env
    rob@focus:~/Projects/scanner-frontend$ source env/bin/activate
    (env) rob@focus:~/Projects/scanner-frontend$ pip install django
    (env) rob@focus:~/Projects/scanner-frontend$ django-admin startproject scanner
    (env) rob@focus:~/Projects/scanner-frontend$ cd scanner/
    (env) rob@focus:~/Projects/scanner-frontend/scanner$ python manage.py \
      startapp frontend

Edited models.py

    # Create your models here.
    class Transmission(models.Model):
        recordtime = DateTimeField()
        sequence = SmallIntegerField()
        transcript = TextField()
        confidence = DecimanField(max_digits=4, decimal_places=3)



    (env) rob@focus:~/Projects/scanner-frontend/scanner$ python manage.py migrate
    Operations to perform:
      Apply all migrations: admin, auth, contenttypes, sessions
    Running migrations:
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      Applying admin.0002_logentry_remove_auto_add... OK
      Applying contenttypes.0002_remove_content_type_name... OK
      Applying auth.0002_alter_permission_name_max_length... OK
      Applying auth.0003_alter_user_email_max_length... OK
      Applying auth.0004_alter_user_username_opts... OK
      Applying auth.0005_alter_user_last_login_null... OK
      Applying auth.0006_require_contenttypes_0002... OK
      Applying auth.0007_alter_validators_add_error_messages... OK
      Applying auth.0008_alter_user_username_max_length... OK
      Applying auth.0009_alter_user_last_name_max_length... OK
      Applying sessions.0001_initial... OK

Add app to settings.py

    (env) rob@focus:~/Projects/scanner-frontend/scanner$ python manage.py makemigrations
    Migrations for 'frontend':
      frontend/migrations/0001_initial.py
        - Create model Transmission
    (env) rob@focus:~/Projects/scanner-frontend/scanner$ python manage.py migrate
    Operations to perform:
      Apply all migrations: admin, auth, contenttypes, frontend, sessions
    Running migrations:
      Applying frontend.0001_initial... OK

    (env) rob@focus:~/Projects/scanner-frontend/scanner$ python manage.py shell
    Python 3.6.5 (default, Apr  1 2018, 05:46:30)
    [GCC 7.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>> from frontend.models import Transmission
    >>> Transmission.objects.all()
    <QuerySet []>
    >>> import datetime
    >>> t = Transmission(transcript=" Hi Benjamin, 2041.", confidence=0.6237885355949402, recordtime=datetime.datetime.now(),sequence=1)
    >>> t.save()
    /home/rob/Projects/scanner-frontend/env/lib/python3.6/site-packages/django/db/models/fields/__init__.py:1423: RuntimeWarning: DateTimeField Transmission.recordtime received a naive datetime (2018-06-20 01:14:58.149402) while time zone support is active.
      RuntimeWarning)
    >>> import pytz
    >>> from django.utils import timezone
    >>> timezone.now()
    datetime.datetime(2018, 6, 20, 1, 17, 1, 306089, tzinfo=<UTC>)
    >>> t = Transmission(transcript=" Hi Benjamin, 2041.", confidence=0.6237885355949402, recordtime=timezone.now(),sequence=1)
    >>> t.save()



    (env) rob@focus:~/Projects/scanner-frontend/scanner$ python manage.py runserver 127.0.0.1:7000
    Performing system checks...

    System check identified no issues (0 silenced).
    June 20, 2018 - 01:19:22
    Django version 2.0.6, using settings 'scanner.settings'
    Starting development server at http://127.0.0.1:7000/
