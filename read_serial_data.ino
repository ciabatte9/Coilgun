#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <Wire.h>
#include <Servo.h>
Servo servoYaw; //yaw
Servo servoPitch; //pitch

int alfa, beta, shoot;

void setup() {
  servoYaw.attach(A0);
  servoPitch.attach(A1);
  servoYaw.write(85);
  servoPitch.write(90);
  pinMode(A5, OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(20);
}

void loop(){

    String teststr = Serial.readString();
    if(teststr != ""){
      teststr.trim();                        // remove any \r \n whitespace at the end of the String
      //Split the readString by a pre-defined delimiter in a simple way. '%'(percentage) is defined as the delimiter in this project.
      int delimiter, delimiter_1, delimiter_2, delimiter_3;
      delimiter = teststr.indexOf("|");
      delimiter_1 = teststr.indexOf("|", delimiter + 1);
      delimiter_2 = teststr.indexOf("|", delimiter_1 +1);
      delimiter_3 = teststr.indexOf("|", delimiter_2 + 1);

      // Define variables to be executed on the code later by collecting information from the readString as substrings.
      String alfaStr = teststr.substring(delimiter + 1, delimiter_1);
      String betaStr = teststr.substring(delimiter_1 + 1, delimiter_2);
      String shootStr = teststr.substring(delimiter_2 + 1, delimiter_3);

      Serial.print(alfaStr);
      Serial.print(" / ");
      Serial.print(betaStr);
      Serial.print(" / ");
      Serial.println(shootStr);

      int alfa = alfaStr.toInt();
      int beta = betaStr.toInt();
      int shoot = shootStr.toInt();

      servoYaw.write(alfa);
      servoPitch.write(beta);


      if(shoot == 1){
        digitalWrite(A5, HIGH);
      }
      else{
        digitalWrite(A5, LOW);
      }

    }
}
