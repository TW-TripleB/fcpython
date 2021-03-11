import random
dicT=[]
while len(dicT)<6:
    Ran=random.randint(1,49)
    if Ran not in dicT:
        dicT.append(Ran)
print(dicT)