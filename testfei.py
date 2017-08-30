import requests
from lxml import etree


sa = 1
ha = 1


# url_sa = "http://app.finance.ifeng.com/list/stock.php?t=sa&f=chg_pct&o=desc&p={pagenum}".format(pagenum=page) for page in range(1, sa + 1)
# url_ha = 'http://app.finance.ifeng.com/list/stock.php?t=ha&f=chg_pct&o=desc&p={pagenum}'.format(pagenum=page) for page in range(1, ha + 1)

# url_sa = []
#
# for page in range(1, sa+1):
#     url_sa.append("http://app.finance.ifeng.com/list/stock.php?t=sa&f=chg_pct&o=desc&p="+str(page))

url_ha = []
for page in range(1, ha+1):
    url_ha.append("http://app.finance.ifeng.com/list/stock.php?t=ha&f=chg_pct&o=desc&p="+str(page))

header = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
}

for url in url_ha:
    r = requests.get(url=url, headers=header, timeout=30)
    html = r.content
    HTMLTree = etree.HTML(html)
    code_list = HTMLTree.xpath('//div[@class="tab01"]//tbody/tr')
    for code in code_list:
        print(code.xpath('./td/a/text()')[1])


# for url in url_sa:
#     r = requests.get(url=url, headers=header, timeout=30)
#     html = r.content
#     HTMLTree = etree.HTML(html)
#     code_list = HTMLTree.xpath('//div[@class="tab01"]//tbody/tr')
#     for code in code_list:
#         print(code.xpath('./td/a/text()')[1])
