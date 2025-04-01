from flask import render_template, request
from app import app
from models import User

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_users_by_name", methods=["GET"])
def getUserByName():
    data = {
        "code": 200,
        "msg": "success",
        "data": []
    }

    name = request.args.get("name")
    if not name:
        data["code"] = 400
        data["msg"] = "name is required"
        return data
    
    users = User.findUsersByName(name)

    if not users:
        data["code"] = 400
        data["msg"] = "user not found"
        return data
    
    data["data"] = [user.to_dict() for user in users]
    return data
    
@app.route("/get_users_by_gender", methods=["GET"])
def getUserByGender():
    data = {
        "code": 200,
        "msg": "success",
        "data": []
    }
    gender = request.args.get("gender")
    if not gender:
        data["code"] = 400
        data["msg"] = "gender is required"
        return data
    
    if gender not in "01":
        data["code"] = 400
        data["msg"] = "gender is invalid"
        print(type(gender), gender)
        return data
    
    data["data"] = [user.to_dict() for user in User.findUsersByGender(gender)]
    return data

@app.route("/get_users_by_age", methods=["GET"])
def getUserByAge():
    data = {
        "code": 200,
        "msg": "success",
        "data": []
    }

    age = request.args.get("age")
    if not age:
        data["code"] = 400
        data["msg"] = "age is required"
        return data
    
    if not age.isdigit():
        data["code"] = 400
        data["msg"] = "age is invalid"
        return data
    
    users = User.query.filter_by(age=age).all()
    data["data"] = [user.to_dict() for user in users]
    return data

@app.route("/get_users_by_age_range", methods=["GET"])
def getUserByAgeRange():
    data = {
        "code": 200,
        "msg": "success",
        "data": []
    }
    age_min = request.args.get("age_min")
    age_max = request.args.get("age_max")

    if not age_min and not age_max:
        data["code"] = 400
        data["msg"] = "age_min and age_max are required"
        return data
    
    if not age_min.isdigit() or not age_max.isdigit():
        data["code"] = 400
        data["msg"] = "age_min and age_max are invalid"
        return data
    
    if int(age_min) > int(age_max):
        data["code"] = 400
        data["msg"] = "age_min is greater than age_max"
        return data

    if not age_min or not age_max:
        data["code"] = 400
        data["msg"] = "age_min and age_max are required"
        return data
    
    users = User.query.filter(User.age >= age_min, User.age <= age_max).all()
    
    data["data"] = [user.to_dict() for user in users]
    return data