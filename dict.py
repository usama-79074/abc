
# a dictionary (dict) is a data type used to store data in key–value pairs.This means each value has a key (name) that you use to access it.



#Student= {                                                                 
# "Name":"Usama Ahmad",
# "Age":18,
# "Adress":"Kps road rachna town lahore",
# "colour":"white",
# "course":["python","ai","basic"],
# "study":"avtive",
# "roll no":36
# }
# a=Student.get("colour")
# print(Student)
# print(Student["Adress"])

#Dict

student2= {
"name":"ali",
"roll_no":12,
"class":10,
"adress":"lahore pakistan",
"course":["ai","basic"]
}

# print(student2)

#types of dict

#lenth dict
# print(len(student2))
#type 
# print(type(student2))
#acess item
# x=student2["name"]
# print(x)
#get method
# y=student2.get("adress")
# print(y)
#keys
# z=student2.keys()
# print(z)
#change item 
# student2["class"]= 12
# print(student2)
#update method
# student2.update({"roll_no":11})
# print(student2)
#add item
# student2["num"]=1100
# print(student2)
#remove item 
# student2.pop("adress")
# print(student2)


user_information ={
    "Name":"Usama Ahmad",
    "Age":18,
    "city":"Lahore"
}
user_information["Grade"]='A+'
print(user_information)
