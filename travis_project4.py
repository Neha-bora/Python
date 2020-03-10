known_users=["Anju","Bob","Neha","Ashu","Kajal","Komal","Abhishek","Vicky"]


while True:
    print("Hi!My name is Neha")
    name = input("what is your name?:").strip().capitalize()

    if name in known_users:
       print("hello{}!".format(name))
       remove = input("would you like to be removed from the system(y/n)?:").strip().lower()

       if remove == "y":
         known_users.remove(name)
    
              
    else:
      print("hmmmm i dont think i have to met yet {}".format(name))
      add_me = input("would you like to be added to the system(y/n)?:").strip().lower()
      if add_me == "y":
        known_users.append(name)
      
    
    
   
