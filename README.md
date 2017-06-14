# stepic_web_project_django

Preconfiguration on clear Linux Ubuntu:
1. install mysql:
sudo apt-get update
sudo apt-get install mysql-server
sudo apt-get install libmysqlclient-dev
2. install nginx server:
sudo apt-get install nginx
3. install pip:
sudo apt-get install python-pip
4. install Gunicorn (Python WSGI HTTP Server for UNIX):
pip install gunicorn
5. Mysql client:
pip install mysqlclient

Then you should copy all files from current project to ~/web/ folder. It requires next scripts to run and configure application. After copy go to ~/web/ folder and run next scripts:

1. sudo ./settingmysql.sh for setup user admin for mysql and create table
2. sudo ./init.sh to run application
