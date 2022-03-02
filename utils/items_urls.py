from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_links() -> List[str]:
    links_urls = []
    i = 1
    
    
    while(len(links_urls) < 100):
        url = "https://www.immoweb.be/nl/zoeken/huis-en-appartement/te-koop?countries=BE&page={}&orderBy=relevance".format(i)
        driver = webdriver.Firefox()
        driver.implicitly_wait(30)
        driver.get(url)

        # target the <a> link in url
        links_collect = driver.find_element(by=By.TAG_NAME, value="a")

        # target the class name of each link items
        elem_class = driver.find_elements(by=By.CLASS_NAME, value="card__title-link")
        for x in elem_class:
            #print(x.get_property("href"))
            links_urls.append(x.get_property("href"))
        driver.quit()
        i += 1
    return links_urls
