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
             tenth = ((number % 100) // 10) * 10                #isolates the second digit  
             digit = number % 10                                 #isolates the last digit 
             
        if 10 <= tenth <= 90 and tenth % 10 == 0 and 1 <= digit <= 9:
            
            return hundreds[hundred - 1] + " " + tens[(tenth // 10) - 2] + " " + digits[digit - 1]
        elif   tenth == 0:
            return hundreds[hundred - 1] + " " + digits[digit - 1]  
        elif hundred == 0:
            return tens[(tenth // 10) - 2] + " " + digits[digit - 1]
        elif digits[digit - 1]:
            return digits[digit - 1]
        else:
            return teens[teen - 10]
                    
        
#try it out
print(number_to_name(254)) 
print(number_to_name(204))
print(number_to_name(54))
print(number_to_name(14))
print(number_to_name(4))