#include <WiFi.h>
#include <DHT.h>
#include <ArduinoJson.h>

const char* ssid = "SALA_2";
const char* password = "sala1234";

DynamicJsonDocument doc(JSON_OBJECT_SIZE(3) + 50);

WiFiServer server(80);

const int rele = 13;
DHT dht(26, DHT11);

void setup() {
  Serial.begin(115200);
  pinMode(rele, OUTPUT);
  dht.begin();
  delay(200);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
  }

  Serial.println("Conectado.");
  Serial.print("IP: ");
  Serial.print(WiFi.localIP());
  server.begin();
}

void loop() {
  WiFiClient client = server.available();
  
  if (client) {
    while (client.connected()) {

      if (client.available()) {

        char c = client.read();
        if (c == '0') {
          digitalWrite(rele, 0);
        } else if (c == '1') {
          digitalWrite(rele, 1);
        } else if (c == '2') {
          int HumSuelo = map(analogRead(33), 4092, 0, 0, 100);
          int HumAmbiente = dht.readHumidity();
          int Temp = dht.readTemperature();

          doc["HumSuelo"] = HumSuelo;
          doc["HumAmbiente"] = HumAmbiente;
          doc["Temp"] = Temp;
          String output;
          serializeJson(doc, output);

          client.println(output);
        }
      }
    }
    client.stop();
  }
}

