int motor+ = 5;
int motor- = 6;
void setup() {
  // Inicializa a comunicação serial
  Serial.begin(9600);
  pinMode(motor+, OUTPUT);
  pinMode(motor-, OUTPUT);
}

void loop() {
  int i = 0;
  while(i > 60){
    delay(1000);
    i++;
  }

  Serial.println("1"); //Envia 1 na porta serial para o python ler

  if (Serial.available() > 0) {  // Verifica se há dados recebidos na porta serial
    String receivedData = Serial.readStringUntil('\n');  // Lê até o caractere de nova linha '\n'
    int receivedInt = receivedData.toInt();  // Converte a String para inteiro
    if(receivedInt == 0){
      Serial.println("Achou algo diferente de limão e laranja");
    } else if(receivedInt < 180){
      Serial.println("Laranja");
      analogWrite(motor+, 0.5);
      analogWrite(motor-, 0);
    } else {
      Serial.println("Limão");
      analogWrite(motor+, 0);
      analogWrite(motor-, 0.5);
    }
  }
}
