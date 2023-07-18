# You can implement user interface functions here.

def mainMenu():
    print("")
    print("1. Create a new account")
    print("2. Manage my account")
    print("3. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("")
    print("1. Edit my details")
    print("2. Add or remove a friend")
    print("3. View all my friends")
    print("4. View or delete messages")
    print("5. Send a message")
    print("6. Block or unblock a user")
    print("7. Change user")
    print("8. <- Go back ")
    print("********************************************************")
    return input("Please Choose a number: ")

def editDetailsMenu():
    print("")
    print("1. Change Name")
    print("2. Change Age")
    print("3. <- Go back")
    print("********************************************************")
    return input("Please Choose a number: ")

def addFriendMenu():
    print("")
    print("1. Add friend")
    print("2. Remove friend")
    print("3. <- Go back")
    print("********************************************************")
    return input("Please Choose a number: ")

def viewFriendsMenu():
    print("")
    print("1. View friends list")
    print("2. <- Go back")
    print("********************************************************")
    return input("Please Choose a number: ")

def changeUserMenu():
    print("")
    print("1. Change user")
    print("2. <- Go back")
    print("********************************************************")
    return input("Please Choose a number: ")

def blockUserMenu():
    print("")
    print("1. Block user")
    print("2. Unblock user")
    print("3. View block list")
    print("4. <- Go back")
    print("********************************************************")
    return input("Please Choose a number: ")
    
def viewMessagesMenu():
    print("")
    print("1. View messages")
    print("2. Delete message from inbox")
    print("3. <- Go back")
    print("********************************************************")
    return input("Please Choose a number: ")

def sendMessageMenu():
    print("")
    print("1. Display friends list")
    print("2. Send a message")
    print("3. <- Go back")
    print("********************************************************")
    return input("Please Choose a number: ")
