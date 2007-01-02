from ablib import Daisy10

d10_module=Daisy10("D10",baudrate=9600,timeout=10)
d10_module.mode("RS422")

d10_module.flushInput()
d10_module.write("Hello World !")

print "Wait %d seconds for something from RS422 bus" % d10_module.timeout
print d10_module.read(20)

