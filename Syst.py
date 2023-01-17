import sys

"""O módulo sys fornece funções e variáveis usadas para manipular diferentes partes do ambiente de tempo de 
execução do Python e apesar de serem completamente diferentes, muitas pessoas confundem o módulo sys e o módulo os (
módulo para manipular o sistema operacional).

Com o módulo sys você pode por exemplo, saber qual a plataforma do dispositivo que está rodando o seu código, 
obter os caminhos de sistema que o interpretador Python utiliza, módulos importados, versão do Python, entre outros."""


print(f"Número de parâmetros: {len(sys.argv)}")
for n, p in enumerate(sys.argv):
    print(f"Parâmetro {n} = {p}")
