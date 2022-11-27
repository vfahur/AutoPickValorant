import pyautogui

def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

escolha = input('Com qual agente você vai jogar hoje? \n').lower()

def check_screen(nome):
    img = pyautogui.locateOnScreen("autolock_{}.png".format(nome), confidence=0.7)
    button_pos = img

    img2 = pyautogui.locateOnScreen("confirmarvava.png", confidence=0.7)
    button_pos2 = img2 

    if button_pos != None:
        click(button_pos.left, button_pos.top)
        
    if button_pos2 != None:
        click(button_pos2.left, button_pos2.top)
        return True 

    return False

def main():
    print('Aguardando partida...', end="\n\n")
    
    while True:
        if check_screen(escolha):
            print('Bom jogo!')       
    
            break
            
    

main()            
