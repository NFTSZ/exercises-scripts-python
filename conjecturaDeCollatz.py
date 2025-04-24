from random import randint

passos = []
c0 = 8
passos.append(c0)

while c0 > 1:
    if c0 % 2 == 0:
      c0 = c0 / 2
    else:
      c0 = 3 * c0 + 1
    passos.append(int(c0))

print(passos)
print(f"Etapas: {len(passos)}")
