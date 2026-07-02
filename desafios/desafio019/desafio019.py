# Crie uma classe livro, que vai simular passagem de paginas de um livro.
# Conciderando tambem  se o usúario chegou ao fim da leitura.

from rich import print
import time

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1

        print(f':open_book: [blue]Você acabou de abrir o livro [red]"{self.titulo}"[/] que tem [green]{self.total_paginas} páginas[/] no total. Você agora está na [yellow]página {self.pagina_atual}[/][/]')

    def avancar_pagina(self, qtd=1):
        contador = 0
        for pg in range(0, qtd, 1):
            if not self.fim_livro():
                self.pagina_atual += 1
                print(f'Pág{self.pagina_atual} :arrow_forward: ', end='')
                time.sleep(0.2)
                contador += 1
        print(f'[blue]Você avançou [green]{contador} páginas[/], agora está na [yellow]página {self.pagina_atual}[/][/]')
        if self.fim_livro():
            print(f':closed_book: [red]Você chegou ao fim do livro "{self.titulo}"[/]')

    
    def fim_livro(self):
        return True if self.pagina_atual > self.total_paginas else False

# Exemplo de uso
# Criando instâncias
l1 = Livro('Copa do Mundo', 20)

# Imprimindo
l1.avancar_pagina(10)
l1.avancar_pagina(5)
l1.avancar_pagina(50)