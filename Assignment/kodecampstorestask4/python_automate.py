import os
import sys
import subprocess
from myModule import command2
from myModule import command1
from myModule import command
from myModule import dirPath
from myModule import users_and_groups
from myModule import directories

# Getting the working directory. Equivalent to the linux command "$ pwd"
cwd = os.getcwd() 

def create_vm():
    # Execute Vagrant up command
    print("creating vm")
    vagrant_sp = subprocess.Popen(command1,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
    vagrant_sp2 = subprocess.Popen(command2,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
    vagrant_sp3 = subprocess.Popen(command,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
    
    vagrant_sp
    vagrant_sp2
    vagrant_sp3
    
    
 

def create_user(user,group):
 # create group
 try:
    subprocess.run(['sudo', 'groupadd', group], check=True)
 
 except subprocess.CalledProcessError as e:
        print(f"Group {group} might already exist: {e}")  
   # Create user and assign to group
 try:  
  subprocess.run(['sudo', 'useradd', '-m', '-g', group, user], check=True)
 
 except subprocess.CalledProcessError as e:
        print(f"User {user} might already exist or error occurred: {e}")
 
def check_dir(directory):
    if cwd == dirPath:
       dirs = os.listdir("./")
       for dir in dirs:
          if dir == directory:
            exist = "Directory exists"
          else:
            exist = "Directory does not exist"
    return exist

def create_dir(directory):
    
    os.makedirs(directory,exist_ok=False)
    os.chmod(directory,0o777)
   
 


   
def resources(): 
    if  cwd == dirPath:
        for user,group in users_and_groups:
           create_user(user,group)
           
              
        for directory in directories:
            dirExist = check_dir(directory)
            
            if dirExist == "Directory does not exists":
               create_dir(directory)
            else:
                print("Directory exists")
                
        print(f"users, groups, directories created sucessfully") 
    else: 
       print(f"users, groups, directories not created")  
       
def create_file(directory, filename):
    if directory not in directories:
        print(f"Error: {directory} is not a valid directory.")
    
    else:
      try:
        file_path = os.path.join(directory, filename)
        file = open(file_path, 'w')
        file.write('')  # Create an empty file
        print(f"File {filename} created successfully in {directory}.")
      except OSError as e:
        print(f"Error creating file {filename} in {directory}: {e}")

def created_file():  
    if cwd == dirPath:  
       directory = input("Enter the directory name: ")
       filename = input("Enter the file name: ")
       create_file(directory, filename)      
       
def main():
    create_vm()
    resources()
    created_file()
    
main()    