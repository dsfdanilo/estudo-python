#Formatação de floats
print("R$ {:f}".format(1.59))

print("R$ {:.2f}".format(1.59))

print("R$ {:.2f}".format(1.5))

print("R$ {:.2f}".format(1234.50))

print("R$ {:07.2f}".format(1.5))

#Formatação de inteiros
print("R$ {:07d}".format(5))

#Exemplo prático
print("Data {:02d}/{:02d}".format(9, 4))

#Padrão americano de nome
print("Ola Sr.{1} {0}".format("Cordeiro","Leonardo"))