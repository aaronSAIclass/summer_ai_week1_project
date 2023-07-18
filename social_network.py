#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui

#bonus todo
#0.5 Checks for if ID doesnt exist
#0.0 (OPTIONAL OPTIONAL task) message as a class instead of a string
#0.001 data storage (meh)
#1. Friends only message setting?
#2. Sending and accepting friend requests instead of instant?
#3. Deleting sent friend requests before they are accepted?
#4. Deleting accounts? Or account shutdown(account cannot be friended, messaged, blocked, and cannot be accessed)?
#5. Passwords and login with ID + password

#Create instance of main social network object
ai_social_network = SocialNetwork()

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            p1 = ai_social_network.create_account() #create account and structure message are sourced to the social network class.
            ai_social_network.appendPerson(p1) #add player to the network's user list
            currentAccount = p1 #account to be modified, can be changed (see change account menu)
            print("Current User:", currentAccount.getName(), "Age:", currentAccount.getAge())
            print("Current User ID:", currentAccount.getID())
            print("********************************************************")
            print("")
        elif choice == "2":
            inner_menu_choice = social_network_ui.manageAccountMenu()
            #Handle inner menu here
            while True:
                if inner_menu_choice == "8": #breaks to main menu
                    break
                elif inner_menu_choice == "1": #edit account menu
                    #display details for clarity before editing account
                    print("Current User:", currentAccount.getName(), "Age:", currentAccount.getAge()) #current account represents the account being modified
                    print("Current User ID:", currentAccount.getID())
                    print("********************************************************")
                    print("")
                    edit_menu_choice = social_network_ui.editDetailsMenu()
                    while True:
                        if edit_menu_choice == "3": 
                            break
                        elif edit_menu_choice == "1":
                            nameT = input("Choose a new name.")
                            p1.setName(nameT) 
                            #can you directly access variables from a class in Python? 
                            #I use Java and in Java we use accesor metods to get variable values from an object and mutator methods to set the variables. 
                            #This sees to work in python but I'd like to know if I could skip this step
                            edit_menu_choice = social_network_ui.editDetailsMenu() #revert back to menu
                        elif edit_menu_choice == "2": #same as last choice different variable
                            ageT = input("Set your age.")
                            p1.setAge(ageT)
                            edit_menu_choice = social_network_ui.editDetailsMenu()
                        else:
                            edit_menu_choice = social_network_ui.editDetailsMenu()
                    break ##break at the end or will infinitely loop
                elif inner_menu_choice == "2": #add /remove friend
                    addfriend_menu_choice = social_network_ui.addFriendMenu()
                    while True:
                        if addfriend_menu_choice == "3":
                            break
                        elif addfriend_menu_choice == "1":
                            nameF = input("What is the ID of the friend? ")
                            for i in range(len(ai_social_network.getList())): #iterate through list of people to access individuals
                                IDL = ai_social_network.getList()[i].getID() #id is how everything runs. I found it too tiring to use direct name and ages which could provide duplicates.
                                
                                if(nameF == IDL): #block checker
                                    blocked = False
                                    for i in range(len(currentAccount.getBlockList())): #check the current account's block list
                                        if(currentAccount.getBlockList()[i].getID() == IDL):
                                            blocked = True
                                    for j in range(len(ai_social_network.getList()[i].getBlockList())):#check the target account's block list
                                        if(ai_social_network.getList()[i].getBlockList()[j].getID() == currentAccount.getID()):
                                            blocked = True
                                    if(blocked == False):   #if not blocked run function
                                        currentAccount.add_friend(ai_social_network.getList()[i])
                                        ai_social_network.getList()[i].add_friend(currentAccount)
                                        print("Friend Added!")
                                    else: #blocked message
                                        print("Failed. User is blockd or you are blocked.")
                            addfriend_menu_choice = social_network_ui.addFriendMenu()
                        elif addfriend_menu_choice == "2": #remove friend. Could benefit from turning this and the block checker into functions because I use both of these several times but nah
                            nameF = input("What is the ID of the friend? ") 
                            for i in range(len(ai_social_network.getList())):
                                IDL = ai_social_network.getList()[i].getID()            
                                if(nameF == IDL): #remove from each other's friend lists
                                    currentAccount.remove_friend(currentAccount.getFriendsList().index(ai_social_network.getList()[i]))
                                    ai_social_network.getList()[i].remove_friend(ai_social_network.getList()[i].getFriendsList().index(currentAccount))
                                    print("Friend Removed!")
                            addfriend_menu_choice = social_network_ui.addFriendMenu()
                        else:
                            addfriend_menu_choice = social_network_ui.addFriendMenu()

                    break

                elif inner_menu_choice == "3": #friends list
                    viewfriends_menu_choice = social_network_ui.viewFriendsMenu()
                    while True:
                        if viewfriends_menu_choice == "2":
                            break
                        elif viewfriends_menu_choice == "1":
                            for i in range(len(currentAccount.getFriendsList())): #iterate through list, print name age user ID
                                friend = currentAccount.getFriendsList()[i]
                                print(friend.getName(),",", friend.getAge(), "years old. ID:", friend.getID())
                            break
                        else:
                            viewfriends_menu_choice = social_network_ui.viewFriendsMenu()
                    break 
                elif inner_menu_choice == "7": #change user
                    userchange_menu_choice = social_network_ui.changeUserMenu()
                    while True:
                        if userchange_menu_choice == "2":
                            break
                        elif userchange_menu_choice == "1":
                            IDP = input("Please Enter your account ID: ") #password in the future?
                            for i in range(len(ai_social_network.getList())):
                                IDB = ai_social_network.getList()[i].getID()
                                if(IDP == IDB):
                                    currentAccount = ai_social_network.getList()[i] #currentaccount is very important is as its what the program centers around
                                    
                                    print("Success!")
                            print("Current User:", currentAccount.getName(), "Age:", currentAccount.getAge())
                            print("Current User ID:", currentAccount.getID())
                            print("********************************************************")
                            print("")
                            userchange_menu_choice = social_network_ui.changeUserMenu()    
                        else:
                            userchange_menu_choice = social_network_ui.changeUserMenu()    
                    break

                elif inner_menu_choice == "6": #block menu
                    blockuser_menu_choice = social_network_ui.blockUserMenu()
                    while True:
                        if blockuser_menu_choice == "4":
                            break
                        elif blockuser_menu_choice == "1": #block
                            persontoblock = input("Enter the ID of the user you would like to block: ")
                            for i in range(len(ai_social_network.getList())):
                                IDB = ai_social_network.getList()[i].getID()
                                if(persontoblock == IDB): #remove friend
                                    for j in range(len(currentAccount.getFriendsList())):
                                        player = currentAccount.getFriendsList()[j]
                                        if(player.getID() == persontoblock):
                                            currentAccount.remove_friend(currentAccount.getFriendsList().index(player)) #copied removefriend method from earlier (see add/remove friend)                                        
                                            player.remove_friend(player.getFriendsList().index(currentAccount))
                                            print("Friend Removed!")
                                    currentAccount.block_user(ai_social_network.getList()[i])
                                    print("User Blocked!")
                            blockuser_menu_choice = social_network_ui.blockUserMenu()
                        elif blockuser_menu_choice == "2": #unblock user
                            persontounblock = input("Enter the ID of the user you would like to unblock: ")
                            for i in range(len(ai_social_network.getList())):
                                IDB = ai_social_network.getList()[i].getID()
                                if(persontounblock == IDB):
                                    print("User Unblocked!")
                                    currentAccount.remove_block(currentAccount.getBlockList().index(ai_social_network.getList()[i]))#block lists are not shared between accounts when adding/removing, though friend lists are
                            blockuser_menu_choice = social_network_ui.blockUserMenu()

                        elif blockuser_menu_choice == "3": #block list
                            for i in range(len(currentAccount.getBlockList())): #basically same as friend list code
                                loser = currentAccount.getBlockList()[i] #funny variable name
                                print(loser.getName(),",", loser.getAge(), "years old. ID:", loser.getID())
                            blockuser_menu_choice = social_network_ui.blockUserMenu()
                        
                        else:
                            blockuser_menu_choice = social_network_ui.blockUserMenu()
                    break

                elif inner_menu_choice == "4": #view messages 
                    viewmessages_menu_choice = social_network_ui.viewMessagesMenu()
                    while True:
                        if viewmessages_menu_choice == "3":          
                            break
                        elif viewmessages_menu_choice == "1": #message list
                            for i in range(len(currentAccount.getMessageList())):
                                message = currentAccount.getMessageList()[i]
                                print(message) #no fancy stuff since a message is just a long string
                            viewmessages_menu_choice = social_network_ui.viewMessagesMenu()
                        elif viewmessages_menu_choice == "2": #delete a message to avoid clutter, gives the option to go back
                            popmessage = input("Please go back and take a look at your messages. Type the index of the message you want to delete here, or -1 to go back. ")
                            if (popmessage == "-1"): #go back
                                viewmessages_menu_choice = social_network_ui.viewMessagesMenu()
                            else:
                                currentAccount.pop_message((popmessage)) #simple
                            break
                        else:
                            viewmessages_menu_choice = social_network_ui.viewMessagesMenu()                           
                    break
                elif inner_menu_choice == "5": #send messages
                    sender_menu_choice = social_network_ui.sendMessageMenu()
                    while True:
                        if sender_menu_choice == "3":
                            break
                        elif sender_menu_choice == "1": 
                            #same code as show the friends list, just gave the option to do it here for convenience. 
                            #Later I could just condense the friend list shower to the add / remove friends menu, 
                            #and the message deletr and shower to this menu. not worth my time though, likely.
                            for i in range(len(currentAccount.getFriendsList())): 
                                friend = currentAccount.getFriendsList()[i]
                                print(friend.getName(),",", friend.getAge(), "years old. ID:", friend.getID())
                            sender_menu_choice = social_network_ui.sendMessageMenu()
                        elif sender_menu_choice == "2": #send message
                            friendID = input("Please enter the ID of the user you would like to send the message to: ") #doesnt actually have to be a friend. In most social media's you can normally message non-blocked users, unless they have a friends only setting
                            messageText = input("Please enter your message: ")
                            finalText = ai_social_network.structure_message(currentAccount.getName(), currentAccount.getID(), messageText) #build message
                            notSent = True #boolean for error message later on
                            for i in range(len(ai_social_network.getList())):
                                IDB = ai_social_network.getList()[i].getID()
                                if(friendID == IDB): #copy of block checker
                                    blocked = False
                                    for k in range(len(currentAccount.getBlockList())):
                                        if(currentAccount.getBlockList()[k].getID() == friendID):
                                            blocked = True
                                    for j in range(len(ai_social_network.getList()[i].getBlockList())):
                                        if(ai_social_network.getList()[i].getBlockList()[j].getID() == currentAccount.getID()):
                                            blocked = True
                                    if(blocked == False):
                                        ai_social_network.getList()[i].add_message(finalText)
                                        print("Message sent!")
                                        notSent = False #message register as sent
                                    else: #blocked error message
                                        print("Could not send message. Either recipient is blocked, or sender is blocked.")      
                            if(notSent == True): #if message failed to send give this error message
                                print("Message failed to send.")          
                            sender_menu_choice = social_network_ui.sendMessageMenu()
                        else:
                            sender_menu_choice = social_network_ui.sendMessageMenu()
                    break
                else:
                    inner_menu_choice = social_network_ui.manageAccountMenu()

        elif choice == "3":
            print("Thank you for visiting. Goodbye3")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
