
## Description
Our program will scrape a real estate website ([Immoweb](https://www.immoweb.be/en)) for data about houses and apartments in Belgium.
Once the information is fetched it will be cleaned and stored in a CSV file.

## Installation
1. Clone the repo
2. Install the libraries
3. Install Selenium WebDriver 
4. Run main.py

Please, follow carefully the [installation manual](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/) for Selenium WebDriver.

## Starting and running
After starting, our program will ask you to select a web driver for Selenium, based on your system. 
You also have to specify how many [search pages](https://www.immoweb.be/en/search/house/for-sale) you want to scrape thus limiting the number of real estate you need to have information about.

Then a Selenium web driver would grab a list of links via the Immoweb search page starting from the most newer real estate.
Fetching information is done with multi-threading to be on par with Selenium scraping. 

## Output
Data would be outputted in (Immoweb_Data_Scraper.csv).

Our program will give these fields about each property: locality, type of property (house or apartment, bungalow, chalet, mansion...), price, type of sale (exclusion or life sale), number of rooms, area, kitchen type, garden, terrace, and swimming pool availability as well as some additional properties.

## Acknowledgements
Thank you,  :)

