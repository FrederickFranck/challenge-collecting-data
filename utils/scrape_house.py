import requests

url = "https://www.immoweb.be/en/classified/villa/for-sale/de-haan/8420/9779450?searchId=621dde082ca76"
r = requests.get(url)

if r.status_code == 200:
    j = r.json()
    print("wow")
    #pprint.pprint(j)
    #with open("a.html","w") as file:
    #    file.write(r.text)
        