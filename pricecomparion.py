"""
open browser
find product on amazon
TAKE the price
find product on flipkart
take price
compare prices"""
from selenium import webdriver
browser=webdriver.Chrome('C:\\Users\Pavana Prabhu\chromedriver_win32 (1)\chromedriver.exe')


print ("checking on Amazon .....")
browser.get('https://www.amazon.in/Test-Exclusive-604/dp/B07HGLBZ5R/ref=sr_1_1?dchild=1&keywords=oneplus+7+pro&qid=1597680500&sr=8-1')
pe=browser.find_element_by_id('priceblock_ourprice')
pr=pe.get_attribute('textContent')
pr=pr[2:]
pl=pr.split(',')

price_a=''
for i in pl:
	price_a+=i
price_a=float(price_a)
print("the price in amazon is  " +str(price_a))



print ("checking on Flipkart .....")
browser.get('https://www.flipkart.com/oneplus-7-pro-nebula-blue-256-gb/p/itmbdc9c2e788399?pid=MOBFKFPECPTUFZQW&lid=LSTMOBFKFPECPTUFZQWLFW5AQ&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=6d37adf2-0965-4a22-956a-affbe107a4f0.MOBFKFPECPTUFZQW.SEARCH&ppt=sp&ppn=sp&ssid=vr5gj00jk00000001597681142598&qH=430521230d5db8b8')
fe=browser.find_element_by_xpath('//div[@class="_1vC4OE _3qQ9m1"]')
fr=fe.get_attribute('textContent')

fr=fr[1:]
fl=fr.split(',')

price_f=''
for j in fl:
	price_f+=j
price_f=float(price_f)
print("the price in flipkart is  " +str(price_f))


if (price_a<price_f):
	print("The price is less on amazon .Buy from amazon.")

elif (price_a>price_f):
	print("The price is less on flipkart .Buy from flipkart.")

else:
	print("The price is same .YOU can buy from any of them.")