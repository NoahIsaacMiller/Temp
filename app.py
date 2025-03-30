from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)


username = "root"
password = "$D:s9whilenhua+e"
ip = "localhost"
database = "test_db"

app.config["SECRET_KEY"] = "kissme"
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{username}:{password}@{ip}/{database}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


with app.app_context():
    db.init_app(app)

def main():
    app.run(debug=True, port=80, host='0.0.0.0')

if __name__ == '__main__':
    main()