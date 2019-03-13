#!/usr/bin/python
########################################################
########################################################
##              Script Description                    ##
##                                                    ##
##      Script developed to rename files with         ##
##		a name list within a files					  ##
##      Developer:      Junior de Oliveira            ##
##      Date:           11/04/2018                    ##
##      Version:        1.1804.16                     ##
##                                                    ##
##                                                    ##
##                                                    ##
########################################################
########################################################




'''
UPGRADES:
- renomear qualquer arquivo com padroes
- renomear arquivos a partir de qualquer pasta

'''
import os
import sys

fileList = [] # sera inserido os nomes dos arquivos em uma lista
count = 0 # count sera usado para verificar a quantidade de arquivos para renomear
indexList = 0

def usage():
    print("Usage mode: " + sys.argv[0] + " folder ext nameList")
    print("Example: " + sys.argv[0] + " /home/folder jpg listName")

def menu():
    option = ""
    while option != 0:
        print("Welcome to script renameFiles")
        print("1. With a list")
        print("2. With patterns")
        print("0. EXIT")
        option = input("Option: ")
        if option == 1:
            print("1. With a list")
        elif option == 2:
            print("2. With patterns")


def __main__():
    if len(sys.argv) < 3:
        usage()
    else:
        folder      = sys.argv[1] # folder de onde esta os arquivos
        ext         = sys.argv[2] # extensao dos arquivos a serem renomeados
        nameList    = sys.argv[3] # lista de nomes que serao usados para renomear os arquivos
        #order       = sys.argv[4]

        for nameFiles in os.listdir(folder):
            if nameFiles.endswith(ext): # verifica a extensao dos arquivos
                fileList.append(nameFiles) # adiciona na lista somente os arquivos com a extensao passada como parametro
                count += 1

        #if order == "order":

        fileList.sort() # ordena a lista

        file = open(nameList, 'r') # abre o arquivo com os nomes
        name = file.readlines() # ler cada linha do arquivo

        if folder == ".":
            folder = os.getcwd()
            newFolder = folder + "/"
            for nameLine in name:
                result = nameLine.rstrip()
                newName = newFolder + result + "." + ext
                os.rename(newFolder + fileList[indexList], newName)
                indexList += 1
                if indexList > count:
                    break
        else:
            newFolder = folder + "/"
            for nameLine in name:
                result = nameLine.rstrip()
                newName = newFolder + result + "." + ext
                os.rename(newFolder + fileList[indexList], newName)
                #print(newFolder + fileList[indexList] + " novo -> " + newName)
                indexList += 1
                if indexList > count:
                    break
__main__()
