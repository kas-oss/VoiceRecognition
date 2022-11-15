from tkinter import *
from tkinter.filedialog import askopenfilename

import reconhecedorFala

def selecionarArquivo():
    #Tk().withdraw() # Isto torna oculto a janela principal
    filename = askopenfilename()
    trancricao = reconhecedorFala.transcreverAudio(filename)
    blocoTexto.insert(index="insert", chars=trancricao)
    

janela = Tk()
janela.title("Transcritor de Voz")
janela.geometry("500x300")

info  = Label(janela,text="Selecione o arquivo de audio.")
info.grid(column=0, row=0)

botao = Button(janela,text="Selecionar", command=selecionarArquivo)
botao.grid(column=0,row=2)

blocoTexto = Text(janela, width=60, height=20)
blocoTexto.grid(column=0)




def exibirJanela():
    janela.mainloop()