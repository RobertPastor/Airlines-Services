## setup Django

$  django-admin startproject airlinesServices Airlines-Services
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services (master)

## web site -> airlinesServices
## Django project name -> Airlines-Services

$ ls -alR Airlines-Services/
Airlines-Services/:
total 5
drwxr-xr-x 1 rober 197609   0 Aug 14 12:09 ./
drwxr-xr-x 1 rober 197609   0 Aug 14 12:09 ../
drwxr-xr-x 1 rober 197609   0 Aug 14 12:09 airlinesServices/
-rwxr-xr-x 1 rober 197609 694 Aug 14 12:09 manage.py*

Airlines-Services/airlinesServices:
total 10
drwxr-xr-x 1 rober 197609    0 Aug 14 12:09 ./
drwxr-xr-x 1 rober 197609    0 Aug 14 12:09 ../
-rw-r--r-- 1 rober 197609    0 Aug 14 12:09 __init__.py
-rw-r--r-- 1 rober 197609  425 Aug 14 12:09 asgi.py
-rw-r--r-- 1 rober 197609 3314 Aug 14 12:09 settings.py
-rw-r--r-- 1 rober 197609  794 Aug 14 12:09 urls.py
-rw-r--r-- 1 rober 197609  425 Aug 14 12:09 wsgi.py
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services (master)


## test the development server

$ python Airlines-Services/manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
August 14, 2026 - 13:36:49
Django version 5.2.17, using settings 'airlinesServices.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/5.2/howto/deployment/
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services (master)

## apply migrations

$ python Airlines-Services/manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services (master)

## launch the development server again
$ python Airlines-Services/manage.py runserver

## open a browser tab and insert the localhost server URL
http://127.0.0.1:8000/

## a dummy front page should appear

## create the "airlines" application (Django application with specific routes/urls)

(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)
$ python manage.py startapp airlines
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)

## create the trajectory application
$ python manage.py startapp trajectory


