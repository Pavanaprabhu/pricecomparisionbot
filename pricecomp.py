from selenium import webdriver
import smtplib
browser=webdriver.Chrome('C:\\Users\Pavana Prabhu\chromedriver_win32 (2)\chromedriver.exe')


def get_price():
	browser.get('https://www.amazon.in/Test-Exclusive-602/dp/B07HGLC2CG/ref=sr_1_1?dchild=1&keywords=redmi+note+9+pro+max&qid=1597916014&s=electronics&sr=1-1')
	pe=browser.find_element_by_id('priceblock_ourprice')
	pr=pe.get_attribute('textContent')
	pr=pr[2:]
	pl=pr.split(',')

	price_a=''
	for i in pl:
		price_a+=i
	price_a=float(price_a)
	print("the price in amazon is  " +str(price_a))
	return price_a

p=19000.00
a=get_price()

def mail():
#referance of connection
	s=smtplib.SMTP('smtp.gmail.com', 587)
#make network secure
	s.starttls()
	ml='****@gmail.com'
	pw='********'

	s.login(ml,pw)
	mt='****@gmail.com'
	message='hurry up the price is low now.Grab the deal.'

	s.sendmail(ml,mt,message)
	s.quit()

if(a<=p):

	print("buy")
	mail()
	print("mailed")
else:
	print("dont buy")

