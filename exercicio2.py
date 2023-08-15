#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def is_anagram(string1, string2):
    # Convertendo as strings para letras minúsculas e removendo espaços em branco
    string1 = string1.lower().replace(" ", "")
    string2 = string2.lower().replace(" ", "")
    # Verificando se as strings são anagramas ao ordenar seus caracteres
    return sorted(string1) == sorted(string2)






# Teste a sua função aqui (caso ache necessário)











