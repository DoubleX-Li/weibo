from scrapy import cmdline

name = 'weibo'
start_uid = '1669282904'    # 谷大白话
cmd = 'scrapy crawl {0} -a uid={uid}'.format(name,uid=start_uid)
cmdline.execute(cmd.split())
