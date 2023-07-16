import requests
import json

from lxml import etree

# 发起网络请求
url = "https://wikiwiki.jp/kancolle/遠征"
response = requests.get(url)

# 解析HTML
html = etree.HTML(response.text)

# 使用XPath定位目标表格
table = html.xpath('//*[@id="content"]/ul[9]/li[6]/div[1]/table')[0]

# 定义存储结果的列表
result = []
ct_tasks = []

tag = ''

# 遍历表格行
for row in table.xpath('.//tr'):
    # 获取每行的单元格
    cells = row.xpath('.//td')
    if len(cells) == 1:
        if cells[0].text:
            if cells[0].text[-2:] == "海域":
                tag = cells[0].text

    if len(cells) == 7:
        # 提取所需信息
        expedition_id = cells[0].text.strip()
        expedition_name = cells[1].text.strip()
        expedition_difficulty = cells[2].text.strip()
        expedition_description = cells[3].xpath('.//span//text()')[0]
        expedition_time = cells[4].text.strip()
        expedition_fuel = cells[5].text.strip()
        expedition_ammo = cells[6].text.strip()

        # 将信息添加到结果列表
        result.append({
            'expedition_id': expedition_id,
            'expedition_name': expedition_name,
            'expedition_difficulty': expedition_difficulty,
            'expedition_description': expedition_description,
            'expedition_time': expedition_time,
            'expedition_fuel': expedition_fuel,
            'expedition_ammo': expedition_ammo,
            'tag': tag
        })

        ct_tasks.append({
            'id': expedition_id,
            'title': expedition_name,
            'time': expedition_time,
            'description': expedition_description,
            'tag': tag
        })

# 将结果输出为JSON文件
with open('json/expeditions.json', 'w', encoding='utf8') as file:
    json.dump(result, file, ensure_ascii=False, indent=4)

with open('json/CT_tasks.json', 'w', encoding='utf8') as file:
    json.dump({"items": ct_tasks}, file, ensure_ascii=False, indent=4)


print("爬取完成并保存为expeditions.json文件。")
