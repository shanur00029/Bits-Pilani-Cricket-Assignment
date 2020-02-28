#Problem Statement 7: Cricket Batting Order Problem
#Group007 - Raza Abbas(2019AD04095);Alkesh Chaturvedi(2019AD04082)
#Group007 - Harsh Bhatia(2019AD04086) & Shanur Rahman (2019AD04065)
#Dated: 16-Feb-2020; Version 1.1

class CricketBattingOrder:

    player = {}
    combinations =[]
    oldcomb = []
    player_position = []
    rec_count = 0
    error_flag = 'N' 
    
#*****************************************************************************#
#                                                                             #                                                                                
#   (1) Read data from i/p file inputPS7.txt present in current working       #
#       directory & populate player dictionary with player name as key and    #
#       player position as dicitionary values.                                # 
#   (2) Remove duplicate positions, if any, for all players records in file   #
#   (3) Count total records present in input file. Only 11 records should     #
#       be entered as input to this program                                   #
#   (4) self.rec_count will be used to write relevant msg if rec_count NE 11  #
#   (5) Assign new names to players for process_data function to work         #
#       appropriately                                                         #
#                                                                             #
#*****************************************************************************#                                                    #

    def readInput(self,inputFile): 

        x = open(inputFile,"r")
        self.rec_count = 0

        for i in x:
            if not i.isspace():
                self.rec_count = self.rec_count + 1
                l = i.strip()
                l = l.replace(' ','').split('/')
                self.player[str(l[0]+'_'+ str(self.rec_count)+'_@')] = (list(set(l[1:])))

        x.close()
        
        return self.rec_count
        
#*****************************************************************************#
#                                                                             # 
#    (1) Convert mapping from Players to Positions --> Positions to Players   #
#    (2) self.player_position list will have lists of players at              #
#        positions 0-10                                                       #                                                                 #
#    (3) Note here that as list index starts at 0, we are considering players'#
#        positions from position 0 to 10                                      #
#    (4) Per point (3) above, all players of position 1 are at list index 0   #
#        in self.player_position list. Likewise, position 2 are at            #
#        list index 1 & so on and so forth                                    #
#                                                                             # 
#*****************************************************************************#  

    def generate_player_position_list(self):

        for i in range(11):
            self.player_position.append([])

        for i,j in self.player.items():

            for k in j:
                if int(k) >= 1 and int(k) <=11:
                    self.player_position[int(k)-1].append(i)
                else:
                    self.error_flag = 'Y'
        
        return self.error_flag

#*****************************************************************************#
#                                                                             #
#     Generate all possible valid batting combinations and store them in      #      
#     self.combinations list                                                  #
#                                                                             #
#*****************************************************************************#

    def process_data(self):

        for pos1_players in self.player_position[0]: 
            self.oldcomb.append(pos1_players)
        for list_of_pos in self.player_position[1:]:
            newcomb = []
            for prevcomb in self.oldcomb:
                for newplayer in list_of_pos:
                    if newplayer not in prevcomb:
                        newcombination = prevcomb + newplayer
                        newcomb.append(newcombination)
            self.oldcomb.clear()
            self.oldcomb = newcomb.copy()
        self.combinations = self.oldcomb.copy()

#*****************************************************************************#
#                                                                             #
#     Calculate length of self.combinations list and save the value as final  #
#     result in outputPS7.txt file                                            #
#                                                                             #
#*****************************************************************************#

    def writeOutput(self, outputFile):

        y = open(outputFile, "w")

        if self.error_flag == 'Y':
           y.write("Position values should be between 1 to 11") 

        elif self.rec_count != 11:
           y.write("Total number of player records in input file is not equal to 11. Please enter 11 player records only") 

        else:  
           y.write("The total number of allocations possible is: %d \n" % len(self.combinations))

        
        y.close()

#*****************************************************************************#
#                                                                             #
#       Main program processing starts here                                   #
#                                                                             #
#       (1) Input file inputPS7.txt present in current working directory is   #
#           read by calling function readInput()                              #
#       (2) Generate player position list                                     #            
#       (3) Main processing to find different possible combinations is done   #
#           by calling function process_data()                                #
#       (4) self.combinations returned from step (3): fun process_data() has  #
#           final result                                                      #
#       (5) Output file is written with the length of self.combinations list  #
#           This is the final result                                          #
#                                                                             #
#*****************************************************************************#

batting_order = CricketBattingOrder()
rec_cnt = batting_order.readInput('inputPS7.txt')
if rec_cnt == 11:  
    err_flg = batting_order.generate_player_position_list()
    if  err_flg == 'N':
        batting_order.process_data()
batting_order.writeOutput('outputPS7.txt')