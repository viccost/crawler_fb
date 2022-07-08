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

    for page in range(MAX_PAGE):
        cont += 1
        print(cont)

        result = our_interaction.initiate()

        if result != 0:
            output.add_collected_data()
        else:
            # output.add_url_error()
            print("Ocorreu um erro")
        our_interaction.next_page(page)

    output.save_collected_data()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        output.save_collected_data()
