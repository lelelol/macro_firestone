import pyautogui
import time
from PIL import ImageGrab
import pygetwindow as gw
#just a small timer for u to open the game
time.sleep(5)
def verifica_cor_pixel(x, y, cor):
    tela = ImageGrab.grab()
    cor_pixel = tela.getpixel((x, y))
    return cor_pixel == cor

def verifica_janela_aberta(nome):
    janelas_abertas = gw.getWindowsWithTitle(nome)
    return len(janelas_abertas) > 1

cor = (42, 116, 39)

while True:
    if(verifica_janela_aberta("firestone")==True):
        if(verifica_cor_pixel(1718, 197, cor)==True):
            pyautogui.click(1718, 197)
            pyautogui.moveTo(100, 100)
        elif(verifica_cor_pixel(1731, 852, cor)==True):
            pyautogui.click(1731, 852)
            pyautogui.moveTo(100, 100)
        elif(verifica_cor_pixel(1731, 746, cor)==True):
            pyautogui.click(1731, 746)
            pyautogui.moveTo(100, 100)
        elif(verifica_cor_pixel(1731, 852, cor)==True):
            pyautogui.click(1731, 519)
            pyautogui.moveTo(100, 100)
        elif(verifica_cor_pixel(1731, 629, cor)==True):
            pyautogui.click(1731, 629)
            pyautogui.moveTo(100, 100)
        elif(verifica_cor_pixel(1731, 852, cor)==True):
            pyautogui.click(1731, 416)
            pyautogui.moveTo(100, 100)
    #timer for the next execution
    time.sleep(5)