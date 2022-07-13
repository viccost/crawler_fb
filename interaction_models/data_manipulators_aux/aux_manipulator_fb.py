"""Module to receive text and maniputlate it"""
from typing import Dict
from constants import INFORMATIONS
from interaction_models.data_manipulators_aux.aux_manipulator import AuxManipulator


class AuxManipulatorFb(AuxManipulator):
    @staticmethod
    def cleanhtml(raw_html: str):
        """cleaning up html.
        :param str raw_html: information font, the raw html to be clean"""

        import re

        texto = raw_html.prettify()
        clean_html = re.sub(re.compile("</div>"), "##", texto)
        clean_html = re.sub(re.compile("</.*?>"), "", clean_html)
        clean_html = re.sub(re.compile("<.*?>"), "", clean_html)
        clean_html = re.sub("Endereço:", "", clean_html)
        clean_html = re.sub("Complemento:", "", clean_html)
        clean_html = re.sub("\n", "", clean_html)
        clean_html = re.sub(" +", " ", clean_html)
        return clean_html

    def split_text_to_dict(self, text: str):
        """Split the text in blocks, transforming in dict
        :param str text: information font, the raw html"""
        informations_list = text.split("##")
        companie_dict = {}
        for block in informations_list:
            # extracting and manipulating
            text_block = block.split(":")
            if len(text_block) > 1:
                for index, string in enumerate(text_block):
                    text_block[index] = string.strip()
                key = text_block[0]
                value = text_block[1]
                companie_dict[key] = value
        return companie_dict

    def are_there_all_informations(self, companie_dict: Dict):
        """checks if we have all necessaries informations"""
        for key in INFORMATIONS:
            if key not in companie_dict.keys():
                companie_dict[key] = "Não consta"
        return companie_dict

    def return_company_information(self, companie_data) -> Dict:
        company_information = self.cleanhtml(companie_data)
        company_information = self.split_text_to_dict(company_information)
        company_information = self.are_there_all_informations(company_information)
        return company_information
