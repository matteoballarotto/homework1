#!/usr/bin/env python
# coding=utf-8

__author__ = "Matteo Ballarotto"
__version__ = "1.0.1"
__license__ = "LGPLv3"

#Nodo 3: riceve un messaggio e una stringa in selezione, in base a quest'ultima stampa a video lo specifico messaggio o parte di esso


import rospy
from std_msgs.msg import String
from homework1.msg import *

messaggio = Message()


def receiveMessage(Message):
    messaggio.name = Message.name
    messaggio.age = Message.age
    messaggio.course = Message.course
    
def receiveChoose(data):
    if data.data == "a":
        rospy.loginfo(messaggio)
    elif data.data == "n":
        rospy.loginfo(messaggio.name)
    elif data.data == "e":
        rospy.loginfo(messaggio.age)
    elif data.data == "c":
        rospy.loginfo(messaggio.course)
    else:
        print ("")

def listener():
    rospy.init_node('nodo3', anonymous=True)
    
    rospy.Subscriber('message', Message, receiveMessage)
    rospy.Subscriber('choose', String, receiveChoose)
    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()