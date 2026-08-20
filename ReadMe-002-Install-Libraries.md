
## assumption - github repo has been clones
## assumption - virtualEnv has been created and activated

(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services (master)

## install Django

$ pip install Django
Collecting Django
  Downloading django-5.2.17-py3-none-any.whl (8.3 MB)
     ---------------------------------------- 8.3/8.3 MB 17.7 MB/s eta 0:00:00
Collecting asgiref>=3.8.1
  Using cached asgiref-3.12.1-py3-none-any.whl (25 kB)
Collecting sqlparse>=0.3.1
  Downloading sqlparse-0.6.0-py3-none-any.whl (50 kB)
     ---------------------------------------- 50.1/50.1 kB 2.5 MB/s eta 0:00:00
Collecting tzdata
  Downloading tzdata-2026.3-py2.py3-none-any.whl (348 kB)
     ------------------------------------- 348.2/348.2 kB 21.1 MB/s eta 0:00:00
Installing collected packages: tzdata, sqlparse, asgiref, Django
Successfully installed Django-5.2.17 asgiref-3.12.1 sqlparse-0.6.0 tzdata-2026.3

[notice] A new release of pip available: 22.3.1 -> 26.2.1
[notice] To update, run: python.exe -m pip install --upgrade pip
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services (master)
$ pip freeze
asgiref==3.12.1
Django==5.2.17
sqlparse==0.6.0
tzdata==2026.3
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services (master)


$ python -m django --version
5.2.17
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services (master)

## pip install method tools to use LRU cache

$ pip install methodtools
Collecting methodtools
  Downloading methodtools-0.4.7-py2.py3-none-any.whl (4.0 kB)
Collecting wirerope>=0.4.7
  Downloading wirerope-1.0.0-py2.py3-none-any.whl (9.2 kB)
Collecting six>=1.11.0
  Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: six, wirerope, methodtools
Successfully installed methodtools-0.4.7 six-1.17.0 wirerope-1.0.0

[notice] A new release of pip available: 22.3.1 -> 26.2.1
[notice] To update, run: python.exe -m pip install --upgrade pip
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)

## xlrd

$ pip install xlrd
Collecting xlrd
  Downloading xlrd-2.0.2-py2.py3-none-any.whl (96 kB)
     ---------------------------------------- 96.6/96.6 kB 5.8 MB/s eta 0:00:00
Installing collected packages: xlrd
Successfully installed xlrd-2.0.2

[notice] A new release of pip available: 22.3.1 -> 26.2.1
[notice] To update, run: python.exe -m pip install --upgrade pip
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)

## jsonschema

$ pip install jsonschema
Collecting jsonschema
  Downloading jsonschema-4.26.0-py3-none-any.whl.metadata (7.6 kB)
Collecting attrs>=22.2.0 (from jsonschema)
  Downloading attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)
Collecting jsonschema-specifications>=2023.03.6 (from jsonschema)
  Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata (2.9 kB)
Collecting referencing>=0.28.4 (from jsonschema)
  Downloading referencing-0.37.0-py3-none-any.whl.metadata (2.8 kB)
Collecting rpds-py>=0.25.0 (from jsonschema)
  Downloading rpds_py-2026.6.3-cp311-cp311-win_amd64.whl.metadata (4.2 kB)
Collecting typing-extensions>=4.4.0 (from referencing>=0.28.4->jsonschema)
  Downloading typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)
Downloading jsonschema-4.26.0-py3-none-any.whl (90 kB)
Downloading attrs-26.1.0-py3-none-any.whl (67 kB)
Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)
Downloading referencing-0.37.0-py3-none-any.whl (26 kB)
Downloading rpds_py-2026.6.3-cp311-cp311-win_amd64.whl (223 kB)
Downloading typing_extensions-4.16.0-py3-none-any.whl (45 kB)
Installing collected packages: typing-extensions, rpds-py, attrs, referencing, jsonschema-specifications, jsonschema

Successfully installed attrs-26.1.0 jsonschema-4.26.0 jsonschema-specifications-2025.9.1 referencing-0.37.0 rpds-py-2026.6.3 typing-extensions-4.16.0
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)
$
