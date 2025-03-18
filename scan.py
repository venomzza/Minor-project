
import requests
from bs4 import BeautifulSoup
import sysfrom urllib.parse import urljoin

s = requests.Session()
s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
#function to get all form
def get_form(url):
    soup = BeautifulSoup(s.get(url).content, "html.parser")
    return soup.find_all("form")
def form_details(form):
    detailsofForm = {}
    action = form.attrs.get("action")
    method = form.attrs.get("method", "get")
    inputs = []