from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\yoyo1\\Desktop\\melee\\develop\\chromedriver_win32\\chromedriver')
driver.implicitly_wait(3)

url = 'http://overwatch.inven.co.kr/overank/rank/all/season5/summary/all/page/1/'


def get_user_url(id, season):
    return 'http://overwatch.inven.co.kr/overank/profile/' + str(id) + '/season/' + str(season)


def get_url_html_soup(url):
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def get_user_list(soup):
    user_data = []
    _list = soup.find_all('td', {'class': 'col1'})
    a = 1
    for i in _list:
        temp_list = []
        for season in range(1, 8):
            temp_list.append(get_user_data(get_user_url(i.find('a').get('data-pidx'), season+1)))
        user_data.append(temp_list)
        print(a)
        a += 1
    return user_data


def get_user_data(url):
    soup = get_url_html_soup(url)
    top_data = soup.find('div', {'class': 'bb_dataBox'})
    return top_data


user_url_list = get_user_list(get_url_html_soup(url))
user_data_list = []
data_list = []
for i in range(len(user_url_list)):
    for k in range(len(user_url_list[i])):
        # index 0: 최고점수, 1: 총 게임 수, 2: 승률, 3: KDA
        for j in range(4):
            data = user_url_list[i][k].find_all('div', {'class': 'bb_topData'})

            if len(data) == 3 or data[1].find('span').get_text() == '0':  # 빠대 전적 or 언랭
                break

            data_list.append(data[j+1].find('span').get_text())

    data_list.append('\n')  # 플레이어간 구분

index = 0
for i in range((len(data_list) - 49) // 4):  # 수정필요 3/2
    if data_list[index] == '\n':
        index = index+1
    print(data_list[index:index+5])
    index = index + 4





