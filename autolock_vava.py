import pyautogui
from time import sleep

def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    pyautogui.FAILSAFE = True

escolha = input('Com qual boneco você vai jogar hoje? \n\n').lower()

def check_screen(nome):
    img = pyautogui.locateOnScreen("autolock_{}.png".format(nome), confidence=0.7)
    button_pos = img

    img2 = pyautogui.locateOnScreen(r"C:\confirmarvava.png", confidence=0.7)
    button_pos2 = img2 

    if button_pos != None:
        click(button_pos.left, button_pos.top)
        
    if button_pos2 != None:
        click(button_pos2.left, button_pos2.top)
        return True 

    return False

def main():
    queue_counter = 0
    print('Estou de olho na fila...', end="\n\n")
    
    while True:
        if check_screen(escolha):
            queue_counter += 1
            print(f'Filas aceitas: {queue_counter}')       
    
            sleep(3)
            
    

main()            