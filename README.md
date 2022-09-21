# flask-mysql Sample

```
if your environment is proxy, edit  app/Dockerfile 

ex)  
ENV http_proxy="http://username:password@proxyserver:port"
ENV https_proxy="http://username:password@proxyserver:port"


# git clone https://github.com/cj-jeon/flask-mysql
# cd flask-mysql
# docker-compose up -d --build

#docker-compose ps
      Name                   Command             State                 Ports
------------------------------------------------------------------------------------------
flaskmysql_app_1   /bin/sh -c python app.py      Up      0.0.0.0:8080->8080/tcp
flaskmysql_db_1    docker-entrypoint.sh mysqld   Up      0.0.0.0:3306->3306/tcp, 33060/tcp

# cul http://localhost:8080/

# curl http://localhost:8080/getdata

```
