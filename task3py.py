
def div (list1=[1,2,3],number=1):
#list1=[1,2,3,4,5]
    print("the numbers in",list1,"that are divisible by",number,"are: ")
    ctr=0
    for i in list1:
        if i%number==0:
            ctr+=1
            print(i)
    if ctr==0:
        print("not found")

div([3,7,8,6,4],2)
