from time import sleep
from interaction_models.selenium_interaction import SeleniumInteraction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from interaction_models.data_manipulators_aux.aux_manipulator_fb import (
    AuxManipulatorFb,
)
from typing import Union, Dict, List
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as ec


from constants import COMMONS_EXCEPTIONS


class SeleniumFbInteraction(SeleniumInteraction):
    def __init__(self, browser):
        super().__init__(browser)
        self.search()

    def search(self):
        """click on search button"""
        WebDriverWait(self.browser, 12).until(
            ec.presence_of_element_located(
                (By.CSS_SELECTOR, "#guia-form > button:nth-child(5)")
            )
        ).click()

    def accept_cookies(self):
        """click on cookies button"""
        WebDriverWait(self.browser, 12).until(
            ec.presence_of_element_located((By.ID, "cn-accept-cookie"))
        ).click()

    def next_page(self, page):
        """click on next page button, getting new informations"""
        try:
            self.browser.find_element_by_xpath(
                f"//button[contains(text(),'{page}')]"
            ).click()
        except COMMONS_EXCEPTIONS:
            input("Problema ao clicar. Clique e continue...")

    def get_companies_details(self, rawhtml: BeautifulSoup) -> List:
        """click on next page button, getting new informations"""

        companies_in_page = rawhtml.find_all("div", attrs={"class": "modal-body p-4"})
        info_tratadas = []
        for raw_html in companies_in_page:
            company_details = AuxManipulatorFb().return_company_information(raw_html)
            info_tratadas.append(company_details)
        print(info_tratadas)
        return info_tratadas

    def __pegar_html_selenium(self) -> BeautifulSoup:
        """get html"""
        html = self.browser.page_source
        pagina_navegador = BeautifulSoup(html, features="lxml")
        return pagina_navegador

    def initiate(self, page: int) -> Union[Dict, int]:
        try:
            if page == 1:
                self.accept_cookies()
            sleep(2)
            rawhtml = self.__pegar_html_selenium()
            data = self.get_companies_details(rawhtml)
            return {"data": data}
        except COMMONS_EXCEPTIONS:
            return 0
