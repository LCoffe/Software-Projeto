import serial
import time
import rcfAuto as rcf

# Configura a porta serial (verifique a porta correta onde o Arduino está conectado)
arduino = serial.Serial('COM6', 9600)  # Substitua 'COMx' pela sua porta, ex: 'COM3' no Windows ou '/dev/ttyUSB0' no Linux/Mac
time.sleep(2)  # Espera o Arduino inicializar

# Função para enviar dados para o Arduino
def enviar_para_arduino(dado):
    arduino.write(str(dado).encode())  # Converte o dado para string e envia via serial
    print(f'Enviado para o Arduino: {dado}')
    arduino.write(b'\n')  # Envia um caractere de nova linha para indicar o final

# Função para receber dados do Arduino
def receber_do_arduino():
    if arduino.in_waiting > 0:  # Verifica se há dados disponíveis para leitura
        linha = arduino.readline().decode('utf-8').strip()  # Lê uma linha de dados e decodifica
        print(f'Recebido do Arduino: {linha}')
        try:
            return int(linha)  # Converte a linha para inteiro e retorna
        except ValueError:
            return 0  # Se não for possível converter, retorna None

# Envia um número inteiro para o Arduino
while True:
    num = receber_do_arduino  # O número que você quer enviar para o Arduino

    # Envia o número inteiro para o Arduino
    if(num == 1):
        aux = rcf.main()
        enviar_para_arduino(aux)
