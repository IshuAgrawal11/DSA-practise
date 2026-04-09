n = input("Enter the binary number in the form of string: ")
i = 0
n = int(n, 2)
while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n += 1
    i = +1
print(i)

# second approach with O(N) time complexity
class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        
        # Walk backwards from the end to the second digit
        for i in range(len(s) - 1, 0, -1):
            digit = int(s[i]) + carry
            
            if digit == 1:
                # Odd: Add 1 (1 step) then divide (1 step) = 2 steps
                steps += 2
                carry = 1
            else:
                # Even: Just divide (1 step)
                steps += 1
                # carry stays whatever it was
                
        return steps + carry