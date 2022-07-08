"""Module to receive text and maniputlate it"""
from typing import List

from interaction_models.data_manipulators_aux.aux_manipulator import AuxManipulator


class AuxManipulatorFb(AuxManipulator):
    @staticmethod
    def cleanhtml(raw_html: str):
        """Transform the html.
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

    def return_company_information(self, companie_data) -> List:
        companie_information = self.cleanhtml(companie_data)
        companie_information = self.split_text_to_dict(companie_information)
        return companie_information
