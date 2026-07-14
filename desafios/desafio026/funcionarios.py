from abc import ABC, abstractmethod
from rich.panel import Panel
from rich import print

class Funcionario(ABC):
    sal_minimo = 1612
    desc_inss = 7.5

    def __init__(self, nome=None):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        qtd_sal = self.salario / self.sal_minimo

        conteudo = f'O salário de [blue]{self.nome}[/] [purple]({type(self).__name__})[/] é de [green]R${self.salario:.2f}[/] e corresponde a [yellow]{qtd_sal:.1f} salário mínimo[/].' 
        # Para pegar o nome da classe, tambem pode usar 'self.__class__.__name__'

        painel = Panel(conteudo, title=f'Analisando salário', width=50)
        print(painel)


class FucionarioHorista(Funcionario):

    def __init__(self,nome, valor_hora=7.37, horas_trab=220): # Dados de horista no Brasil
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab
        self.sal_bruto = self.valor_hora * self.horas_trab

    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * Funcionario.desc_inss / 100)

    
class FucionarioMensalista(Funcionario):

    def __init__(self, nome, sal_bruto=Funcionario.sal_minimo):
        super().__init__(nome)
        self.sal_bruto = sal_bruto

    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * Funcionario.desc_inss / 100)