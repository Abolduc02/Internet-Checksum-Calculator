'''
Title: Internet Checksum Calculator
Author: Aaron Bolduc
Date: December 6, 2022
'''

## Initialize variables used in program
binaryNumber = 0
userInput = None
sum = 0

## Get the checksum length the user wants to calculate
checksumLength = int(input("Enter checksum length (in bits): "))

## Have user enter in binary numbers they want to include in checksum, save in variable
while True:
    userInput = input("Enter binary string, or press enter to continue: ")
    
    if userInput == "":
        break

    binaryNumber += int(userInput, 2)

## Wrap bits and add to number if needed (based on checksum length)
while binaryNumber > 0:
    sum += (binaryNumber % (2 ** checksumLength))
    binaryNumber >>= checksumLength

    ## If sum goes over checksum length, wrap bits
    if sum >= (2 ** checksumLength):
        sum += sum >> checksumLength
        sum -= (2 ** checksumLength)

## Invert bitstring to get final checksum and print out
print(bin(sum ^ ((2 ** checksumLength) - 1))[2:])