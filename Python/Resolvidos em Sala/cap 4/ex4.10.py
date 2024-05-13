import re

frase = str(input("Digite uma frase: "))

# o, os, a, as, uma, umas, um, uns
artigos = r'\b(o|a|os|as|um|uma|uns|umas|e|à)\b'
nova_frase = re.sub(artigos, "", frase)

while nova_frase.find("  ") >= 0: 
    nova_frase = nova_frase.replace("  ", " ")

print(f"Nova frase:{nova_frase}")