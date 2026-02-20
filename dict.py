d=None 
k=[]
v=[]
def create():
    n=int(input("Enter the no. of key elements: "))
    for i in range(n):
        a=int(input())
        k.append(a)
    print("Enter the value of elements")
    for i in range(n):
        b=int(input())
        v.append(b)
        d=dict(zip(k,v))
    print(d)
def add():
    key=input("Enter the key to add: ")
    value=int(input("Enter the value to add"))
    d[key]=value 
    print("After adding: ",d)
def delete():
    x=input("Enter the key to delete")
    if x in d:
        del d[x]
        print("After deleting: ",d)
    else:
        print("Key not found")
def dispaly_keys():
    key=list(d.keys())
    if key:
        print("Keys in dictionary= ",key)
    else:
        print("Dictionary is empty")
def dispaly_values():
    value=list(d.values())
    if value:
        print("values in dictionary= ",value)
    else:
        print("Dictionary is empty")
def remove():
    d.clear()
    print("All elemnts deleted") 
create()
add()
delete()
dispaly_keys()
dispaly_values()
remove()