# Getting started


### What is VRS?
VRS stands for "Vaccine Registration System," and is a system that
distributes COVID-19 vaccines to those who need them most. The
system strives to be, above all, easy to use. Those who would like
to be vaccinated need only register. These users will be refered to
as 'vaccinees' in later sections.


### Installing
1. Download the repository from GitHub.
2. Download and install Python and Pip3.
	- The most recent python version can be found here: https://www.python.org/downloads/ 
3. Install flask and flask-sqlalchemy. This can be done by running the following in a 
terminal or command prompt window. 
```
pip3 install flask flask-sqlalchemy
```
4. Run the project via the `webserver/Flaskserver.py` file.
	- You can either run this file by double clicking it, opening it with Python, or navigating to it in a terminal window and then typing `python3 Flaskserver.py`.
5. Once the project is running, visit localhost:5000 in a web browser. 
	- To see the webpage on another computer, navigate to the ip address of the host computer
followed by `:5000`. For example, if the computer you're running the project on has an ip address
of `123.123.123.123`, you would visit `123.123.123.123:8000`.

