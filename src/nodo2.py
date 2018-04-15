#!/usr/bin/env python
# coding=utf-8
__author__ = "Matteo Ballarotto"
__version__ = "1.0.1"
__license__ = "LGPLv3"

#Nodo 2: invia al Nodo 3 la scelta inserita dall'utente


import rospy
from std_msgs.msg import String


def talker2():
    pub = rospy.Publisher('choose', String, queue_size=10)
    rospy.init_node('nodo2', anonymous=True)
    choose = String()
    val = True
    while val:
    	choose = raw_input("Inserire la scelta: \n a -> messaggio completo \n n -> nome \n e -> età \n c -> corso \n q -> esci \n---------: ")
    	if choose in ("a", "n", "e", "c", "q"):
        	if choose != "q":
            		pub.publish(choose)
        	else:
            		val = False
    	else:
        	print("Scelta errata")

if __name__ == '__main__':
	try:
		talker2()
	except rospy.ROSInterruptException:
		pass