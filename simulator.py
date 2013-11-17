import random

count = 0
kop = 0
munt = 0

times = raw_input("How many coin tosses? ")
times = int(times)

while count < times:
    rand = random.randint(1,2)
    if rand == 1:
        kop += 1
    else:
        munt += 1
    count += 1

percentage = float(kop) / count

print "Heads = " + str(kop)
print "Tails = " + str(munt)
print "Percentage heads = " + str(percentage)
