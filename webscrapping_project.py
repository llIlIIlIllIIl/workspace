import requests
from bs4 import BeautifulSoup

def scrape_weather():
    print("[강서구 방화1동]\n")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EA%B0%95%EC%84%9C%EA%B5%AC+%EB%B0%A9%ED%99%941%EB%8F%99+%EB%82%A0%EC%94%A8&oquery=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&tqi=hX5igsp0JywssDPnzTwssssssPw-204156"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    # 어제보다 OO° 낮아요 구름OO
    summary = soup.find("p", attrs={"class":"summary"}).get_text().replace("흐림", "/  흐림")
    # 현재 OO℃ 
    temperature_text = soup.find("div", attrs={"class":"temperature_text"}).get_text().replace("현재 온도", "")
    # 체감 OO° 습도 OO% Om/s  
    summary_list = soup.find("dl", attrs={"class":"summary_list"}).get_text().replace("습도", "/  습도 ").replace("바람", "/  바람")
    # 미세먼지 초미세먼지 자외선 일몰
    report_card_wrap = soup.find("div", attrs={"class":"report_card_wrap"}).get_text().replace("자외선", "/  자외선")
    # 오전 강수확률 OO% / 오후 강수확률 OO%
    cell_weather = soup.find("div", attrs={"class":"cell_weather"}).get_text()

    # 출력
    print("{}".format(summary))
    print("현재 온도 :{}".format(temperature_text))
    print("체감 온도 :{}".format(summary_list))
    print("미세먼지 :{}".format(report_card_wrap))
    print("강수량 :{}".format(cell_weather))

if __name__ == "__main__":
    scrape_weather() # 오늘의 날씨 정보 가져오기