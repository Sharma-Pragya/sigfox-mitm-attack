from network import Sigfox
import socket
import binascii
# init Sigfox for RCZ1 (Europe)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ2)

# create a Sigfox socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)
sigfox.public_key()

# make the socket blocking
s.setblocking(True)

# configure it as DOWNLINK specified by 'True'
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, True)

# send some bytes and request DOWNLINK

output = s.send(bytes([1]))

# await DOWNLINK message
input  = s.recv(32)
print(output)
print(binascii.hexlify(input))
