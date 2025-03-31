from flask import Flask
from extension import db
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

from views import *

database = "test_db"

password = os.environ.get("PASSWORD")
username = os.environ.get("USERNAME")
database = os.environ.get("DATABASE")
ip = os.environ.get("IP")

print(f"当前密码为{password}, 用户名为{username}, ip为{ip}, 数据库名为{database}")

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{username}:{password}@{ip}/{database}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

def main():
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=9999, host='0.0.0.0')

if __name__ == '__main__':
    main()