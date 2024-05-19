import random

import requests
from lxml import html
import time
import re

import csv
etree = html.etree

fp = open('nj58.csv', 'a+', encoding='utf-8-sig',newline='')
csv_writer = csv.writer(fp, dialect='excel')
csv_writer.writerow(["标题", "总价（万）", "单价", "小区", "区域", "房间数", "大小",  "朝向","建造时间","标签"])
cookie = 'commontopbar_new_city_info=172%7C%E5%8D%97%E4%BA%AC%7Cnj; commontopbar_ipcity=su%7C%E8%8B%8F%E5%B7%9E%7C0; userid360_xml=4BDD7E5301D8BD5254C5832742B4A769; time_create=1707814484804; f=n; id58=CrINZWUvkwkPTkW9BUVOAg==; aQQ_ajkguid=41EE6832-395A-4044-ABD9-F06A696EAFC0; sessid=280B27E9-48CF-47C8-8176-FED6D155A4FA; ajk-appVersion=; 58tj_uuid=228a4907-8560-4e74-8427-ae8347a1183c; als=0; wmda_uuid=5d6ab965e5324501fca2dc4e07156017; wmda_new_uuid=1; xxzlclientid=bd418a72-6705-4407-a476-1699255295433; xxzlxxid=pfmxI9r0ViziKLOtaRP29c94kvIOfnQFtVvwd8EWrDFfPlDzg3WjE3IHd1p6n1fD1Mkv; xxzl_deviceid=yInCn2uIIeiCzmK40hdqH%2FNgNj6uAROXs%2Fxho%2FmPmMtv88e%2FDnyQfUKYf2P4boKQ; xxzl_smartid=f468666cbd5a3ae7ae3ff90b67a8a995; wmda_visited_projects=%3B10104579731767%3B1731916484865; city=bj; 58home=bj; fzq_h=a186e79136690299df05573c2a52b0bc_1705222472063_6527461263be48c5ba704d32026f14a9_47924973871565360041313087863872094569; new_uv=4; utm_source=; spm=; init_refer=; ctid=172; new_session=0; wmda_session_id_10104579731767=1705222886536-08b7c747-fe3b-50b7; xxzlbbid=pfmbM3wxMDI5M3wxLjUuMXwxNzA1MjIyOTI5ODUyfHBFTEZReFlMQTg5RGxBaVRmcnRPbUFwY29jTDlyRDZ6TFFHVTZkRXgxcDg9fDZhOTExN2U0YTNhYjE0MTY2NjEwMTAwMmQ3NGU0YjY2XzE3MDUyMjI5MDM4MTFfMDFmNDRkMzQ1MTUwNDFlMzlhZjUzNzE3YTk0MWJjOTRfMTk2ODI4Njg1NXxmZmQzY2RhOWE0MzQ5MGU4MzEwNmJlMGY4NGI2ZGJlYl8xNzA1MjIyOTA0MTA3XzI1Ng==; www58com="UserID=78951011952147&UserName=khtdvxi12"; 58cooper="userid=78951011952147&username=khtdvxi12"; 58uname=khtdvxi12; passportAccount="atype=0&bstate=0"; PPU=UID=78951011952147&UN=khtdvxi12&TT=4cceefc7d566440c288b734a17bfd7cf&PBODY=BwnLFV8Xw9XUDqFrv2AqB2MTUU8tT9Y5fgHAyi0WOJKdl0myMOiOz9vLTGOdjBDiwuOig-v_aWnoJHgNjiouvU_cTqajOY_aX673UQKxgS_46L3yLnJCKjGvkZ_RSM9K7uSeDB1OgGMWUHTa6jP2C9ttID_p8uu5QIcEeCIoAhs&VER=1&CUID=6cvyqBpLGJD-y73XCYoGzg; xxzl_cid=8b99946fbae348049bee3c41d613e726; xxzl_deviceid=llN4+MXOp3vWO4wB+zCu+CC8lgrBB0hNHy6jZryPyXEfwzwe62InrYSN3/kw6MQv'
for i in range(1,50):
    time.sleep(random.randint(3,7))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'cookie':cookie
    }
    # url ='https://nj.58.com/ershoufang/p{}?'.format(i)
    url = f'https://nj.58.com/ershoufang/p{i}/?pts=1705222903672&PGTID=0d30000c-000a-cd48-d03f-60f33a20dbdf&ClickID=1'
    page_text = requests.get(url=url,headers=headers).text

    tree = etree.HTML(page_text)
    li_list = tree.xpath('//section[@class="list"][1]/div')
    datalist=[]
    for li in li_list:
        # '//*[@id="esfMain"]/section/section[3]/section[1]/section[2]/div/a/div[2]/div[1]/div[1]/h3'
        title = li.xpath('normalize-space(./a/div[2]/div[1]/div[1]/h3/text())')
        price_count = li.xpath('normalize-space(./a/div[2]/div[2]/p[1]/span[1]/text())')
        price = li.xpath('./a/div[2]/div[2]/p[2]/text()')
        xiaoqu = li.xpath('normalize-space(./a/div[2]/div/section/div[2]/p/text())')
        quyu = li.xpath('normalize-space(./a/div[2]/div/section/div[2]/p[2]/span[1]/text())')
        home_num = li.xpath('normalize-space(./a/div[2]/div/section/div/p/span[1]/text())')
        size = li.xpath('normalize-space(./a/div[2]/div/section/div/p[2]/text())').replace(' ','')
        chaoxiang = li.xpath('normalize-space(./a/div[2]/div/section/div/p[3]/text())')
        jianzao = li.xpath('normalize-space(./a/div[2]/div[1]/section/div[1]/p[5]/text())')
        tags = li.xpath('./a/div[2]/div[1]/section/div[3]//text()')
        datalist.append([title, price_count, price[0], xiaoqu, quyu, home_num, size,chaoxiang, jianzao,tags])
        csv_writer.writerow([title, price_count, price[0], xiaoqu, quyu, home_num, size,chaoxiang, jianzao,tags])
    print(datalist)
        # filename.close()
fp.close()
print("over")


