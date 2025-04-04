# para imprimir uma letra embaixo da outra
print('A','L','U','R','A',sep='\n')

# diferentes formas de imprimir textos
# Criação das Variáveis
nome = 'Karol'
idade = 34

# Abordagem mais simples
print('Meu nome é',nome,'e tenho',idade,'anos.')

# Abordagem do f-string
print(f'Meu nome é {nome} e tenho {idade} anos.')

# Abordagem do .format()
print('Meu nome é {} e tenho {} anos.'.format(nome,idade))

# Abordagem da % (Formatação de String Antiga - Python 2)
print('Meu nome é %s e tenho %i anos.'%(nome,idade))

# diferentes formas de imprimir o número de PI
pi = 3.14159

# Abordagem de f-string
print(f'O valor arredondado de pi é: {pi:.2f}')

# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}'.format(pi))

# Utilizando a função round()
print('O valor arredondado de pi é:', round(pi, 2))


# MODULO 2
# match expressão:
    # case padrão_1:
        # Código a ser executado se expressão corresponder a padrão_1
    # case padrão_2:
        # Código a ser executado se expressão corresponder a padrão_2
    # ... outros casos ...
    # case _:
        # Código a ser executado se nenhum dos padrões anteriores corresponder. Isso é útil para tratar casos não específicos.

def classificar_musica(genero_favorito, genero_musica):
    if genero_favorito == genero_musica:
        return 'recomendada'
    elif genero_favorito == 'Pop' or genero_favorito == 'Rock':
        return 'neutra'
    else:
        return 'não recomendada'

resultado = classificar_musica('Rock', 'Pop')
print(resultado)