/*
  LED

  This example creates a Bluetooth® Low Energy peripheral with service that contains a
  characteristic to control an LED.

  The circuit:
  - Arduino MKR WiFi 1010, Arduino Uno WiFi Rev2 board, Arduino Nano 33 IoT,
    Arduino Nano 33 BLE, or Arduino Nano 33 BLE Sense board.

  You can use a generic Bluetooth® Low Energy central app, like LightBlue (iOS and Android) or
  nRF Connect (Android), to interact with the services and characteristics
  created in this sketch.

  This example code is in the public domain.
*/

#include <ArduinoBLE.h>
#include <Arduino_LSM6DS3.h>

BLEService ledService("19B10000-E8F2-537E-4F6C-D104768A1214"); // Bluetooth® Low Energy LED Service

// Bluetooth® Low Energy LED Switch Characteristic - custom 128-bit UUID, read and writable by central
//BLEByteCharacteristic switchCharacteristic("19B10001-E8F2-537E-4F6C-D104768A1214", BLERead | BLEWrite);
BLEStringCharacteristic switchCharacteristic("19B10001-E8F2-537E-4F6C-D104768A1214", (unsigned int)(BLERead| BLENotify| BLEWrite),255);
const int ledPin = LED_BUILTIN; // pin to use for the LED

void setup() {
  Serial.begin(9600);
  while (!Serial);

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");

    while (1);
  }
  
  // set LED pin to output mode
  pinMode(ledPin, OUTPUT);

  // begin initialization
  if (!BLE.begin()) {
    Serial.println("starting Bluetooth® Low Energy module failed!");

    while (1);
  }

  // set advertised local name and service UUID:
  BLE.setLocalName("LED");
  BLE.setAdvertisedService(ledService);

  // add the characteristic to the service
  ledService.addCharacteristic(switchCharacteristic);

  // add service
  BLE.addService(ledService);

  // set the initial value for the characeristic:
  switchCharacteristic.writeValue("");

  // start advertising
  BLE.advertise();

  Serial.println("BLE LED Peripheral");
}

void loop() {
  // listen for Bluetooth® Low Energy peripherals to connect:
  if(!Serial)
  {
    Serial.begin(9600);
    while (!Serial);
  }
  BLEDevice central = BLE.central();
  //Serial.println("Waiting to connect");
  // if a central is connected to peripheral:
  if (central) {
    Serial.println(central.deviceName());
    Serial.print("Connected to central: ");
    // print the central's MAC address:
    Serial.println(central.address());

    // while the central is still connected to peripheral:
    while (central.connected()) {
      // if the remote device wrote to the characteristic,
      // use the value to control the LED:
      if (switchCharacteristic.written()) {
        if (switchCharacteristic.value()!="") 
        {   // any value other than 0
          Serial.println(switchCharacteristic.value());
          if(switchCharacteristic.value()=="rssi")
          {
            switchCharacteristic.setValue(String(central.rssi()));
          }
          else if(switchCharacteristic.value()=="accelerometer")
          {
            float x,y,z;
            IMU.readAcceleration(x, y, z);
            String accel = "x: "+String(x)+"\ty: "+String(y)+"\tz: "+String(z);
            switchCharacteristic.setValue(accel);
          }
          else
          {
            switchCharacteristic.setValue("Received");
          }
          digitalWrite(ledPin, HIGH);
        }
        else 
        {                              // a 0 value
          Serial.println(F("LED off"));
          digitalWrite(ledPin, LOW);          // will turn the LED off
        }
      }
    }

    // when the central disconnects, print it out:
    Serial.print(F("Disconnected from central: "));
    Serial.println(central.address());
  }
}
