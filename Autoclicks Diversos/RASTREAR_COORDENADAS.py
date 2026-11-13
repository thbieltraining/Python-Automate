
import pyautogui
import keyboard
import time

print("=== RASTREADOR DE COORDENADAS ===")
print("Movimente o mouse para consultar X e Y.")
print("Pressione ESC para encerrar.")

ultima_posicao = None

try:
    while True:

        posicao = pyautogui.position()

        if posicao != ultima_posicao:
            x, y = posicao

            print(f"X: {x} | Y: {y}")

            ultima_posicao = posicao

        if keyboard.is_pressed("esc"):
            print("\nPrograma encerrado.")
            break

        time.sleep(0.05)

except KeyboardInterrupt:
    print("\nPrograma encerrado.")
