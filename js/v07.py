import json
#促使student是一个dict格式的内容,不是json
student={
    "name":"liujun",
    "age":18,
    "mobile":"13550211725"
}

print(type(student))

stu_json = json.dumps(student)
print(type(stu_json))
print("JSON对象:{0}".format(stu_json))

stu_dict = json.loads(stu_json)
print(type(stu_dict))
print(stu_dict)