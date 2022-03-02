from typing import List
import csv
from utils.property import Property
from utils.scrape_house import parse_property
import datetime

start = datetime.datetime.now()


def print_to_csv(properties: List[Property]) -> None:

    with open("test.csv", "w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(Property.header)
        writer.writerows(properties)


# GET URLS FROM SCRAPING
urls = [
    "https://www.immoweb.be/en/classified/villa/for-sale/de-haan/8420/9779450?searchId=621dde082ca76",
    "https://www.immoweb.be/en/classified/apartment/for-sale/liege/4000/9778981?searchId=621dde458e4f5",
    "https://www.immoweb.be/en/classified/house/for-sale/lebbeke/9280/9773744?searchId=621dde458e4f5",
    "https://www.immoweb.be/en/classified/house/for-sale/ronse/9600/9774325?searchId=621dde458e4f5",
    "https://www.immoweb.be/en/classified/apartment/for-sale/schaerbeek/1030/9778701?searchId=621dde458e4f5",
    "https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/braine-lalleud/1420/9778240?searchId=621dde458e4f5",
    "https://www.immoweb.be/en/classified/apartment/for-sale/knokke-heist/8301/9777391?searchId=621dde458e4f5",
    "https://www.immoweb.be/en/classified/apartment/for-sale/gent/9000/9778808?searchId=621dde458e4f5",
]


def main():
    properties = []
    # loop over all links and scrape the data for each one
    # save properties in a list and print them out a csv file

    for url in urls:
        try:
            properties.append(parse_property(url))
        except:
            continue

    print_to_csv(properties)
    end = datetime.datetime.now()
    print(f"Execution time : {(end - start)}")


if __name__ == "__main__":
    main()
