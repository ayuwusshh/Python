info={
  "name":"Ayush",
  "cgpa":9.6,
  "marks":[98,55,65]
}
# print(info["name"])

# nested dictionary
student={
  "name":"Ayush",
  "subject":{
    "phy":97,
    "chem":88,
    "bio":68
  },
  "age":31
}

#print(student["subject"]["phy"])
print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
print(student.update({"phn": 9631643696}))
print(student)