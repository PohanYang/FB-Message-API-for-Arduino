import fbchat
import serial
import sys
import pickle

def main():
	sp = serial.Serial()
	sp.port = 'COM3'
	sp.baudrate = 9600
	sp.timeout = 5
	sp.open()
	sp.readline()
	while 1:
		with open("fbchat.p", "rb") as fp:
			chat = pickle.load(fp)
		fp.close()
		print chat
		sp.write(chat)
	sp.close()	

if __name__ == "__main__":
    main()