## 删除用户
URL: /delete_user
Method: post

参数: user_id
格式: json
`{"id": <user_id> }`

返回:<br>
    `{"code": 0, "msg": "ok"}`<br>
    `{"code": 1, "msg": "error"}`


## 通过用户名字获取用户信息

URL: /get_user_by_name<br>
method: get<br>
参数: name<br>
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

