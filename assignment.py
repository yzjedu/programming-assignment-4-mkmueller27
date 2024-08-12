# Programmer: Kristina Mueller
# Course: CS701/GB-731, Dr. Yalew
# Date: 08/12/2024
# Programming Assignment: 4
# Program Inputs: A positive integer < 1000
# Program Outputs: The English name of the integer


def main():
    pass

## Turns a number into its English name.
#  @param number a positive integer < 1,000
#  @return the name of the number (e.g. "two hundred seventy four")
#
def number_to_name(number):
        hundreds = ["one-hundred", "two-hundred", "three-hundred", "four-hundred", "five-hundred","six-hundred", 
                    "seven-hundred", "eight-hundred", "nine-hundred"]
        tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", 
                 "eighty", "ninety"]
        teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fiveteen", "sixteen", 
                 "seventeen", "eighteen", "nineteen"]
        digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        
        if 100 <= number <= 999:
            hundred = number//100                              #isolates the first digit
            tenth = (number % 100) // 10 * 10                  #isolates the second digit  
            digit = number % 10                                 #isolates the last digit 
             
            if 10 <= tenth <= 90 and tenth % 10 == 0 and 1 <= digit <= 9:
                return hundreds[hundred - 1] + " " + tens[(tenth // 10) - 2] + " " + digits[digit - 1]
            elif   tenth == 0:
                return hundreds[hundred - 1] + " " + digits[digit - 1]  
        elif 20 <= number <= 99: 
            tenth = number // 10 * 10               
            digit = number % 10  
            if digit == 0:
                 return tens[(tenth // 10) - 2] 
            else:
                 return tens[(tenth // 10) - 2] + " " + digits[digit - 1]
        elif 10 <= number <= 19:
            return teens[number - 10]
        elif 1 <= number <= 9:
             return digits[number - 1]
                    
        
#try it out
print(number_to_name(254)) 
print(number_to_name(204))
print(number_to_name(54))
print(number_to_name(14))
print(number_to_name(4))


## Turns a digit into its English name.
#  @param digit an integer between 1 and 9
#  @return the name of digit ("one" ... "nine")
#
def digit_to_name(digit):
        digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        if 1 <= digit < 9:
            return digits[digit - 1]
#try it out
print(digit_to_name(7))

## Turns a number between 10 and 19 into its English name.
#  @param number an integer between 10 and 19
#  @return the name of the given number ("ten" ... "nineteen")
#
def teen_to_name(teen):
        teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fiveteen", "sixteen", 
                 "seventeen", "eighteen", "nineteen"]
        if 10 <= teen <= 19:
            return teens[teen - 10]
#try it out
print(teen_to_name(17))                 

## Gives the name of the tens part of a number between 20 and 99.
#  @param number an integer between 20 and 99
#  @return the name of the tens part of the number ("twenty" ... "ninety")
#
def tens_to_name(tenth):
        tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", 
                 "eighty", "ninety"]
        if 10 <= tenth <= 90 and tenth % 10 == 0:
            return tens[(tenth // 10) - 2]
#try it out
print(tens_to_name(20))                

# Start the program.
if __name__ == "__main__":
    main()