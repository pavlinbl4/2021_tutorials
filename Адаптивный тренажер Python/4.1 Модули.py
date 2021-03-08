import math

a1,b1,c1 = map(int, input().split())
a2,b2,c2 = map(int, input().split())

print( round(math.acos(a1*a2 + b1*b2 + c1*c2) / (math.sqrt( a1**2 + b1**2 + c1**2) * math.sqrt(a2**2 + b2**2 + c2**2))* 360 / math.pi, 2 ))

# math.?