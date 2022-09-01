from re import T


n=int(input('How many print #* : '))
t=int(n/2)
for i in range(t):
    print('#'+'*',end="")
if n%2!=0:
    print('#')    