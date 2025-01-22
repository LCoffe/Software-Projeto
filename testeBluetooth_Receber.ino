void setup() {
  // Inicializa a comunicação serial
  Serial.begin(9600);
  
  // Mensagem inicial
  Serial.println("Aguardando número inteiro...");
}

void loop() {
  if (Serial.available() > 0) {  // Verifica se há dados recebidos na porta serial
    String receivedData = Serial.readStringUntil('\n');  // Lê até o caractere de nova linha '\n'
    int receivedInt = receivedData.toInt();  // Converte a String para inteiro

    // Exibe o valor recebido no monitor serial
    Serial.print("Número recebido: ");
    //Serial.println(receivedInt);
    if(receivedInt == 0){
      Serial.println("Achou algo diferente de limão e laranja");
    } else if(receivedInt < 180){
      Serial.println("Laranja");
    } else {
      Serial.println("Limão");
    }
  }
}
