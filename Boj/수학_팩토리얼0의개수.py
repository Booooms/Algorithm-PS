n=int(input())

cnt=0
while n>0:
  cnt+=n//5
  n//=5

print(cnt)

# other solution
# n = int(input())
# print(n//5 + n//25 + n//125)