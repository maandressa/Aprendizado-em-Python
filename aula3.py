# Texto original que será criptografado
text = 'Hello World'

# Define o deslocamento (shift) para a cifra de César
shift = 3

# Define o alfabeto que será usado para a criptografia
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Inicializa uma string vazia para armazenar o texto criptografado
encrypted_text = ''

# Loop para percorrer cada caractere do texto original
for char in text.lower():  # Converte o texto para minúsculas para facilitar a criptografia
    # Verifica se o caractere é um espaço
    if char == ' ':
        encrypted_text += char  # Adiciona o espaço ao texto criptografado sem alterá-lo
    # Verifica se o caractere está no alfabeto definido
    elif char in alphabet:
        # Encontra o índice do caractere no alfabeto
        index = alphabet.find(char)
        # Calcula o novo índice após o deslocamento (shift)
        # O operador % (módulo) garante que o índice não ultrapasse o tamanho do alfabeto
        new_index = (index + shift) % len(alphabet)
        # Adiciona o caractere criptografado ao texto final
        encrypted_text += alphabet[new_index]
    # Caso o caractere não esteja no alfabeto (como números ou pontuações)
    else:
        encrypted_text += char  # Mantém o caractere original no texto criptografado
    
    # Exibe o caractere atual e o texto criptografado até o momento
    print('char:', char, 'encrypted text:', encrypted_text)