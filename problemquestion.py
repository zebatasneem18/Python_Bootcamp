N=int(input())
a,b,c=map(int,input().split())
sa=a*15
sb=b*4
sc=c*5
tot=sa+sb+sc
if(tot<N):
     print("The shopkeeper did not cheat")
elif(N>tot):
     print("The shopkeeper cheated")

