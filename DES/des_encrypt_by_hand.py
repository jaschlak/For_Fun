# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 08:18:30 2021

@author: joebl
"""

import sys

# %%

# convert decimal to binary(string)
def decimalToBinary(x,w,fill_len):
    
    # error handling convert to int
    x = int(x)
    w = int(w)
    
    #perform xor and leave only string
    binval = bin(x^w).replace("0b", "")
    
    # confirm not more than 5 bits or throw error
    if len(binval) <= fill_len:
        
        #pad with preceeeding 0's
        binval = binval.zfill(fill_len)
        
        return binval
    else:
        sys.exit('val ' + binval + ' in "decimalToBinary" too large!')
    
# convert binary to decimal
def binaryToDecimal(binary):
      
    binary = int(binary)
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal


# permiate value and return string
def p_to_string(xor_bin, p):
    
    #check if permiation order unique
    if len(set(p)) != len(p):
        sys.exit('permiation order not unique!')
    
    # build new string in permiation order
    p_string = ''
    for i in p:
        p_string += xor_bin[i]
        
    return p_string

# function1 (used in function2)
def encrypt1(x,w):
    
    # chosen
    p = [4,3,2,0,1]
    k=17
    
    # fill length required to  be 5 in this assignment
    fill_len = len(p)
    
    # perform xor and convert to binary string
    xor_bin = decimalToBinary(x,w,fill_len)
    
    # build permiated string
    perm_string = p_to_string(xor_bin, p)
    perm_int = int(perm_string)
    
    # return encrypted value
    return bin((perm_int * k) % 32)[2:]
    
    
def encrypt2(X,w):
    
    # perform xor and convert to binary string
    xor_bin = decimalToBinary(X,w,15)
    
    # num of iterations
    max_iter = int(len(xor_bin)/5)
    
    enc_val = ''
    for i in range(0,max_iter):
        
        # build blocks to process
        st = 0 + i*5
        end = 5 + i*5
        binary = xor_bin[st:end]
        
        # convert back to decimal to accomedate function1
        decimal_block = binaryToDecimal(xor_bin[st:end])
        
        # build appended encryption string
        enc_val += encrypt1(decimal_block,w)
        
    return enc_val

 # %%
# decimal inputs
x = 5
w = 3

# permiation order


# odd integer
k = 17


# run function 1
answer_1 = encrypt1(x,w)
print(answer_1)


# run function 2
X = 1090
answer_2 = encrypt2(X,w)

print(answer_2)