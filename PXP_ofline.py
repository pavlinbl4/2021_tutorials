import csv
from bs4 import BeautifulSoup

def write_csv(usefull_data):
    with open("pxp_all_time_report.cvs","a") as output_file:
        writer = csv.writer(output_file)
        writer.writerow([usefull_data["image_id"],usefull_data["sell_date"],usefull_data["buyer"],usefull_data["income"]])



def get_data(offline_html):
    with open(offline_html, encoding="cp1251") as input_file:
        pxp = input_file.read()
        soup = BeautifulSoup(pxp,'lxml')
        trs = soup.find('table').find('tbody').find_all('tr')
        trs = trs[:-5]
        count = len(trs)  #1788
        for i in range(2,4,2):
            tds = trs[i].find_all('td')
            sell_date = tds[0].find('small').text.strip()
            image_id = tds[2].find('small').text.strip()[2:]
            buyer = tds[4].find('small').text.strip()
            income = tds[14].find('small').text.strip() #  2 - image id , 4 - buyer, 14 - income
            image_link = tds[2].find('small').find('a').get('href')
            image_link_bad = f"http://preview.photoxpress.ru/preview/photoxpress_ru/news_info/{image_id}.jpg"
            #                  http://preview.photoxpress.ru/preview/photoxpress_ru/news_info/604811109.jpg
            #   http://preview.photoxpress.ru/preview/photoxpress_ru/news_info/3216032041.jpg
            sell_date = sell_date.replace("\xa0", "_")
            usefull_data = {"sell_date": sell_date,
                            "image_id": image_id,
                            "buyer": buyer,
                            "income":income
                            }
            # write_csv(usefull_data)
            # print(usefull_data)
            print(image_id)
            print(image_link_bad)
            print(image_link
                  )



offline_html = "/Users/evgeniy/Downloads/PXP/PhotoXPress - фотоАРХИВ и фотоНОВОСТИ_files/pc_base_data/source_report.html"
get_data(offline_html)

