# !/usr/bin/python3
# coding: utf8
# @author Bulls90
# v3.1
# Importing  modules
import os
import shutil
import sys

# Path of input and output files
src = input('Please indicate the path of the input files: ')
dest = input('Please indicate the path to leave the files: ')

if src:
    print('The route of entry is: ' + src)
else:
    sys.exit('¡You must enter an inbound route! Ending program...')
if dest:
    print('The exit route is: ' + dest)
else:
    sys.exit('¡You must indicate an exit route! Ending program...')

os.chdir(dest)


# Creates folders by file name, and then moves the files to the corresponding folder
def classify():
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


print('Sorting out files, please wait...')
classify()
print('¡DONE!')
