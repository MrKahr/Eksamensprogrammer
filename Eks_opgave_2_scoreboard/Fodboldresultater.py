
"""
Link til github
https://github.com/MrKahr/Eksamensprogrammer
"""

'''
Første eksamens opgave i IPD: Sports resultater
@authors: Mads Andersen, Eric van den Brand, Daniel Hansen, Thor Skatka og Andreas Hansen
Beskrivelse:
Programmet tager match data fra en gruppe tekst filer, og ved hjælp af dette laver et sorteret og overskueligt scoreboard. 
'''

import io #Package for reading "æ, ø and å"

# Rounds played
amount_of_rounds = 6

# Standings list
standings = []

# Index of variables in team in standings
team,        g_played = 0,1
g_won,       g_drawn  = 2,3
g_lost,      ttl_gls  = 4,5
ttl_gls_c,   ttl_p    = 6,7


# ! filling standings with teams and scorecards (Written by: Andreas, Daniel and Thor)
nations_file = 'nations.txt'
team_file = io.open(nations_file,mode="r",encoding="utf-8") #Open file, read (r) and encoding is UTF-8 (æ, ø, å)

teams = []


def team_list():
    for item in team_file: #For each country + newline, add to the list
        teams.append(item.rstrip("\n")) #rstrip to strip "\n" from the right side of the string
    return teams


def add_team_scorecard(standings):
    for team in teams: #Create lists within lists for every nation
        team_scorecard = [team,0,0,0,0,0,0,0] #New list with nation and zeros for each type of score
        standings.append(team_scorecard)
    
    return standings


team_list() #Add items to nations
add_team_scorecard(standings) # Adds scorecards to standings


# ! Calculation and implimention scores and points in standings (Written by: Eric and Mads)
# Finds index of team in standings
def find_position_in_standings(standings,team):
    for entry in standings:
        if team == entry[0]:
            return standings.index(entry)


# Stores who won or a tie as result
def who_won(l_score, r_score):
    # l_team wins = 0
    if l_score > r_score:
        return 0
    
    # r_team wins = 1
    elif l_score < r_score:
        return 1
    
    # Tie = 2
    else:
        return 2


# Adds games played, won, tied and lost to standings for both teams
def games_wdl(standings, l_team, r_team, result):
    # Games played incremented by 1 
    standings[l_team][g_played] += 1
    standings[r_team][g_played] += 1
    
    # Adds 1 win and 1 loss to left team and right team respectively
    # Adds 3 points for left team
    if result == 0: 
        standings[l_team][g_won]  += 1
        standings[r_team][g_lost] += 1
        
        standings[l_team][ttl_p]  += 3
        
        return standings
    
    # Adds 1 win and 1 loss to right team and left team respectively
    # Adds 3 points for right team
    elif result == 1:
        standings[l_team][g_lost] += 1
        standings[r_team][g_won]  += 1
        
        standings[r_team][ttl_p]  += 3
        
        return standings
    
    # Adds 1 draw to both teams
    # Adds 1 point for both teams
    else:
        standings[l_team][g_drawn] += 1
        standings[r_team][g_drawn] += 1
        
        standings[l_team][ttl_p]   += 1
        standings[r_team][ttl_p]   += 1
        
        return standings


# Total goals scored and total goals conceded 
def goal_giver(standings, l_team, r_team, l_score, r_score):
    # Adds goals scored and goals conceded for left team 
    standings[l_team][ttl_gls]   += l_score
    standings[l_team][ttl_gls_c] += r_score
    
    # Adds goals scored and goals conceded for right team
    standings[r_team][ttl_gls]   += r_score
    standings[r_team][ttl_gls_c] += l_score
    
    return standings 


# Calls all functions and returns standings
def add_standings(standings, l_team, r_team, l_score, r_score):
    # Find index of l_team and r_team in standings
    l_team_index = find_position_in_standings(standings, l_team)
    r_team_index = find_position_in_standings(standings, r_team)
    
    # Sets who_won as result for this match
    result = who_won(l_score, r_score)
    
    # Adds a win, draw or loss and points for both teams
    games_wdl(standings, l_team_index, r_team_index, result)
    
    # Adds the given goals scored to both teams
    goal_giver(standings, l_team_index, r_team_index, l_score, r_score)
    
    return standings


# ! Makes list of rounds and matches in them (Written by: Andreas, Daniel and Thor)
for j in range(1,amount_of_rounds+1): # Run the program for every file
    file_path = 'round'+str(j)+'.txt'
    this_round_file = io.open(file_path,mode="r",encoding="utf-8") # Open file, read (r) and encoding is UTF-8 (æ, ø, å)
    
    this_round = this_round_file.read() # Take strings from file
    
    match_list = this_round.split('\n') # Create a list where we split file content by newline
    
    type_list = [] # Prepare a list split by goals and nations
    
    for item in match_list: # Take every list from matchlist
        i = item.split('\t') # Split it by "tab" (large space) - Creates new lists
        type_list.append(i) # Add new lists to the typelist
    
    match_type_list = [] # List that splits nations and scores into seperate lists by match
    
    for types in type_list:
        match_team_list = types[0].split(" - ") # Split the list with nations into items by " - " - Changes an item into more items [Danmark-Skotland] becomes [Danmark,Skotland]
        match_score_list = types[1].split(" - ") # Split the list of scores into items by " - " - Changes an item into more items [0-2] becomes [0,2]
        match_type_list.append([match_team_list ,match_score_list]) # Append the new lists

    # Index of variables in match and teams/scores in match
    teams,scores =    0,1
    l_team,r_team =   0,1
    l_score,r_score = 0,1

    for match in match_type_list: # Take values for nations and scores individually
        l_team_m =  match[teams][l_team] # Values to be extracted to standings
        r_team_m =  match[teams][r_team] # First index is either country or score, next index is left or right
        l_score_m = int(match[scores][l_score])
        r_score_m = int(match[scores][r_score])
        
        add_standings(standings, l_team_m, r_team_m, l_score_m, r_score_m)


# ! Format the text from the list (Written by: Andreas, Daniel and Thor)
def pretty(text, spaces): #Formula to format the text from the list
    text = str(text) #Ensure type is str
    return text+((spaces-len(text))*" ") #Make sure the returns a value


# ! make and print scoreboard (Written by: Andreas, Daniel and Thor)
# Create sorted list based on index 7 (points)
# Lambda is an anonymous function, takes x as and argument and x[7] as an expression
# "key=" creates a new list to sort over - Lambda defines which elements are in the new list
# Lambda creates a functions, runs it and destroys it again

# First sort alphabetaically, then sort by goal difference, then by points
# This makes it so that if points are the same, then goal difference matters,
# and if goal difference is the same, then alphabet matters
sorted_standings = sorted(standings, key = lambda x : x[team],reverse=False)
sorted_standings = sorted(sorted_standings, key = lambda x : x[ttl_gls]-x[ttl_gls_c],reverse=True)
sorted_standings = sorted(sorted_standings, key = lambda x : x[ttl_p],reverse=True)


for item in sorted_standings: #Unmakes standings list, prints each item in list
    team_t    = pretty(item[team]     ,10) #For every list in standings, run the function
    plays     = pretty(item[g_played] ,3)
    wins      = pretty(item[g_won]    ,3)
    draws     = pretty(item[g_drawn]  ,3)
    losses    = pretty(item[g_lost]   ,3)
    goals     = pretty(item[ttl_gls]  ,3)
    g_against = pretty(item[ttl_gls_c],3)
    points    = pretty(item[ttl_p]    ,3)
    result    = team_t + plays + wins + draws + losses + goals + "- " + g_against + points

    print(result)