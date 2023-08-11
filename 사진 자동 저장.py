import urllib.request
url="http://img.hankyung.com/photo/201810/01.18131413.1.jpg"
savename= "test.jpg"
urllib.request.urlretrieve(url,savename)
print("저장완료")
url2="https://cdnmos-bikeradar.global.ssl.fastly.net/images/bikes-and-gear/bikes/mountain/1324585111779-rzjacf0uw1im-630-80.jpg"
savename="test2.jpg"
mem =urllib.request.urlopen(url2).read()

with open(savename,mode="wb")as f:
    f.write(mem)
    print('저장2완료')

    
