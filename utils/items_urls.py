from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_links(filename) -> List[str]:
    """This function will generate a list of properties from (https://www.immoweb.be) urls and also write the into a txt file"""

    # list to be returned
    links_urls = []
    # Pagenumber for the url
    pagenumber = 1
    # The minimum amount of links we would like to scrape
    # We ask for a little over 10000 so we can lose a few links to 404 & malformed html while scrapping
    _amount = 12000
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)

    # Open the textfile to write the links
    file = open(filename, "w", newline="")

    # Loop until we have the required minimum amount of links
    while len(links_urls) < _amount:
        # Update the pagenumber
        url = "https://www.immoweb.be/nl/zoeken/huis-en-appartement/te-koop?countries=BE&page={}&orderBy=most_expensive".format(
            pagenumber
        )
        # Update webdriver
        driver.get(url)

        # Target the class name of each link items to get all the links
        elem_class = driver.find_elements(by=By.CLASS_NAME, value="card__title-link")
        for link in elem_class:
            # write the link in txt file
            file.write(link.get_property("href"))
            file.write("\n")
            # Append the link to list
            links_urls.append(link.get_property("href"))

        # increment page number
        pagenumber += 1
    # Close file
    file.close()
    # Close selenium driver
    driver.quit()
    return links_urls
