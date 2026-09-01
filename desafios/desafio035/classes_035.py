from abc import ABC, abstractmethod

class Arquivo(ABC):
    def __init__(self, nome: str, ext: str, tam: int=0):
        self._nome = nome
        self._extencao = None                            
        self.tam = tam    
        self.extensao = ext

    @abstractmethod
    def abrir(self):
        pass

    @property
    def extensao(self):
        return self._extencao

    @extensao.setter
    def extensao(self, ext: str):
        formatos = ['pdf', 'doc','docx']
        if ext in formatos:
            self._extencao = ext
        else:
            raise AttributeError('O arquivo está no formato inválido.')

    @property
    def nome_completo(self):
        return f'"{self._nome}.{self.extensao}"({self.tam/1_000_000}MB)'


class PDF(Arquivo):
    def __init__(self, nome: str, tam: int):
        super().__init__(nome, 'pdf', tam)

    def abrir(self):
        print(f'Abrir o arquivo {self.nome_completo} no Adobe Acrobat Reader.')


class DOC(Arquivo):
    def __init__(self, nome: str, tam: int):
        super().__init__(nome, 'docx', tam)

    def abrir(self):
        print(f'Abrir o arquivo {self.nome_completo} no Microsoft Word.')


def abrir_arquivo(arquivo: Arquivo):
    arquivo.abrir()