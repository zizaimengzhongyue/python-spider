import config
import urllib.request
import re
import time

#网站 url 和分页
url = config.url
page = config.page

#抓图图片目标数和图片保存路径
target = config.target
path = config.path

count = 1

while count <= target:

    #抓取图片并提取图片路径
    response = urllib.request.urlopen(url + str(page)).read().decode('utf-8')
    regex = '(src|data-lazy)="(https://cdn.pixabay.com.*?)"(.*?class="icon icon_like"></i> (\d+))?'
    matches = re.finditer(regex, response)

    #判断图片点赞数并下载
    for match in matches:
        #处理图片
        image_url = match.group(2)
        image_url = image_url.replace("_340.jpg", "1280.jpg")
        image_like_num = match.group(4)
        if int(image_like_num) >= 100:
            #获取保存路径
            image = urllib.request.urlopen(image_url).read()
            image_path = path + "/" + str(count) + ".jpg"
            print(image_path)
            #保存图片
            ch = open(image_path, 'wb')
            ch.write(image)
            ch.close()
            time.sleep(1)
            count += 1
    
    page += 1

print("finish")
