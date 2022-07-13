"""class that defines the output format off collected data"""

from pandas import DataFrame
import salvar_ajustar.salvar_ajustar as sv


class SpreadsheetOutputData:
    """class that defines the output format off collected data"""

    def __init__(self):
        self.dataFrameDict = {
            "Nome Fantasia": [],
            "CNPJ": [],
            "Inscrição Estadual": [],
            "Telefones": [],
            "E-mail": [],
            "Site": [],
            "Atividade Econômica": [],
            "Lista de Produtos": [],
            "Lista de Insumos": [],
            "Número total de Funcionários": [],
            "Logradouro": [],
            "Bairro": [],
            "Estado": [],
            "Município": [],
            "CEP": [],
            "Page": [],
        }

    @staticmethod
    def getdata():
        from datetime import datetime

        return datetime.now().strftime("%d-%m-%Y %H-%M-%S")

    def add_url_error(self, page: int) -> None:
        error_message = "problem checking"
        self.dataFrameDict["Nome Fantasia"].append(error_message)
        self.dataFrameDict["CNPJ"].append(error_message)
        self.dataFrameDict["Inscrição Estadual"].append(error_message)
        self.dataFrameDict["Telefones"].append(error_message)
        self.dataFrameDict["E-mail"].append(error_message)
        self.dataFrameDict["Site"].append(error_message)
        self.dataFrameDict["Atividade Econômica"].append(error_message)
        self.dataFrameDict["Lista de Produtos"].append(error_message)
        self.dataFrameDict["Lista de Insumos"].append(error_message)
        self.dataFrameDict["Número total de Funcionários"].append(error_message)
        self.dataFrameDict["Logradouro"].append(error_message)
        self.dataFrameDict["Bairro"].append(error_message)
        self.dataFrameDict["Estado"].append(error_message)
        self.dataFrameDict["Município"].append(error_message)
        self.dataFrameDict["CEP"].append(error_message)
        self.dataFrameDict["Page"].append(page)

    def add_collected_data(
        self,
        nome_fantasia,
        cnpj,
        inscricao_estadual,
        telefones,
        email,
        site,
        atividade_economica,
        lista_de_produtos,
        lista_de_insumos,
        numero_total_de_funcionarios,
        logradouro,
        bairro,
        estado,
        municipio,
        cep,
        page,
    ) -> None:
        self.dataFrameDict["Nome Fantasia"].append(nome_fantasia)
        self.dataFrameDict["CNPJ"].append(cnpj)
        self.dataFrameDict["Inscrição Estadual"].append(inscricao_estadual)
        self.dataFrameDict["Telefones"].append(telefones)
        self.dataFrameDict["E-mail"].append(email)
        self.dataFrameDict["Site"].append(site)
        self.dataFrameDict["Atividade Econômica"].append(atividade_economica)
        self.dataFrameDict["Lista de Produtos"].append(lista_de_produtos)
        self.dataFrameDict["Lista de Insumos"].append(lista_de_insumos)
        self.dataFrameDict["Número total de Funcionários"].append(
            numero_total_de_funcionarios
        )
        self.dataFrameDict["Logradouro"].append(logradouro)
        self.dataFrameDict["Bairro"].append(bairro)
        self.dataFrameDict["Estado"].append(estado)
        self.dataFrameDict["Município"].append(municipio)
        self.dataFrameDict["CEP"].append(cep)
        self.dataFrameDict["Page"].append(page)

    def save_collected_data(self) -> None:
        dataFrame = DataFrame.from_dict(self.dataFrameDict)
        sv.salvar_arquivo_planilha(dataFrame, f"Scrape {self.getdata()}", "xlsx")
