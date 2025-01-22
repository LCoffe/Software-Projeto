import serial
import time
import rcfAuto as rcf

# Configura a porta serial (verifique a porta correta onde o Arduino está conectado)
arduino = serial.Serial('COM5', 9600)  # Substitua 'COMx' pela sua porta, ex: 'COM3' no Windows ou '/dev/ttyUSB0' no Linux/Mac
time.sleep(2)  # Espera o Arduino inicializar

# Envia um número inteiro para o Arduino
while True:
    num = int(input("Escreve aí: "))  # O número que você quer enviar
    aux = 0

    # Envia o número inteiro para o Arduino
    if(num == 1):
        aux = rcf.main()

    arduino.write(str(aux).encode()) # Converte o número para string e envia via serial
    print(f'Enviado para o Arduino: {aux}')

    # Envia um caractere de nova linha para indicar o final
    arduino.write(b'\n')
