import random
import requests
from time import sleep
from bs4 import BeautifulSoup

def larissa(name):
	param = {
		"u":name
	}
	ht = requests.post("https://shindanmaker.com/749828",param)

	soup = BeautifulSoup(ht.text, "html.parser")
	result = soup.find("div",class_="result2").find("div").text
	return result.strip()

def randSleep():
	#ランダム待ち
	sec = random.randint(5,10)
	sleep(sec)
	
def main():
	
	names = ['saru','SARU','さる','おさる','おさるのまーち',
	'猿','お猿','お猿のマーチ','をさる','お猿だそうさ','おさるだそうさ',
	'さるまーち','さるさる','さるを','さるぎゃー','さるっち']
	random.shuffle(names)
	print(names)
	
	for name in names:
		#診断
		result = larissa(name)
		
		if result == "武田羅梨沙多胡":
			print('成功！：'+name+'/'+result)
			break
		else:
			print('失敗！：'+name+'/'+result)
			randSleep()
	print('終了！！！！')

if __name__ == '__main__':
	main()