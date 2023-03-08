def numeg(x:str,d:dict):
    x=list(x)
    it=list(d.items())
    arv=0
    for o in it:
        for p in o[1]:
            for i in x:
                if i==p:
                    arv+=o[0]
    arv=sum(list(map(int,list(str(arv)))))
    while len(list(str(arv)))>1:
           arv=sum(list(map(int,list(str(arv)))))
    print(f"Ваша цифра - {arv}")
    with open(f"{arv}.txt","r",encoding="utf-8-sig") as f:
        for line in f:
            print(line)
    return arv 

def salv(x:str,y:int,lis:list): 
    lis.append(x.title()+"-"+str(y)+"\n") 
    with open("nimed.txt","w",encoding="utf-8-sig") as f:
        f.writelines(lis) 
    return lis
