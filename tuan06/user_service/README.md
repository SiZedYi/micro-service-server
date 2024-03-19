1. Setup
    ```
    $ sudo apt install git gcc g++ make python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev gettext curl -y
    $ sudo apt install mariadb-server libmysqlclient-dev - y
    ```
    ```
    $ sudo mysql
    mariadb> CREATE DATABASE user_service DEFAULT CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb4_general_ci;
    mariadb> GRANT ALL PRIVILEGES ON user_service.* TO 'user_service'@'localhost' IDENTIFIED BY '<mariadb user password>';
    mariadb> exit
    ```
    ```
    $ python3 -m venv venv
    $ source venv/bin/activate
    ```
    ```
    $ pip3 install -r requirements.txt
    $ python manage.py migrate
    ```
