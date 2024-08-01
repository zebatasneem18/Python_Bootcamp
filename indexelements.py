#Sum of elements present in k+1 index
#k=3
#input=parameter 3 6 8 4 61 2
#N=2 
#Output: 2

k=int(input())
N=int(input())
my_list=list(map(int,input().split()))
for i in range(0,len(my_list)):
    print(my_list[k+N],end=" ")
    break