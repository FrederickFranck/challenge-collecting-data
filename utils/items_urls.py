from selenium import webdriver
from selenium.webdriver.common.by import By


url = "https://www.immoweb.be/fr/recherche/maison/a-vendre/gent/arrondissement?countries=BE&page=1&orderBy=relevance"
links_urls = []
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(url)

# target the <a> link in url
links_collect = driver.find_element(by=By.TAG_NAME, value="a")

# target the class name of each link items
elem_class = driver.find_elements(by=By.CLASS_NAME, value="card__title-link")
for x in elem_class:
    print(x.get_property("href"))
driver.quit()
