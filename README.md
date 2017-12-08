# TD Rest Api Python

## Notes
Use this python Rest API to get information about your server :

- List services and stop them
- View disk usage informations

Security options not included :

- JSON Web Tokens
- OAuth2
- sudoers


## Requirements
    * Python 2.7 (tested on 2.7.13)
    * PIP (tested on 9.0.1)
    * Developped on DEBIAN 8

## Installation
    
    $ git clone git@github.com:clementtournier/td-python-rest.git
    $ cd td-python-rest
    $ git checkout develop
    $ pip install -r requirements.txt
    $ python server.py
    
Now the server is listening on 127.0.0.1:5000
    
## API endpoints

### GET /disk_usage
Use this endpoint to get informations about server disk usage.
```
[
    {
        "available": "3.9G", 
        "filesystem": "udev", 
        "mountpoint": "/dev", 
        "size": "3.9G", 
        "used": "0", 
        "used_percent": "0%"
    }, 
    {
        "available": "778M", 
        "filesystem": "tmpfs", 
        "mountpoint": "/run", 
        "size": "787M", 
        "used": "9.8M", 
        "used_percent": "2%"
    }, 
    ...
]
```
#### SAMPLE CALL
````
curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://localhost:5000/disk_usage
````
### GET /processes
Use this endpoint to list every processes. (eq = "ps -aux")
```
[
    {
        "c": "0", 
        "cmd": "/sbin/init", 
        "pid": "1", 
        "ppid": "0", 
        "stime": "17:26", 
        "time": "00:00:01", 
        "tty": "?", 
        "uid": "root"
    },
    {
        "c": "0", 
        "cmd": "[ksoftirqd/0]", 
        "pid": "3", 
        "ppid": "2", 
        "stime": "17:26", 
        "time": "00:00:00", 
        "tty": "?", 
        "uid": "root"
    },
    ...
]
```
#### SAMPLE CALL
````
curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://localhost:5000/processes
````

### POST /processes
Use this endpoint to stop a process. (eq = "systemctl stop service_name")
```
POST /processes HTTP/1.1
Host: 127.0.0.1:5000
Cache-Control: no-cache
Postman-Token: 48a0ea07-b1e6-f0a1-184b-fe23c7172b91
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="process"

apache2
```

..return True if service is stopped or False.
