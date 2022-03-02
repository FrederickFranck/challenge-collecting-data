import threading
import time
from typing import List
import csv
from utils.property import Property
from utils.scrape_house import parse_property
import datetime
from utils.items_urls import get_links

start = datetime.datetime.now()

def print_to_csv(properties: List[Property]) -> None:

    with open("test.csv", "w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(Property.header)
        writer.writerows(properties)

def read_urls(filename:str) -> List[str]:
    file = open(filename,'r')
    content = file.read()
    return content.split("\n")[:-1]
    

def main():
    properties = []
    threads = []
    # loop over all links and scrape the data for each one
    # save properties in a list and print them out a csv file
    print("Scrapping Links")
    #urls = get_links()
    urls = read_urls("links.txt")
    print("Scrapping")


    url_chunks = []
    chunk_size = 500
    #Split urls parsing into chunks to avoid disconnects
    for i in range(0, len(urls),chunk_size):
        url_chunks.append(urls[i:i+chunk_size])

    for index, urls in enumerate(url_chunks):
        for url in urls:
            #parse_property(url,properties)
            x = threading.Thread(target=parse_property, args=(url,properties,), daemon=True)
            threads.append(x)
            x.start()

        for t in threads:
            t.join()
        print(f"CHUNK {index}/{len(url_chunks)} DONE")
        time.sleep(2)

    print("Printing")
    print_to_csv(properties)
    end = datetime.datetime.now()
    print(f"Execution time : {(end - start)}")


if __name__ == "__main__":
    main()
