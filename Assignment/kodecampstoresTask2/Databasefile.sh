#!/bin/bash
# Update and install MySQL
sudo apt-get update
sudo apt-get install -y mysql-server


# Allow MySQL to listen on all interfaces
sudo sed -i "s/bind-address.*/bind-address = 0.0.0.0/" /etc/mysql/mysql.conf.d/mysqld.cnf

# Restart MySQL service
sudo systemctl restart mysql
sudo systemctl enable mysql

