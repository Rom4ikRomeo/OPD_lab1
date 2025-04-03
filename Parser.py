from bs4 import BeautifulSoup
import requests


def parse():
    url = 'https://www.omgtu.ru/general_information/faculties'
    page = requests.get(url)
    print(page.status_code)

    soup = BeautifulSoup(page.text, "html.parser")
    block = soup.find_all('div', class_='main__content')

    description = ''
    for data in block:
        all_ul = data.find_all('ul')
        for ul in all_ul:
            description += ul.text.strip() + '\n'

    with open("faculties.txt", "w", encoding="utf-8") as file1:
        file1.write(description)


if __name__ == '__main__':
    parse()