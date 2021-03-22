# from bs4 import BeautifulSoup as bsp
# import re
# text='''<div class="ggb" style="position: relative; z-index: 3">
#        <div class="content-box1200" style="background-color: #e7e7e7;">
#            <div class="webPath" id="link2">
#                <a href="/Default.aspx" id="link2">首页</a>

#                <i class="Hui-iconfont Hui-iconfont-arrow2-right"><a href="/Default.aspx">首页copy</a></i><a href="/List.aspx?cid=451">程序开发</a>

#                <i class="Hui-iconfont Hui-iconfont-arrow2-right" id="link2">666</i><a href="/List.aspx?cid=732">Python爬虫教程</a>

                
#            </div>
#        </div>
#    </div'''
# soup=bsp(text,"lxml")
# print(soup.prettify())
#获取标签以及内容
# print(soup.a)
# print(soup.a.string)
# #获取标签名
# print(soup.div.name)
# #获取标签属性
# print(soup.a.attrs["href"])
#获取直接子标签
# print(soup.i.contents)
#以生成器形式获取直接子标签(需要遍历)
# # print(soup.i.children)
# for i in soup.i.children:
# 	print(i)
#获取所有子标签以及所有内容，结果是一个生成器
# print(soup.i.descendants)
# for i in soup.i.descendants:
# 	print(i)
#查找所有标签,返回结果集(非列表)
# data=soup.find_all("i")
# print(data[0].string)
#用正则表达式查找标签
# data=soup.find_all(re.compile("^i"))
# for i in data:
# 	print(i)
#根据属性查找标签
# data=soup.find_all(href="/Default.aspx")
# print(data[1].string)
#根据标签内容获取标签内容
# data=soup.find_all(text="首页")
# data2=soup.find_all(text=re.compile("首"))
# print(data2)
#css选择器有类名选择器，标签名选择器，id名选择器
#通过标签名获取标签
# data=soup.select("i")
# print(data[0].string)
#通过类名获取
# data=soup.select(".ggb")
# print(data)
#通过id获取
# data=soup.select("#link2")
# data1=soup.select("i#link2")
# print(data1)
#通过其他属性查找
# data=soup.select('a[href="/Default.aspx"]')
# print(data)
from bs4 import BeautifulSoup as bsp
import urllib
from urllib import request
import re
import requests

# for page in range(1,4):

# 	index={"index":page}
# 	index=urllib.parse.urlencode(index)
# 	info={"pageIndex":"x","timestamp":"timestamp","pageSize":10,"language":"zh-cn","area":"cn"}

# 	url="https://careers.tencent.com/search.html?"+index
# 	req=urllib.request.Request(url,headers=header)
# 	data=urllib.request.urlopen(req).read().decode()

	# pat=re.compile("post_id")
	# ss=pat.findall(data)
	# print(data)

	# soup=bsp(data,"lxml")
	# data1=soup.select('td a[tagart="_blank"]')
	# for x in data1:
	# 	urllist=soup.x.attrs["href"]
	# 	print(urllist)
# import threading
# import time 
# def run(name):
# 	print(name,"线程执行了！")
# t1 = threading.Thread(target=run,args=("t1",))
# t2 = threading.Thread(target=run,args=("t2",))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("执行完毕")
# class myThread(threading.Thread):
# 	def __init__(self, name):
# 		threading.Thread.__init__(self)
# 		self.name = name	
# 	def run(self):
# 		print("线程开始",self.name)
# 		print("线程执行中-----1")
# 		time.sleep(1)
# 		print("线程执行中-----2")
# 		time.sleep(1)
# 		print("线程执行中-----3")
# 		time.sleep(1)
# 		print("线程执行中-----4")
# 		time.sleep(1)
# 		print("线程执行中-----5")
# 		time.sleep(1)
# 		print("线程结束",self.name)
# t1=myThread("t1")
# t2=myThread("t2")
# t3=myThread("t3")
# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()
# print("执行完毕")
# import queue
# q=queue.Queue(maxsize=10)
# for i in range(1,11):
# 	q.put(i)
# print(q.get(i))
# print(q.get(i))
#一个get方法取一个，判断是否为空循环取出数值
# while not q.empty():
# 	print(q.get())
# import threading
# import queue
# import requests
# from lxml import etree
# import time
# #采集网页线程--爬取段子列表所在的网页放进队列
# class Thread1(threading.Thread):
# 	def __init__(self, threadName,pageQueue,dataQueue):
# 		threading.Thread.__init__(self)
# 		self.threadName = threadName
# 		self.pageQueue = pageQueue
# 		self.dataQueue = dataQueue
# 		self.headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36"}
# 	def run(self):
# 		print("线程开始"+self.threadName)
# 		while not flag1:
# 			try:
# 				page=self.pageQueue.get()
# 				url="https://www.qiushibaike.com/8hr/page/"+str(page)+"/"
# 				content=requests.get(url,headers=self.headers).text
# 				time.sleep(0.5)
# 				self.dataQueue.put(content)
				
# 			except Exception as e:
# 				pass
# 		print("线程结束"+self.threadName)
# #解析网页线程--从队列中拿到列表网页，进行解析，并保存到本地
# class Thread2(threading.Thread):
# 	def __init__(self, threadName,dataQueue,fileName):
# 		threading.Thread.__init__(self)
# 		self.threadName = threadName
# 		self.dataQueue = dataQueue
# 		self.fileName = fileName
# 	def run(self):
# 		print("线程开始"+self.threadName)
# 		while not flag2:
			
# 			try:
# 				data1=self.dataQueue.get()

# 				html=etree.HTML(data1)
# 				node_list=html.xpath('//div/a[@class="recmd-content"]')
# 				for node in node_list:
# 					data2=node.text
# 					self.fileName.write(data2+"\n")
# 			except Exception as e:
# 				raise e		
# 		print("线程结束"+self.threadName)
# flag1=False
# flag2=False

# def main():
# 	#url页码队列
# 	pageQueue=queue.Queue(2)
# 	for i in range(1,3):
# 		pageQueue.put(i)
# 	#网页数据队列
# 	dataQueue=queue.Queue()
# 	fileName=open(r"D:\英雄时刻\duanzi.txt","a")

# 	t1=Thread1("采集线程",pageQueue,dataQueue)
# 	t1.start()
# 	t2=Thread2("解析线程",dataQueue,fileName)
# 	t2.start()
# 	while not pageQueue.empty():
# 		pass
# 	global flag1
# 	flag1=True
# 	while not dataQueue.empty():
# 		pass
# 	global flag2
# 	flag2=True

# 	t1.join()
# 	t2.join()
	
# 	print("结束")
# 	fileName.close()

	
# if __name__ == '__main__':
# 	main()
# from aip import AipOcr
# import re
# import requests
# APP_ID="19274269"
# API_KEY="f9156V9VGb8lX0dvzNt77CCU"
# SECRET_KEY="U1x6jezvzNhDsaHTbm7oDSoV4IYQrcOb"

# client=AipOcr(APP_ID,API_KEY,SECRET_KEY)

# data=requests.get("https://www.51zxw.net/list.aspx?cid=732#!fenye=4").text
# pat=re.compile(r'<img src="(.*?)" alt="Python爬虫教程">')
# result1=pat.findall(data)
# url=result1[0]
# image=requests.get(url).content


# # with open(r"D:\英雄时刻\aa.jpg","rb") as f:
# # 	image=f.read()
# data=str(client.basicGeneral(image))
# pat=re.compile(r"'words_result': \[{'words': '(.*?)'}\]}")
# result=pat.findall(data)[0]
# print(result)
# import xlsxwriter
# workbook=xlsxwriter.Workbook('test.xlsx')
# worksheet=workbook.add_worksheet()
# #写入数据
# worksheet.write("A1","我测试一下")
# worksheet.write("A2","我在测试一下")
# workbook.close()
# import pymysql
# db=pymysql.Connect(host="localhost",port=3306,user="py.lyl",passwd="lyl113",db="spider",charset="utf8")
# cursor=db.cursor()
# sql="insert into tel(name,phone) values('单位','000')"
# cursor.execute(sql)
# db.commit()
# db.close()
# from selenium import webdriver

# # 创建 WebDriver 对象，指明使用chrome浏览器驱动
# wd = webdriver.Chrome(r'd:\2345Soft\2345Explorer\chromedriver.exe')

# # 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
# wd.get('https://www.baidu.com')
