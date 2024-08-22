# So in Azul you draw tiles, so theres a list of tiles
# there's 20 of each of the 5 tiles
tile_bag = [
    {
        "color":"white",
        "num_in_bag":20
        # could do this proportionally: (20 - numberCOLORremoved)/100 which goes down as you pull from there
    },
    {
        "color":"blue",
        "num_in_bag":20
        },
    {
        "color":"red",
        "num_in_bag":20
    },
    {
        "color":"black",
        "num_in_bag":20
    },
    {
        "color":"orange",
        "num_in_bag":20
    },
]
# for each factory, which is dependent on number of players (5, 7, or 9), there are 4 tiles
class Factory():
    def __init__(self, tiles):
        self.contents = []

        #Randomly select 4 tiles from the source, where tiles knows what color it is
        for i in range(4):
            self.contents.append(tiles)

players = []
if players.len() == 2:
    num_factory = 5
elif players.len() == 3:
    num_factory = 7
else: 
    num_factory = 9

total_factories = []
for i in range(num_factory - 1):
    total_factories.append(Factory(tile_bag))

# And theres a player board with spots for each tile
# this is a 5x5 grid and only one of each tile can occupy each row and column
board = [
    {
        "In_Progress":{
            "color":None,
            "number_built":0
        },
        "Complete":{
            "blue":False, # (1,1)
            "orange":False, # (1,2)
            "red":False, # (1,3)
            "black":False, # (1,4)
            "white":False # (1,5)
            }
    },
        {
        "In_Progress":{
            "color":None,
            "number_built":0
        },
        "Complete":{
            "white":False, # (2,1)
            "blue":False,
            "orange":False,
            "red":False,
            "black":False
            }
    },
        {
        "In_Progress":{
            "color":None,
            "number_built":0
        },
        "Complete":{
            "black":False, # (3,1)
            "white":False,
            "blue":False,
            "orange":False,
            "red":False
            }
    },
        {
        "In_Progress":{
            "color":None,
            "number_built":0
        },
        "Complete":{
            "red":False, # (4,1)
            "black":False,
            "white":False,
            "blue":False,
            "orange":False
            }
    },
        {
        "In_Progress":{
            "color":None,
            "number_built":0
        },
        "orange":False, # (5,1)
        "red":False,
        "black":False,
        "white":False,
        "blue":False
    }
]

 # So you take all the matching tiles in a given factory, which is known since the we know the tiles in the factories
 # and your row defines how many tiles you need to get of one color to fill that position

chosen_factory = 1 # whichever factory you want to take from
color_seek = "black" 
