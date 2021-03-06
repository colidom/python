# !/usr/bin/python3
# coding: utf8
# @author colidom
# v4.2
# Importing  modules
import os
import shutil
import sys

# Path of input and output files
src = input('Please indicate the path of the input files: ')
dest = input('Please indicate the path to leave the files: ')

if src == '':
    sys.exit("""
*******************************************************
* ¡You must indicate a source path! Ending program... *
*******************************************************""")
if dest == '':
    sys.exit("""
************************************************************
* ¡You must indicate a destination path! Ending program... *
************************************************************""")


# Creates folders by file name, and then moves the files to the corresponding folder changing filenames.
def classify_new_name():
    os.chdir(dest)
    for f in os.listdir(src):
        splitname = f.split('_')
        status = splitname[1]
        topic = splitname[2]
        foldername = topic + '_' + 'Status_' + status
        msgName = 'Message_0'
        newFileName = foldername + '\\' + msgName + '.xml'
        if not os.path.exists(foldername):
            os.mkdir(foldername)
        else:
            while os.path.isfile(newFileName) is True:
                msgInt = int(msgName[8:])
                msgInt += 1
                msgName = msgName[:8] + str(msgInt)
                newFileName = foldername + '\\' + msgName + '.xml'
        shutil.move(os.path.join(src, f), newFileName)
        names = newFileName.split('\\')
        print('Moving file: ' + f + ' into the folder--> ' + names[0] + ' renamed to : ' + names[1])
    print('¡Done!')


# Creates folders by file name, and then moves the files to the corresponding folder keeping original filenames.
def classify():
    os.chdir(dest)
    for f in os.listdir(src):
        splitname = f.split('_')
        status = splitname[1]
        topic = splitname[2]
        foldername = topic + '_' + 'Status_' + status
        if not os.path.exists(foldername):
            os.mkdir(foldername)
        shutil.move(os.path.join(src, f), foldername)
    print('¡Done!')


def question():
    option = str
    option = (input("""
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|Choose one of the following options:   |                                            
|  (a) Keeping original file name       |
|  (b) Rename files                     |
|  (c) Exit                             |  
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
Chosen option:""") + option())
    if option == 'a' or option == 'A':
        print('Sorting out keeping the original name of the files, please wait...')
        classify()
    elif option == 'b'or option == 'B':
        print('Shorting out and renaming file names, please wait...')
        classify_new_name()
    elif option == 'c' or option == 'C':
        sys.exit('Closing tool...See you later.!')
    else:
        print('¡ERROR! The entered value is not correct')
        question()


question()
