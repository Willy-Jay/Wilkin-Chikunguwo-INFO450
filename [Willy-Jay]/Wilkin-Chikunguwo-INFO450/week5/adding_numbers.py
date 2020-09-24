numbers = open( "a.txt", "r")

sum = 0

for line in numbers:
     sum = sum + int(line)
print( sum)
