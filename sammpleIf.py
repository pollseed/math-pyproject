__author__ = 'shn'

x = [1,2,3,4,5,6,7,8,9]
print dict([(v,v**2) for v in x if v > 4])