
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

## install jsonschema

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

## install module called yaml

$ pip install pyyaml
Collecting pyyaml
  Downloading pyyaml-6.0.3-cp311-cp311-win_amd64.whl.metadata (2.4 kB)
Downloading pyyaml-6.0.3-cp311-cp311-win_amd64.whl (158 kB)
Installing collected packages: pyyaml
Successfully installed pyyaml-6.0.3
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)
$

## install matplotlib

$ pip install matplotlib
Collecting matplotlib
  Downloading matplotlib-3.11.1-cp311-cp311-win_amd64.whl.metadata (80 kB)
Collecting contourpy>=1.0.1 (from matplotlib)
  Downloading contourpy-1.3.3-cp311-cp311-win_amd64.whl.metadata (5.5 kB)
Collecting cycler>=0.10 (from matplotlib)
  Using cached cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
Collecting fonttools>=4.28.2 (from matplotlib)
  Downloading fonttools-4.63.0-cp311-cp311-win_amd64.whl.metadata (121 kB)
Collecting kiwisolver>=1.3.1 (from matplotlib)
  Downloading kiwisolver-1.5.0-cp311-cp311-win_amd64.whl.metadata (5.2 kB)
Requirement already satisfied: numpy>=1.25 in C:\Users\rober\git\Airlines-Services\virtualEnv\Lib\site-packages (from matplotlib) (2.4.6)
Collecting packaging>=20.0 (from matplotlib)
  Downloading packaging-26.3-py3-none-any.whl.metadata (3.5 kB)
Collecting pillow>=9 (from matplotlib)
  Downloading pillow-12.3.0-cp311-cp311-win_amd64.whl.metadata (9.3 kB)
Collecting pyparsing>=3 (from matplotlib)
  Downloading pyparsing-3.3.2-py3-none-any.whl.metadata (5.8 kB)
Requirement already satisfied: python-dateutil>=2.7 in C:\Users\rober\git\Airlines-Services\virtualEnv\Lib\site-packages (from matplotlib) (2.9.0.post0)
Requirement already satisfied: six>=1.5 in C:\Users\rober\git\Airlines-Services\virtualEnv\Lib\site-packages (from python-dateutil>=2.7->matplotlib) (1.17.0)
Downloading matplotlib-3.11.1-cp311-cp311-win_amd64.whl (9.3 MB)
   ---------------------------------------- 9.3/9.3 MB 17.5 MB/s  0:00:00
Downloading contourpy-1.3.3-cp311-cp311-win_amd64.whl (225 kB)
Using cached cycler-0.12.1-py3-none-any.whl (8.3 kB)
Downloading fonttools-4.63.0-cp311-cp311-win_amd64.whl (2.4 MB)
   ---------------------------------------- 2.4/2.4 MB 16.8 MB/s  0:00:00
Downloading kiwisolver-1.5.0-cp311-cp311-win_amd64.whl (73 kB)
Downloading packaging-26.3-py3-none-any.whl (129 kB)
Downloading pillow-12.3.0-cp311-cp311-win_amd64.whl (7.2 MB)
   ---------------------------------------- 7.2/7.2 MB 18.6 MB/s  0:00:00
Downloading pyparsing-3.3.2-py3-none-any.whl (122 kB)
Installing collected packages: pyparsing, pillow, packaging, kiwisolver, fonttools, cycler, contourpy, matplotlib

Successfully installed contourpy-1.3.3 cycler-0.12.1 fonttools-4.63.0 kiwisolver-1.5.0 matplotlib-3.11.1 packaging-26.3 pillow-12.3.0 pyparsing-3.3.2
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)
$

## scipy

$ pip install scipy
Collecting scipy
  Downloading scipy-1.17.1-cp311-cp311-win_amd64.whl.metadata (60 kB)
Requirement already satisfied: numpy<2.7,>=1.26.4 in C:\Users\rober\git\Airlines-Services\virtualEnv\Lib\site-packages (from scipy) (2.4.6)
Downloading scipy-1.17.1-cp311-cp311-win_amd64.whl (36.6 MB)
   ---------------------------------------- 36.6/36.6 MB 19.9 MB/s  0:00:01
Installing collected packages: scipy
Successfully installed scipy-1.17.1
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)
$

## install xlsxwriter

$ pip install xlsxwriter
Collecting xlsxwriter
  Downloading xlsxwriter-3.2.9-py3-none-any.whl.metadata (2.7 kB)
Downloading xlsxwriter-3.2.9-py3-none-any.whl (175 kB)
Installing collected packages: xlsxwriter
Successfully installed xlsxwriter-3.2.9
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)
$


$ pip install pytz
Collecting pytz
  Downloading pytz-2026.3.post1-py2.py3-none-any.whl.metadata (22 kB)
Downloading pytz-2026.3.post1-py2.py3-none-any.whl (508 kB)
Installing collected packages: pytz
Successfully installed pytz-2026.3.post1
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)
$

$ pip install xarray
Collecting xarray
  Downloading xarray-2026.7.0-py3-none-any.whl.metadata (12 kB)
Requirement already satisfied: numpy>=1.26 in C:\Users\rober\git\Airlines-Services\virtualEnv\Lib\site-packages (from xarray) (2.4.6)
Requirement already satisfied: packaging>=24.2 in C:\Users\rober\git\Airlines-Services\virtualEnv\Lib\site-packages (from xarray) (26.3)
Requirement already satisfied: pandas>=2.2 in C:\Users\rober\git\Airlines-Services\virtualEnv\Lib\site-packages (from xarray) (3.0.5)
Requirement already satisfied: python-dateutil>=2.8.2 in C:\Users\rober\git\Airlines-Services\virtualEnv\Lib\site-packages (from pandas>=2.2->xarray) (2.9.0.post0)
Requirement already satisfied: tzdata in C:\Users\rober\git\Airlines-Services\virtualEnv\Lib\site-packages (from pandas>=2.2->xarray) (2026.3)
Requirement already satisfied: six>=1.5 in C:\Users\rober\git\Airlines-Services\virtualEnv\Lib\site-packages (from python-dateutil>=2.8.2->pandas>=2.2->xarray) (1.17.0)
Downloading xarray-2026.7.0-py3-none-any.whl (1.4 MB)
   ---------------------------------------- 1.4/1.4 MB 10.7 MB/s  0:00:00
Installing collected packages: xarray
Successfully installed xarray-2026.7.0
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)
$


$ pip install tabulate
Collecting tabulate
  Downloading tabulate-0.10.0-py3-none-any.whl.metadata (40 kB)
Downloading tabulate-0.10.0-py3-none-any.whl (39 kB)
Installing collected packages: tabulate
Successfully installed tabulate-0.10.0
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)
$

$ pip install xmltodict
Collecting xmltodict
  Downloading xmltodict-1.0.4-py3-none-any.whl.metadata (14 kB)
Downloading xmltodict-1.0.4-py3-none-any.whl (13 kB)
Installing collected packages: xmltodict
Successfully installed xmltodict-1.0.4
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)
$


## requests library used to query "Metars" through http

$ pip install requests
Collecting requests
  Downloading requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
Collecting charset_normalizer<4,>=2 (from requests)
  Downloading charset_normalizer-3.5.1-cp311-cp311-win_amd64.whl.metadata (46 kB)
Collecting idna<4,>=2.5 (from requests)
  Downloading idna-3.19-py3-none-any.whl.metadata (9.2 kB)
Collecting urllib3<3,>=1.26 (from requests)
  Downloading urllib3-2.7.0-py3-none-any.whl.metadata (6.9 kB)
Collecting certifi>=2023.5.7 (from requests)
  Downloading certifi-2026.7.22-py3-none-any.whl.metadata (2.5 kB)
Downloading requests-2.34.2-py3-none-any.whl (73 kB)
Downloading charset_normalizer-3.5.1-cp311-cp311-win_amd64.whl (206 kB)
Downloading idna-3.19-py3-none-any.whl (68 kB)
Downloading urllib3-2.7.0-py3-none-any.whl (131 kB)
Downloading certifi-2026.7.22-py3-none-any.whl (136 kB)
Installing collected packages: urllib3, idna, charset_normalizer, certifi, requests

Successfully installed certifi-2026.7.22 charset_normalizer-3.5.1 idna-3.19 requests-2.34.2 urllib3-2.7.0
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)
$


## whitenoise to ease managing static files

$ pip install whitenoise
Collecting whitenoise
  Downloading whitenoise-6.12.0-py3-none-any.whl.metadata (3.7 kB)
Downloading whitenoise-6.12.0-py3-none-any.whl (20 kB)
Installing collected packages: whitenoise
Successfully installed whitenoise-6.12.0
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)
$
