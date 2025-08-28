#1.Multiples of 3 or 5
s=0
for i in range(1,1000):
    if i%3==0 or i%5==0:
        s+=i
print(s) 

#6.Sum Square Difference
s1=0
s2=0
for i in range(1,101):
    s1+=(i**2)
    s2+=i
print((s2**2)-s1)       
