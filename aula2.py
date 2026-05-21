def calcular_preco_final(preco_original, valor_desconto):
    preco_final = preco_original - valor_desconto
    return preco_final

print(calcular_preco_final(100, 20))