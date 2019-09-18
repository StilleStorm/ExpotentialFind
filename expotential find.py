# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 14:18:09 2018

@author: StilleStorm
"""


    
def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    #base = int(base)
    #name = int(num)
    
    def exp(base, num):
        '''
        base and num integers only
        will return 0 if base > num
        returns expotential for number given a base
        if number does not have expotential of base
        it returns expotential value for nearest number lower than num
        '''
        
        if num // base == 0:
            return 1
        
        exp = 1
        
        while num // base != 1 and num // base > base:
            num = num // base
            exp += 1
            
        return exp
    
    #based on inner function, ref function derscription
    exponent = exp(base, num)
    
    #checking if we found proper exponent, if not definig lower and higher bound of exponent
    if base ** exponent == num:
        return exponent
    
    elif base ** exponent < num:
        exponentLow = exponent
        exponentHigh = exponent + 1
        if exponentHigh == num:
            return exponentHigh
        
    else:
        exponentHigh = exponent
        exponentLow = exponent - 1
        if exponentLow == num:
            return exponentLow
        
    print ( (base **exponentLow) - num,  (base ** exponentHigh) - num)
    # Checking wich exponent is the nearest. If tey are even returning lower     
    if num - (base **exponentLow) == num - (base ** exponentHigh):
        return exponentLow
    elif num - (base ** exponentLow) < num - (base ** exponentHigh):
        return exponentLow
    elif num - (base **exponentLow) > num - (base ** exponentHigh):
        return exponentHigh
    
    
    
        
            