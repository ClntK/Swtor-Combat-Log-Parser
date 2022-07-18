# Filename: CMBTLOGDMGCalc.py
# Created Date: 6/13/2022
# Author: Clint Kline
# Phase: Gamma
# Purpose: analyze only the damage in a single combat log. 

# ---------------------------------------------------------------------------------------------
# IMPORTS
# ---------------------------------------------------------------------------------------------

import os
import re
from pathlib import Path


# ---------------------------------------------------------------------------------------------
# VARIABLES
# ---------------------------------------------------------------------------------------------

# designate file path to combat log folder
path = 'C:/Users/ClntK/Documents/Star Wars - The Old Republic/CombatLogs'
# create a variable to rep the CombatLogs folder as a directory
dirName = os.path.dirname(path)
# create a variable that selects the most recent file in the Combat logs folder
fileName = os.listdir('.')[-1]
#  count the number of files in 'path'
# make a list of all files in the folder
fileList = ([name for name in os.listdir('.') if os.path.isfile(name)])
# print(fileList)
# convert the files list to a dictionary
fileList_dict = { ind: name for (ind,name) in enumerate(fileList)}
# print(fileList_dict)


# ---------------------------------------------------------------------------------------------
# FUNCTIONS
# ---------------------------------------------------------------------------------------------

def fileCount():
    fCount = (len([name for name in os.listdir('.') if os.path.isfile(name)]))
    return fCount

pointer = fileCount()
# ---------------------------------------------------------------------------------------------

def fileInfo():
    print('\n\nFile Path: ', dirName)
    print('File Name: ', fileName)
    countLines(combatLog)
    print('\n')

# ---------------------------------------------------------------------------------------------

def fightData():
    print('Character Name: ', player, '\n\n')
    print("{:<15} {:<15} {:<15} {:<15}".format('Character:','Damage:','Heals:','Threat:'))
    print('-' * 60)
    for data in row.items():
        # print('data:', data[1])
        c, d, h, t = data[1]
        print("{:<15} {:<15} {:<15} {:<15}".format(c, d, h, t))
        print('-' * 60)
    print('\n\n')
      
# ---------------------------------------------------------------------------------------------

def getCombatLog():       
    # choose last file in folder
    with open(fileList_dict[pointer - 1], "r") as file:
        combatLog = file.readlines()
        print('\nfile is not empty, processing...')
        return combatLog

# ---------------------------------------------------------------------------------------------

# function to count lines in file
def countLines(combatLog):
    # variable to track line number
    linecount = 0
    for line in combatLog:
        linecount = linecount + 1        
    print('File Linecount: ', linecount)
    
# ---------------------------------------------------------------------------------------------

def deleteEmptyFiles():
    count = 0   
    path = "C:\\Users\\ClntK\\Documents\\Star Wars - The Old Republic\\CombatLogs"
    for file in os.listdir(path):
        with open(file) as f:
            f.seek(0, os.SEEK_END) # go to end of file
            if f.tell() == 0: #return current position of python pointer, if == 0 file is empty
                print('deleting empty file: ', f.name)
                # close the file
                f.close()
                # delete the file
                os.remove(f.name)
                count += 1
    print(count, ' file(s) deleted.')

# ---------------------------------------------------------------------------------------------

def getPlayerName(combatLog):
    
    playerNames =['Kluu', 'Lii\'f', 'Mard\'kk', 'Metalyth', 'Lumin\'ia', 'Qwin\'ten', 'Vulcara']
    playerName = ''
    
    for line in combatLog:
        for playerName in playerNames:
            if playerName in line:
                # print('\nCharacter: ', playerName)
                return playerName
            
            else:
                pass
        
# ---------------------------------------------------------------------------------------------
        
def DamageTotal(combatLog, player):
    #  find the instances of the damage keyword in the log
    # variable to track damage total
    total = 0
    player = getPlayerName(combatLog)

    for line in combatLog:
        # variable to record digits copied from file as a string
        num = ''
        if player in line:
            if 'Damage' in line:
                # print("Line: ", linecount, line, "\n\n\nnext number>>\n")
                # variable to track whether or not text is being recorded
                # read backwards because the damage number is at the end of the line
                if '<' and ">" in line:  
                    for ch in line[::-1]:
                        # if the character is a '<' break the line/end the loop
                        if ch == '<':
                            break
                        # if the character is not a digit/number, restart the loop
                        elif not ch.isdigit():
                            pass    
                        # otherwise record digit to num variable
                        else:
                            # print('before num: ', type(num))
                            # print('before ch: ', type(ch))
                            num = num + str(ch)
                            # print('after num: ', type(num))
                            # print('after ch: ', type(ch))
                            # print('num: ', num)
                            # print('ch: ', ch)
                    # rearrange the numbers into the original order to represent the actual number. 
                    num = num[::-1]
                    # convert num to integer type
                    num = int(num)
                    # print('int num: ', type(num))
                    # print('still ch: ', type(ch), '\n\n\n')
                    # add num to total
                    total = total + num
                    # print('total: ', total, '\n\n')

                else:
                    pass
            else:
                pass
        else:
            pass
    # print('\nTotal Damage: ', total)
    return total

# ---------------------------------------------------------------------------------------------

def HealTotal(combatLog):
    #  find the instances of the Heal keyword in the log
    # variable to track Heal total
    total = 0
    # variable to track line number
    linecount = 0
    
    for line in combatLog:
        # variable to record digits copied from file as a string
        num = ''
        if 'Heal' in line:
            linecount = linecount + 1
            # print("Line: ", linecount, line, "\n\n\nnext number>>\n")
            # variable to track whether or not text is being recorded
            # read backwards because the Heal number is at the end of the line
            if "~0)" in line:  
                for ch in line[::-1]:
                    # if the character is a '(' break the line/end the loop
                    if ch == '(':
                        break
                    # if the character is a digit, record digit to num variable
                    elif ch.isdigit():
                        num = num + str(ch)
                    # if the character is not a digit/number, restart the loop
                    elif not ch.isdigit():
                        pass    
                # rearrange the numbers into the original order to represent the actual number. 
                num = num[::-1]
                # convert num to integer type
                num = int(num)
                # add num to total
                total = total + num
                # print('total: ', total, '\n\n')
            else:
                pass
        else:
            pass
    # print('Total Heals: ', total)
    return total

# ---------------------------------------------------------------------------------------------

def ThreatTotal(combatLog):
    #  find the instances of the Threat keyword in the log
    # variable to track Threat total
    total = 0
    # variable to track line number
    linecount = 0
    
    for line in combatLog:
        # variable to record digits copied from file as a string
        num = ''
        if 'Threat' in line:
            linecount = linecount + 1
            # print("Line: ", linecount, line, "\n\n\nnext number>>\n")
            # variable to track whether or not text is being recorded
            # read backwards because the Threat number is at the end of the line
            if '<' and ">" in line:  
                for ch in line[::-1]:
                    # if the character is a '<' break the line/end the loop
                    if ch == '<':
                        break
                    # if the character is not a digit/number, restart the loop
                    elif not ch.isdigit():
                        pass    
                    # otherwise record digit to num variable
                    else:
                        num = num + str(ch)
                # rearrange the numbers into the original order to represent the actual number. 
                num = num[::-1]
                # convert num to integer type
                num = int(num)
                # add num to total
                total = total + num
                # print('total: ', total, '\n\n')
            else:
                pass
        else:
            pass
    # print('Total Threat Generated: ', total)
    return total              

# ---------------------------------------------------------------------------------------------
# options functions
    
def nextFile(fcount):
    print("next file")
    print("filecount = ", fcount)
    fcount = fcount + 1
    print("filecount = ", fcount)
    fileInfo()
    fightData()
    fileOptions()
    
def prevFile(fileCount):
    fcount = fileCount()
    print("prev file")
    print("filecount = ", fcount)
    fcount = fcount - 1
    print("filecount = ", fcount)
    fileInfo()
    fightData()
    fileOptions()
    
def delFile(fileName):
    fcount = fileCount()
    print("delete file")
    os.remove(fileName)
    print("filecount = ", fcount)
    fileInfo()
    fightData()
    fileOptions()
    
def pickToon():
    print("search character cooming soon.")
    fileInfo()
    fightData()
    fileOptions()
    

# ---------------------------------------------------------------------------------------------
    
def fileOptions():
    fileCount()
    option = int(input("File options: \n1. Next File\n2. Prev File\n3. Delete File\n4. Search for Character\n\nenter a selection: "))
    if option:
        if option == 1:
            nextFile(fileCount)
            
        elif option == 2:
            prevFile(fileCount)
            
        elif option == 3:
            delFile(fileName)
            
        elif option == 4:
            pickToon()
            
        else:
            getCombatLog()
    else:
        print("please choose an option, or hit enter to finish.")

# ---------------------------------------------------------------------------------------------
# function variables    /     function call
# ---------------------------------------------------------------------------------------------
# pull the latest combat log file 
combatLog = getCombatLog()       
# pull the character name from the log  
player = getPlayerName(combatLog)
# calculate the total damage done by the character
dmg = DamageTotal(combatLog, player)
# calculate total heals
heals = HealTotal(combatLog)
# calculate total threat
threat = ThreatTotal(combatLog)
row = {'row:': [player, dmg, heals, threat]}

# ----------------------------
# BEGIN PROGRAM
# ----------------------------
          
deleteEmptyFiles()
fileInfo()
fightData()
fileOptions()

