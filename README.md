### How to install?
1. git clone
```.sh
git clone https://github.com/kde2podfreebsd/BackTesting.git
cd BackTesting/
```
2. Setup environment
```.sh
chmod +x setup.sh
./setup.sh
``` 

3. Start docker with PostgreSQL Database
```.sh
sudo docker stop $(sudo docker ps -a -q)
sudo docker rm $(sudo docker ps -a -q)
docker-compose -f database.yaml build
docker-compose -f database.yaml up
``` 

4.  Change database IP
```.sh
❯ docker inspect pgdb | grep IPAddress
            "SecondaryIPAddresses": null,
            "IPAddress": "",
                    "IPAddress": "172.22.0.2",
``` 
```.cpp
const  char* connectionInfo = "host=172.22.0.2 dbname=tickerdb user=root password=root";
```

6. Build project
```.sh
make clean
make
```  
