# coding=utf-8

'''
作成:みぐりー

◆getLink
　引数：料理名
　返り値：クックパッドのリンク一覧

◆getMaterial
　引数：URL
　返り値：材料

◆getRecipe
　引数：URL
　返り値：手順
'''
import lxml.html
import requests


def getTotalPage(search_url):
	response = requests.get(search_url)
	html = lxml.html.fromstring(response.content)
	return int(str(html.xpath('string(//*[@id="main_content"]/div[1]/div[1]/em)')).replace("品", "").replace(",", ""))


def getLink(Cookname):
	links = []
	url = 'https://cookpad.com/search/' + str(Cookname)

	total = getTotalPage(url)

	if total > 50:
		total = 50

	for page in range(1, int(total / 10) + 1):

		response = requests.get(url + "?page=" + str(page))
		html = lxml.html.fromstring(response.content)

		i = 0
		while True:
			link = html.xpath('//*[@id="recipe_' + str(i) + '"]/div[2]/span[1]/a/@href')
			if str(link) in '[]':
				break
			i += 1
			links.append("https://cookpad.com" + link[0])

	return links


def getMaterial(url):
	materials = {}
	response = requests.get(url)
	html = lxml.html.fromstring(response.content)

	foodstuffs = []
	amounts = []
	i = 1
	while True:
		foodstuff = html.xpath('//*[@id="ingredients_list"]/div[ ' + str(i) + ']/div[1]/span')
		amount = html.xpath('//*[@id="ingredients_list"]/div[' + str(i) + ']/div[2]')

		if str(amount) in '[]':
			break

		if foodstuff[0].text == None:
			foodstuff = html.xpath('//*[@id="ingredients_list"]/div[ ' + str(i) + ']/div[1]/span/a')
		i += 1

		foodstuffs.append(foodstuff[0].text)
		amounts.append(amount[0].text)

		materials.setdefault(foodstuff[0].text, amount[0].text)

	return materials


def getRecipe(url):
	responses = {}
	response = requests.get(url)
	html = lxml.html.fromstring(response.content)

	step = html.xpath('//*[@id="recipe"]/div[4]/@data-step-count')[0]

	for i in range(1, int(step) + 2):
		recipe = html.xpath('string(//*[@id="steps"]/div[' + str(i) + ']/dl/dd/p)')
		text = ''
		for t in recipe:
			if not t == '\n':
				text = text + t

		if not text == '':
			responses.setdefault(int(i) - 1, text)

	return responses