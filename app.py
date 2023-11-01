import pywhatkit
import pyautogui
import time
from datetime import datetime

contatos = ['+553381985946513', '+553381987137941']

while len(contatos) > 0:
    # Verifica se ainda há contatos antes de tentar enviar a mensagem
    if len(contatos) > 0:
        pywhatkit.sendwhatmsg(contatos[0], 'Vamos automatizar tudo!!', datetime.now().hour, datetime.now().minute + 2)
        time.sleep(10)  # Aguarde 10 segundos para a mensagem ser enviada

        # Use pyautogui para fechar a aba
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(2)  # Aguarde 2 segundos antes de passar para o próximo contato
        del contatos[0]
    else:
        break  # Sai do loop se não houver mais contatos

    
    

