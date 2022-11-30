# import the Flask framework
from flask import Flask, jsonify
from flaskext.mysql import MySQL

# import the blueprint objects from their respective locations
from src.artist.artist import artist
from src.collector.collector import collector
from src.admin.admin import admin

# create a flask object
app = Flask(__name__)

# path relative to mount within container
with open('/run/secrets/db_password') as pw_file:
    DB_PW = pw_file.readline().rstrip('\n')

print(f"DB_PW is {repr(DB_PW)}")

# register the blueprints we created with the current Flask app object.
app.register_blueprint(artist, url_prefix='/arts')
app.register_blueprint(collector, url_prefix='/cltr')
app.register_blueprint(admin, url_prefix='/adm')


app.config['SECRET_KEY'] = 'someCrazyS3cR3T!Key.!'
app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'webapp'
app.config['MYSQL_DATABASE_PASSWORD'] = DB_PW
app.config['MYSQL_DATABASE_DB'] = 'ART_INTERSECTION'
db_connection = MySQL()
db_connection.init_app(app)

# --------------------------------------------------------------------
# Create a function named hello world that
# returns a simple html string
# the @app.route("/") connects the hello_world function to
# the URL /
@app.route("/")
def hello_world():
    return f'<h1>Hello From the Flask-MySQL Connection Tutorial</h1>'

@app.route('/db_test')
def db_testing():
   cur = db_connection.get_db().cursor()
   cur.execute('select * from Artist')
   row_headers = [x[0] for x in cur.description]
   json_data = []
   theData = cur.fetchall()
   for row in theData:
       json_data.append(dict(zip(row_headers, row)))
   return jsonify(json_data)

# If this file is being run directly, then run the application
# via the app object.
# debug = True will provide helpful debugging information and
#   allow hot reloading of the source code as you make edits and
#   save the files.
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 4000)
