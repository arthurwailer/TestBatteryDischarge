#define DIGITAL_BATTERY_A 2
#define DIGITAL_BATTERY_B 3
#define DIGITAL_BATTERY_C 4
#define DIGITAL_BATTERY_D 5
#define DIGITAL_BATTERY_E 6
#define DIGITAL_BATTERY_F 7

#define ANALOG_BATTERY_A A0
#define ANALOG_BATTERY_B A1
#define ANALOG_BATTERY_C A2
#define ANALOG_BATTERY_D A3
#define ANALOG_BATTERY_E A4
#define ANALOG_BATTERY_F A5

#define VOLTAGE_MIN_BATTERY 2.5

const long numInputs = 6;  // Number Analog Input
long analogInputs[numInputs] = {ANALOG_BATTERY_A, ANALOG_BATTERY_B, ANALOG_BATTERY_C, ANALOG_BATTERY_D, ANALOG_BATTERY_E,ANALOG_BATTERY_F}; // Array analogoc Imput 

int analogValue = 0;
float voltage = 0;
float voltageFinal = 0;

void setup() {
  Serial.begin(9600);  // Start Serial Protocol
  pinMode(DIGITAL_BATTERY_A, OUTPUT);
  pinMode(DIGITAL_BATTERY_B, OUTPUT);
  pinMode(DIGITAL_BATTERY_C, OUTPUT);
  pinMode(DIGITAL_BATTERY_D, OUTPUT);
  pinMode(DIGITAL_BATTERY_E, OUTPUT);
  pinMode(DIGITAL_BATTERY_F, OUTPUT);
}

void loop() {
  outputOnTransistor();
  forBattery();
  _delay_ms(60000);
  outputOffTransistor();
  forBattery();
  _delay_ms(60000);
}
void outputOnTransistor(){
  digitalWrite(DIGITAL_BATTERY_A, HIGH);
  digitalWrite(DIGITAL_BATTERY_B, HIGH); 
  digitalWrite(DIGITAL_BATTERY_C, HIGH); 
  digitalWrite(DIGITAL_BATTERY_D, HIGH); 
  digitalWrite(DIGITAL_BATTERY_E, HIGH); 
  digitalWrite(DIGITAL_BATTERY_F, HIGH);    // ON pin1
}
void outputOffTransistor(){
  digitalWrite(DIGITAL_BATTERY_A, LOW);
  digitalWrite(DIGITAL_BATTERY_B, LOW);
  digitalWrite(DIGITAL_BATTERY_C, LOW);
  digitalWrite(DIGITAL_BATTERY_D, LOW);
  digitalWrite(DIGITAL_BATTERY_E, LOW);
  digitalWrite(DIGITAL_BATTERY_F, LOW);  
}

void forBattery(){
  for (int i = 0; i < 6; i++){
  analogValue = analogRead(analogInputs[i]);
  voltage = 0.0048 * analogValue;
  Serial.print(i);
  Serial.print("|");
  Serial.println(voltage,3);
  }
}