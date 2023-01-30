#include <Adafruit_MLX90614.h>
Adafruit_MLX90614 mlx = Adafruit_MLX90614();

float BGL, Volt;
int sensorValue, red=12, green=3, cntr=0;
int senstivity= 150; // decrease the value for batter sensitivity
void setup() {
  pinMode(green, OUTPUT);
  pinMode(red, OUTPUT);
  digitalWrite(green, LOW);
  digitalWrite(red, LOW);
  Serial.begin(9600);
  while (!Serial);
  Serial.println(F("Breath Analyzer"));

  if (!mlx.begin()) {
    Serial.println(F("Error connecting to Temperature sensor. Check wiring."));
    while (1);
  };
}

void loop() {
  sensorValue = analogRead(A0); // Figaro sensor
  Volt = sensorValue*5.0/1024.0;
  
  if(sensorValue>=senstivity)
  {
//    Serial.print(F(String("Raw Data: "))+ sensorValue);
   
    BGL = ((158.12 * Volt) - senstivity)/6;
//    Serial.print(F("  BGL: "));
//    Serial.print(F(BGL));
//    Serial.println(F(" mg/dl"));
    if(BGL>=0.00)
    {
       Serial.print(F("Sensor Reading: "));
      Serial.print(Volt/2.00);
      Serial.print(F("mg/dl in BGL"));
      BGL =BGL /4;
      Serial.print(F("\tTemperature: "));
      Serial.print(mlx.readObjectTempF());
      Serial.println(F(" *F")); 
      cntr++;
    if(cntr==3)
    {
      digitalWrite(green, LOW);
      digitalWrite(red, HIGH);
      delay(100);
    }
    }
    
  }
  else
  {
    Volt=0;
    BGL=0;
//    Serial.print(String("Raw Data: ")+ sensorValue);
    Serial.print(F("\tSensor: "));
    Serial.print(Volt);
    Serial.print(F(" mg/dl in BGL"));
    Serial.print(F("\tTemperature: ")); 
    Serial.print(mlx.readObjectTempF()); 
    Serial.println(F("*F"));
    Serial.println();
    digitalWrite(green, HIGH);
    digitalWrite(red, LOW);
    cntr=0;
  }
  delay(1000);        // delay in between reads for stability
}
