#encoding:'utf-8'

# while 1==1:

# 	before=float(input("你本月所得工资总额为："))
# 	m1=float(input("请输入社保扣除金额"))

# 	ss=0#纳税金额
# 	ys=before-m1-5000#应纳税所得额

# 	if ys<3000 and ys>0:
# 		ss=ys*0.03

# 	elif ys<12000:
# 		ss=ys*0.1-460
# 	elif ys<25000:
# 		ss=ys*0.2-1410
# 	elif ys<45000:
# 		ss=ys*0.25-2660
# 	elif ys<80000:
# 		ss=ys*0.3-7160
# 	elif ys>80000:
# 		ss=ys*0.45-15160
# 	print("您的纳税金额为：",ss,"到手工资为",before-m1-ss)
        

# # a=[1418,4552,441241,6141241241,5,6,7777,888]
# # maxx=a[0]
# # for x in range(0,len(a)-1):
# # 	if maxx<=a[x+1]:
# # 		maxx=a[x+1]
	
# # print(maxx)

# i=0
# while i<=100:
# 	print(i)
# 	if i>98:
# 		print("over")

# 	i=i+1
# i=1
# sunm=0

# while i<=20:
# 	sunm=sunm+1.2
# 	print("第",i,"年到了")
# 	if i==10:
# 		print("你受伤了，就不用给我了")
# 		i=i+1
# 		continue


# 	j=1
# 	while j<=12:
# 		if j==8:
# 			j=j+1
# 			break
		# print("第",i,"年第",j,"月彩礼已支付，累计支付：",round(sunm,2),"万元")
# 		j=j+1
	
# 	i=i+1
# import time

# i=1
# while False:
# 	print("执行中")
# 	i=i+1
# 	time.sleep(1)
# card1="1001"
# pwd1="123456"
# ban1=10000

# card2="1002"
# pwd2="123456"
# ban2=10000

# card3="1003"
# pwd3="123456"
# ban3=10000
# times=0
# while True:
# 	print("欢迎来到李玉林的银行！")
# 	card=input("请输入您的银行账号：")
# 	pwd=input("请输入您的银行密码：")

# 	ban=0
# 	if card==card1 and pwd==pwd1:
# 		ban=ban1
			
# 	elif card==card2 and pwd==pwd2:
# 		ban=ban2
# 	elif card==card3 and pwd==pwd3:
# 		ban=ban3
# 	else:
# 		times=times+1
# 		if times>3:
# 			print("您已经连续输入错误三次，银行卡已被锁定！")
# 			break
# 		else:

# 			print("账号或密码错误，请重新输入！")
# 		continue
# 	while True:
# 		num=input("请输入您要办理的业务：1.取款 2.存款 3.退卡")
# 		if num=="1":
# 			out=float(input("请输入取款金额："))
# 			if out<=0:
# 				print("输入错误，请重新输入")
# 				continue
# 			elif out>=ban:
# 				print("余额不足")
# 				continue
# 			else:
# 				ban=ban-out
# 				print("取款成功，取出：",out,"元，余额为：",ban,"元")
# 		if num=="2":
# 			inn=float(input("请输入存款金额："))
# 			if inn<=0:
# 				print("输入错误，请重新输入")
# 				continue
# 			else:
# 				ban=ban+inn
# 				print("存款成功，存入：",inn,"元，余额为：",ban,"元")

# 		if num=="3":
# 			print("请收好您的卡片，欢迎您下次再来！")
# 			brea
# 	else:
# 		pirnt("输入有误")
# 		continue


# def add(a,b,c,d):
# 	e=a+b+c+d
# 	print(e)

# print(add(4,6,6,7))
# def zzj(f):
# 	if f=="苹果" or f=="草莓":

# 		print("正在榨汁")
# 		print("请稍等两分钟....")
# 		zhi="一杯"+f+"汁"
# 		return zhi
# 	else:
# 		print("错误")
# h=zzj("苹果")
# print(h)
# def show(name,sex,hobby,age=18):
# 	print("我叫：",name,"年龄：",age,"性别：",sex,"爱好：",hobby)
# show("张三",hobby="男",sex="打球",age=77)
# def sow(*args):
# 	j=0
# 	for i in args:
# 		j=j+i
# 	return j
# h=sow(1,24,5,6,7,8)
# print(h)


# from random import *


# b=choice(["张三",4,5,5])
# print(b)
# from test3 import f1
# b=f1(2,3,5)
# print(b)
# from urllib import request
# url="https://www.zhihu.com"
# dt=request.urlopen(url).read()
# print(dt.decode())
# import os
# os.system(r"C:\Users\DELL\AppData\Roaming")


# os.rename("C:\Users\DELL\AppData\Roaming,")
# import webbrowser
# webbrowser.open("https://www.zhihu.com")

# from PIL import Image,ImageFilter

# im=Image.open(r"C:\Intel\ccc.jpg")
# im2=im.filter(ImageFilter.BLUR)
# im2.save(r"C:\Intel\bbb.jpg")

# fh1=open(r"D:\CLIPART\101.txt","r")
# data=fh1.readlines()
# data1=fh1.read()
# print(data[0:5])
# print(data1)
# for i in fh1:
# 	print(i)
# fh1.close()
# fh2=open(r"D:\CLIPART\002.txt","a")
# fh2.write("\ngeiyepa")
# fh2.close()

# fh=open(r"E:\2345Downloads\tianyu.jpg","rb")
# data=fh.read()
# print(data)


# fh2=open(r"C:\Users\dasd\002.txt","w")
# fh2.write("dada")
# fh2.close()
# fh.close()
# class Dog(object):
# 	typee="宠物" #类变量

# 	#初始化方法
# 	def __init__(self,a,age,color):  #self表示当前对象

# 		self.name = a #实例变量（属性）
# 		self.age = age
# 		self.color = color
# 	def eat(self):  #普通方法
# 		print(self.name,"在吃东西")
# 	def run(self,speed):
# 		print(self.name,"狗狗在飞跑,速度:",speed)
# dog=Dog("小黑",5,"白色")
# dog.color="黑色"

# print(dog.color)
# print(dog.name)
# dog.eat()
# dog.run("3m/s")
# class Card(object):
	
# 	def __init__(self,num,pwd,ban):
# 		self.__num=num  #私有属性，只能从内部访问
# 		self.pwd=pwd
# 		self.ban=ban

# 	def cun(self):
# 		print("存款")
# 	def get(self,pwdd,ban):
# 		if pwdd==self.pwd and ban==self.ban:
# 			return self.__num
# 		else:
# 			return "错误"
# card=Card("10001","123456",10000)
# print(card._Card__num)
# print(card.get("123456",10000))
# class Nycard(Card):
# 	pass
# ny=Nycard("313","23131",31231)
# ny.cun()	
		
# class Animal(object):
		
# 		def __init__(self, color):
# 			self.color = color
# 		def eat(self):
# 			print("在吃东西")
# 		def run(self):
# 			print("动物在跑")
# class Cat(Animal):
# 	def eat(self):
# 		print("小猫在吃鱼")
# cat=Cat("黑色")
# print(cat.color)
# class Dog(Animal):
	
# 	def __init__(self, name,age,color):
# 		super(Dog,self).__init__(color)
# 		self.name=name
# 		self.age=age
# 	def eat(self):
# 		print("狗在啃骨头")
# dog=Dog("小白",4,"彩虹色")
# print(dog.name)
# dog.eat()
# print(dog.color)
# def feed(obj):
# 	obj.eat()
# an=Animal("黄色")
# cat=Cat("黑色")
# dog=Dog("小黑",5,"彩虹色")
# feed(dog)
# import tushare
# import time
# import smtplib
# from email.mime.text import MIMEText

# class Share(object):		
# 	def __init__(self,code,buy,sale):
# 		self.buy=buy
# 		self.sale=sale
# 		self.code=code
# def getrealtimedata(share):
# 	dataNow=tushare.get_realtime_quotes(share.code)

# 	share.name=dataNow.loc[0][0]
# 	share.price=float(dataNow.loc[0][3])
# 	share.high=dataNow.loc[0][4]
# 	share.low=dataNow.loc[0][5]
# 	share.volumn=dataNow.loc[0][8]
# 	share.amount=dataNow.loc[0][9]
# 	share.openToday=dataNow.loc[0][1]
# 	share.pre_colse=dataNow.loc[0][2]
# 	share.timee=dataNow.loc[0][30]
# 	share.describe="股票名："+share.name+"当前价格："+str(share.price)
# 	return share
# 	# print("股票名：",name,"当前价格：",price,"最高价：",high,"最低价：",low,)
# def sendemail(subject,content):

# 	msg_from="lyl1512050897@163.com"#发送方
# 	pwd="12344321a"#授权码
# 	to="1512050897@qq.com"#接收方
# 	#构造邮件
# 	msg=MIMEText(content)
# 	msg["Subject"]=subject
# 	msg["From"]=msg_from
# 	msg["To"]=to
# 	try:
# 		ss=smtplib.SMTP_SSL("smtp.163.com",465)
# 		ss.login(msg_from,pwd)
# 		ss.sendmail(msg_from,to,msg.as_string())
# 		print("发送成功")
		
# 	except Exception as e:
# 		print("发送失败，详情为：",e)


# def main(shl):
# 	for share in shl:

# 		sss=getrealtimedata(share)
# 		print(sss.describe)

# 		if sss.price<=sss.buy:
# 			print("可以买入了")
# 			sendemail("达到买点","快去看看吧"+sss.describe)
# 		elif sss.price>=sss.sale:
# 			print("可以卖出了")
# 			sendemail("达到卖点",sss.describe)
# 		else:
# 			print("不买也不卖，等着")
# # while True:

# 	share1=Share("000591",3.2,3.5)
# 	share2=Share("600106",3.3,3.6)
# 	share3=Share("601988",3.5,3.8)
# 	list1=(share1,share2,share3)
# 	main(list1)
# 	time.sleep(90)

# a=[33,54,54,34,23,53,0,"b",143,545,676,66,27]
# for i in a:
# 	try:
# 		print("-------",i)
# 		print(3/i)
# 	except Exception as e:
# 		print("出现错误，错误是：",e)
# 	else:
# 		print("正常")
# 	finally:
# 		print("本次结束")
# pwd="123456"
# if len(pwd)<8:
# 	ex=Exception("密码长度不得低于八位数")
# 	raise ex

# else:
# # 	print("密码设置成功")
# #客户端代码
# import socket
# client=socket.socket()#生成连接的对象
# client.connect(("localhost",6969))
# client.send("hello world".encode())
# client.close()
# #服务端代码
# import socket
# server=socket.socket()
# server.bind(('localhost',6969))
# server.listen()
# print("准备接电话了")
# con,addr=server.accept()
# print(con,addr)
# data=con.recv(1024)
# print("接受到的消息是：",data)
# server.close()
# import smtplib
# from email.mime.text import MIMEText
# msg_from="lyl1512050897@163.com"#发送方
# pwd="12344321a"#授权码
# to="1512050897@qq.com"#接收方

# subject="这是python发送过来的邮件"#主题
# content="你家着火了"#内容
# #构造邮件
# msg=MIMEText(content)
# msg["Subject"]=subject
# msg["From"]=msg_from
# msg["To"]=to
# try:
# 	ss=smtplib.SMTP_SSL("smtp.163.com",465)
# 	ss.login(msg_from,pwd)
# 	ss.sendmail(msg_from,to,msg.as_string())
# 	print("发送成功")
	
# except Exception as e:
# 	print("发送失败，详情为：",e)
import threading
# import time

# def run(name):
# 	print(name,"线程已执行")
# 	time.sleep(3)
# t1=threading.Thread(target=run,args=("t1",))
# t2=threading.Thread(target=run,args=("t2",))
# t1.start()
# t2.start()
# t1.join()#让主线程等待子线程执行完毕之后再执行主线程
# t2.join()
# print("执行完毕")
# lock=threading.Lock()
# a=1
# def run(name):
# 	lock.acquire()
# 	global a
# 	a+=1
# 	print(a,"线程执行了，当前线程a的值为：",a)
# 	lock.release()
# for i in range(100):

# 	t=threading.Thread(target=run,args=(a+1,))
# 	t.start()
#多进程解决GIL（全局解释器锁）问题
# from multiprocessing import Process
# import time
# def run(name):
# 	print(name,"线程执行了")
# 	time.sleep(5)
# if __name__=='__main__':
# 	p1=Process(target=run,args=("p1",))
# 	p2=Process(target=run,args=("p2",))
# 	p3=Process(target=run,args=("p3",))
# 	p4=Process(target=run,args=("p4",))
# 	p5=Process(target=run,args=("p5",))

# 	p1.start()
# 	p2.start()
# 	p3.start()
# 	p4.start()
# 	p5.start()
#景区卖票
# lock=threading.Lock()
# num=100
# def sale(name):
# 	lock.acquire()
# 	global num
# 	if num>0:
# 		num=num-1
# 		print(name,"窗口已卖出一张票，还剩",num,"张票")
# 	lock.release()

# while 1==1:
# 	if num>0:
# 		ta=threading.Thread(target=sale,args=("A窗口",))
# 		tb=threading.Thread(target=sale,args=("B窗口",))
# 		ta.start()
# 		tb.start()
# 		ta.join()
# 		tb.join()
# 	else:
# 		break
# print("票已经卖完了")
# import pymysql
#打开数据库连接，主机地址，端口号3306，用户名，密码，数据库名，
# db=pymysql.Connect(host="localhost",port=3306,user="py.lyl",passwd="lyl113",db="stu.lyl",charset="utf8")
# #创建一个游标对象 cursor()
# cursor=db.cursor()
# #定义sql语句
# sql="""create table student(
# 	id int not null,
# 	name varchar(20),
# 	age int

# )"""
# cursor.execute(sql)#执行sql语句
# db.close()
# db=pymysql.Connect(host="localhost",port=3306,user="py.lyl",passwd="lyl113",db="stu.lyl",charset="utf8")
# cursor=db.cursor()
# sql='''insert into student(id,name,age)
# 	values(2,"张三",13)

# '''
# cursor.execute(sql)
# db.commit()
# db.close()
# # 查询数据
# cursor=db.cursor()
# sql="select * from student where id=1"#select *from student and fetchall
# cursor.execute(sql)
# data1=cursor.fetchone()
# print(data1[2])
# db.close()
# # 更新操作
# cursor=db.cursor()
# sql="update student set age=age+1"
# cursor.execute(sql)
# db.commit()
# db.close()
# 删除操作以及异常处理
# cursor=db.cursor()
# sql="delete from student where name='张三'"
# sql1="delete from student where namme='李四'"
# try:
# 	cursor.execute(sql)
# 	cursor.execute(sql1)
# 	db.commit()
# except Exception as e:
# 	db.rollback()
# 	print("出现异常")

# db.close()
# import datetime
# #日期转字符串
# now=datetime.datetime.now()
# d=now.strftime("%y-%m-%d:%H:%M:%S")
# print(now)
#字符串转日期
# s="2020-3-4 2:30:20"
# d=datetime.datetime.strptime(s,"%Y-%m-%d %H:%M:%S")
# print(d)
# import json
# j='{"city":"北京","name":"熊猫"}'
# p=json.loads(j)
# print(type(p))
# print(p["city"])
#字典转json
# j={"city":"北京","name":"熊猫"}
# ss=json.dumps(j,ensure_ascii=False)
# print(ss)
#编码与解码
#ascci  gb2312 gbk unicode utf-8
# a="我爱北京"
# b=a.encode("utf-8")
# print(b)

# c=b.decode("utf-8")
# print(c)
# import urllib.request

# from urllib import request
# import re
# import random
# agent1="Mozilla/5.0 (Linux; Android 8.1.0; ALP-AL00 Build/HUAWEIALP-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.11 (Baidu; P1 8.1.0)"
# agent2="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36"
# list1=[agent1,agent2]
# agent=random.choice(list1)
# print(agent)
# #创建请求头信息
# header={"User-Agent": agent}
# url=r"http://www.baidu.com/"
# #创建自定义请求（对抗反爬，封装多个）
# #反爬机制1：判断是否以浏览器访问
# req=request.Request(url,headers=header)

# reponse=request.urlopen(req).read().decode()
# #（数据清洗，re：正则表达式）
# pat=r"<title>(.*?)</title>"
# data=re.(pat,reponse)
# print(data[0])
#自定义opener
# from urllib import request
# import random
# import json
# 创建http处理器对象（处理http请求的对象）
# http_handler=request.HTTPHandler()
# #创建自定义oppner（可以处理代理，cookie等高级信息）
# opener=request.build_opener(http_handler)
# #创建自定义请求头

# url="http://www.baidu.com/"
# header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36"}
# req=request.Request(url,headers=header)
# #建全局opener
# request.install_opener(opener)#之后用opener.open()或者request.urlopen()
# #发送请求获取响应
# # reponse=opener.open(req).read()#或者如下
# reponse=request.urlopen(req).read()
# print(reponse)
# 反爬虫2：判断请求来源的ip地址(代理ip)
# proxylist=[
# 	{"https":"118.113.246.234:9999"},
# ]
# proxy=random.choice(proxylist)
# # print(proxy)
# #创建代理器处理对象
# proxyhandler=request.ProxyHandler(proxy)
# opener=request.build_opener(proxyhandler)
# req=request.Request("https://www.baidu.com")

# reponse=opener.open(req).read()
# print(reponse)
#处理get请求

# _*_ coding:utf-8 _*_
# import requests
# import urllib
# from urllib import request
# import time
# import re
# wd={"wd":"北京"}#url编码parse解析
# url="http://www.baidu.com/s?"
# wdd=urllib.parse.urlencode(wd)
# url=url+wdd
# req=request.Request(url)
# reponse=request.urlopen(req).read().decode()
# print(reponse)
# def loadpage(url,filename):
# 	print("正在下载:"+filename)
# 	header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36 2345Explorer/10.7.0.20186"}
# 	req=request.Request(url,headers=header)
# 	return request.urlopen(req).read()

# def writepage(html,filename):
# 	print("正在保存"+filename)
# 	with open(filename,"wb") as f:
# 		f.write(html)
# 	print("-------------")

# def tiebaspider(url,beginpage,endpage):
# 	for page in range(beginpage,endpage+1):
# 		pn=(page-1)*50
# 		filename="e:/第"+str(page)+"页.html"
# 		fullurl=url+"&pn="+str(pn)
# 		html=loadpage(fullurl,filename)
# 		writepage(html,filename)
# 		print("谢谢使用")

# if __name__ == '__main__':
# 	kw = input("请输入需要爬取的贴吧名：")
# 	beginpage = int(input("请输入起始页："))
# 	endpage = int(input("请输入结束页："))

# 	url = "http://tieba.baidu.com/f?"
# 	key = urllib.parse.urlencode({"kw":kw})
# 	fullurl = url+key
# 	tiebaspider(fullurl,beginpage,endpage)

# time.sleep(5)
# header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64)\ AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36 2345Explorer/10.7.0.20186"}
# url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
# # key=input("请输入需要翻译的单词：")
# key="你好"
# fromdata={
# 	"i": key,
# 	"from": "AUTO",
# 	"to": "AUTO",
# 	"smartresult": "dict",
# 	"client": "fanyideskweb",
# 	"salt": "15839910881178",
# 	"sign": "a8c0a7649bc88cd27b52734be4e0980c",
# 	"ts": "1583991088117",
# 	"bv": "656f750600466990f874a839d9f5ad23",
# 	"doctype": "json",
# 	"version": "2.1",
# 	"keyfrom": "fanyi.web",
# 	"action": "FY_BY_REALTlME"
# }
# # data=urllib.parse.urlencode(fromdata).encode("utf-8")
# # #data有参数则是post请求，没有参数则是get
# # req=request.Request(url,data=data,headers=header)
# # reponse=request.urlopen(req).read().decode()
# reponse=requests.post(url,headers=header,data=fromdata).text
# pat=re.compile(r'"tgt":"(.*?)"}]',re.I)#或者pat=r"'"tgt":"(.*?)"}]'"
# data=pat.findall(reponse)#以及data=re.findall(pat,reponse)
# print(data[0])

# time.sleep(6)
#异常处理
# list1=[
# "http://www.baidu.com",
# "http://www.baidu.com",
# "http://www.baidu.com",
# "http://www.dawkjhgalkkjbdskhgkja.com",
# "http://www.baidu.com",


# ]
# i=0
# for url in list1:
	
# 	try:
# 		i=i+1
# 		request.urlopen(url)
# 		print("第",i,"次请求完成")
# 	except Exception as e:
# 		print(e)
# cookie设置
# import webbrowser
# import requests
# from urllib import request
# import urllib
# header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36 2345Explorer/10.7.0.20186",
# "Cookie":"pgv_pvi=1684014080; eas_sid=t1x5w7I2m748u8G0Q4P8T4J2D5; pgv_pvid=4071858470; tvfe_boss_uuid=c5e19a5f4fbd023b; RK=tjA431hNGX; ptcz=7afb47868bf5debcfbc6e1e12a5e2a149310444702f878207598fc378ef915fd; qz_screen=1536x864; QZ_FE_WEBP_SUPPORT=1; LW_uid=H1L5d7C8b0P437D8u1X5A8e3q3; LW_sid=K1O5h738A0o4A7T8g2z106y2Y2; o_cookie=1512050897; pac_uid=1_1512050897; ptui_loginuin=1173215041; lskey=00010000bb46dbcdaaf82c26f159dc5fbd64ad62ecfd4147a474690c8754521d62c11e3238abf3e721a67cf3; __Q_w_s__QZN_TodoMsgCnt=1; uin=o1512050897; p_uin=o1512050897; Loading=Yes; pgv_info=ssid=s2293399010; _qpsvr_localtk=0.22845713242135113; pgv_si=s7027851264; skey=@cTzPRv3ap; pt4_token=HvhC3FmojN645vDCFCaGGEwTnq5cmLlzzEqvpjWYDME_; p_skey=VPCPM6bzstsdWe4ktiVMA2F2JnK1cqaJGoS4qaWg4Q4_; cpu_performance_v8=19"}
# url="https://user.qzone.qq.com/1512050897/infocenter?via=toolbar"


# response=requests.get(url,headers=header)
# print(response.text)
# webbrowser.open("https://user.qzone.qq.com/1512050897")

# import requests
# header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64)\
#  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36"}
# wd={"wd":"中国"}

# reponse=requests.get("http://i.baidu.com/s?",params=wd,headers=header).content.decode()#text返回一个unicode即字符串形式 content返回二进制形式数据
# print(reponse)
# import requests
# url="http://www.baidu.com/"
# proxy=[{"http":"221.180.170.104:8080"}

# ]
# reponse=requests.get(url,proxies=proxy[0])
# print(reponse.content.decode())
# 获取cookie响应信息
# response=requests.get(url)
# cookiejar=response.cookies
# cookiedict=requests.utils.dict_from_cookiejar(cookiejar)
# print(cookiedict)
#创建session对象传递用户名密码爬取数据
# header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64)\
#  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36"}
# ses=requests.session()
# data={"loginStr":"13795976396","pwd":"lyl113"}
# ses.post("https://www.51zxw.net/login",data=data)
# response=ses.get("https://www.51zxw.net/Login/UserCenter")
# print(response.content.decode())


import time
import re
# songid=[]
# songname=[]

# for i in range(0,2):
# 	url="http://www.htqyy.com/top/musicList/hot?pageIndex="+str(i)+"&pageSize=20"
# 	html=requests.get(url)
# 	strr=html.text
# 	pat1=r'title="(.*?)" sid'
# 	pat2=r'sid="(.*?)"'

# 	namelist=re.findall(pat1,strr)
# 	idlist=re.findall(pat2,strr)
# 	songname.extend(namelist)
# 	songid.extend(idlist)

# for i in range(0,len(songid)):
# 	songurl="http://f2.htqyy.com/play7/"+str(songid[i])+"/mp3/3"
# 	songName=songname[i]

# 	data=requests.get(songurl).content
# 	print("正在下载第",i+1,"首")
# 	with open("D:\\英雄时刻\\{}.mp3".format(songName),"wb") as f:
# 		f.write(data)

# 	time.sleep(5)
# 	break
#\w任意数字字母下划线\W与小写w相反\d十进制数字\D非十进制数字\s空白字符\S非空白字符
#数字[0-9]英文[a-z][A-Z]中文[\u4e00-\u9fa5] ^开头&结尾
# name="wJ4hW7我不知道"

# pat=r"[^a-zA-Z0-9]"*3
# req=re.search(pat,name)
# print(req)
# with open(r"C:\Users\DELL\Desktop\笔记本.txt","r") as f:
# 	data=f.read()
# pat=r"\s"*2
# response=re.findall(pat,data)
# print(response)
# a="#@@#$$$^^&boy**&&^$#$#@张3三33#@#paython##@$%!!!@#$%23*()*&&(&("
# pat=r".+"
# print(re.search(pat,a))
# a="1248WD()NMDocao814python188,"
# b="028-1354737"
# pat=re.compile(r"1248wd",re.I)
# print(pat.match(a))
# a="helloworld----------worldhello----------worldhello-------\
#  helloworld----------worldhello----------helloworld"
# pat=r"hello|world"
# rea=re.finditer(pat,a)
# s=[]
# r=[]
# for i in rea:
# 	s.append(i.group())
# print(s)
# a="张三@@@@@李四@@@@@王五@@@@@赵六"
# pat1=re.compile(r"@+")
# result=pat1.split(a)
# result2=pat1.sub("垃圾",a)
# print(result2)
import requests
import re
import xlsxwriter
import pymysql
#写入数据库需要的连接
db=pymysql.Connect(host="localhost",port=3306,user="py.lyl",passwd="lyl113",db="spider",charset="utf8")
cursor=db.cursor()

header={"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64)\
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36"}
url="http://changyongdianhuahaoma.51240.com/"
req=requests.get(url,headers=header).text

pat1=r'<tr bgcolor="#EFF7F0">[\s\S]*?<td>(.*?)</td>[\s\S]*?<td>[\s\S]*?</td>[\s\S]*?</tr>'
pat2=r'<tr bgcolor="#EFF7F0">[\s\S]*?<td>[\s\S]*?</td>[\s\S]*?<td>(.*?)</td>[\s\S]*?</tr>'
response=re.compile(pat1)
response2=re.compile(pat2)

result=response.findall(req)
# print(result)
result2=response2.findall(req)
#写入excel
# workbook=xlsxwriter.Workbook("测试二.xlsx")
# worksheet=workbook.add_worksheet()
#删除数据库
sqll="delete from tel"
cursor.execute(sqll)
db.commit()

list1=[]
for i in range(0,len(result)):
	list1.append(result[i]+result2[i])
	#写入数据库
	sql="insert into tel(name,phone) values('"+result[i]+"','"+result2[i]+"')"
	cursor.execute(sql)
	#写入excel
	# worksheet.write("A"+str(i+1),result[i])
	# worksheet.write("B"+str(i+1),result2[i])
db.commit()
db.close()

print(list1)	
# workbook.close()
# from urllib import request

# namelist=[]
# scorelist=[]
# i=0
# while 1==1:

# 	fullurl=r"https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start="+str(i)+"&limit=20"
# 	i=i+20
# 	header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML\
# 	, like Gecko) Chrome/69.0.3947.100 Safari/537.36"}
# 	req=request.Request(fullurl,headers=header)
# 	data=request.urlopen(req).read().decode()
# 	pat1=r'"title":"(.*?)"'
# 	pat2=r'"rating":\["(.*?)",'
# 	pattern1=re.compile(pat1)
# 	pattern2=re.compile(pat2)
# 	data1=pattern1.findall(data,re.I)
# 	data2=pattern2.findall(data,re.I)
	
# 	namelist.extend(data1)
# 	scorelist.extend(data2)
# 	if i>100:
# 		break
# for x in range(0,len(namelist)):
	
# 	print("电影名：",namelist[x],"排名：",x+1,"得分：",scorelist[x])
from lxml import etree
import requests
# text='''<div class="container">
# 	<div id="content">
# 		<div class="inner">
# 			<div class="title"><h3>最近更新</h3></div>
# 			<div class="details">
# 			<ul class="gengxin">
# 								<li>
# 						<span class="col1"><a href="/danhuangwudi/"  target="_blank">丹皇武帝</a></span>
# 						<span class="col2"><a href="/book/2430.html" target="_blank">第542章 轮回妖花</a></span>
# 						<span class="col3">实验小白鼠</span>
# 						<span class="col4">03-22 11:37</span>
# 					</li>
# 									<li>
# 						<span class="col1"><a href="/dijiutequ/"  target="_blank">第九特区</a></span>
# 						<span class="col2"><a href="/book/2427.html" target="_blank">第五八三章 没有底线的匪徒</a></span>
# 						<span class="col3">伪戒</span>
# 						<span class="col4">03-22 10:13</span>
# 					</li>
# 									<li>
# 						<span class="col1"><a href="/shijianzhongqiyouxi/"  target="_blank">绍宋</a></span>
# 						<span class="col2"><a href="/book/2426.html" target="_blank">第五十六章 胡思</a></span>
# 						<span class="col3">榴弹怕水</span>
# 						<span class="col4">03-22 00:00</span>
# 					</li>'''
# #将字符串解析成特殊的html文件
# html=etree.HTML(text)
# result=etree.tostring(html,encoding="utf-8").decode()
# print(result)
#处理本地html文档用parse()方法

html=etree.parse(r"D:\英雄时刻\测试2.html",etree.HTMLParser())
# result=etree.tostring(html,encoding="utf-8").decode()
# print(result)
result=html.xpath("//*[@class='btitle2']")
print(result[0].text)
# result=html.xpath("//a/@href")

# for i in result:
# 	print(i)
# result2=html.xpath("//div/li//@class")
# print(result2)
#获取倒数的标签内容
# result=html.xpath("//li/em")
# print(result[-2].text)
#获取对应属性的标签名
# result=html.xpath("//*[@class='btitle2']")
# print(result[0].tag)
# url="https://www.qiushibaike.com/text"
# header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64)\
#  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36"}
# response=requests.get(url,headers=header).text
# #找文字段子：
# result=etree.HTML(response).xpath("//div[@class='content']//span")
# namel=[]
# for site in result:
# 	namel.append(site)
# for i in namel:
# 	print(i.text)

#找段子链接
# html=etree.HTML(response)
# result=html.xpath("//div//a[@class='recmd-content']/@href")
# for site in result:
# 	xurl=url+site
# 	response2=requests.get(xurl).text
# 	result2=etree.HTML(response2).xpath("//div[@class='content']")
# 	print(result2[0].text)
# import urllib
# import urllib.request
# class Spider(object):
# 	def __init__(self):
# 		self.tiebaName="java"
# 		self.beginpage=1
# 		self.endpage=2
# 		self.fileName=1
# 		self.url="http://tieba.baidu.com/f?"
# 		self.ua_header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586"}
# 	def tbspider(self):
# 		for page in range(self.beginpage,self.endpage):
# 			pn=(page-1)*50
# 			wd={"kw":self.tiebaName,"pn":pn}
# 			word=urllib.parse.urlencode(wd)
# 			myurl=self.url+word
# 			myspider.loadPage(myurl)
# 	def loadPage(self,url):

# 		req=urllib.request.Request(url)
# 		data=urllib.request.urlopen(req).read().decode("utf-8")
# 		html=etree.HTML(data)
# 		links=html.xpath('//div[@class="threadlist_title pull_left j_th_tit "]//a/@href')
# 		for link in links:
# 			linkn="http://tieba.baidu.com"+link
# 			self.imageLoad(linkn)
# 	def imageLoad(self,link):
# 		req=urllib.request.Request(link)
# 		data=urllib.request.urlopen(req).read().decode("utf-8")

# 		html=etree.HTML(data)
# 		links=html.xpath('//img[@class="BDE_image" ]//@src')
# 		for link in links:
# 			self.imagesload(link)
# 	def imagesload(self,imageslink):
# 		print("正在写入：",self.fileName,".....")
# 		response=urllib.request.urlopen(imageslink).read()
# 		with open(r"F:\image\\"+str(self.fileName)+".jpg","wb") as f:
# 			f.write(response)
# 		self.fileName+=1

					

# if __name__ == '__main__':
	
# 	myspider=Spider()

# 	myspider.tbspider()
# 	print("执行中")


			

			
