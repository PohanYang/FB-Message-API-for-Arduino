import fbchat
import serial
import pickle
import sys

def fb_buffer(client):
	sp = serial.Serial()
	sp.port = sys.argv[4]
	sp.baudrate = 9600
	sp.timeout = 5
	sp.open()
	sp.readline()
	while(1):
		chofid = client.getUsers(sys.argv[3])[0]
		last_messages = client.getThreadInfo(chofid.uid, last_n=2)
		fbm = str(last_messages[0].body) 
		sp.write(fbm)

if __name__ == '__main__':
	client = fbchat.Client(sys.argv[1], sys.argv[2])
	fb_buffer(client)