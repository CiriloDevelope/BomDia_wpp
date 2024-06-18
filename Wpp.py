import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import urllib
import pyautogui
import datetime
import pyperclip
import keyboard


#Determinando Horario de envio da Msg
horario_bomdia = datetime.time(8, 0) #Ex caso seu interesse seja enviar a tarde basta colocar (13, 30)

mensagem = 'Bom dia' #Escreva a mensagem de interesse.
numero = 5511999999999 #Coloque o numero de interesse.

#Processo de Entrar no Google Chrome/Entrar diretamente na conversa desejada e enviar a Mensagem
texto = urllib.parse.quote(mensagem)
navegador = webdriver.Chrome()
link = f'https://web.whatsapp.com/send?phone={numero}&text={texto}'
pyperclip.copy(mensagem)
navegador.get('https://web.whatsapp.com/')

 #Processo de entrar no Wpp   
while len(navegador.find_elements('xpath', '//*[@id="app"]/div/div[2]/div[3]/header/div[1]')) < 1:
    sleep(2)
    navegador.get(link)
    sleep(5)


#Função para apertar o botao de enviar e colar a msg novamente 
def meu_programa():
    navegador.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
    sleep(2)
    keyboard.press('ctrl')
    keyboard.press('v')
    

#Processo de repetiçao de mensagem diariamente.  
while True:

    data_atual = datetime.datetime.now()
    apenas_hr = data_atual.time()
    
    if apenas_hr >= horario_bomdia and apenas_hr < (datetime.datetime.combine(datetime.date.today(), horario_bomdia) + datetime.timedelta(minutes=1)).time():
        meu_programa()
        sleep(60)
    
    else:
        print('Aguardando Horario do Bom dia! Proxima verificação daqui 1 min.')
        sleep(60)


#Criado por Cicero (@Ciriloous)