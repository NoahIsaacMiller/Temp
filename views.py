from app import app
from models import User

from flask import render_template, request


@app.route("/")
def index():
    return "Hello World!"

@app.route("/get_user_by_name", methods=["GET"])
def getUser():
    data = {
        "code": "200",
        "msg": "success",
        "data": []
    }

    name = request.args.get("name")
    if not name:
        data["code"] = "400"
        data["msg"] = "name is required"
        return data
    
    users = User.findUsersByName()

    if not users:
        data["code"] = "400"
        data["msg"] = "user not found"
        return data
    

@app.route("/add_user", methods=["POST"])
def addUser():
    data = {
        "code": "200",
        "msg": "success",
        "data": []
    }

    name = request.form.get("name")
    age = request.form.get("age")
    gender = request.form.get("gender")

    if not name:
        data["code"] = "400"
        data["msg"] = "name is required"
        return data
    
    if not age:
        data["code"] = "400"
        data["msg"] = "age is required"
        return data
    
    if not gender:
        data["code"] = "400"
        data["msg"] = "gender is required"
        return data
    
    user = User(name=name, age=age, gender=gender)
    user.save()
    return data

@app.route("/update_user", methods=["POST"])
def updateUser():
    data = {
        "code": "200",
        "msg": "success",
        "data": []
    }
    id = request.form.get("id")
    name = request.form.get("name")
    age = request.form.get("age")
    gender = request.form.get("gender")
    if not id:
        data["code"] = "400"
        data["msg"] = "id is required"
        return data
    
    user = User.findUserById(id)
    if not user:
        data["code"] = "400"
        data["msg"] = "user not found"
        return data
    

@app.route("/get_user_by_gender", methods=["GET"])

def getUserByGender():
    data = {
        "code": "200",
        "msg": "success",
        "data": []
    }
    gender = request.args.get("gender")
    if not gender:
        data["code"] = "400"
        data["msg"] = "gender is required"
        return data
    
    users = User.findUsersByGender(gender)
    if not users:
        data["code"] = "400"
        data["msg"] = "user not found"
        return data
    
    data["data"] = users
    return data