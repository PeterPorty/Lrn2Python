
class Adventure:
    X = 0
    Y = 1
    maze = [[False, False, "Win", False, False],
    [False, True, True, False, True],
    [False, True, False, True, True],
    [False, True, False, True, False],
    [False, True, "Start", True, False]]

    def __init__(self):
        game_running=True
        self.location = [2, 4]
        while game_running==True:
            self.action()
            if self.location==[2, 0]:
                game_running=False
            
    def move(self, x, y):
        if self.maze[self.location[self.Y] + y][self.location[self.X] + x]:
            self.location[self.X] += x
            self.location[self.Y] += y
        else:
            raise Exception("You can't move here.")

    def action(self): 
        action=raw_input("What would you want to do?" )
        action=action.split()
        Help='These are the things you can do: Take, Use, Examine, Look, Go, Inv. Type      "Help_<Command>" to learn more about a specific command. You can see this again any time by typing "Help".'
        Help_Take='With this command, you can grab items from the world and add them to your inventory. You can not grab every object, and sometimes you need to do something before you can grab a particular one.  Use: "Take <name_of_object_in_the_world>". Objects will always be a single word, so keep that in mind.'
        Help_Use="""Use is an important command, since it allows you to interact with the objects in your inventory and in the world. Not every object is usable all the time, so you've got to think about when it would be useful. Use: "Use <name of item in inventory>"."""
        Help_Examine='This is simply to read further about a certain object found in the world; you can even find items hiding behind something when examining it. Use: "Examine <anything_in_the_scenery>".'
        Help_Look='This command is simply to show again the message describing the current scenery; this can be helpful when you think the scenery has changed after something happened. Use: "Look".'
        Help_Go='The Go command is the one that allows you to move around and explore the world. Use: "Go <N/S/W/E>".'
        Help_Inv='It simply lists all you have in your inventory.'
        inventory=[]
        Inv=inventory
        game_running=True
        #Sword
        SWORD_pickable=True
        SWORD_location=[2, 4]
        if action[0]=="Go":
            direction=action[1]
            try:
                if direction=="N":
                    self.move(0,-1)
                    print self.location
                elif direction=="E":
                    self.move(1,0)
                    print self.location
                elif direction=="W":
                    self.move(-1,0)
                    print self.location
                elif direction=="S":
                    self.move(0,1)
                    print self.location
                else:
                    print "well done, asshole, I already told you the ways you can go."
            except:
                pass
        elif action[0]=="Help":
            print Help
        elif action[0]=="Help_Use":
            print Help_Use
        elif action[0]=="Help_Inv":
            print Help_Inv
        elif action[0]=="Help_Examine":
            print Help_Examine
        elif action[0]=="Help_Take":
            print Help_Take
        elif action[0]=="Help_Go":
            print Help_Go
        elif action[0]=="Help_Look":
            print Help_Look
        elif action[0]=="Inv":
            print Inv
        elif action[0]=="End":
            game_running=False
        elif action[0]=="Take":
            item=action[1]
            if self.__dict__[item+"_pickable"]==True and self.__dict__[item+"_location"]==self.location:
                inventory.append(item)
            else:
                print "You can't take that!"
            
#Only the move function is ready... I think... But this system allows for the user to type any of the commands and it will be define in another elif... Woohoo!

def main():
    game = Adventure()

main()


