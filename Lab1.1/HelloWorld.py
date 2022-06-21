import sys

print ("Hello World!")
print ("Hello World!")

s="This is another text"
print (sys.getsizeof(s))

def test(x):
    print(x)
    return x*x

print(test(50)+test(20))


