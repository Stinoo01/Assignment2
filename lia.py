import math    
#input data        
# k< or == to 7                                                        
k = 6                                                                          
n = 17      
# n is < that P (2^k)                                                                    
P = 2**k                     
#setting probability (final output) == 0                                                  
probability = 0                                                                
for x in range(n, P + 1):                                                      
    prob = (math.factorial(P) / (math.factorial(x) * math.factorial(P - x))) * (0.25**x) * (0.75**(P - x))                                                        
    probability += prob                                                        
print(probability)        