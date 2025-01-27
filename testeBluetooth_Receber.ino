#include <SoftwareSrial.h>
#include <Servo.h>

int motorPlus = 5;
int motorMinus = 6;
int rxPin = 10;
int txPin = 11;
SoftwareSerial mySerial(rxPin, txPin);
Servo myServo;
void setup() {
  // Inicializa a comunicação serial
  Serial.begin(9600);
  mySerial.begin(9600);
  myServo.attach(9);
  pinMode(motorPlus, OUTPUT);
  pinMode(motorMinus, OUTPUT);
}

void loop() {
  if (Serial.available() > 0 && mySerial.available() > 0) {  // Verifica se há dados recebidos na porta serial
    while(mySerial.read() == '1'){ //Caso saia do while e por que esta off o aplicativo bluetooth 
      delay(30000);
      Serial.println("1");

      String receivedData = Serial.readStringUntil('\n');  // Lê até o caractere de nova linha '\n'
      int receivedInt = receivedData.toInt();  // Converte a String para inteiro
  
      if(receivedInt == 0){
        Serial.println("Achou algo diferente de limão e laranja");
        analogWrite(motorPlus, 0);
        analogWrite(motorMinus, 128);
      } else if(receivedInt < 180){
        Serial.println("Laranja");
        myServo.write(40;
        analogWrite(motorPlus, 128);
        analogWrite(motorMinus, 0);
        delay(1000);
      } else {
        Serial.println("Limão");
        myServo.write(140);
        analogWrite(motorPlus, 128);
        analogWrite(motorMinus, 0);
        delay(1000);
      }
    }
  }
  analogWrite(motorPlus, 0);
  analogWrite(motorMinus, 0);
}