with open("text.txt","r+") as file:
  #https://youtu.be/Uh2ebFW8OYM (File objects - Reading and writing to file. Includes iterating through file lines)

  l = [] #empty list to append items in the lines of file
  for line in file:
    line = line.strip()
    l.append(line)

#Let's convert the list to dictionary with key being ticket id, and value being a list of four parameters.
  D = {}
  for i in range(len(l)):
    ticket = l[i].split(", ")
    D[ticket[0]] = [ticket[1],ticket[2],ticket[3],ticket[4]]

  # In the same way let's make a list collecting all tickets as list items.
  lst1 = []
  for i in range(len(l)):
    lst1.append(l[i].split(", "))



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
  admin_input = input("""Admin Menu:
1. Display Statistics
2. Book a Ticket
3. Display all Tickets
4. Change Ticket’s Priority
5. Disable Ticket
6. Run Events
7. Exit
Please enter the number of your choice: """  )
  if int(admin_input) == 1:
    dispStat()
    dispAdMenu()
  elif int(admin_input) == 2:
    bookTicket()
    saveChanges()
    dispAdMenu()
  elif int(admin_input) == 3:
    dispAllTickets()
    dispAdMenu()
  elif int(admin_input) == 4:
    changePriority()
    saveChanges()
    dispAdMenu()
  elif int(admin_input) == 5:
    removeTicket()
    saveChanges()
    dispAdMenu()
  elif int(admin_input) == 6:
    runEvents()
    dispAdMenu()
  elif int(admin_input) == 7:
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
  if int(user_input) == 1:
    bookTicket1()
    saveChanges()
    print("""Your ticket has been successfully booked.
    You can book another ticket or exit.""")
    dispUserMenu()
  elif int(user_input) == 2:
    print("You have logged out.")
    dispMenu(n)
  else:
    print("Wrong entry. Please choose a number from the menu.")
    dispUserMenu()


##############################
# Normal User Menu Functions:#
##############################

# 1- Book a ticket:


def bookTicket1(): #same as admin book ticket function except that in this case the priority will be 0 by default without normal user interferance.
  id_list = [i for i in D]
  id_list.sort()
  new_ticket = int((id_list[-1][4:]))+1
  
  if new_ticket < 10:
    ticket_id = "tick00" + str(new_ticket)
  elif 10 <= new_ticket <100 :
    ticket_id = "tick0" + str(new_ticket)
  else:
    ticket_id = "tick" + str(new_ticket)

  user_name = input("Please enter the username you want to print on ticket: ")
  event_id = input("Please enter the event id: ")
  event_date  =input("Please enter the event date in the form YYYYMMDD: ")

  D[ticket_id] = [event_id,user_name,event_date, "0"]
  print(ticket_id + " was successfully booked.")

######################
#Admin Menu Functions#
######################

# 1- Display Statistics:
"""event_dict = {}
for i in D:
  if D[i][0] not in event_dict:
    event_dict[D[i][0]]=[i]
  else:
    event_dict[D[i][0]].append(i)


date_dict = {}
for i in D:
  if D[i][2] not in date_dict:
    date_dict[D[i][2]]=[i]
  else:
    date_dict[D[i][2]].append(i)"""

def dispStat():
  events_dict = {}
  for item in lst1:
    event_id = item[1]
    events_dict[event_id] = events_dict.get(event_id, 0) + 1
  max_event = max(events_dict, key=events_dict.get)
  print(f"The event with the most tickets is {max_event}, with {events_dict[max_event]} tickets.")

  

#list that shows all events: here I tried to make a dictionary to use later to count each event lists considering events with same id but different date different events, but I did not manage to discriminate events based on both date and id.

all_ev_lst = []
for i in range(len(lst1)):
  for j in range(len(lst1[i])):
    temp_lst = [lst1[i][3],lst1[i][1]]
    if temp_lst not in all_ev_lst: 
      all_ev_lst.append(temp_lst)

        
# 2- Admin Book ticket

def bookTicket():

  id_list = [i for i in D]
  id_list.sort()
  new_ticket = int((id_list[-1][4:]))+1
  
  if new_ticket < 10:
    ticket_id = "tick00" + str(new_ticket)
  elif 10 <= new_ticket <100 :
    ticket_id = "tick0" + str(new_ticket)
  else:
    ticket_id = "tick" + str(new_ticket)

  user_name = input("Please enter the username: ")
  event_id = input("Please enter the event id: ")
  event_date  =input("Please enter the event date in the form YYYYMMDD: ")
  priority = input("Please enter the priority of the ticket: ")

  D[ticket_id] = [event_id,user_name,event_date,priority]
  print(ticket_id + " was successfully booked.")

# 3- Display All Tickets

def dispAllTickets():
  today_events = []
  tomorrow_events = []
  upcoming_events = []
  mergeSort(lst1)
  from datetime import date
  today = date.today() # dd/mm/YY
  date = today.strftime("%Y%m%d")
  for ticket in lst1:
    if int(ticket[3])  == int(date):
      today_events.append(ticket)
      mergeSort1(today_events)
    elif int(ticket[3])  == int(date) + 1:
      tomorrow_events.append(ticket)
      mergeSort(tomorrow_events)
    elif int(ticket[3])  > int(date) + 1:
      upcoming_events.append(ticket)
      mergeSort(upcoming_events)
      #mergeSort1(upcoming_events) #I failed to sort this list according to event id because it ruined sorting according to date.

  print("Today's events tickets are: ")
  print(today_events)
  print("Tomorrow's events tickets are: ")
  print(tomorrow_events)
  print("Upcoming events tickets are: ")
  print(upcoming_events)
#mergeSort1(upcoming_events)
 # print(upcoming_events)
  
def mergeSort(l): #I used merge sorting based on date.
  if len(l)>1:
    left_side=l[:len(l)//2]
    right_side=l[len(l)//2:]
    mergeSort(left_side) 
    mergeSort(right_side)

    i=0 
    j=0 
    m=0 
    while i<len(left_side) and j<len(right_side):
      if int(left_side[i][3])<int(right_side[j][3]):
        l[m]=left_side[i]
        i+=1
      else:
        l[m]=right_side[j]
        j+=1
      m+=1
    while i<len(left_side):
      l[m]=left_side[i]
      i+=1
      m+=1
    while j>len(right_side):
      l[m]=right_side[j]
      j+=1
      m+=1
  else:
    return 
#To import date from computer and format it as specified:
  from datetime import date
  today = date.today() # dd/mm/YY
  date = today.strftime("%Y%m%d")   #https://www.programiz.com/python-programming/datetime/current-datetime

#Then I used another merge sorting function to sort lists based on evend id (but this lead me later to a bug when the list contain lists having different date (upcoming events list) since it will ruin the sorting by date.)
def mergeSort1(l):
    if len(l)>1:
      left_side=l[:len(l)//2]
      right_side=l[len(l)//2:]
      mergeSort1(left_side) 
      mergeSort1(right_side)

      i=0 
      j=0 
      m=0 
      while i<len(left_side) and j<len(right_side):
        if int(left_side[i][1][2:])<int(right_side[j][1][2:]):
          l[m]=left_side[i]
          i+=1
        else:
          l[m]=right_side[j]
          j+=1
        m+=1
      while i<len(left_side):
        l[m]=left_side[i]
        i+=1
        m+=1
      while j>len(right_side):
        l[m]=right_side[j]
        j+=1
        m+=1
    else:
      return

# 4- Change Priority:

def changePriority():
  ticket_id = input("Enter the id of the ticket you want to change priority for: ")
  if ticket_id not in D:
    print("The ticket id entered does not exist in the system. please enter a correct ticket id.")
    changePriority()
  else:
    new_priority = int(input("Enter the new priority value to be assigned to this ticket: "))
    D[ticket_id][3] = new_priority
    print("The ticket " + ticket_id + " has been successfully assigned a " + str(new_priority) + " priority value.")
  dispAdMenu()

# 5- Remove Ticket:
def removeTicket():
  ticket_id = input("Enter the id of the ticket you want to remove: ")
  if ticket_id not in D:
    print("The ticket id entered does not exist in the system. please enter a correct ticket id.")
    removeTicket()
  else:
    print("The ticket " + ticket_id + " has been successfully removed.")
    del D[ticket_id]
  dispAdMenu()


  

# 6 Run Events:
#same used before to get date from computer:
from datetime import date
today = date.today() # dd/mm/YY
date = today.strftime("%Y%m%d") #https://www.programiz.com/python-programming/datetime/current-datetime
def runEvents():
  print("The following tickets are to be run today: ")
  today_events = [ticket for ticket in lst1 if ticket[3] == date]
  


  """today_events = []
  for ticket in lst1:
    if ticket[3] == date:
      today_events.append(ticket)"""

  def sortPriority(today_events): #merge sort our list by priority to show higher priority tickets first
    if len(today_events)>1:
      left_side=today_events[:len(today_events)//2]
      right_side=today_events[len(today_events)//2:]
      mergeSort1(left_side) 
      mergeSort1(right_side)

      i=0 
      j=0 
      m=0 
      while i<len(left_side) and j<len(right_side):
        if int(left_side[i][4])>int(right_side[j][4]):
          today_events[m]=left_side[i]
          i+=1
        else:
          today_events[m]=right_side[j]
          j+=1
        m+=1
      while i<len(left_side):
        today_events[m]=left_side[i]
        i+=1
        m+=1
      while j>len(right_side):
        today_events[m]=right_side[j]
        j+=1
        m+=1
    else:
      return

  sortPriority(today_events)
  today_events.sort(key=lambda ticket: int(ticket[4])) ##used .sorted lambda because merge sort function I've created (sortPriority) is not executed in runEvent().
  for ticket in today_events:
    print(ticket)

  updated_lst1 = [ticket for ticket in lst1 if ticket not in today_events]
  lst1.clear()
  lst1.extend(updated_lst1)
  saveChanges()
    

# Defining a function to save changes to txt file:
def saveChanges():
  new_list=[]
  for i in D:
    new_list.append(', '.join(str([i]+D[i])))
  with open("text.txt","w") as file:
    for i in new_list:  
      file.write(i+"\n")
  return




dispMenu(n)