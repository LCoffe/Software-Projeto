from pyfirmata import Arduino # type: ignore
import cv2
import time
import tkinter as tk
import rcfAuto as rcf

webcam = cv2.VideoCapture(0)

if(not webcam.isOpened()):
    print("Error: Could not open webcam.")
    exit(1)

window = tk.Tk()
window.configure(bg='black')
window.geometry("500x500")
window.title("Bluetooth Control")

board = Arduino('COM5')

pin_5 = board.get_pin('d:5:p')
pin_6 = board.get_pin('d:6:p')

def motor_on():
    pin_5.write(0.5)
    pin_6.write(0)
    print("Motor ON")

def motor_off():
    pin_5.write(0)
    pin_6.write(0)

    print(rcf.main()) # Função principal para reconhecimento.

    print("Motor OFF")

button_on = tk.Button(window, text="ON", command=motor_on, bg='green', fg='white')
button_on.place(x=100, y=100)

button_off = tk.Button(window, text="OFF", command=motor_off, bg='red', fg='white')
button_off.place(x=200, y=100)
 
window.mainloop()

webcam.release()
cv2.destroyAllWindows()