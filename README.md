# API
Modern Health: Back-End Take Home Exercise


## Setup

Clone repository:
~~~
$ git clone https://github.com/alejandra-zapata/API.git
~~~
Create a virtual environment:
~~~
$ virtualenv env
~~~
Activate the virtual environment:
~~~
$ source env/bin/activate
~~~
Install dependencies:
~~~
$ pip install -r requirements.txt
~~~
Create database:
~~~
python -i model.py
~~~
While in interactive mode, create tables:
~~~
db.create_all()
~~~
Now, quit interactive mode. Start up the flask server:
~~~
python server.py
~~~
Go to localhost:5000 with an active internet connection to use the web app.
