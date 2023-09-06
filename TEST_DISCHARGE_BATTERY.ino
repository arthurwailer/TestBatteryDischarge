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

#define VOLTAGE_MIN_BATTERY 2.4

const int numInputs = 6;  // Number Analog Input
int analogInputs[numInputs] = {ANALOG_BATTERY_A, ANALOG_BATTERY_B, ANALOG_BATTERY_C, ANALOG_BATTERY_D, ANALOG_BATTERY_E,ANALOG_BATTERY_F}; // Array analogoc Imput 

const int numOutputs = 6; // Number Digital Output
int digitalOutput[numOutputs] = {DIGITAL_BATTERY_A, DIGITAL_BATTERY_B, DIGITAL_BATTERY_C, DIGITAL_BATTERY_D, DIGITAL_BATTERY_E,DIGITAL_BATTERY_F}; // Array Digital Outputs 

const int batteryNum = 6;
bool batteryArray[batteryNum] = {1, 1, 1, 1, 1, 1};



int analogValue = 0;
float voltage = 0;
float voltageFinal = 0;
bool flag = false;
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
  flag = false;
  forBattery();
  _delay_ms(60000);
  outputOffTransistor();
  flag = true;
  forBattery();
  _delay_ms(60000);
}
void outputOnTransistor(){
  for (int i = 0; i < 6; i++){
    if(batteryArray[i]==1)
    {
    digitalWrite(digitalOutput[i], HIGH);
    }
  }
  
}
void outputOffTransistor(){
 for (int i = 0; i < 6; i++){
    digitalWrite(digitalOutput[i], LOW);
  }
}

void forBattery(){
  for (int i = 0; i < 6; i++){
  analogValue = analogRead(analogInputs[i]);
  voltage = 0.0048 * analogValue;
  if(flag == false){
    if(voltage <= VOLTAGE_MIN_BATTERY){
        batteryArray[i]  = 0;
    }
  }
  Serial.print(i);
  Serial.print("|");
  Serial.println(voltage,3);
  }
}
