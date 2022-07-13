from dotenv import load_dotenv
from os import getenv
from selenium.common.exceptions import (
    ElementNotInteractableException,
    TimeoutException,
    NoSuchElementException,
    StaleElementReferenceException,
    ElementClickInterceptedException,
)
from selenium.webdriver.support import expected_conditions as ec

load_dotenv()

HEADER = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/83.0.4103.97 Safari/537.36 "
}

MAX_PAGE = 712
URL = getenv("URL")

COMMONS_EXCEPTIONS = (
    ec.NoSuchElementException,
    ElementNotInteractableException,
    TimeoutException,
    NoSuchElementException,
    StaleElementReferenceException,
    ElementClickInterceptedException,
)

INFORMATIONS = [
    "Nome Fantasia",
    "CNPJ",
    "Inscrição Estadual",
    "Telefones",
    "E-mail",
    "Site",
    "Atividade Econômica",
    "Lista de Produtos",
    "Lista de Insumos",
    "Número total de Funcionários",
    "Logradouro",
    "Bairro",
    "Estado",
    "Município",
    "CEP",
]
