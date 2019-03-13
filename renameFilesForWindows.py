from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os
import sys

#pyinstaller --onefile --windowed renameFilesForWindows.py

fileList = [] # sera inserido os nomes dos arquivos em uma lista

indexList = 0
global contentFiles
global nomeDiretorio
folder = ''

def extList():

    combo = ttk.Combobox(width = 15)
    combo['values'] = ("JPG", "PDF")
    combo.grid(column = 1, row = 0)

def selectFolder():
    opcoes = {}
    opcoes['initialdir'] = ''    # será o diretório atual
    opcoes['title'] = 'Selecione a pasta dos arquivos'
    folder = filedialog.askdirectory(**opcoes)
    lbSelectedFolder["text"] = folder
    varFolder.set(folder)

def selectFileList():
    opcoes = {}
    opcoes['defaultextension'] = '.txt'
    opcoes['filetypes'] = [('Todos arquivos', '.*'), ('arquivos texto', '.txt')]
    opcoes['initialdir'] = ''    # será o diretório atual
    opcoes['initialfile'] = '' #apresenta todos os arquivos no diretorio
    opcoes['title'] = 'Diálogo que retorna um objeto arquivo'
    contentFiles = filedialog.askopenfile(mode='r', **opcoes)
    lbSelectedList["text"] = "Lista Selecionada!"
    varFile.set(contentFiles)

def rename():
    opcoes = {}
    opcoes['defaultextension'] = '.txt'
    opcoes['filetypes'] = [('Todos arquivos', '.*'), ('arquivos texto', '.txt')]
    opcoes['initialdir'] = ''    # será o diretório atual
    opcoes['initialfile'] = '' #apresenta todos os arquivos no diretorio
    opcoes['title'] = 'Selecione o arquivo'
    contentFiles = filedialog.askopenfile(mode='r', **opcoes)
    lbSelectedList["text"] = "Em Progesso..."

    file = contentFiles
    folder = varFolder.get()
    ext = extList.get()
    count = 0 # count sera usado para verificar a quantidade de arquivos para renomear
    countERROR = 0
    indexList = 0

    for nameFiles in os.listdir(folder):
        #os.rename(nameFiles.endswith(ext), nameFiles.lower())
        if nameFiles.endswith(ext): # verifica a extensao dos arquivos
            fileList.append(nameFiles) # adiciona na lista somente os arquivos com a extensao passada como parametro
            count += 1
    fileList.sort() # ordena a lista

    contentFiles = file.readlines() # ler cada linha do arquivo
    contentFiles.sort()
    #print(contentFiles)

    newFolder = folder + "/"
    for nameLine in contentFiles:
        countERROR += 1
        try:
            result = nameLine.rstrip()
            newName = newFolder + result + "." + ext
            os.rename(newFolder + fileList[indexList], newName)
            indexList += 1
            lbCountFiles["text"] = "{} arquivos foram renomeados!".format(indexList)


        except Exception:
            lbSelectedList["text"] = "ERROR: A quantidade de arquivos para renomear deve ser a mesma que os nomes na lista!"
            #print(indexList)
            break
    if (indexList == countERROR):
        lbSelectedList["text"] = "Concluído com Sucesso!"


##############################################
############## App Execution #################

janela = Tk()
janela.title("Renomear Arquivos")

lbExt = Label(janela, text="Selecione a extensão:")
lbExt.place(x=10,y=10)

extList = StringVar()
combo = ttk.Combobox(width = 15, textvariable = extList)
combo['values'] = ("jpg", "pdf")
combo.place(x = 170,y = 10)

lb = Label(janela, text="Pasta selecionada:")
lb.place(x=10,y=40)

varFolder = StringVar()


lbFolder = Label(janela)
lbFolder.place(x=200, y=15)

btFolder = Button(janela, width=10, text="Selecionar",command=lambda: selectFolder())
btFolder.place(x = 450,y = 40)


#lbFolder.place(x=200, y=15)

lbSelectedFolder = Label(janela)
lbSelectedFolder.place(x = 140, y=40)

lbStatus = Label(janela, text="STATUS:")
lbStatus.place(x = 10, y = 130)

lbCountFiles = Label(janela, text="")
lbCountFiles.place(x = 70, y = 130)


lbSelectedList = Label(janela, text="")
lbSelectedList.place(x = 10, y=150)

btList = Button(janela, width=10, text="Renomear", command=rename)
btList.place(x = 250,y = 100)
# LxA+E+T
# 300x300+100+100
janela.geometry("650x200+400+250")
janela.mainloop()
