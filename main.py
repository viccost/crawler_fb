from selenium import webdriver
from chrome_options import ChromeOptions
from interaction_models.selenium_interaction_fb import SeleniumFbInteraction
from output_data import SpreadsheetOutputData
from constants import MAX_PAGE, URL


def iniciar_chrome() -> webdriver.Chrome:
    chrome_options = ChromeOptions().chrome_options
    driver = webdriver.Chrome(options=chrome_options)
    return driver


output = SpreadsheetOutputData()


def main():
    chrome = iniciar_chrome()
    cont = 0
    # settings
    interaction_model = SeleniumFbInteraction
    # settings
    chrome.get(URL)
    our_interaction = interaction_model(chrome)

    for page in range(1, MAX_PAGE):
        print(page)

        result = our_interaction.initiate(page)

        if result != 0:
            for company_information in result["data"]:
                nome_fantasia = company_information["Nome Fantasia"]
                cnpj = company_information["CNPJ"]
                inscricao_estadual = company_information["Inscrição Estadual"]
                telefones = company_information["Telefones"]
                email = company_information["E-mail"]
                site = company_information["Site"]
                atividade_economica = company_information["Atividade Econômica"]
                lista_produtos = company_information["Lista de Produtos"]
                lista_insumos = company_information["Lista de Insumos"]
                num_funcionarios = company_information["Número total de Funcionários"]
                logradouro = company_information["Logradouro"]
                bairro = company_information["Bairro"]
                municipio = company_information["Município"]
                estado = company_information["Estado"]
                cep = company_information["CEP"]

                output.add_collected_data(
                    nome_fantasia,
                    cnpj,
                    inscricao_estadual,
                    telefones,
                    email,
                    site,
                    atividade_economica,
                    lista_produtos,
                    lista_insumos,
                    num_funcionarios,
                    logradouro,
                    bairro,
                    estado,
                    municipio,
                    cep,
                    page,
                )
        else:
            output.add_url_error()
            print("Ocorreu um erro")

        our_interaction.next_page(page)

    output.save_collected_data()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        output.save_collected_data()
