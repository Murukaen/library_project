# Library Web App - POC
## Prerequisites
- Python 3.8 or newer
## Run project
1. Run `source .venv/library/bin/activate` from project root dir - this should activate the python environment
2. Run `python manage.py migrate` - this sets up the db
3. Start server with `python manage.py runserver` - this starts the web server on localhost and the default port 8000; if you want to pick a different port, say 8080, you can run `python manage.py runserver 8080`
4. Run `python manage.py createsuperuser` to create an admin user
5. You can access admin page at localhost:port/admin
6. Enjoy

