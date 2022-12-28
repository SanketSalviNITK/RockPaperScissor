import random
options={1:"Rock",2:"Paper",3:"Scissor"}
s=random.randint(1,3)
cpu=options[s]
print("1. Rock\n2. Paper\n3. Scissor\n")
u=int(input("Select option:"))
user=options[u]
print("CPU:",cpu,"vs User:",user)
print("Result is:",end=" ")
if (s==1 and u==3) or (s==2 and u==1) or (s==3 and u==2):
  print("CPU won")
elif user==cpu:
  print("Draw")
else:
  print("User won")