import requests
from bs4 import BeautifulSoup
import js2py

# token2 = js2py.eval_js("""
# function randomString(len) {
#   var str = "";
#   for (var i = 0; i < len; i++) {
#     var rand = Math.floor(Math.random() * 62);
#     var charCode = rand += rand > 9 ? (rand < 36 ? 55 : 61) : 48;
#     str += String.fromCharCode(charCode);
#   }
#   return str;
# }
# """)


def cars(url ="https://bidfax.info/"):
    # aes_js = "https://bidfax.info/aes.min.js"
    parse_url="https://bidfax.info/bmw/x1/f/from-year=2017/to-year=2018/"
    headers = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
               "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/97.0.4692.99 Safari/537.36",
               "cookie": "PHPSESSID=b376e91a2233f3268b6af391e3454607; _ga=GA1.2.131394243.1635970187; FORT=e3e2f08d2bce43221c8464d33feb32ee; _gid=GA1.2.2063647082.1643917666"}
    response = requests.get(parse_url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)


cars()
