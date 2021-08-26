#!/usr/bin/env python3

message = 'severe hurricane'

windspeed = int(input("what is windspeed "))

if windspeed >= 125:
    message = message + 'cat 5'
else:
    message = message + 'not severe'
print (message)

