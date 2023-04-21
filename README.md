#  Course api


### An async api to manager your courses

Python version:

    3.11
    
Database:

    async sqlite
    
    
This project uses type hint

### Endpoints:

    /docs
    
 ![image](https://user-images.githubusercontent.com/88283829/233525980-7c99d52d-770a-4554-92df-4d4e2fcb7322.png)

    /redoc
    
 ![image](https://user-images.githubusercontent.com/88283829/233526821-4784e0b7-8bd1-4183-8748-783588b80c2e.png)


    Methods:
    
    - GET, PUT, POST, DELETE on /api/v1/courses or /api/v1/courses/<id>

![image](https://user-images.githubusercontent.com/88283829/233528709-4d7b7a1e-438a-4a95-9b3f-a147ed00725d.png)


### RUN

if not exists:

    python /dao/create_tables.py
    
After that:

    python main.py
    

    
