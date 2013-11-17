import random

count = 0
heads = 0
tails = 0

times = raw_input("How many coin tosses? ")
times = int(times)

while count < times:
    rand = random.randint(1,2)
    if rand == 1:
        heads += 1
    else:
        tails += 1
    count += 1

percentage = (float(heads) / count) * 100

print "Heads = " + str(heads)
print "Tails = " + str(tails)
print "Percentage heads = " + str(percentage) + "%"
