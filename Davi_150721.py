#question2
for item in range(1,21):
    print(item)

#question3
print("3*************************")
for item in range(1,21):
    if item <4:
      print(str(item) +" é menor que 4")
    elif item <8:
        print(str(item) + " is bigger than or equal to 4, but smaller than 8")
    elif item <12:
        print(str(item) + " is bigger than or equal to 8, but smaller than 12")
    elif item <16:
        print(str(item) + " is bigger than or equal to 12, but smaller than 16")
    else:
        print(str(item) + " is bigger than or equal to 16")
    
#question4
print("3***************************")
alien={"planeta":"vênus","idade":47}

#question5
print(alien)

#question6
print("6***************************")
print(alien["idade"])

#question7
print("7***************************")
del alien["planeta"]
print(alien)

#question8
print(alien)

#question9
print("9***************************")
alien["name"]="E.T Bilu"

#question10
print(alien)




