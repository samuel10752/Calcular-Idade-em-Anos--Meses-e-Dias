# 1) Calcular Idade em Anos, Meses e Dias
def idade_em_anos_meses_dias(dias_totais):
    anos = dias_totais // 365
    meses = (dias_totais % 365) // 30
    dias = (dias_totais % 365) % 30
    return anos, meses, dias

# Exemplo de uso:
dias_totais = int(input("Digite a idade em dias: "))
anos, meses, dias = idade_em_anos_meses_dias(dias_totais)
print("{} anos, {} meses e {} dias".format(anos, meses, dias))
