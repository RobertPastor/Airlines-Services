
rober@RobertPastor MINGW64 ~/git
$ ls -al
total 68
drwxr-xr-x 1 rober 197609 0 Aug 14 10:36 ./
drwxr-xr-x 1 rober 197609 0 Aug 12 17:41 ../
drwxr-xr-x 1 rober 197609 0 Nov  2  2024 AnsPRCDataChallenge2024/
drwxr-xr-x 1 rober 197609 0 Jun 30  2024 MestraJavaXMLMaven/
drwxr-xr-x 1 rober 197609 0 Nov 20  2025 PRCdataChallenge2025/
drwxr-xr-x 1 rober 197609 0 Nov 22  2023 apache-maven-3.9.5/
drwxr-xr-x 1 rober 197609 0 Jun  4 13:12 flight-profile/
drwxr-xr-x 1 rober 197609 0 Aug 13 18:17 music-rungis/
drwxr-xr-x 1 rober 197609 0 Nov 12  2024 openap/
drwxr-xr-x 1 rober 197609 0 Nov 20  2025 pybada/
drwxr-xr-x 1 rober 197609 0 Dec  5  2023 qual_sonarqube_plugin_issueresolver/
drwxr-xr-x 1 rober 197609 0 Jun  4 23:22 raphael-artist-old/
drwxr-xr-x 1 rober 197609 0 Aug  6 16:50 raphael-the-artist/

rober@RobertPastor MINGW64 ~/git

## clone 

$ git clone https://github.com/RobertPastor/Airlines-Services.git
Cloning into 'Airlines-Services'...
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 5 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (5/5), 14.71 KiB | 1.23 MiB/s, done.

rober@RobertPastor MINGW64 ~/git
$ ls -al
total 72
drwxr-xr-x 1 rober 197609 0 Aug 14 11:43 ./
drwxr-xr-x 1 rober 197609 0 Aug 12 17:41 ../
drwxr-xr-x 1 rober 197609 0 Aug 14 11:43 Airlines-Services/
drwxr-xr-x 1 rober 197609 0 Nov  2  2024 AnsPRCDataChallenge2024/
drwxr-xr-x 1 rober 197609 0 Jun 30  2024 MestraJavaXMLMaven/
drwxr-xr-x 1 rober 197609 0 Nov 20  2025 PRCdataChallenge2025/
drwxr-xr-x 1 rober 197609 0 Nov 22  2023 apache-maven-3.9.5/
drwxr-xr-x 1 rober 197609 0 Jun  4 13:12 flight-profile/
drwxr-xr-x 1 rober 197609 0 Aug 13 18:17 music-rungis/
drwxr-xr-x 1 rober 197609 0 Nov 12  2024 openap/
drwxr-xr-x 1 rober 197609 0 Nov 20  2025 pybada/
drwxr-xr-x 1 rober 197609 0 Dec  5  2023 qual_sonarqube_plugin_issueresolver/
drwxr-xr-x 1 rober 197609 0 Jun  4 23:22 raphael-artist-old/
drwxr-xr-x 1 rober 197609 0 Aug  6 16:50 raphael-the-artist/

rober@RobertPastor MINGW64 ~/git

## move the current repository

$ cd Airlines-Services/

rober@RobertPastor MINGW64 ~/git/Airlines-Services (master)
$ ls -al
total 57
drwxr-xr-x 1 rober 197609     0 Aug 14 11:43 ./
drwxr-xr-x 1 rober 197609     0 Aug 14 11:43 ../
drwxr-xr-x 1 rober 197609     0 Aug 14 11:43 .git/
-rw-r--r-- 1 rober 197609  4846 Aug 14 11:43 .gitignore
-rw-r--r-- 1 rober 197609 35823 Aug 14 11:43 LICENSE
-rw-r--r-- 1 rober 197609    99 Aug 14 11:43 README.md

rober@RobertPastor MINGW64 ~/git/Airlines-Services (master)

## create a virtual environment

$ python -m venv virtualEnv

rober@RobertPastor MINGW64 ~/git/Airlines-Services (master)
$ ls -al
total 57
drwxr-xr-x 1 rober 197609     0 Aug 14 11:45 ./
drwxr-xr-x 1 rober 197609     0 Aug 14 11:43 ../
drwxr-xr-x 1 rober 197609     0 Aug 14 11:43 .git/
-rw-r--r-- 1 rober 197609  4846 Aug 14 11:43 .gitignore
-rw-r--r-- 1 rober 197609 35823 Aug 14 11:43 LICENSE
-rw-r--r-- 1 rober 197609    99 Aug 14 11:43 README.md
drwxr-xr-x 1 rober 197609     0 Aug 14 11:45 virtualEnv/

rober@RobertPastor MINGW64 ~/git/Airlines-Services (master)
$ code .

## ignore the virtual environment from the git tracking

## activate the virtual environment in windows using GitBash

$ . ./virtualEnv/Scripts/activate
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services (master)
$
