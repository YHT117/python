import urllib.request  
import http.cookiejar
from lxml import etree

head = {  
    'Connection': 'Keep-Alive',  
    'Accept': 'text/html, application/xhtml+xml, */*',  
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',  
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'  
}
def makeMyOpener(head):  
    cj = http.cookiejar.CookieJar()  
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))  
    header = []  
    for key, value in head.items():  
        elem = (key, value)
        header.append(elem)  
    opener.addheaders = header  
    return opener

oper = makeMyOpener(head)
uop = oper.open('http://localhost:8000/loginpanel', timeout = 1000)
data = uop.read()  
html = data.decode()
#print(html)
#lxml提取
selector = etree.HTML(html)
links = selector.xpath('//form/input[@name="csrfmiddlewaretoken"]/@value')
for link in links:
	csrfmiddlewaretoken = link
	print(link)
url = 'http://localhost:8000/users/userLogin'
datas = {'csrfmiddlewaretoken':csrfmiddlewaretoken,'email':'aa','pwd':'aa'}
data_encoded = urllib.parse.urlencode(datas).encode(encoding='utf-8')
response = oper.open(url, data_encoded)
content = response.read()
html = content.decode()
print(html)