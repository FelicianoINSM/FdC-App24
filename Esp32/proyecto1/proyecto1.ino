#include <DHT.h>

DHT dht(26, DHT11); //temperatura y humedad.
void setup() {
  pinMode(13, OUTPUT); //rele.
  dht.begin();
  delay(200);
  Serial.begin(115200);
}

void loop() {

  if (Serial.available() > 0) {


    String mensaje = Serial.readString();

    if (mensaje.equals("r1")) {
      digitalWrite(13, 1);
    }

    else if (mensaje.equals("r0")) {
      digitalWrite(13, 0);
    }

    else if (mensaje.equals("hs")) {
      int HumSuelo = map(analogRead(34), 4092, 0, 0, 100); //humedad del suelo.
      Serial.print("HumS: ");
      Serial.print(HumSuelo);
      Serial.println(" %");
    }

    else if (mensaje.equals("th")){
      float temp = dht.readTemperature();
      float hum = dht.readHumidity();
      Serial.print("Temp: ");
      Serial.print(temp);
      Serial.println(" °C");

      Serial.print("Hum: ");
      Serial.print(hum);
      Serial.println(" %");
    }
  }

}