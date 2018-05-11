from math import factorial
import time
def getCatalanNumber(n):
    return factorial(2*n)/(factorial(n+1)*factorial(n))
i = ""
while True:
    i = raw_input("Enter a whole number: ").lower()
    if i.isdigit():
        n = time.time()
        print "Catalan #" + i + " is " + str(getCatalanNumber(int(i))) + ".\n     Took " + str(time.time()-n) + " seconds."
    elif i in "quit":
        break
    else:
        print "    Enter a whole number!\n"
