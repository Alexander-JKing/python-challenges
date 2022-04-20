# -*- coding: utf-8 -*-
"""
Created on Fri May  7 14:26:59 2021

@author: Danilo.Bento
"""
import os
import glob
import shutil

imageFolder = 'D:/projects/SIB2/data/img/DAERA_100Parcels/highlands'
txtFolder = 'D:/projects/SIB2/data/img/VHRValidation_v1/enhanced/VHRValidation_v1_enhanced/labels'


def copyImageTxt(img_folder, txt_folder):
    '''
    Take img name and use to copy the respective txt file
    '''
    fileNames = []
    for file in glob.glob(os.path.join(img_folder,"*.txt")):
        fileBaseName = os.path.basename(file)
        fileBaseName = fileBaseName.replace('.txt', '.png')
        fileNames.append(fileBaseName)
    
    for fileName in fileNames:
        fullName = os.path.join(txt_folder, fileName)
        excCount = 0
        try:
            shutil.copy(fullName, imageFolder)
        except:
            excCount = excCount + 1
            print(f'missed more one txt. Total {excCount}')
        
        print(f'{excCount} files missed')


copyImageTxt(imageFolder, txtFolder)