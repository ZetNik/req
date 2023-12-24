import requests
from bs4 import BeautifulSoup

file = open("result_url.txt", "w")
URL = 'http://www.google.com/search?q='
URL2 = 'https://yandex.com/search/?text='
URL3 = 'https://yandex.ru/search/?text='
URL4 = 'https://yandex.ru/search/?lr=36&text='  # lr - регион
number = 15

# маскировка под браузер
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
USER_AGENT_M = ("Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/59.0.3071.125 Mobile Safari/537.36")
headers = {"user-agent" : USER_AGENT}

quests = ['сейфовая ячейка',
          'арендовать банковскую ячейку',
          'арендовать ячейку',
          'арендовать сейф',
          'арендовать сейфовую ячейку',
          'снять ячейку']

try:
    for query in quests:
        print(query)
        file.write(query + '\n')
        page = requests.get(URL + query)
        # page = requests.get(URL + query, headers=headers)

        if page.status_code == 200:
            i = 0
            soup = BeautifulSoup(page.text, 'html.parser')  # html.text

            for link in soup.find_all('a'):

                if i < number:
                    g = link.get('href')

                    if g.find('url?q=') == True:
                        print(g)
                        file.write(g + '\n')
                        i += 1
                else:
                    break

finally:
    file.close()
