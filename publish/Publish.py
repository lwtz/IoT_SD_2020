# encoding: utf-8

import paho.mqtt.client as mqtt
import os
import time

from random import randint
from time import sleep


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    cls()

    print('===========================================================')
    print('=             Sensor de temperatura (Publish)             =')
    print('===========================================================')
    print('')
    ip = raw_input('Informe o ip do Broker: ')
    print('')

    topico = "casa/sala/temperatura"

    client = mqtt.Client("C" + str(time.time()))
    client.connect(ip, 1883)

    for x in range(0, 500):
        temp = randint(0, 100)
        client.publish(topico, temp)

        print topico + " " + str(temp)

        sleep(1)

    client.disconnect()


main()
