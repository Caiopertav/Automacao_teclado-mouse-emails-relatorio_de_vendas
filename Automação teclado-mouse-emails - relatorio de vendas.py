import time
import pyautogui


from tkinter import *

root = Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()
xo=1366
yo=768
yfac=monitor_height/yo
xfac=monitor_width/xo
#print("width x height = %d x %d (pixels)" %(monitor_width, monitor_height))
#mainloop()

def x(x):
    x1=x*xfac
    return x1
def y(y):
    y1=y*yfac
    return y1

link="https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema"

###


# considerando que vamos abrir nova aba
#pyautogui.press("win")  poderia ser tecla win mas e melhor clicar no campo de busca que nao da erro
pyautogui.click(x=x(35), y=y(749))
time.sleep(3)
pyautogui.write("Chrome")

pyautogui.press("enter")
time.sleep(9)
pyautogui.click(x=x(525), y=y(47))

pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

###

# agora vamos clicar no campo do login e senha
pyautogui.click(x=x(743), y=y(351))
pyautogui.write("loginzao")


pyautogui.click(x=x(630), y=y(405))
pyautogui.write("senha")


#dar ok na pag
pyautogui.click(x=x(665), y=y(482))
                
time.sleep(10) #esperar carregar sempre depois de da inicio aseu_login um processo

###

#considere serie de clicks para baixar arquivo no drive

pyautogui.click(x=x(501), y=y(322))

pyautogui.click(x=x(599), y=y(630))
time.sleep(3)

###

#agora imaginando configuração normal, arquivo vai pra pasta downloads e vamos redireciona-lo para pasta raiz desse arquivo
#objetivo de tornar ambiente mais organizado

#chegamos na pasta de downloads(caminho pode variar, foi usado o item de downloads do navegador)
pyautogui.click(x=x(1189), y=y(66))
pyautogui.click(x=x(1193), y=y(111))
time.sleep(3)
#selecionamos o arquivo e copiamos o arquivo
pyautogui.click(x=x(258), y=y(252))
pyautogui.hotkey("ctrl","c")
#nos encaminhamos para pasta raiz da aplicação
pyautogui.click(x=x(1094), y=y(152))
pyautogui.write("C:\Users\Caio\Downloads\Python Intensivao Hash\Aula 1")
#colamos o arquivo na pasta 
pyautogui.click(x=x(1094), y=y(152))
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")#para o caso de sustituir o arquivo

#obs: Não seria necessário esse passo caso quisessemos trabalhar com arquivo na pasta downloads,esse pedaço preza pela ordem

###

import pandas as pd
#após isso iremos trabalhar com pandas para data frame, usando arquivo na pasta, e gerar os dados que temos interesse
#manipulando os dados com ajuda do pandas podemos 
df=pd.read_csv("Compras.csv",sep=",")

total_gasto=df["ValorFinal"].sum()
quantidade=df["quantidade"].sum()
preco_medio=total_gasto/quantidade
#print (total_gasto)
#print(quantidade)
#print(preco_medio)

###

#agora já tendo gerado os dados , vamos automatizar envio de emails, primeiro entramos na pagina
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://mail.google.com/mail/u/0/")
pyautogui.press("enter")

time.sleep(5)

###

#clica-se para escrever e-mail
pyautogui.click(x=x(147), y=y(216))
#preenche-se os campos
pyautogui.write("caio_auto@hotmail.com")
pyautogui.press("tab")
pyautogui.press("tab")

# campo assunto
import pyperclip# copiamos essa informação com piper e colamos logo em seguida
pyperclip.copy("Relatório de compras")
pyautogui.hotkey("ctrl","v")
pyautogui.press("tab")


###

#preenchimento do conteudo

texto=f'''
Prezados,
Segue resumo das compras:

Gasto Total: R${total_gasto:,2f}
Quantidade: {quantidade:,}
Preço Médio: R$ {preco_medio:,2f}

att.'''
pyperclip.copy(texto)
pyautogui.hotkey("ctrl","v")

pyautogui.hotkey("ctrl","enter")
