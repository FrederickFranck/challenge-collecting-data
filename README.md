
BeCode Data Collection Challenge by:
Frederik Franck, Saïf Malkshahi and Lelo Tokwaulu
--------------------------------------------------------------------------------------

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

Contributions:
--------------

Frederik Frank : 
- Properties Class
- Property data collection

Saïf Malkshahi:
- Search page result automation 

Lelo Tokwaulu:
- Properties links collection 
- ReadMe file




