
end=int(input("deger giriniz:"))
sum=0
start=2
for j in range(start,end+1):
    c=0
    for i in range(1,j+1):
        if(j%i==0):
            c=c+1
    if(c==2):
        sum=sum+j
    else:
        pass
print(end,"sayisina kadarki asal sayilar toplami",sum)