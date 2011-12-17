# Turning Pete's program into a class.
class Adventure:
    X = 0
    Y = 1
    maze = [[False, False, True, False, False],
    [False, True, True, False, True],
    [False, True, False, True, True],
    [False, True, False, True, False],
    [False, True, True, True, False]]

#So the starting position is the last line, on 3, right?

    def __init__(self):
        location = [2, 4]
        self.get_input(location)
        print location

    def move(self, loc, x, y):
        if self.maze[loc[self.Y] + y][loc[self.X] + x]:
            loc[self.X] += x
            loc[self.Y] += y
        else:
            raise Exception("You can't move here.")

    def get_input(self,location):   
        location = [2, 4]     
        direction=raw_input("Where'd you like to go? Up, Right, Left or Down?" )
        if direction=="Up":
            self.move(location,0,1)
        elif direction=="Right":
            self.move(location,1,0)
        elif direction=="Left":
            self.move(location,-1,0)
        elif direction=="Down":
            self.move(location,0,-1)
        else:
            print "well done, asshole, you broke the game by not choosing from the options."

def main():
    game = Adventure()

main()


