import requests
from bs4 import BeautifulSoup

#key = "api키 입력"

f = open("name.csv", "w", encoding="UTF-8-sig")

#for pageNo in range(1,2):
pageNo=1
while True:
    queryParams = "ServiceKey="+key + "&pageNo="+str(pageNo)
    #queryParams = "ServiceKey="+key + "&numOfRows="+str(4) + "&pageNo="+str(pageNo)
    url = "http://apis.data.go.kr/1470000/FoodRwmatrInfoService/getFoodRwmatrList?" + queryParams
    req = requests.get(url)
    #print(type(req))

    html = req.text
    #print(type(html))
    #print(html[:150])
    soup = BeautifulSoup(html, 'html.parser')

    #print(soup)
    finded_values=soup.find_all('rprsnt_rawmtrl_nm')
    names = [x.text for x in finded_values]
    if names == []:
        break
    else:
        print(names)
        for name in names:
            f.write(name + "\n")
            pageNo +=1
f.close()
