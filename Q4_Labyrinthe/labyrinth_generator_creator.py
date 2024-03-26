import sys
import random

cell_size = 10 #mm
wall_height = 10 #mm
wall_thickness = 1 #mm
n = 4

strategy_choice = 1

class Strategy :
    def __init__(self):
        # grid of cells
        self.cells = [[0 for _ in range(n)] for _ in range(n)]     


        # Grid of all interior walls: 2*n*(n-1) walls
        # x+n for horizontal walls.
        self.walls = [[1 for _ in range(n)] for _ in range(2*n-1)]

        self.firstCell = [random.getrandbits(1)*(n-1), random.getrandbits(1)*(n-1)]      # first cell on the border
       

    def Apply(self):
        print("Applying Abstract Strategy")

    def DoSomething(self):
        
        print("Do Something")
        print(self.walls)
        return self.walls
    
    def markFirstCell(self):
        return self.firstCell

# Randomized Prim algorithm
# https://weblog.jamisbuck.org/2011/1/10/maze-generation-prim-s-algorithm
class Algorithm1(Strategy) :

    wallsToPrint = []
    discoveredWalls = []
    neighbours = []
    




    def addWallToPrint(x,y):
        global wallsToPrint
        global n
        if (x >= 0 and y >= 0 and x <= n and y <= n):
            wallsToPrint.append([x,y])

    def addNeighbour(self,x,y):
        n = self.n
        global neighbours
        if (x >= 0 and y >= 0 and x < n and y < n):
            neighbours.append([x-1,y])


    def markCell(self,x, y):
        cells = self.cells
        cells[x][y] = 1


    def addWall(self, x,y):   #x,y: coordinates of cell
        # n = self.n
        discoveredWalls = self.discoveredWalls
        cells = self.cells
        if (y < n-1):         # vertical wall to the left
            discoveredWalls.append([x,y])
        if (y > 0):              # vertical wall to the right
            discoveredWalls.append([x,y-1])
        if (x < n-1):             # horizontal wall under
            discoveredWalls.append([x+n,y])
        if (x > 0):               # horizontal wall aboveS
            discoveredWalls.append([x+n-1,y])

    # Destroy a wall🔨
    def addPassage (self, i,j):       #coordinates of a wall
        walls = self.walls
        walls[i][j]=0

    def Apply(self):
        super().Apply()
        print(self.walls)
    # global cells 
    # global walls
        discoveredWalls = self.discoveredWalls
    # global neighbours
    #    n = self.n
     #  wallsToPrint = []
     #  discoveredWalls = []
     #  neighbours = []
     #  n = 4
        cells = self.cells
        walls = self.walls
        firstCell = self.firstCell
 
        print("Applying Algorithm1")

        # algorithm
        # Initialization
       # firstCell = [random.getrandbits(1)*(n-1), random.getrandbits(1)*(n-1)]      # first cell on the border
        print(firstCell)
        cells[firstCell[0]][firstCell[1]]=1     #cell visited
        print(firstCell[0], firstCell[1])
        self.addWall(firstCell[0], firstCell[1])
        


        while (len(discoveredWalls) >0):
            pickedWall = discoveredWalls[random.randint(0, len(discoveredWalls)-1)]
            print("pickedWall= ", pickedWall)
            print("wall exists? ", walls[pickedWall[0]][pickedWall[1]])
            x = pickedWall[0]
            y = pickedWall[1]
            nextcell = []

            # Check if only one of the cells that the wall divides is visited
            if (walls[pickedWall[0]][pickedWall[1]]==0):       # wall already removed from labyrinth
                nextcell=[]

            elif (x<n and cells[x][y]==0):     # vertical wall
                nextcell = [x,y]
                
            elif (x<n and cells[x][y+1]==0):     # vertical wall
                nextcell = [x,y+1]
            
            elif (x>=n and cells[x-n][y]==0):   #horizontal wall
                nextcell = [x-n,y]

            elif (x>=n and cells[x-n+1][y]==0):  #horizontal wall
                nextcell = [x-n+1,y]

            else:
                print("surrounding cells already visited!")
            
            if (len(nextcell)>0):
            
                print ("nextcell= ", nextcell)

                # remove the wall from labyrinth
                walls[x][y] = 0
                # mark the new cell as visited
                cells[nextcell[0]][nextcell[1]] = 1

                # Add the neighboring walls of the cell to the wall list
                self.addWall(nextcell[0], nextcell[1])
                
                print("discovered walls= ", discoveredWalls)
            
            # Remove the wall from the list of discovered walls
            discoveredWalls.remove(pickedWall)
            
            print("discovered walls= ", discoveredWalls)


        print (walls)
    


class Algorithm2(Strategy) :

    def Apply(self):
        #super().Apply()
        print("Applying Algorithm2")

class Generator() :
    strategy = None

    def __init__(self):
        pass

    def SetStrategy(self, new_strategy):
        self.strategy = new_strategy

    def Generate(self):
        self.strategy.Apply()
        walls = self.strategy.DoSomething()
        firstCell = self.strategy.markFirstCell()
        print(firstCell)

        print("Generate!!")
        content = "// base plate \n translate([-0.5,-0.5,-1]){ \n cube(["+ str(cell_size*n+wall_thickness) +"," + str(cell_size*n+wall_thickness) + ",1], center=false); \n }  \n"
      #for i in range (4):
      #    content += "// borders \n translate([" + str(cell_size*n*(i//2)) +"," + str(cell_size*n*(i//3)) +",0]){ \n cube([" + str(cell_size*n*(i%2)) +"," + str(cell_size*n*((i+1)%2)) + ",10], center=false); \n } \n "
      #    print((i+1)%2)

        content += "// borders  \n translate([-0.5,-0.5,0]){ \n cube(["+ str(cell_size*n) +","+str(wall_thickness)+","+str(wall_height)+"], center=false); \n } \n "
        content += "translate([-0.5,-0.5,0]){ \n cube(["+str(wall_thickness)+"," + str(cell_size*n)+ ","+str(wall_height)+"], center=false); \n } \n"
        content += "translate([-0.5," + str(cell_size*n-0.5*wall_thickness) +",0]){ \n cube(["+ str(cell_size*n+wall_thickness) +","+str(wall_thickness)+","+str(wall_height)+"], center=false); \n } \n "
        content += "translate(["+str(cell_size*n-0.5*wall_thickness)+",-0.5,0]){ \n cube(["+str(wall_thickness)+"," + str(cell_size*n+wall_thickness)+ ","+str(wall_height)+"], center=false); \n } \n \n //interior walls \n "

        for x in range(n):
            for y in range (len(walls[x])-1):
                if walls[x][y] ==1:       #there is a wall
                    content+= "translate(["+ str(cell_size*(x+1)-cell_size/2) +"," + str(cell_size*(y+1)) + ","+str(wall_height/2)+"]){  \n cube(["+str(cell_size+wall_thickness)+","+str(wall_thickness)+","+str(wall_height)+"], center=true); \n } \n" 

        for x in range(n, 2*n-1):
            for y in range (len(walls[x])):
                if walls[x][y] ==1:       #there is a wall
                    content+= "translate(["+ str(cell_size*(x-n+1)) +"," + str(cell_size*(y+1)-cell_size/2) + ","+str(wall_height/2)+"]){  \n rotate([0,0,90]){ \n cube(["+str(cell_size+wall_thickness)+","+str(wall_thickness)+","+str(wall_height)+"], center=true); \n } \n } \n" 


        
        return content



class Creator() :
    def __init__(self, filename):
        self.filename = filename

    def PrintLabyrinth(self, content):

        file = open(self.filename, "w")
        file.write(content)
        file.close()


# main call
def main():
    global strategy_choice
    args = sys.argv[:]
    if len(args) >= 2 :
        strategy_choice = int(args[1])

    # Generator
    my_generator = Generator()
    if strategy_choice == 1:
        my_generator.SetStrategy(Algorithm1())
    elif strategy_choice == 2:
        my_generator.SetStrategy(Algorithm2())
    else :
        print("error strategy choice")
    content = my_generator.Generate()

    #Creator
    my_creator = Creator("labyrinth.scad")
    my_creator.PrintLabyrinth(content)


if __name__ == "__main__":
    main()
