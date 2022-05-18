# signode-db-replica

running the .py file will added all the requrired test db to your local mongodb

Steps to follow:
1. start your mongod server in the background 

  ```run mongod``` in CLI

   or try

  ```mongod --dpath path-to/data/db``` in CLI

2. open mongoddb compass to verify changes
3. run ```db-signode-replica.py``` 

running the .py file may give you some errors, you might have to pip install couple of things. Also make sure you are running python3. 
