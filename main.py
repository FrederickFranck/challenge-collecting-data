import threading
import time
import csv
import datetime
from typing import List
from utils.property import Property
from utils.scrape_house import parse_property
from utils.items_urls import get_links

# Used to calculate Execution Time
# Latest Execution Time (Scrapping Link + Properties) : 18m 37s
start = datetime.datetime.now()


def print_to_csv(properties: List[Property]) -> None:
    """Function which loops over properties and writes them to a CSV file"""

    with open("test.csv", "w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(Property.header)
        writer.writerows(properties)


def read_urls(filename: str) -> List[str]:
    """Read the urls from a txt file instead of scrapping them"""
    file = open(filename, "r")
    content = file.read()
    return content.split("\n")[:-1]


def main():
    """Loop over all links and scrape the data for each one save properties in a list and print them out a csv file"""
    # List of properties
    properties = []
    # List of threads
    threads = []

    print("Scrapping Links")
    urls = get_links("links.txt")
    # urls = read_urls("links.txt")
    print("Scrapping")

    url_chunks = []
    chunk_size = 500
    # Split urls parsing into chunks to avoid disconnects
    for i in range(0, len(urls), chunk_size):
        url_chunks.append(urls[i : i + chunk_size])

    # Loop over chuncks of urls
    for index, urls in enumerate(url_chunks):
        # Loop over each url in the chucnk
        for url in urls:
            # Create a thread to parse the data from each url
            x = threading.Thread(
                target=parse_property,
                args=(
                    url,
                    properties,
                ),
                daemon=True,
            )
            threads.append(x)
            x.start()

        # Wait for all running threads to complete
        for t in threads:
            t.join()

        # Print Progress and Sleep to avoid disconnects
        print(f"CHUNK {index+1}/{len(url_chunks)} DONE")
        print(f"Currently: {len(properties)}properties scrapped")
        time.sleep(2)

    # Print the list of properties to a CSV file
    print("Printing")
    print_to_csv(properties)

    # Calculate Execution Time
    end = datetime.datetime.now()
    print(f"Execution time : {(end - start)}")


if __name__ == "__main__":
    main()
