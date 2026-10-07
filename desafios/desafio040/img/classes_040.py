class Aluno:
    def __init__(self, nome, curso, serie):
        self.nome = nome
        self.curso = curso
        self.serie = serie


class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class XML:
    def exportar(self, dados: list):
        import xml.etree.ElementTree as ET

        nome = dados[0].__class__.__name__.lower()
        pai = ET.Element('dados')
        for item in dados:
            filho = ET.SubElement(pai, nome)
            for chave, valor in item.__dict__.items():
                neto = ET.SubElement(filho, chave)
                neto.text = str(valor)
        ET.indent(pai, space='\t')
        txt = ET.tostring(pai, encoding='unicode', xml_declaration=True)
        return txt


class JSON:
    def exportar(self, dados: list):
        from json import dumps

        lista = []
        for item in dados:
            lista.append(item.__dict__)
        txt = dumps(lista, indent=4, ensure_ascii=False)
        return txt


# Função genérica para converter dados
def exportar_dados(formato, dados: list):
    print(formato.exportar(dados))