x = ["a","b","c"]

i = 0
while i < len(x):
    print(f"{i} --- {x[i]}")
    i += 1


print("====================================")




i = 0
while i != len(x):
     print(f"{i} --- {x[i]}")
     i += 1




print("====================================")



for el in x:
      print(el)


print("====================================")




for sdfvbgearwgawergi,verywrthywetrhwerthw in enumerate(x):
    print(f"{sdfvbgearwgawergi}  ----- {verywrthywetrhwerthw}")



print("====================================")




for i in range(len(x)):
      print(f"{i}  ----- {x[i]}")




print("====================================")




for i in range(3):
    print(i)


for _ in range(3):
     print("Hej hej")


for i in range(2,12,2):
     print(i)




print("====================================")






import time





x = []
i = 0
while i <= 10:
     print(f"{i}  ---- {x} ----- {i}<10 =? {i<10}")
     time.sleep(2)
     x.append(2**i)
     i += 1
print(x)




x = []
i = 0
while i != 11:
     x.append(2**i)
     i += 1
print(x)



x = []
for i in range(11):
     x.append(2**i)
print(x)



from random import randint




x = []
i = 0
while i != 10:
     x.append(randint(1,10))
     i += 1
print(x)
print(len(x))




x = []
for _ in range(10):
     x.append(randint(1,10))
print(x)
print(len(x))




from random import randint





x = []
while len(x) != 10:
   k = randint(1,1000000)
   if k % 5 == 0 and k % 13 == 0:
       x.append(k)


from random import randint
x = []
while len(x) != 10:
   k = randint(1,1000000)
   if k % 5 == 0 and k % 13 == 0 and k not in x:
       x.append(k)




