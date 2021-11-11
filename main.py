import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

arquivo_log = 'simualcao-teste/log2'
parametro = 'omega'


def carrega_dados(nome_arquivo, param):
    with open(nome_arquivo) as arquivo:
        for linha in arquivo:
            if param in linha:
                valor = linha.split(',')[2].split('=')[1]
                yield float(valor)
            if 'str' in linha:
                break


def funcao(i):
    ax.cla()
    y = list(carrega_dados(arquivo_log, 'Uy'))
    print(y)
    ax.semilogy(y)

y = []
fig, ax = plt.subplots()

ani = FuncAnimation(fig, funcao)

fig.tight_layout()
plt.show()
