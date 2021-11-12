import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class ExtratorParametro:
    def __init__(self, linha, param, tipo):
        self.param = param
        self._linha = linha
        self.tipo = tipo

    @property
    def linha(self):
        return self._linha

    @linha.setter
    def linha(self, nova_linha):
        self._linha = nova_linha

    def get_residual(self):
        indice_residuos = self._linha.find(",")
        residuo = self._linha[indice_residuos:]
        return residuo

    def valor_residuo(self):
        indice_tipo = self.get_residual().find(self.tipo)
        indice_valor = indice_tipo + len(self.tipo) + 3
        indice_separador = self.get_residual().find(',', indice_valor)
        valor = self.get_residual()[indice_valor:indice_separador]
        return valor


arquivo_log = 'simualcao-teste/log2'
parametro = 'omega'
tipo = 'Initial residual'


def filtra_dados(nome_arquivo, param):
    with open(nome_arquivo) as arquivo:
        for linha in arquivo:
            if param in linha:
                conteudo = ExtratorParametro(linha, param, tipo)
                yield float(conteudo.valor_residuo())



def funcao(i):
    ax.cla()
    y = list(filtra_dados(arquivo_log, 'Uy'))
    print(y)
    ax.semilogy(y)


y = []
fig, ax = plt.subplots()

ani = FuncAnimation(fig, funcao)

fig.tight_layout()
plt.show()
