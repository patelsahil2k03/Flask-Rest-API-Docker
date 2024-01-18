# Flask-Rest-API-Docker
A simple project for learning and implementing docker container for the Flask Project , working with Flask and checking APIs with Postman.

Here we are using Test data of a restaurant having customers subscribed to a meal subscription having fields like: - Id, name, email, meal_size, meal_time, days, status.

## Installation and Execution

### Pre-requisites:

* Ensure that Python 3 is installed on your system.

* Make sure that Pip, the Python package installer, is available.

* Install Docker on your machine. You can find instructions for your specific operating system on the Docker website.

* If you plan to clone or manage your project with Git, ensure that Git is installed on your machine.

### Execution Commands:

1) Creates a virtual environment named 'venv' to isolate project dependencies.
```
python3 -m venv venv
```
2) Activates the virtual environment to ensure that project dependencies are isolated.
```
source venv/bin/activate
```
3) Installs the Flask framework, which is a web framework for Python.
```
pip install flask
```
4) Runs the Flask application defined in 'app.py'.
```
python3 app.py
```
5) Builds a Docker image named 'flask-rest-api' based on the instructions in 'Dockerfile.dockerfile'.
```
docker build -t flask-rest-api -f Dockerfile.dockerfile .
```
6) Lists Docker images, including the newly built 'flask-rest-api'.
```
docker images
```
7) Starts a Docker container named 'flask-rest-api', daemonized (-d), and maps port 5000 on the host to port 5000 in the container.
```
docker run -d -p 5000:5000 flask-rest-api
```
8) Displays the logs for the specified Docker container, providing information about the running application.
```
docker logs <docker container name>
```
--> These commands are typically used in a development environment to set up and run a Flask application using Docker.


