import time 

#%a : day in three letters
#%A : full day name
#%b : month in three digits
#%B : full month name
#%c : Tue Nov  7 13:54:35 2023  
#%C : this will tell about the centuries
#%d : date two digit
#%D : 11/07/23 date
#%e : date in one digit
#%F : date in 2023-11-07
#%g : Year in last two 23 
t=time.strftime("%g")
print(t)