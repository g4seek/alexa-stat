# encoding: utf-8
import os
import urllib2
from bs4 import BeautifulSoup
from datetime import datetime


def fetch_alexa(rank_url, save_dir):
    """
    抓取alexa的排名数据
    :param rank_url: 数据抓取链接
    :param save_dir: 结果保存目录
    """

    # 1. 创建目录,打开文件
    if not os.path.isdir(save_dir):
        os.mkdir(save_dir)
    save_path = save_dir + "/" + datetime.now().strftime("%d") + ".txt"
    save_file = open(save_path, "w+")

    # 2. 读取alexa提供的20页共500条数据
    for i in range(0, 20):
        url = rank_url.format(i)
        html = urllib2.urlopen(url).read()
        # 3. 解析页面html源代码
        soup = BeautifulSoup(html, "html.parser")
        sites = soup.select(".site-listing")
        # 4. 获取列表中每个站点的信息
        for site in sites:
            # 5. 获取排名,站点地址,描述
            rank = site.select(".count")[0].string
            name = site.a.string
            # desc = site.select(".desc-container .description")[0].text.replace("\n", "")
            # line = rank + ":\t" + name + "\t" + desc
            line = name
            # 6. 输出到控制台和文件
            print (rank + ":" + name)
            save_file.write(line.encode("utf-8") + "\n")
    # 7. 关闭文件
    save_file.close()


if __name__ == '__main__':
    # 全球alexa排名
    global_rank_url = "http://www.alexa.com/topsites/global;{0}"
    global_save_dir = "E:/doc/alexa/global/" + datetime.now().strftime("%Y-%m")
    print ("-" * 10 + "global" + "-" * 10)
    fetch_alexa(global_rank_url, global_save_dir)
    print ("-" * 10 + "global" + "-" * 10)

    # 中国alexa排名
    print ("-" * 10 + "china" + "-" * 10)
    china_rank_url = "http://www.alexa.com/topsites/countries;{0}/CN"
    china_save_dir = "E:/doc/alexa/china/" + datetime.now().strftime("%Y-%m")
    fetch_alexa(china_rank_url, china_save_dir)
    print ("-" * 10 + "china" + "-" * 10)
