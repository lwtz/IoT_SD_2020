# encoding: utf-8

import paho.mqtt.client as mqtt
import os
import time


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado com o Broker \n")
    else:
        print("Falha na Conexão com o Broker \n")


def on_message(client, userdata, msg):
    print(msg.topic + " " + msg.payload)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    cls()

    print("================== MQTT - Broker Mosquitto - Python =================")
    print('=====================================================================')
    print('=            Simulador Sensor de temperatura (Subscribe)            =')
    print('=====================================================================')
    print('')
    ip = raw_input('Informe o ip do Broker: ')
    print('')

    client = mqtt.Client("C" + str(time.time()))
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(ip, 1883, 60)
    client.subscribe("casa/+/temperatura", 0)

    client.loop_forever()


main()
