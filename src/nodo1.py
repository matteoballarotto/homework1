#!/usr/bin/env python
# coding=utf-8
__author__ = "Matteo Ballarotto"
__version__ = "1.0.1"
__license__ = "LGPLv3"

#Nodo 1: invia al Nodo 3, con frequenza 1 Hz, un messaggio



import rospy
from homework1.msg import *

messaggio = Message()
messaggio.name = "Matteo"
messaggio.age = 21
messaggio.course = "Informatica"


def talker():
    pub = rospy.Publisher("message", Message, queue_size=10)        #Apro il canale e lo denoto con "message", ovvero ciò che comunicherò in quel canale
    rospy.init_node('nodo1', anonymous=True)                        #Inizializzazione del nodo
    rate = rospy.Rate(1) # 1 messaggio al secondo
    while not rospy.is_shutdown():
        pub.publish(messaggio)                                  #con il metodo publish pubblico il messaggio nel canale
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass