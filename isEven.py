# Naive
def modulo(num): # checks remainder when dividing number by 2
    return num%2 == 0

# Bitwise Operators
def bitshiftEquality(num): # bitshift right and left to force last bit as zero, then checks equality
    return num == (num >> 1) << 1

def bitshiftXOR(num): # XOR on bitshiftEquality() to check if both numbers are the same (a XOR a = 0)
    return (num ^ (num >> 1) << 1) == 0

def bitwiseAND(num): # bitwise AND with 1 to check if last bit is 1 or 0
    return num & 1 == 0

# Iterative
def iterative(num): # iterates till num, toggling a boolean state till it reaches the number
    ret = True
    for i in range(num):
      ret != ret
    return ret

# Memoised
memo = {0:True}
def memoized(num): # stores isEven status in a dictionary and references to find result. 2 cases to ensure it works with negatives
  if num not in memo:
    if num > 0:
      memo[num] = not memoized(num-1)
    else:
      memo[num] = not memoized(num+1)
  return memo[num]

# Math Operations
def floatDivision(num): # checks if division by 2 equals the same converted to an integer
    return num / 2 == int(num / 2)

def intDivision(num): # same as float division, but uses integer division (//)
    return num / 2 == num // 2

# String Operations
def base10Check(num): # checks if last digit is an even number
    return str(num)[-1] in ['0', '2', '4', '6', '8']

def binaryCheck(num): # checks if last bit is 0
    return str(bin(num))[-1] == '0'
