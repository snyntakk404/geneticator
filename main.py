import random
import os

gene_poss = "q w e r t y u i o p a s d f g h j k l z x c v b n m".split(" ")

genes = random.choice(gene_poss)

input("Start? [CLICK ENTER]\n")
os.system("clear")

print(genes)

input("[CLICK ENTER]\n")

while True:
  os.system("clear")

  genes = genes + random.choice(gene_poss)

  print(genes)

  step = input("Continue? [Y/N]\n")
  if step.upper() == "Y":
    continue
  else:
    break