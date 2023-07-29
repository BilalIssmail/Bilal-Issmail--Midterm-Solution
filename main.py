with open("text.txt","r+") as file:
  #https://youtu.be/Uh2ebFW8OYM (File objects - Reading and writing to file. Includes iterating through file lines)

  l = [] #empty list to append items in the lines of file
  for line in file:
    line = line.strip()
    l.append(line)
#Let's convert the list to dictionary witj key being ticket id, and value being a list of four parameters.
  D = {}
  for i in range(len(l)):
    ticket = l[i].split(", ")
    D[ticket[0]] = [ticket[1],ticket[2],ticket[3],ticket[4]]





####################
#Date: Create a variable that takes date from computer and format it as specified in the midterm assignment##
####################

from datetime import date

today = date.today()

# dd/mm/YY
date = today.strftime("%Y%m%d")
#https://www.programiz.com/python-programming/datetime/current-datetime





####################
#Display Main Menu:#
####################


n = 0 # setting a counter for admin attempts
def dispMenu(n):
  # taking user input
  if n < 5 : # max attempt limit
    print("Hello! Please enter username and password. If you're here to book a ticket, leave password blank.")
    
    user_name = input("Enter your username:")
    password = input("Enter your password:")

    if password == "": #blank password indicate normal user
      if user_name == "admin":
        print("You've entered a wrong password. Please enter the correct admin password, or enter your username and leave password blank if you want to book a ticket.")
        n += 1
        print("You have " + str(5 - n) + " attempts left to access admin menu.")
        dispMenu(n)

      else:
        print("Welcome " + user_name + "!")
        dispUserMenu()

    elif user_name == "admin" and password == "admin123123":
      print ("Welcome admin!")
      dispAdMenu()
    else: # entering any password is considered an admin attempt
      print("You've entered a wrong password. Please enter the correct admin password, or enter your username and leave password blank if you want to book a ticket.")
      n += 1 # incrementing the attempt counter
      print("You have " + str(5 - n) + " attempts left to access admin menu.")
      dispMenu(n)

  else:
    print("You have reached maximum attempt limit.")


#####################
#Display Admin Menu:#
#####################


def dispAdMenu():
  admin_input = input("""Please select the number of your choice:
1. Display Statistics")
2. Book a Ticket
3. Display all Tickets
4. Change Ticket’s Priority
5. Disable Ticket
6. Run Events
7. Exit
"""  )
  if admin_input == 1:
    dispStat()
    dispAdMenu()
  elif admin_input == 2:
    bookTicket()
    dispAdMenu()
  elif admin_input == 3:
    dispAllTickets()
    dispAdMenu()
  elif admin_input == 4:
    changePriority()
    dispAdMenu
  elif admin_input == 5:
    disableTicket()
    dispAdMenu()
  elif admin_input == 6:
    runEvent()
    dispAdMenu()
  elif admin_input == 7:
    print("You have logged out.")
    dispMenu(n)
  else:
    print("Wrong entry. Please select a number from the shown menu.")
    dispAdMenu()


###########################
#Display Normal User Menu:#
###########################


def dispUserMenu():
  user_input = input("""Please select the number of your choice:
  1. Book a ticket
  2. Exit
  """)
  if user_input == 1:
    bookTicket()
    print("""Your ticket has been successfully booked.
    You can book another ticket or exit.""")
    dispUserMenu()


###############






