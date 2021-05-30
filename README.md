# game_app
Test Game App

## How to run project
1. Create directory : $mkidr game_app
2. clone repository : $git clone https://github.com/rohan-khairnar/game_app.git
3. Create Virtual environment : $Virtualenv ven ( or any other package like pipenv)
4. install requirements : $pip install -r requirements.txt
5. update mysql database path which is in dev.cfg file (Please provide complete path up to database name)
6. migrate db: <br>
    a. $flask db init : It will create migration file in core directory.<br>
    b. $flask db migrate -m "< commit >". <br>
    c. $flask db upgrade : You can see tables in your database. <br>
   
7. flask run or python app.py(for debug)

### Urls are mentioned in config.py file.

## Project directory details
1.core : It has migration, model and services abstract class.<br>
    a.Services abstract classes are use as parent class for implementation classes service.<br>
        So the implementation will be based on this abstract classes.<br>
2.src : It has view files and services directory which has database operation in repository dir and the APIs logic implementation in impl directory.<br>
    a. This repositories and services are passed to app_service.py in src/services/ which has AppServiceImpl class.<br>
    b. This AppServiceImpl class is called in src/__init__.py file which get called initially. So the service are passed to views through this class.
