"""Python Interpreter and Basics Exercise.

Copyright (c) 2018-2021 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print(f"Type of 'pi': {type(pi)} . Value: {pi}")

# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if(i < 50):
    print(f"i ({i}) is less than 50")
elif(i > 50):
    print(f"i ({i}) is more than 50")
else:
    print("i is 50")


# TODO: Write a conditional that prints the color of the selected sportsball
picked_sportsball = random.choice(['tennis', 'basketball', 'golf'])

if len(picked_sportsball) == 4:
    print("Sports ball is white")
elif len(picked_sportsball) == 6:
    print("Sports ball is green")
else:
    print("Sports ball is orange")

print(f"Sports ball was: {picked_sportsball}")

# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.

def mult(val1, val2):
    return val1 * val2   

# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =", mult(12, 96))

print("48 x 17 =", mult(48, 17))

print("196523 x 87323 =", mult(196523,87323))
