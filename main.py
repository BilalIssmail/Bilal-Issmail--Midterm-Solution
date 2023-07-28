n = 0 # setting a counter for admin attempts
def dispMenu(n):
  # taking user input
  if n < 5 : # max attempt limit
    print("Hello! Please enter username and password. If you're here to book a ticket, leave password blank.")
    
    user_name = input("Enter your username:")
    password = input("Enter your password:")

    if password == "": #blank password indicate normal user
      print("Welcome " + user_name + "!")
      print("def dispUserMenu")

    elif user_name == "admin" and password == "admin123123":
      print ("Welcome admin!")
      print("def dispAdMenu")
    else: # entering any password is considered an admin attempt
      print("You've entered a wrong password. Please enter the correct admin password or leave password blank if you want to book a ticket.")
      n += 1 # incrementing the attempt counter
      print("You have " + str(5 - n) + " attempts left to access admin menu.")
      dispMenu(n)

  else:
    print("You have reached maximum attempt limit.")

dispMenu(n)
