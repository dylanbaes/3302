from multiprocessing.connection import answer_challenge
import os

# algorithm for reading the RPN equation:
# read the line character by character, if it reads an operator character, apply that function to the previous 2 numbers
# once a function has been executed, turn those 3 characters (the 2 numbers and the operator that follows) into one number, which is the result
# a stack will be used for this algorithm

top = -1

numbers = []

operators = "+-*/"
kar = '^'

def fpop():
    global top
    if (top == -1):
        print("The stack is empty.")
        return
    else:
        top -= 1
        return numbers.pop()

# for EC, I implemented the power function, whereby if the "^" is found, the 2 integers before it are applied
# in which the function results in the first value to the power of the second value
def karat(v1, v2):
    answer = 0

    answer = pow(int(v2),int(v1))

    return answer

def fpush(number):
    global top
    top += 1
    numbers.append(number)

def readLine (line):
    result = 0
    #print(line) # string type for line
    arr = line.split(" ")
    for c in arr:
        if operators.find(c) == -1 and kar.find(c) == -1:
            fpush(c)
        elif kar.find(c) != -1:
            v1 = fpop()
            v2 = fpop()
            newNum = karat(v1, v2)
            fpush(newNum)
        else:
            # do the operation on previous two characters
            v1 = fpop()
            v2 = fpop()
            newNum = eval(str(v2) + str(c) + str(v1))
            # print(str(v2) + str(c) + str(v1) + str(newNum)) this prints out each of the expressions for debugging
            fpush(newNum)
    result = fpop()

    return result

file = "input_RPN.txt"

if (os.path.exists(file)):
    p = open(file, "r")
    input = p.read().splitlines()
    p.close()

for lines in input:
    # print("\n\n")
    result = readLine(lines)
    print(result)

