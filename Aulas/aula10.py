#STRINGS e Métodos
# .islower .isupper    (TRUE or FALSE)
# .lower / .upper (lowercase or uppercase)
# .capitalize() .replace() .tittle()  .count()
# .startswith() .endswith()   (TRUE or FALSE)
# .find(x) .rfind(x)
# .strip()
# .isdigit() .isalnum() .isalpha()

super_man = "     socorraM me subi no onibus em marrocos     "
print(super_man[::-1])


print(super_man.strip())
print(super_man.lower().strip().endswith("marrocos"))


print(super_man.rfind("u"))   #Encontra a maior ou menor (.find()) posicao da string. Opcional: fornecer o intervalo

print("josue\tcleyton".expandtabs(int(58)))