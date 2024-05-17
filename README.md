# Django Template Project #

_Created 15/may/2024_

python 3.8

### Set Up ###
0. Clone repository.
1. Create environment using python 3.8 and activate it.
2. Move to the correct directory: `django_template`. You should see the `manage.py` file in that directory.
3. Install requirements: `pip install --upgrade pip && pip install -r requirements.txt`
4. Activate virtual environment variables if not already active (For example: `source outside_project/local_env_vars.sh`)
5. Check for pending migrations: `python manage.py makemigrations`
6. Run migrations: `python manage.py migrate` (It will generate a Database file in the current directory, called: `db.sqlite3`)
7. The server is ready to run. See "Create superuser" to have user with master admin privileges.

### Creating Superuser ###
You can create a superuser running:
`python manage.py createsuperuser`
and following the instructions presented in the command line

### Database Configuration ###
Django will create a database file (`db.sqlite3`) in the current directory when migrations are executed.
Feel free to remove this file if you want to restart the database.

### Environment Variables ###
An example of environment variables are in the directory `outside_project` (`local_env_vars.sh`, `production_env_vars.sh`)
You can activate them executing the bash file, for example:
`source local_env_vars.sh`

### Run the server ###
To activate the server in order to provide responses, run:
`python manage.py runserver`
Now you can go to your browser and put `localhost:8000/admin` to se a response.

Another port could be selected, and you can make the server available to the local network running something like:
`python manage.py runserver 0.0.0.0:8001`

### Admin ###
Once the server is up and running, you could access the admin page in your web browser via the url:
`localhost:8000/admin`

In this admin you can create, modify and delete users and its permissions using groups or particular restrictions.

### How to run tests ###
To run tests just run:
`python manage.py test`

Additional options could be found running:
`python manage.py test --help`

### Tips ###
To see available django commands run:
`python manage.py --help`

And particular options for that command running
`python manage.py <the command> --help`

### Contact ###
* juanmanuel.ca.se@gmail.com
