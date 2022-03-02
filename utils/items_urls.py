from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_links() -> List[str]:
    links_urls = []
    i = 1
    _amount = 12000
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    file = open("links.txt","w",newline='')
    while(len(links_urls) < _amount):
        url = "https://www.immoweb.be/nl/zoeken/huis-en-appartement/te-koop?countries=BE&page={}&orderBy=most_expensive".format(i)

        driver.get(url)

        # target the <a> link in url
        links_collect = driver.find_element(by=By.TAG_NAME, value="a")

        # target the class name of each link items
        elem_class = driver.find_elements(by=By.CLASS_NAME, value="card__title-link")
        for x in elem_class:
            #print(x.get_property("href"))
            file.write(x.get_property("href"))
            file.write("\n")
            links_urls.append(x.get_property("href"))
        
        i += 1
    file.close()
    driver.quit()
    return links_urls
