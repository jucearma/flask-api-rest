# Tutorial : https://www.nintyzeros.com/2019/11/flask-mysql-crud-restful-api.html
#           https://code.visualstudio.com/docs/python/tutorial-flask
#           https://github.com/Microsoft/python-sample-vscode-flask-tutorial
# Install dependencies
mkdir django_rest_api && cd django_rest_api
# Update pip
python -m pip install --upgrade pip
#python -m venv env
#env\Scripts\Activate.ps1 # Windows
#virtualenv -p python3 venv
virtualenv -p python venv
source venv/bin/activate
(venv)> pip install flask flask-sqlalchemy httpie pymysql marshmallow-sqlalchemy

# Create requeriments.txt
pip freeze > requirements.txt

# Install requeriments
pip install -r requirements.txt

# https://github.com/sonyarianto/docker-compose-mysql-with-adminer
# Run Mysql Container
docker-compose up -d
# Check Mysql container is running
docker ps
# Check volumes
docker volume ls
# Go to http://localhost:8080 or http://127.0.0.1:8080 and fill the credential. User root and password rootpassword.
# Via command line
mysql -uroot -prootpassword -h 127.0.0.1
# How to stop the MySQL server
# To shutdown database without delete all containers.
docker-compose stop
# To shutdown database and delete all containers.
docker-compose down

# Create app.py 
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

# Set an environment variable for FLASK_APP. On Linux and macOS, use export set FLASK_APP=webapp; on Windows use set FLASK_APP=webapp.
export set FLASK_APP=alerts.webapp
# Execute application
python -m flask run
# Especifi hostname and port 
python -m flask run --host=0.0.0.0 --port=80

# Sugerencia : Si desea utilizar un nombre de archivo diferente a app.py, por ejemplo program.py, defina una variable de entorno llamada FLASK_APP y establezca su valor en el archivo elegido. El servidor de desarrollo de Flask usa el valor de FLASK_APP en lugar del archivo predeterminado app.py. Para obtener más información, consulte Interfaz de línea de comandos de Flask.

