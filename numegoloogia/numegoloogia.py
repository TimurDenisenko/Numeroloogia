from numod import *

x1=["а","и","с","ъ"]
x2=["б","й","т","ы"]
x3=["в","к","у","ь"]
x4=["г","л","ф","э"]
x5=["д","м","х","ю"]
x6=["е","н","ц","я"]
x7=["ё","о","ч"]
x8=["ж","п","ш"]
x9=["з","р","щ"]
lis=[]
numelog={1:x1,2:x2,3:x3,4:x4,5:x5,6:x6,7:x7,8:x8,9:x9}
while True:
    menu=input("""1-Vaata nimed 
2-Uurige oma numbrit
3-Selged nimed
""")
    if menu=="1":
        with open("nimed.txt","r",encoding="utf-8-sig") as f:
            for line in f:
                print(line)
    elif menu=="2":
        nimi=input("Kirjutage sinu nimi ").lower()
        if nimi.isalpha():
            arv=numeg(nimi,numelog) 
            lis=salv(nimi,arv,lis)
    elif menu=="3":
        with open("nimed.txt","w",encoding="utf-8-sig") as f:
            f.writelines("")