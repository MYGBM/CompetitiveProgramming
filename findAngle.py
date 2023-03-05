from math import atan, degrees
AB = int(input())
BC = int(input())

angleC = atan(AB/BC) #angleC is in rads
#angleC needs to be converted to degrees and rounded to the next integer
angleC=round(degrees(angleC))
# print angle with degree sign
degree_sign=chr(176)
print(f'{angleC}{degree_sign}')





