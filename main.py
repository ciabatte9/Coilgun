#!/usr/bin/env python3
import time
from clamps import PS4Joystick
import serial

arduino = serial.Serial('COM3', 9600)
time.sleep(2)
print("pronto a ricevere")


def main():

    x = 90
    lim_x_upper = 160
    lim_x_lower = 20

    y = 90
    lim_y_upper = 130
    lim_y_lower = 50

    threshold = 0.1
    rot_speed = 10
    starting_x = 90
    starting_y = 90

    js = PS4Joystick() # or PS5Joystick()

    while js.valid:
        try:
            ps4 = js.get()

            if ps4.buttons.x is True:
                arduino.write( ("|" + str(int(x)) + "|" + str(int(y)) + "|" + "1").encode('utf-8') )
                print( ("|" + str(int(x)) + "|" + str(int(y)) + "|" + "1") )
                time.sleep(0.3)
                arduino.write( ("|" + str(int(x)) + "|" + str(int(y)) + "|" + "0").encode('utf-8') )
                print( ("|" + str(int(x)) + "|" + str(int(y)) + "|" + "0") )
                time.sleep(0.1)

            if ps4.buttons.L3 :
                x = starting_x
                y = starting_y
                arduino.write( ("|" + str(int(x)) + "|" + str(int(y)) + "|" + "0").encode('utf-8') )
                print( ("|" + str(int(x)) + "|" + str(int(y)) + "|" + "0") )

            # controllo il joystick e se supero una certa soglia inizio ad interagire
            if ps4.leftstick.x >= threshold or ps4.leftstick.x <= -threshold or ps4.leftstick.y >= threshold or ps4.leftstick.y <= -threshold:

                # controllo se i valori superano i valori limite e nel caso li correggo
                if x > lim_x_upper:
                    x = lim_x_upper
                elif x < lim_x_lower:
                    x = lim_x_lower

                if y > lim_y_upper:
                    y = lim_y_upper
                elif y < lim_y_lower:
                    y = lim_y_lower

                # se il valore è compreso nel limite (come ovviamente è siccome li ho appena corretti) aggiungo o tolgo
                if lim_x_lower <= x <= lim_x_upper:
                    x -= ps4.leftstick.x * rot_speed

                if lim_y_lower <= y <= lim_y_upper:
                    y += ps4.leftstick.y * rot_speed

                arduino.write( ("|" + str(int(x)) + "|" + str(int(y)) + "|" + "0").encode('utf-8') )
                print( ("|" + str(int(x)) + "|" + str(int(y)) + "|" + "0") )

            time.sleep(0.1)

            if ps4.buttons.dp_up is True:
                break
        except KeyboardInterrupt:
            print('js exiting ...')
            break


if __name__ == "__main__":
    main()
