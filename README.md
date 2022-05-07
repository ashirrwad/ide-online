# ide-online
This is a sample prototype online playground for Fortran.
It's a basic Flask App which runs the code from editor on the servers compiler and outputs it onto the webpage

Instructions to run

Needed:

1. Python 3
2. GCC (10.3.0)

To run the applictaion:

1. Install dependencies 
```
pip install flask
```
2. Run the application
```
flask run
```
Note: Use administrator mode while running the app from your cmd if on Windows or just sudo it on linux, it uses system default PATH for gfortran which might cause errors without admin permission.

This app is a very simple implementation and acts as a proof-of-concept for the idea, it has a lot of security loopholes and it is highly advised not to use this as it is on a production environment. 
