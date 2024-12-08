
##Sorting Logic 
a=[2,9,51,6]
a.sort()
b = sorted(a)
print(a, "Using sort")
print(b, "Using sorted")

##Mapping logic
l = [1,2,3,4,5]
output_list = list(map(lambda x: x+1,l))
print(output_list," Mapped List")

a=[2,5,8,12]
b=[]
c = []
for i in a:
    if (i>5):
        b.append(i)
print(b)