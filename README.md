# Project Title

A blogging application using Django -->  This project when deployed will allow users share the bloggin experience.

## Getting Started

To get started you must have python 3 up and running on your system.

### Ruuning the application

Create a virtual environment using the following scripts:

```
python3 -m venv ["name of your Virtual Env"]
```

Install the the libraries used for this project by copying and pasting the below script in your terminal

```
pip install -r requirements.txt # This will install the libraries used for this project
```

Run the database migrations using the commands below:

```
python manage.py makemigrations 

python manage.py migrate
```

Start the developement server with this command:

```
python manage.py runserver
```
