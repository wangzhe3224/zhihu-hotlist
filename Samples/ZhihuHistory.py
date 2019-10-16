import requests
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
import json

from bs4 import BeautifulSoup


def parseHotList(content: str) -> [{}]:
    """ parse content from 'http://duzhihu.cc/date/{date}'

    :param content:
    :return:
        results.append({
            "question": question.contents[1]['href'].strip(),
            "answer": first.contents[1]['href'].strip(),
            "content": question.text
        })
    """
    soup = BeautifulSoup(content, 'html.parser')
    divs = soup.findAll("div", class_='answer_item')
    results = []

    for div in divs:
        _, user, _, question, _, first, _ = div.contents
        results.append({
            "question": question.contents[1]['href'].strip(),
            "answer": first.contents[1]['href'].strip(),
            "content": question.text
        })

    return results


def hotListWorker(date: str):
    """

    :param date:
    :return:
    """
    print('Processing ', date)
    url = 'http://duzhihu.cc/date/{date}'.format(date=date)
    content = requests.get(url).text
    result = parseHotList(content)
    # Dump
    with open('/home/wz/ZheProject/Zhihu/Data/Hist/%s.json' % date, 'w', encoding='utf8') as f:
        json.dump(result, f)


def parseSummary(content: str) -> [str]:
    """ parse text from 'http://duzhihu.cc/history'

    :param content:
    :return:
    """
    soup = BeautifulSoup(content, 'html.parser')
    divs = soup.findAll("h3", class_='panel-title')
    result = []
    for div in divs:
        result.append(div.text.strip())

    return result


if __name__ == '__main__':

    import datetime

    url = 'http://duzhihu.cc/date/{date}'
    summary = 'http://duzhihu.cc/history'

    dates = ['%s' % (datetime.datetime.now()-datetime.timedelta(days=1)).date().strftime('%Y-%m-%d')]
    print(dates)

    pool = ThreadPool(10)
    results = pool.map(hotListWorker, dates[:])
    pool.close()
    pool.join()
