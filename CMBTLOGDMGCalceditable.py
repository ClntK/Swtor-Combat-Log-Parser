# Filename: CMBTLOGDMGCalc.py
# Created Date: 6/13/2022
# Author: Clint Kline
# Phase: Gamma
# Purpose: analyze and print the total damage, healing and damage taken for a given character in a single combat log. 

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
path = r'C:\Users\ClntK\Documents\Star Wars - The Old Republic\CombatLogs\\'
# create a variable to rep the CombatLogs folder as a directory
dirName = os.path.dirname(path)
# print("dirName: ", dirName)
# create a variable that selects the most recent file in the Combat logs folder
fileName = os.listdir(path)[-1]
# print("fileName: ", fileName)
# make a list of all files in the folder
fileList = os.listdir(path)
# print("fileList: ", fileList)
# convert the files list to a dictionary
fileList_dict = { ind: name for (ind,name) in enumerate(fileList)}
# print(fileList_dict)


# ---------------------------------------------------------------------------------------------
# FUNCTIONS
# ---------------------------------------------------------------------------------------------

def fileCount():
    fCount = len(os.listdir(path))
    return fCount

print('\n\n\033[0;30;40m**********************************************\033[0;37;40m')
print('       \033[1;33;40mCLINT\'s SWTOR COMBAT FILE PARSER\033[0;37;40m')
print('\033[0;30;40m**********************************************\033[0;37;40m')

fcount = fileCount()
print("\n\nThere are ", fcount, " files in the Combat Logs folder.")
# ---------------------------------------------------------------------------------------------

def filePointer(fcount):
    pointer = fcount
    return pointer

pntr = filePointer(fcount)

# ---------------------------------------------------------------------------------------------

# function to count lines in file
def countLines(combatLog):
    # variable to track line number
    linecount = 0
    for line in combatLog:
        linecount = linecount + 1        
    print('File Linecount: ', '{:,}'.format(linecount))
        
# ---------------------------------------------------------------------------------------------

def fileInfo(combatLog, pntr):
    print('\n\n***************************')
    print('     FILE DETAILS')
    print('***************************')
    print('\n\nFile Path: ', dirName)
    fileName = os.listdir(path)[pntr - 1]
    print('File Name: ', fileName)
    print('File Number: ', pntr)
    countLines(combatLog)
    print('\n')

# ---------------------------------------------------------------------------------------------

def fightData(pntr):
    with open(path + fileList_dict[pntr - 1], "r") as file:
        combatLog = file.readlines()
        player = getPlayerName(combatLog)
        # calculate the total damage done by the character
        dmg = DamageTotal(combatLog)
        # calculate total heals
        heals = HealTotal(combatLog)
        # calculate total threat
        threat = ThreatTotal(combatLog)
        row = {'row:': [player, dmg, heals, threat]}
        # print('Character Name: ', player, '\n\n')
        print("{:<15} {:<15} {:<15} {:<15}".format('Character:','Damage:','Heals:','Dmg Taken:'))
        print('-' * 60)
        for data in row.items():
            c, d, h, t = data[1]
            print("\033[0;33;40m{:<16}\033[0;37;40m" 
                  "\033[0;34;40m{:<16}\033[0;37;40m" 
                  "\033[0;32;40m{:<16}\033[0;37;40m" 
                  "\033[0;36;40m{:<15}\033[0;37;40m".format(c, '{:,}'.format(d), '{:,}'.format(h), '{:,}'.format(t)))
            
            print('-' * 60)
        print('\n\n')
      
# ---------------------------------------------------------------------------------------------

def getCombatLog(initial, pntr):       
    # choose last file in folder
    try:
        with open(path+fileList_dict[pntr - 1], "r") as file: 
            combatLog = file.readlines()
            print('\n\033[3;34;40mprocessing combat log...\033[0;37;40m')
            if initial == 0:
                return combatLog
            else:
                fileInfo(combatLog, pntr)
                fightData(pntr)
                fileOptions(pntr)
    except:
        pntr = pntr - 1
        # getCombatLog(initial, pntr)

# ---------------------------------------------------------------------------------------------

def deleteEmptyFiles():
    count = 0   
    for file in fileList:
        with open(path + file) as f:
            f.seek(0, os.SEEK_END) # go to end of file
            if f.tell() == 0: #return current position of python pntr, if == 0 file is empty
                print('\033[3;34;40mdeleting empty file:\033[0;37;40m ', f.name)
                # close the file
                f.close()
                # delete the file
                os.remove(f.name)
                count += 1
    print(count, ' file(s) deleted.')

# ---------------------------------------------------------------------------------------------

def getPlayerName(combatLog):    
    playerNames =['Kluu', 'Lii\'f', 'Mard\'kk', 'Metalyth', 'Lumin\'ia', 'Qwin\'ten', 'Vulcara']
    for line in combatLog:
        for playerName in playerNames:
            if playerName in line:
                # print('\nCharacter: ', playerName)
                return playerName
            
            else:
                pass
        
# ---------------------------------------------------------------------------------------------
        
def DamageTotal(combatLog):
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
    
def nextFile(pntr):
    if (pntr < fcount):
        # print("filecount = ", pntr)
        print(">> next file")
        plusOne = pntr + 1
        # print("filecount = ", plusOne)
        getCombatLog(1, plusOne)
    elif (pntr == fcount):
        print("\033[1;34;40mYou are already viewing the latest file.\033[0;37;40m \n")
        getCombatLog(1, pntr)
    else:
        print("\033[1;34;40msomething weird happened... im sending you back..\033[0;37;40m \n")
        getCombatLog(1, pntr)
        
def prevFile(pntr):
    print(">> prev file")
    # print("File Number = ", pntr)
    pntr = pntr - 1
    # print("File Number = ", pntr)
    getCombatLog(1, pntr)
    
def delFile(pntr):
        print("\033[1;34;40m>> deleting file...\033[0;37;40m\n")
        fileList_nums = { ind: name for (ind, name) in enumerate(fileList)}
        file = fileList_nums[pntr - 1]
        print(file)
        
        os.remove(file)
        print(file, " \033[1;34;40mdeleted.\033[0;37;40m\n")
        print("Latest file:\n\n")
        getCombatLog(1, pntr)

def pickToon(pntr):
    print("\n\033[1;32;40msearch character cooming soon.\033[0;37;40m\n\n")
    fileOptions(pntr)
    

# ---------------------------------------------------------------------------------------------
    
def fileOptions(pntr):

    option = input("File options: \n1. Next File\n2. Prev File\n3. Delete File\n4. Search for Character\n\nenter a selection: ")
    if option.isdigit():
        if option == '1':
            nextFile(pntr)
            
        elif option == '2':
            prevFile(pntr)
            
        elif option == '3':
            delFile(pntr)
            
        elif option == '4':
            pickToon(pntr)
            
        else:
            print("please choose an option, or hit enter to finish.\n")
            fileOptions(pntr)
    else:
        print("please choose an option, or hit enter to finish.\n")
        fileOptions(pntr)


print("\n\n\033[3;34;40mchecking for empty files...\033[0;37;40m")
deleteEmptyFiles()

# ---------------------------------------------------------------------------------------------
# function variables    /     function call
# ---------------------------------------------------------------------------------------------
# pull the latest combat log file 
combatLog = getCombatLog(0, pntr)    
# print('combat log: ', combatLog)   
# pull the character name from the log  
player = getPlayerName(combatLog)
# calculate the total damage done by the character
dmg = DamageTotal(combatLog)
# calculate total heals
heals = HealTotal(combatLog)
# calculate total threat
threat = ThreatTotal(combatLog)
row = {'row:': [player, dmg, heals, threat]}

# ----------------------------
# BEGIN PROGRAM
# ----------------------------
          
fileInfo(combatLog, pntr)
fightData(pntr)
fileOptions(pntr)

