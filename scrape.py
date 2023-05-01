import requests
from bs4 import BeautifulSoup

def getShreeMarutiTable(request):
    url = "https://shreemaruti.com/network-map/"

    payload = {
        "_csrf-frontend" : "",
        "wpsl_search_input_pid": "",
        "wpsl-search-inputp": request.args.get('pincode')
    }

    r = requests.post(url,data = payload)

    soup = BeautifulSoup(r.text,'html.parser')

    table_html = str(soup.find_all("table", class_="table_shippment"))

    return table_html
