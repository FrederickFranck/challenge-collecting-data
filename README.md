
# BeCode Data Collection Challenge by:

### [Frederik Franck](https://github.com/FrederickFranck), [Saïf Malkshahi](https://github.com/saifalbaghdadi) and [Lelo Tokwaulu](https://github.com/lelotok)
--------------------------------------------------------------------------------------

## Description
Our program will scrape a real estate website ([Immoweb](https://www.immoweb.be/en)) for data about houses and apartments in Belgium.
Once the information is fetched it will be cleaned and stored in a CSV file.


We have collected data for houses and apartments for sale in Belgium on ImmoWeb.be

How we achieved that?

1. Basically we started by creating class "Property" and all its functions that would 
contain all the elements from the data that a property for sale contain.

2. We wrote the loop to extract from each property every element needed
(locality, rooms, etc..)

3. We wrote a loop to extract from each search page all the property's links.

4. We came up with 2 way to automate the scraping for each search page result one
after another, and we picked the fastest one, 18 min 30 sec for 12.000 links.

5. After checking our code we saved all the data in the .csv file that you can download.

Module used:
------------

- selenium
- webdriver_manager
- geckodrdiver for firefox


## Installation
1. Clone the repo
2. Install the libraries
3. Install Selenium WebDriver 
4. Run main.py

Please, follow carefully the [installation manual](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/) for Selenium WebDriver.

## Starting and running
First our program will collect all the links from the website using selenium and store them in [links.txt](https://github.com/FrederickFranck/challenge-collecting-data/blob/main/links.txt).

After this is will divide the links into chunks of 500 urls and scrape the data for each property. Once all chunks have been scraped its will output the data to a CSV file.

## Output
Data would be outputted in (Immoweb_Data_Scraper.csv).

Our program will give these fields about each property: locality, type of property (house or apartment, bungalow, chalet, mansion...), price, type of sale (exclusion or life sale), number of rooms, area, kitchen type, garden, terrace, and swimming pool availability as well as some additional properties.

## Data

We create a dataset which holds the following columns :

- Locality
- Type of property (House/apartment)
- Subtype of property (Bungalow, Chalet, Mansion, ...)
- Price
- Type of sale (Exclusion of life sales)
- Number of rooms
- Area
- Fully equipped kitchen (Yes/No)
- Furnished (Yes/No)
- Open fire (Yes/No)
- Terrace (Yes/No)
  - If yes: Area
- Garden (Yes/No)
  - If yes: Area
- Surface of the land
- Surface area of the plot of land
- Number of facades
- Swimming pool (Yes/No)
- State of the building (New, to be renovated, ...)

## Files

```main.py```: The Complete Project

### utils

```property.py```: Contains class to store all the data 

```items_urls.py```: Code to scrape all the links of different properties

```scrape_house.py```: Code to scrape the data for each individual property


### data

```links.txt```: Contains all the links scrapped by ```items_urls.py```

```Immoweb_Data_Scraper.csv```: Contains all the [data](#data) formatted as CSV file described in here




Contributions:
--------------

Frederik Frank : 
- Properties Class
- Property data collection

Saïf Malkshahi:
- Search page result automation 
- ReadMe file
- Alternate Scrapper

Lelo Tokwaulu:
- Properties links collection 
- ReadMe file

## Versions 
The Other version made by Saif is availble [here](https://github.com/FrederickFranck/challenge-collecting-data/tree/SAIF#description)


## Acknowledgements
Thank you,  :)

