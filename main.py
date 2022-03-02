from typing import List
import csv
from utils.property import Property
from utils.scrape_house import parse_property
from utils.items_urls import get_links


def print_to_csv(properties: List[Property]) -> None:

    with open("test.csv", "w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(Property.header)
        writer.writerows(properties)

def main():
    properties = []
    # loop over all links and scrape the data for each one
    # save properties in a list and print them out a csv file
    urls = get_links()

    for url in urls:
        try:
            properties.append(parse_property(url))
        except:
            continue

    print_to_csv(properties)


if __name__ == "__main__":
    main()
