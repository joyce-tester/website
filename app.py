from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@localhost/education_platform'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# Import routes
from routes import *

if __name__ == "__main__":
    app.run(debug=True)
