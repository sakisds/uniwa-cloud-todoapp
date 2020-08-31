# TODO App

A simple TODO app, project 1 of the Cloud Computing class at UNIWA, Department
of Electrical and Electronic Engineering.

## Installation
You can install the dependencies using pip and then run the app, either using
`gunicorn` for production or Flask's development server. Python 3 is required.

```sh
> pip install -r requirements.txt

# Development
> python -m todoapp

# Production
> gunicorn todoapp:app
```

## Docker
You can run the application using Docker and `docker-compose` (or `podman` and `podman-compose`):

```sh
> docker build . -t todoapp:1.1.0
> docker-compose up
```

## Demo
You can check the app at [Heroku](https://uniwa-cc-todoapp.herokuapp.com/).

## License
This app was written for the purposes of the class, feel free to use the code
for whenever reason. For the legalise check ![License.md].