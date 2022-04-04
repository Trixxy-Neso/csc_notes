######################################################################
#   Name:           Josephine Rei Sale
#   Date:           12/20/2021
#   Description:    A room exploring adventure!!
######################################################################
######################################################################
# the blueprint for a room
class Room:
# the constructor
    def __init__(self, name):
# rooms have a name, exits, exit locations, items, item descriptions, and grabbables
        self.name = name
        self.exits = []
        self.locations = []
        self.hidden = []            # New Catagory!!!
        self.items = []
        self.descriptions = []
        self.grabbables = []
    # getters and setters for the instance variables
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def exits(self):
        return self._exits
    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def locations(self):
        return self._locations
    @locations.setter
    def locations(self, value):
        self._locations = value

    @property
    def hidden(self):
        return self._hidden
    @hidden.setter
    def hidden(self, value):
        self._hidden = value

    @property
    def items(self):
        return self._items
    @items.setter
    def items(self, value):
        self._items = value

    @property
    def descriptions(self):
        return self._descriptions
    @descriptions.setter
    def descriptions(self, value):
        self._descriptions = value

    @property
    def grabbables(self):
        return self._grabbables
    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    def addExit(self, exit, room):
        self._exits.append(exit)
        self._locations.append(room)

    def addHidden(self, room):
        self._hidden.append(room)


    def addItem(self, item, desc):
        self._items.append(item)
        self._descriptions.append(desc)

    def addGrabbable(self, item):
        self._grabbables.append(item)

    def delGrabbable(self, item):       # I don't remember if I added this or not...
        self._grabbables.remove(item)

    def __str__(self):
        s = "You are in the {}.\n".format(self.name)
        s += "You see: "
        for item in self.items:
            s += item + " "
        s += "\n"
        s += "Exits: "
        for exit in self.exits:
            s += exit + " "
        return s


# creates the rooms
def createRooms():
    global currentRoom
    r1 = Room("entry")
    r2 = Room("living room")
    r3 = Room("library")
    r5 = Room("laboratory")
    r4 = Room("bedroom")
    # add exits to room 1
    r1.addExit("east", r2) 
    r1.addExit("south", r3)
    # add grabbables to room 1
    r1.addGrabbable("key")
    # add items to room 1
    r1.addItem("chair", "It is made of wicker. It looks unstable.")
    r1.addItem("table", "It is made of oak. A golden key rests on it.")
    # add exits to room 2
    r2.addExit("west", r1)
    r2.addExit("south", r4)
    r2.addExit("north", None)
    # add items to room 2
    r2.addItem("carpet", "It is ornate and old. The colors are hard to make out due to dust.")
    r2.addItem("fireplace", "A fire crackles away, but who lit it...?")
    # add exits to room 3
    r3.addExit("north", r1)
    r3.addExit("east", r4)
    # add grabbables to room 3
    r3.addGrabbable("book")
    # add items to room 3
    r3.addItem("bookshelves", "They are full of dusty tomes.")
    r3.addItem("statue", "A marble figure resembling an angel. Tears near the eyes are stark black.")
    r3.addItem("desk", "The statue is resting on it. So is a book.")
    # add exits to room 4
    r4.addExit("north", r2)
    r4.addExit("west", r3)
    r4.addHidden(r5)
    # add items to room 4
                                # New Room!
    r4.addItem("bed", "The bed is made, but the blankets are worn and tattered.")
    r4.addItem("dresser", "It is made of dark wood. The drawers are stuck shut.")
    r4.addItem("rug", "Moving it reveals a trap door.") # It's a path!
    # add exit to room 5
    r5.addExit("up", r4)
    # add grabbables to room 5
    r5.addGrabbable("vial")
    # add items to room 5
    r5.addItem("distiller", "It is being used to brew some sort of murky substance. A strange vial is resting beside it.")
# set room 1 as the current room at the beginning of the game
    currentRoom = r1

def death():
    print(" " * 17 + "u" * 7)
    print(" " * 13 + "u" * 2 + "$" * 11 + "u" * 2)
    print(" " * 10 + "u" * 2 + "$" * 17 + "u" * 2)
    print(" " * 9 + "u" + "$" * 21 + "u")
    print(" " * 8 + "u" + "$" * 23 + "u")
    print(" " * 7 + "u" + "$" * 25 + "u")
    print(" " * 7 + "u" + "$" * 25 + "u")
    print(" " * 7 + "u" + "$" * 6 + "\"" + " " * 3 + "\"" + "$" * 3 + "\"" + " " * 3 + "\"" + "$" * 6 + "u")
    print(" " * 7 + "\"" + "$" * 4 + "\"" + " " * 6 + "u$u" + " " * 7 + "$" * 4 + "\"")
    print(" " * 8 + "$" * 3 + "u" + " " * 7 + "u$u" + " " * 7 + "u" + "$" * 3)
    print(" " * 8 + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3)
    print(" " * 9 + "\"" + "$" * 4 + "u" * 2 + "$" * 3 + " " * 3 + "$" * 3 + "u" * 2 + "$" * 4 + "\"")
    print(" " * 10 + "\"" + "$" * 7 + "\"" + " " * 3 + "\"" + "$" * 7 + "\"")
    print(" " * 12 + "u" + "$" * 7 + "u" + "$" * 7 + "u")
    print(" " * 13 + "u$\"$\"$\"$\"$\"$\"$u")
    print(" " * 2 + "u" * 3 + " " * 8 + "$" * 2 + "u$ $ $ $ $u" + "$" * 2 + " " * 7 + "u" * 3)
    print(" u" + "$" * 4 + " " * 8 + "$" * 5 + "u$u$u" + "$" * 3 + " " * 7 + "u" + "$" * 4)
    print(" " * 2 + "$" * 5 + "u" * 2 + " " * 6 + "\"" + "$" * 9 + "\"" + " " * 5 + "u" * 2 + "$" * 6)
    print("u" + "$" * 11 + "u" * 2 + " " * 4 + "\"" * 5 + " " * 4 + "u" * 4 + "$" * 10)
    print("$" * 4 + "\"" * 3 + "$" * 10 + "u" * 3 + " " * 3 + "u" * 2 + "$" * 9 + "\"" * 3 + "$" * 3 + "\"")
    print(" " + "\"" * 3 + " " * 6 + "\"" * 2 + "$" * 11 + "u" * 2 + " " + "\"" * 2 + "$" + "\"" * 3)
    print(" " * 11 + "u" * 4 + " \"\"" + "$" * 10 + "u" * 3)
    print(" " * 2 + "u" + "$" * 3 + "u" * 3 + "$" * 9 + "u" * 2 + " \"\"" + "$" * 11 + "u" * 3 + "$" * 3)
    print(" " * 2 + "$" * 10 + "\"" * 4 + " " * 11 + "\"\"" + "$" * 11 + "\"")
    print(" " * 3 + "\"" + "$" * 5 + "\"" + " " * 22 + "\"\"" + "$" * 4 + "\"\"")
    print(" " * 5 + "$" * 3 + "\"" + " " * 25 + "$" * 4 + "\"")
    print(" " * 7 + "You Burned!")

def search (search_val, the_list):              # useful later
    current_index = 0
    found = False
    while current_index < len (the_list) and found == False:
        if the_list [current_index] == search_val:
            found = True
        else:
            current_index += 1
    return found


######################################################################
# START THE GAME!!!
inventory = [] # nothing in inventory...yet
createRooms() # create the rooms
                                            # An intro cutscene!!
print ("While walking through the woods, you came across a derelict mansion.\nYou decided to explore.\n\nThe door locked behind you....")
while (True):
# set the status so the player has situational awareness
    status = "{}\nYou are carrying: {}\n".format(currentRoom, inventory)
    if (currentRoom == None):
        death()
        break
# display the status
    print("========================================================")
    print(status)
# take an input
    action = input("What to do? ")
    action = action.lower()
    # added extra ending words (kept forgetting the default words)
    if (action == "quit" or action == "exit" or action == "bye" or action == "end" or action == "stop"):
        break
    response = "I don't understand. Try verb noun. Valid verbs are go, look, take, and use"
    words = action.split()
    if (len(words) == 2):
        verb = words[0]
        noun = words[1]
        if (verb == "go"):
            response = "Invalid exit." # Default Response
            for i in range(len(currentRoom.exits)):
                if (noun == currentRoom.exits[i]):
                    currentRoom = currentRoom.locations[i]
                    response = "Room changed."
                    break
        elif (verb == "look"):
            response = "I don't see that item."
            for i in range(len(currentRoom.items)):
                if (noun == currentRoom.items[i]):
                    response = currentRoom.descriptions[i]
                    break
        elif (verb == "take"):
            response = "I don't see that item."
            for grabbable in currentRoom.grabbables:
                if (noun == grabbable):
                    inventory.append(grabbable)
                    currentRoom.delGrabbable(grabbable)
                    response = "Item grabbed."
                    break
    elif (words[0] == "use"):           # New Mechanic!! (Very limited use... sugestions?)
        response = ("I don't think that works here...")
        if words[1] == "key":
            if search ("key", inventory) == True:
                 for i in range(len(currentRoom.items)):
                    if ("rug" == currentRoom.items[i]):
                        if words[2] == "rug":
                            response = ("Going down...")
                            currentRoom = currentRoom.hidden[0]

    print("\n{}".format(response))
