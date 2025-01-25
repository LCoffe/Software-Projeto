int motorPlus = 5;
int motorMinus = 6;
void setup() {
  // Inicializa a comunicação serial
  Serial.begin(9600);
  pinMode(motorPlus, OUTPUT);
  pinMode(motorMinus, OUTPUT);
}

void loop() {
    delay(10000);

  Serial.println("1"); //Envia 1 na porta serial para o python ler

  if (Serial.available() > 0) {  // Verifica se há dados recebidos na porta serial
    String receivedData = Serial.readStringUntil('\n');  // Lê até o caractere de nova linha '\n'
    int receivedInt = receivedData.toInt();  // Converte a String para inteiro
    if(receivedInt == 0){
      Serial.println("Achou algo diferente de limão e laranja");
      analogWrite(motorPlus, 0);
      analogWrite(motorMinus, 0.5);
    } else if(receivedInt < 180){
      Serial.println("Laranja");
      analogWrite(motorPlus, 0.5);
      analogWrite(motorMinus, 0);
    } else {
      Serial.println("Limão");
      analogWrite(motorPlus, 0.5);
      analogWrite(motorMinus, 0);
    }
  }
}
