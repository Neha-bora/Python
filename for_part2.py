student = {

     "male":["abhishek","vicky","ashu","suraj","faiz","yuvi",
             "vipin biduri","shashikant"],
     "female": ["komal","anju","kajal","vaishali",
                "pinky","neha","yukti","pooja"],

             }

for key in student.keys():
   for name in student[key]:
    if "a" in name:
       print(name)
