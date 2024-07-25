age=int(input())
if(age>=18 and age<24):
    print("Only two wheeler")
elif(age>=18 and age<45):
    print("Two or four wheelers")
elif(age<18):
    print("restricted")
else: 
    print("All")