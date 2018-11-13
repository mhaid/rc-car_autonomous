#define CS_THRESHOLD 100

int statpin = 13;
int inApin[2] = {7, 4};  // INA: Clockwise input
int inBpin[2] = {8, 9}; // INB: Counter-clockwise input
int pwmpin[2] = {5, 6}; // PWM input
int cspin[2] = {2, 3}; // CS: Current sense ANALOG input
int enpin[2] = {0, 1}; // EN: Status of switches output (Analog pin)

int tmp = 0;
bool f_locked = false;
bool r_locked = false;

void setup()
{
  pinMode(statpin, OUTPUT);

  // Initialize output Pins
  for (int i = 0; i < 2; i++)
  {
    pinMode(inApin[i], OUTPUT);
    pinMode(inBpin[i], OUTPUT);
    pinMode(pwmpin[i], OUTPUT);
  }

  // Initialize as braked
  for (int i = 0; i < 2; i++)
  {
    digitalWrite(inApin[i], LOW);
    digitalWrite(inBpin[i], LOW);
  }

  activate_motor(5);
  activate_motor(0);
  activate_motor(6);
  activate_motor(0);

  Serial.begin(115200);
}


void loop()
{
  if (Serial.available() > 0)
  {
    int command = int(Serial.read());

    if(f_locked == true)
    {
      if(command == 4 || command > 12)
      {
        Serial.println("Empfangen: " + command);
        if(command != 16)
        {
          tmp = command;
        }
        activate_motor(command); 
      }
      else
      {
        Serial.println("Blockiert: " + command); 
      }
    }
    else if(r_locked == true)
    {
      if(command != 4 && command  != 13 && command != 14)
      {
        Serial.println("Empfangen: " + command);
        if(command != 16)
        {
          tmp = command;
        }
        activate_motor(command); 
      }
      else
      {
        Serial.println("Blockiert: " + command); 
      }
    }
    else
    {
      Serial.println("Empfangen: " + command);

      // Set new temp command
      tmp = command;
      activate_motor(command); 
    }
  }
  else
  {
    activate_motor(17);
    //activate_motor(tmp);
  }
}


void forward1(int time) {
  digitalWrite(inApin[0], HIGH);
  digitalWrite(inBpin[0], LOW);
  analogWrite(pwmpin[0], 200);
  delay(time);

  if ((analogRead(cspin[0]) < CS_THRESHOLD) && (analogRead(cspin[1]) < CS_THRESHOLD))
    digitalWrite(statpin, HIGH);
}

void forward2(int time) {
  digitalWrite(inApin[0], HIGH);
  digitalWrite(inBpin[0], LOW);
  analogWrite(pwmpin[0], 500);
  delay(time);

  if ((analogRead(cspin[0]) < CS_THRESHOLD) && (analogRead(cspin[1]) < CS_THRESHOLD))
    digitalWrite(statpin, HIGH);
}

void forward3(int time) {
  digitalWrite(inApin[0], HIGH);
  digitalWrite(inBpin[0], LOW);
  analogWrite(pwmpin[0], 1000);
  delay(time);

  if ((analogRead(cspin[0]) < CS_THRESHOLD) && (analogRead(cspin[1]) < CS_THRESHOLD))
    digitalWrite(statpin, HIGH);
}

void reverse(int time) {
  digitalWrite(inApin[0], LOW);
  digitalWrite(inBpin[0], HIGH);
  analogWrite(pwmpin[0], 500);
  delay(time);

  if ((analogRead(cspin[0]) < CS_THRESHOLD) && (analogRead(cspin[1]) < CS_THRESHOLD))
    digitalWrite(statpin, HIGH);
}

void right(int time) {
  digitalWrite(inApin[1], HIGH);
  digitalWrite(inBpin[1], LOW);
  analogWrite(pwmpin[1], 1000);
  delay(time);

  if ((analogRead(cspin[0]) < CS_THRESHOLD) && (analogRead(cspin[1]) < CS_THRESHOLD))
    digitalWrite(statpin, HIGH);
}

void left(int time) {
  digitalWrite(inApin[1], LOW);
  digitalWrite(inBpin[1], HIGH);
  analogWrite(pwmpin[1], 1000);
  delay(time);

  if ((analogRead(cspin[0]) < CS_THRESHOLD) && (analogRead(cspin[1]) < CS_THRESHOLD))
    digitalWrite(statpin, HIGH);
}


void forward1_right(int time) {
  digitalWrite(inApin[0], HIGH);
  digitalWrite(inBpin[0], LOW);
  analogWrite(pwmpin[0], 200);

  digitalWrite(inApin[1], HIGH);
  digitalWrite(inBpin[1], LOW);
  analogWrite(pwmpin[1], 1000);
  delay(time);

  if ((analogRead(cspin[0]) < CS_THRESHOLD) && (analogRead(cspin[1]) < CS_THRESHOLD))
    digitalWrite(statpin, HIGH);
}

void forward2_right(int time) {
  digitalWrite(inApin[0], HIGH);
  digitalWrite(inBpin[0], LOW);
  analogWrite(pwmpin[0], 500);

  digitalWrite(inApin[1], HIGH);
  digitalWrite(inBpin[1], LOW);
  analogWrite(pwmpin[1], 1000);
  delay(time);

  if ((analogRead(cspin[0]) < CS_THRESHOLD) && (analogRead(cspin[1]) < CS_THRESHOLD))
    digitalWrite(statpin, HIGH);
}

void forward3_right(int time) {
  digitalWrite(inApin[0], HIGH);
  digitalWrite(inBpin[0], LOW);
  analogWrite(pwmpin[0], 1000);

  digitalWrite(inApin[1], HIGH);
  digitalWrite(inBpin[1], LOW);
  analogWrite(pwmpin[1], 1000);
  delay(time);

  if ((analogRead(cspin[0]) < CS_THRESHOLD) && (analogRead(cspin[1]) < CS_THRESHOLD))
    digitalWrite(statpin, HIGH);
}

void forward1_left(int time) {
  digitalWrite(inApin[0], HIGH);
  digitalWrite(inBpin[0], LOW);
  analogWrite(pwmpin[0], 200);

  digitalWrite(inApin[1], LOW);
  digitalWrite(inBpin[1], HIGH);
  analogWrite(pwmpin[1], 1000);
  delay(time);

  if ((analogRead(cspin[0]) < CS_THRESHOLD) && (analogRead(cspin[1]) < CS_THRESHOLD))
    digitalWrite(statpin, HIGH);
}

void forward2_left(int time) {
  digitalWrite(inApin[0], HIGH);
  digitalWrite(inBpin[0], LOW);
  analogWrite(pwmpin[0], 500);

  digitalWrite(inApin[1], LOW);
  digitalWrite(inBpin[1], HIGH);
  analogWrite(pwmpin[1], 1000);
  delay(time);

  if ((analogRead(cspin[0]) < CS_THRESHOLD) && (analogRead(cspin[1]) < CS_THRESHOLD))
    digitalWrite(statpin, HIGH);
}

void forward3_left(int time) {
  digitalWrite(inApin[0], HIGH);
  digitalWrite(inBpin[0], LOW);
  analogWrite(pwmpin[0], 1000);

  digitalWrite(inApin[1], LOW);
  digitalWrite(inBpin[1], HIGH);
  analogWrite(pwmpin[1], 1000);
  delay(time);

  if ((analogRead(cspin[0]) < CS_THRESHOLD) && (analogRead(cspin[1]) < CS_THRESHOLD))
    digitalWrite(statpin, HIGH);
}

void reverse_right(int time) {
  digitalWrite(inApin[0], LOW);
  digitalWrite(inBpin[0], HIGH);
  analogWrite(pwmpin[0], 500);

  digitalWrite(inApin[1], HIGH);
  digitalWrite(inBpin[1], LOW);
  analogWrite(pwmpin[1], 1000);
  delay(time);

  if ((analogRead(cspin[0]) < CS_THRESHOLD) && (analogRead(cspin[1]) < CS_THRESHOLD))
    digitalWrite(statpin, HIGH);
}

void reverse_left(int time) {
  digitalWrite(inApin[0], LOW);
  digitalWrite(inBpin[0], HIGH);
  analogWrite(pwmpin[0], 500);

  digitalWrite(inApin[1], LOW);
  digitalWrite(inBpin[1], HIGH);
  analogWrite(pwmpin[1], 1000);
  delay(time);

  if ((analogRead(cspin[0]) < CS_THRESHOLD) && (analogRead(cspin[1]) < CS_THRESHOLD))
    digitalWrite(statpin, HIGH);
}

void breaking() {
  for (int i = 0; i < 2; i++)
  {
    digitalWrite(inApin[i], LOW);
    digitalWrite(inBpin[i], LOW);
    analogWrite(pwmpin[i], 0);
  }
}

void forward_lock()
{
  breaking();
  f_locked = true;
}

void forward_unlock()
{
  breaking();
  f_locked = false;
}

void reverse_lock()
{
  breaking();
  r_locked = true;
}

void reverse_unlock()
{
  breaking();
  r_locked = false;
}

void activate_motor(int command)
{
  int time = 200;
  switch (command)
  {
    case 0: breaking(); break;

    case 1: forward1(time); break;
    case 2: forward2(time); break;
    case 3: forward3(time); break;
    case 4: reverse(time); break;
    case 5: right(time); break;
    case 6: left(time); break;

    case 7: forward1_right(time); break;
    case 8: forward2_right(time); break;
    case 9: forward3_right(time); break;
    case 10: forward1_left(time); break;
    case 11: forward2_left(time); break;
    case 12: forward3_left(time); break;
    case 13: reverse_right(time); break;
    case 14: reverse_left(time); break;

    case 15: forward_lock(); break;
    case 16: forward_unlock(); break;
    case 18: reverse_lock(); break;
    case 19: reverse_unlock(); break;

    case 17: delay(time); break;
  }
}

