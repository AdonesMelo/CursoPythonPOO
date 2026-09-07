from abc import ABC, abstractmethod
import locale

class Pagamento(ABC):
    def __init__(self):
        self._valor = None

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        if valor > 0:
            self._valor = valor
        else:
            raise AttributeError('O pagamento só pode ser positivo.')

    @property
    def fvalor(self):
        #return f'Pagamento CONFIRMADO de R$ {self._valor:,.2f}'
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return locale.currency(self._valor, grouping=True, symbol=True, international=False)

    @abstractmethod
    def pagar(self, valor: float):
        pass


class Boleto(Pagamento):
    def pagar(self, valor: float):
        try:
            self.valor = valor
            # Codigo para efetuar o pagamento...
            return f'Pagamento CONFIRMADO de {self.fvalor} via Boleto Bancário.'
        except Exception as e:
            return f'Falha no pagamento {self.fvalor} via Boleto Bancário! {e}'


class Pix(Pagamento):
    def pagar(self, valor: float):
        try:
            self.valor = valor
            # Codigo para efetuar o pagamento...
            return f'Pagamento CONFIRMADO de {self.fvalor} via Pix.'
        except Exception as e:
            return f'Falha no pagamento {self.fvalor} via Pix! {e}'


class Credito(Pagamento):
    def pagar(self, valor: float):
        try:
            self.valor = valor
            # Codigo para efetuar o pagamento...
            return f'Pagamento CONFIRMADO de {self.fvalor} via Cartão de Crédito.'
        except Exception as e:
            return f'Falha no pagamento {self.fvalor} via Cartão de Crédito! {e}'


# Função genérica para pagar
def finalizar_compra(tipo_pag: Pagamento, valor: float):
    print(tipo_pag.pagar(valor))