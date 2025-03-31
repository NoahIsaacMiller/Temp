## 通过用户名字获取用户信息
URL: `/get_users_by_name`<br>
method: `get`<br>
参数: `name`<br>
返回:<br>
    `{"code": 200, "msg": "ok", "data": [...]}`<br>
    `{"code": 400, "msg": "not found"}`

    data包含用户对象    
    User对象结构:
        {
            "id": id,
            "username": username,
            "gender": gender,
            "age": age
        }

## 通过获取制定性别的用户
URL: `/get_users_by_gender`<br>
method: `get`<br>
参数: `gender`<br>
返回:<br>
    `{"code": 200, "msg": "ok", "data": [...]}`
```
data包含用户对象    
User对象结构:
    {
        "id": id,
        "username": username,
        "gender": gender,
        "age": age
    } 
```

## 通过获取制定年龄的用户
URL: `/get_users_by_age`<br>
method: `get`<br>
参数: `age`<br>
返回:<br>
    `{"code": 200, "msg": "ok", "data": [...]}`
 ```
 data包含用户对象    
 User对象结构:
     {
         "id": id,
         "username": username,
         "gender": gender,
         "age": age
     }
```

## 通过年龄范围获取用户
URL: `/get_users_by_age_range`<br>
method: `get`<br>
参数: `age_min`, `age_max`
返回:<br>
    `{"code": 200, "msg": "ok", "data": [...]}`
```
data包含用户对象    
User对象结构:
    {
        "id": id,
        "username": username,
        "gender": gender,
        "age": age
    }
```
