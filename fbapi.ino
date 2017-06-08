char incomingOption;
void setup()
{
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(9, OUTPUT);
  Serial.begin(9600);
}
void loop()
{
  incomingOption = Serial.read();
  switch (incomingOption) {
    case '1':
      digitalWrite(13, HIGH);
      break;
    case '2':
      digitalWrite(12, HIGH);
      break;
    case '3':
      digitalWrite(11, HIGH);
      break;
    case '4':
      digitalWrite(10, HIGH);
      break;
    case '5':
      digitalWrite(9, HIGH);
      break;
    case '0':
      digitalWrite(13, LOW);
      digitalWrite(12, LOW);
      digitalWrite(11, LOW);
      digitalWrite(10, LOW);
      digitalWrite(9, LOW);
      break;

  }
}
