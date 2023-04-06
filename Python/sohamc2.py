# QUESTION:-
# You are given the names of 11 cricket players, and the scores in K overs played
#   by them. You have to output, for each player, the number of balls faced and
#   runs scored by them.
# Here is a brief description of how cricket is played:
#   (*) In the beginning, the first two players are on the pitch, with player 1 on strike.
#   (*) Every ball is either an integer RUNS or W.
#       (i) Given RUNS, the player on strike scores as many runs. If RUNS is odd,
#           the player on strike changes (with the other person on the pitch).
#       (ii) Given W, the player on strike is out. They are replaced by the next
#           player in the roster, who comes in on strike.
#   (*) Each over has 6 balls. At the end of an over, the player on strike changes.
#
# Input:
# First line: A space-separated list of strings name, where the ith string is the
#   name of the ith player.
# Next line: An integer K, the number of overs played.
# Next K lines: A string over i, the description of the ith over. over i is a space
#   separated list of 6 characters, each either an integer or W.
#
# Output:
# Print 11 lines. On the ith line display:
# <name i> <balls faced> <runs scored>
# The players in the output must appear in the order given. If a player has not
#   faced any balls or scored any runs, output 0 for them.
# 
# Sample Input:
# P1 P2 P3 P4 P5 P6 P7 P8 P9 P10 P11
# 3
# 1 2 4 6 W 0
# W W 2 1 0 0
# 0 0 3 6 W 4
# Sample Output:
# P1 2 1
# P2 4 12
# P3 5 6
# P4 1 0
# P5 5 6
# P6 1 4
# P7 0 0
# P8 0 0
# P9 0 0
# P10 0 0
# P11 0 0

class Node:
    def __init__(self, name, balls, runs, index):
        self.name       =   name
        self.balls      =   balls
        self.runs       =   runs
        self.index      =   index

class Match:
    def __init__(self):
        self.striker    =   None
        self.nstriker   =   None
        self.next       =   None
        self.players    =   []
    
    def insert(self, name, balls, runs, index):
        node=Node(name, balls, runs, index)
        self.players.append(node)
    def bat(self,run):
        self.striker.balls  += 1
        self.striker.runs   += run
    def display(self):
        for i in self.players:
            print(i.name,i.balls,i.runs)


x=Match()
players=input().split()
for k in range(11):
    x.insert(players[k],0,0,k)

x.striker=x.players[0]
x.nstriker=x.players[1]
x.next=x.players[2]
flag=2
overs=int(input())
for i in range(overs):
    over=input().split()
    for ball in over:
        if ball == 'W':

            x.bat(0)
            x.players[x.striker.index]=x.striker
            if flag == -1:
                break
            if flag == 10:
                x.striker=x.next
                flag = -1
            else:
                flag+=1
                x.striker=x.next
                x.next=x.players[flag]
        else:
            x.bat(int(ball))
            if int(ball)%2 == 1:
                x.striker, x.nstriker = x.nstriker, x.striker
    x.striker, x.nstriker = x.nstriker, x.striker
        

x.display()