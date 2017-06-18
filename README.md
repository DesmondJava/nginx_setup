# stepic_web_project_django

I am using ubuntu 64 bit - 17.04, Python 2.7.13, Django - 1.11.2 final

Preconfiguration on clean Linux Ubuntu:
1. install mysql:  
sudo apt-get update  
sudo apt-get install mysql-server (type empty password for root user)  
sudo apt-get install libmysqlclient-dev   
2. install nginx server:  
sudo apt-get install nginx  
3. install pip:  
sudo apt-get install python-pip  
4. install Gunicorn (Python WSGI HTTP Server for UNIX):  
pip install gunicorn  
5. Mysql client:  
pip install mysqlclient  
6. Install Django framework:  
pip install Django  
7. Setup your mysql table
cd ~/web/ask
8. Collect static content  
python manage.py collectstatic

Then you should copy all files from current project to ~/web/ folder. It requires next scripts to run and configure application. After copy go to ~/web/ folder and run next scripts:  

1. Setup your mysql table: cd ~/web/ask, python manage.py syncdb
2. sudo ./settingmysql.sh for setup user admin for mysql and create table  
3. sudo ./init.sh to run application  

Open any browser and go to http://0.0.0.0:80 Nginx must move you to application where it runs on http://0.0.0.0:8000
