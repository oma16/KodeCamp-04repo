#!/bin/bash
# Update and install Nginx
sudo apt-get update
sudo apt-get install -y nginx

# Start Nginx service
sudo systemctl start nginx
sudo systemctl enable nginx
