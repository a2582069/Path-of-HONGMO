from bs4 import BeautifulSoup
import requests
import re

def get_url(url):
    zz1 = re.compile('.*m/(.*)')
    zz2 = re.compile('\w*[^\s,]')
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    start_urls = [url.format(pn) for pn in range(1,84)]
    for start_url in start_urls:
        html = requests.get(start_url,headers=headers).text
        soup = BeautifulSoup(html,'lxml')
        #print html
        for item in soup.find_all(class_='albumfaceOutter'):
            print item.img['alt']
            ccc = re.findall(zz1,item.a['href'])
            htmlpage = requests.get(item.a['href'],headers=headers).text
            soup2 = BeautifulSoup(htmlpage, 'lxml')
            #page 2
            htmlpage1 = requests.get(item.a['href'] + '?page=2', headers=headers).text
            soup2_1 = BeautifulSoup(htmlpage1, 'lxml')
            for itempage in soup2.findAll(class_='personal_body'):
                numbs = re.findall(zz2,itempage['sound_ids'])
                ypnum = 0
                for numb in numbs:
                    ypnum = ypnum + 1
                    #get json
                    html2 = 'http://www.ximalaya.com/tracks/{}.json'
                    html3 = html2.format(numb)
                    getjson = requests.get(html3,headers=headers).json()
                    print getjson.get('play_path_32')
                print str(ypnum)+''
            #print htm3
'''albumfaceOutter'''

if __name__ == '__main__':
    start_url = 'http://www.ximalaya.com/dq/book/{}'
    get_url(start_url)