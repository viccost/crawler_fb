from abc import ABC
from selenium.webdriver import Keys
from time import sleep
from interaction_models.selenium_interaction import SeleniumInteraction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    ElementNotInteractableException,
    TimeoutException,
    NoSuchElementException,
    StaleElementReferenceException,
)
from interaction_models.data_manipulators_aux.aux_manipulator_fb import (
    AuxManipulatorFb,
)
from typing import Union, Dict
from bs4 import BeautifulSoup

commons_exceptions = (
    ec.NoSuchElementException,
    ElementNotInteractableException,
    TimeoutException,
    NoSuchElementException,
    StaleElementReferenceException,
)


class SeleniumFbInteraction(SeleniumInteraction):
    def __init__(self, browser):
        super().__init__(browser)

    def search(self):
        WebDriverWait(self.browser, 12).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "#guia-form > button:nth-child(5)"))
        ).click()

    def next_page(self, page):
        self.browser.find_element_by_xpath(f"//button[contains(text(),'{page}')]").click()

    def get_companies_details(self, rawhtml: BeautifulSoup) -> Dict:
        companies_in_page = rawhtml.find_all('div', attrs={'class': 'modal-body p-4'})
        info_tratadas = []
        for raw_html in companies_in_page:
            company_details = AuxManipulatorFb().return_company_information(raw_html)
            info_tratadas.append(company_details)
        print(info_tratadas)
        return info_tratadas

    def __pegar_html_selenium(self) -> BeautifulSoup:
        html = self.browser.page_source
        pagina_navegador = BeautifulSoup(html, features="lxml")
        return pagina_navegador

    def initiate(self) -> Dict:
        #try:
            self.search()
            sleep(2)
            rawhtml = self.__pegar_html_selenium()
            data = self.get_companies_details(rawhtml)
            return {"data": data}
        #except commons_exceptions:
         #   return 0
