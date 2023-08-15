#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def conta_palavras_unicas(frase):
    # Quebra a frase em palavras e remove qualquer pontuação
    palavras = frase.lower().split()
    # Cria um grupo de palavras únicas usando um "set"
    palavras_unicas = set(palavras)
    # Retorna quantas palavras únicas encontramos
    return len(palavras_unicas)






# Teste a sua função aqui (caso ache necessário)











