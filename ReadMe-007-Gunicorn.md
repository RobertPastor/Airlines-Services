

## using a windows administrator account modify the etc/hosts file
## located in c:\windows\System32\drivers\etc\hosts

## add the following line
127.0.0.1	mytestapplication.local

## activate the virtual environment

$ . ./virtualEnv/Scripts/activate
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services (master)
$

## install gunicorn with pip

$ pip install gunicorn
Requirement already satisfied: gunicorn in .\virtualEnv\Lib\site-packages (26.1.0)
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services (master)
$

## launch the unicorn server simulating a local host with a domain
not used -> waitress-serve --listen=mytestapplication.local:8000 wsgi:application

## create a server.py python module
