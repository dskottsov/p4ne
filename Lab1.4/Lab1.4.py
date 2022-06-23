class Subnet:
    def __init__(self, n="0.0.0.0", p="/0"):
        self.network = n
        self.prefix = p
    def __str__(self):
        return self.network + self.prefix
    def getnet(self):
        return self.network
    def getprefix (self):
        return self.prefix

n1 = Subnet("192.168.1.0","/24")
print(n1.getnet(),n1.getprefix())
print(n1)


