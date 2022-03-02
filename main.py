import time
from utils.csv_data import raw_to_csv
from utils.fetch_data import fetching_urls, fetching_data, FetchThread, select_driver
from selenium import webdriver
from threading import Thread
from bs4 import BeautifulSoup
import requests


threads = list()

def main():
    # Here the user enters the browser name, or the default browser will be Firefox
    driver_name = input("Select Your webdriver: chrome or firefox: ")
    driver = select_driver(driver_name)

    n = int(input("Enter the number of search pages for homes and apartments, between (1 to 333 pages): "))

    start = time.time()

    for property_type in ("house", "apartment"):
        i = 1
        while i <= n:
            url = f"https://www.immoweb.be/en/search/{property_type}/for-sale?countries=BE&page={i}&orderBy=newest"
            urls = fetching_urls(url, driver)

            t = FetchThread(name='Test_{}'.format(i), target=fetching_data, args=(urls,))
            t.start()    # fetching_data(urls)

            threads.append(t)
            time.sleep(0.1)
            print(f"{property_type} batch number {i} : DONE")
            i += 1

    print(time.time() - start)
    data = []

    for thread in threads:
        while thread.is_alive():
            time.sleep(0.5)
        data.extend(thread.data)
        print(f"Thread of length {len(thread.data)} completed")

    print(time.time() - start)
    driver.close()

    raw_to_csv(data)

if __name__ == '__main__':
    main()
