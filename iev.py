#taking the six non negative interers
P1, P2, P3, P4, P5, P6 = 17955, 16252, 16788, 18491, 18744, 16698
#couples with dominant allele AA x BB 
E1, E2, E3 = 2, 2, 2,    
#couple with dominant allele AA x Ab                       
E4 = 2 * 0.75         
#couple with dominant allele Ab x Ab                                
E5 = 2 * 0.5      
#a couple receives no child with a dominant allele aa x bb
E6 = 2 * 0         
#doing calculations
E = (E1 * P1) + (E2 * P2) + (E3 * P3) + (E4 * P4) + (E5 * P5) + (P6 * E6) 
#printing result 
print(E)  