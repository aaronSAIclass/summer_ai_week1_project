# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
import random as rand
class SocialNetwork:
    def __init__(self):
        self.list_of_people = []
        self.counter = 0 # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
                                 
    def getList(self):
        return self.list_of_people
    def appendPerson(self, Person):
        self.list_of_people.append(Person)    
    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def create_account(self):
        name = input("Enter your name. ")
        print("")
        age = input("Enter your age. ")
        print("")
        a1 = Person(name, age, str(self.counter)) 
        #Having a random ID is a fun idea but a bad one. First I dont want to check for duplicates every time I create an account 
        #When you are checking 1,000,000,000 accounts for a duplicate ID that is stupid. Also these are much simpler to remember
        #In the future I may add zeros in front of the ID up to a point but I find that useless and frustrating, and a design choice that makes a simple thing into a complex problem.
        self.counter += 1
        print("Creating ...")
        return a1
    def structure_message(self, sender, senderID, text): #just combines strings. Pretty simple
        variable = "From: "
        variable += sender
        variable += ". ID: "
        variable += senderID
        variable += ". Message: "
        variable += text
        return variable


class Person:
    def __init__(self, name, age, ID):
        self.id = name
        self.year = age
        self.friendlist = []
        self.messages = [] #would like to make message its own object class sometime but too much effort I think
        self.card = ID 
        self.blocklist = []

    def add_friend(self, person_object):
        #implement adding friend. Hint add to self.friendlist
        self.friendlist.append(person_object)
        pass

    def block_user(self, person_object):
        self.blocklist.append(person_object)
        pass

    def remove_friend(self, index):
        self.friendlist.pop(index)
        pass
    
    def remove_block(self, index):
        self.blocklist.pop(index)
        pass

    def add_message(self, theText):
        self.messages.append(theText)
        pass
    def pop_message(self, index):
        indexFin = int(index)
        if(indexFin < len(self.messages) and indexFin > -1):
            self.messages.pop(indexFin)
            print("Message deleted.")
        else:
            print("Message index out of bounds.") #didnt do this with the others but this is the only one you manually input an index into anyways
        pass
    def setAge(self, age):
        self.year = age
        pass
    def setName(self, name):
        self.id = name
        pass
    def getName(self):
        return self.id
        pass
    def getAge(self):
        return self.year
        pass ##I should really look up what "pass" does before I put it under every method but I am not going to
    def getFriendsList(self):
        return self.friendlist
        pass
    def getID(self):
        return self.card
        pass

    def getBlockList(self):
        return self.blocklist
        pass
    def getMessageList(self):
        return self.messages
        pass