#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-06-08 11:17:35
# @Author  : zealous (doublezjia@163.com)
# @Link    : https://github.com/doublezjia
# @Version : $Id$
# @@Desc   : 百度翻译Python版 
# 百度翻译开放平台文档：http://api.fanyi.baidu.com/api/trans/product/apidoc

import os,requests,random,sys
import hashlib
import json



# APPID & secretKey 百度翻译开放平台提供
appid = '注册百度翻译开放平台获取'
secretKey = '注册百度翻译开放平台获取'

# 通用翻译API HTTP地址基本地址
bash_url = 'http://api.fanyi.baidu.com/api/trans/vip/translate?q={trans_query}&from={trans_from}&to={trans_to}&appid={appid}&salt={salt}&sign={sign}'

def baidu_trans(trans_query,trans_from = 'auto',trans_to = 'zh'):

	# trans_query 要翻译的内容
	# # 原语言 不确定时可设置为auto
	# trans_from = 'auto'
	# # 目标语言 语种不可设置为 auto
	# trans_to = 'zh' 默认翻译中文

	# 随机数
	salt = random.randint(1000,5000)
	# 签名 appid+q+salt+密钥 的MD5值 详细请看文档
	sign = appid + trans_query + str(salt) + secretKey
	m1 = hashlib.md5()
	m1.update(sign.encode('utf-8'))
	sign = m1.hexdigest()



	# 完整URL地址
	url = bash_url.format(trans_query=trans_query,trans_from=trans_from,trans_to=trans_to,
		appid=appid,salt=salt,sign=sign)
	# 请求 结果以json形式返回
	req = requests.get(url)
	# 将str类型的数据转成dict
	data = json.loads(req.text)
	# 获取结果并输出
	src = data['trans_result'][0]['src']
	dst = data['trans_result'][0]['dst']

	print ('原 词 语：%s' % src)
	print ('翻译结果：%s' % dst)


def main():


	# 可用翻译语言
	trans_language = {
		'中文':'zh','英语':'en','粤语':'yue','文言文':'wyw','日语':'jp',
		'韩语':'kor','法语':'fra','西班牙语':'spa','泰语':'th','阿拉伯语':'ara',
		'俄语':'ru','葡萄牙语':'pt','德语':'de','意大利语':'it','希腊语':'el',
		'荷兰语':'nl','波兰语':'pl','保加利亚语':'bul','爱沙尼亚语':'est',
		'丹麦语':'dan','芬兰语':'fin','捷克语':'cs','罗马尼亚语':'rom',
		'斯洛文尼亚语':'slo','瑞典语':'swe','匈牙利语':'hu','繁体中文':'cht','越南语':'vie',
		}
	# 先定义语言列表变量
	language_list = []
	# 先定义翻译的语言变量
	trans_to = ''
	for i in trans_language:
		language_list.append(i)
	print ("可以翻译的语言如下:")
	# 一行显示四个语言
	for n in range(0,len(language_list),4):
		print ('%s.%s %s.%s %s.%s %s.%s \n' % (n,language_list[n],n+1,language_list[n+1],n+2,language_list[n+2],n+3,language_list[n+3]))

	trans_language_num = input('请输入要翻译的语言的编号按ENTER继续(默认为中文，输入q退出)：')
	# 判断翻译语言是否有输入，如果没输入就默认中文
	if trans_language_num != '':
		# 判断是否为数字
		if trans_language_num.isdigit():
			# 判断输入的数字是否小于列表的长度
			if int(trans_language_num) < len(language_list):
				# 有输入翻译语言，通过输入的数字获取列表中的对应的语言
				language = language_list[int(trans_language_num)]
				# 通过上面获取的语言在字典中获取对应的值
				trans_to = trans_language[language]
			else:
				print ('\n请输入翻译语言对应的数字\n')
				return main()	
		elif trans_language_num == 'q':
			sys.exit('退出运行')			
		else:
			print ('\n请输入翻译语言对应的数字\n')
			return main()			
	
	# 要输入翻译内容
	while True:
		trans_query = input('请输入要翻译的内容按ENTER继续(输入q退出)：')
		# 判断是否输入内容，如果输入q就退出，如果有内容就退出循环
		if trans_query != '' :
			if trans_query == 'q':
				sys.exit('退出运行')
			else:
				break

	# 判断翻译语言是否为空	
	if trans_to != '':
		baidu_trans(trans_query,trans_to=trans_to)
	else:
		baidu_trans(trans_query)


if __name__ == '__main__':
	try:
		print (' 百 度 翻  译 \n')
		main()
	except KeyboardInterrupt:
		sys.exit('\n退出运行')
