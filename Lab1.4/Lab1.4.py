import ipaddress
import random


#a = random.randint(8, 24)
#b = random.randint(0x0B000000, 0xDF000000)
#net1 = ipaddress.IPv4Network((b,a), strict=False)

#print (net1)

class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self, a=1, b=1):
        self.ip_addr=random.randint(0x0b000000, 0xdf000000)
        self.ip_net=random.randint(8,24)
        ipaddress.IPv4Network.__init__(self, (self.ip_addr, self.ip_net), strict=False)

test1 = IPv4RandomNetwork()

class Networks_list(IPv4RandomNetwork):
    def ret_random_net(self):
        for i in range(0, 50):
            rn = IPv4RandomNetwork()
            return rn

test2=Networks_list()

print(test2.ret_random_net())











