'''
Extras
Extras are runs scored by a means other than a batsman hitting the ball. A batsman is not given credit for extras other than runs scored off the bat from a no ball, and the extras are tallied separately on the scorecard and count only towards the team’s score. the types of extras are No ball, Wide, Bye, Leg-bye and Penalty. 1 Penalty corresponds to 5 runs.
Find the total runs that the Extras contribute to the team’s score, given the number of No-balls, wides, byes, leg-byes and penalty given off by the bowlers in innings.
Input format:
First line of the input contains an integer that corresponds to the number of No-balls.
Second line of the input contain an integer that corresponds to the numbers of wides.
Third line of the input contains an integer that corresponds to the number of byes.
Fourth line of the input contain an integer that corresponds to the numbers of led-byes.
Fifth line of the input contains an integer that corresponds to the numbers of penalty runs.
Output format:
Output should display an integer that returns the total runs that the extras together contribute to team’s total.
Sample input and output 1:
4
7
3
10
3
39
Sample input and output 2:
2
3
7
1
17


'''
def calculate_extras(no_balls, wides, byes, leg_byes, penalties):
    
    total_extras = no_balls + wides + byes + leg_byes + (penalties * 5)
    return total_extras


no_balls = 4
wides = 7
byes = 3
leg_byes = 10
penalties = 3
print(calculate_extras(no_balls, wides, byes, leg_byes, penalties))  

no_balls = 2
wides = 3
byes = 7
leg_byes = 1
penalties = 17
print(calculate_extras(no_balls, wides, byes, leg_byes, penalties))  
