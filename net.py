file1=open('1.txt', "r", encoding="utf-8")
kol1=0
str1=""
for line1 in file1:
  kol1+=1
  str1+="Файл 1 строка "+str(kol1) + " - " + line1 
  
file2=open('2.txt', "r", encoding="utf-8")
kol2=0
str2=""
for line2 in file2:
  kol2+=1
  str2+="Файл 2 строка "+str(kol2) + " - " + line2
  
file3=open('3.txt', "r", encoding="utf-8")
kol3=0
str3=""
for line3 in file3:
  kol3+=1
  str3+="Файл 3 строка "+str(kol3) + " - " + line3

def itog1():
  print('1.txt')
  print(kol1)
  print(str1)

def itog2():
  print('2.txt')
  print(kol2)
  print(str2)

def itog3():
  print('3.txt')
  print(kol3)
  print(str3)

if kol1<kol2 and kol1<kol3:
  itog1()
  if kol2<kol3:
    itog2()
    itog3()
elif kol2<kol1 and kol2<kol3:
  itog2()
  if kol1<kol3:
    itog1()
    itog3()
elif kol3<kol1 and kol3<kol2:
  itog3()
  if kol1<kol2:
    itog1()
    itog2()
