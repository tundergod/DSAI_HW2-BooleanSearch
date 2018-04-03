import numpy as np

my =  open('my.txt').read().splitlines()
ans = open('ans.txt').read().splitlines()

ans = str(ans).split(',')
my = str(my).split(',')

for i in range(len(ans)):
    if ans[i] !=  my[i]:
        print(ans[i])
        break
