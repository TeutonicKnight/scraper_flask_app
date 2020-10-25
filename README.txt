Flask exercise for MEN Technology and Media

Flask application that scrapes data from a table on https://ageofempires.fandom.com/wiki/Siege_weapons_(Age_of_Empires_II)

Below info is for my own reference.

----------------------
Git Bash commands used
----------------------
$ python -m venv env | Create new virtual environment
$ source .env | to set the venv and the environment variables manually on windows.
$ python -m pip freeze > requirements.txt | To update the requirements file
$ python manage.py runserver | start the development server
$ echo $APP_SETTINGS | Check environment variables

$ heroku login | login to heroku. Doesn't work on Bash, but loging in with cmd works
$ heroku create APP_NAME | create heroku app (best practice to create production and staging)
$ heroku create --remote REMOTE_VARIABLE | add heroku remote for GIT commands (production and staging)
$ git config heroku.remote REMOTE_VAR | Set default for heroku CLI commands, important when having multiple apps
$ heroku apps:rename NEWNAME --app OLDNAME | rename default heroku app name
$ heroku config:set APP_SETTINGS=config.ENVIRONMENTConfig --remote REMOTE_VAR | Set environment variables on Heroku (set prod and stage)
$ heroku run python app.py --app APP_NAME | Run app on heroku
$ heroku config --app APP_NAME | Check state of Heroku environment settings

$ python manage.py db init | Initialize Alembic
$ python manage.py db migrate | Create database migration
$ python manage.py db upgrade | apply the upgrades to the database
$ heroku addons:create heroku-postgresql:hobby-dev --app APP_NAME | Add postgress addon to heroku app
$ heroku run python manage.py db upgrade --app APP_NAME | Add migrations to heroku database (run after deployment)




