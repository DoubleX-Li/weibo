from scrapy import cmdline

name = 'weibo'
# start_uid = '1669282904'    # 谷大白话
# cmd = 'scrapy crawl {name} -s JOBDIR=crawls/{name}-1 -a uid={uid}'.format(name=name,uid=start_uid)
cmd = 'scrapy crawl {name} -s JOBDIR=crawls/{name}-1'.format(name=name)
cmdline.execute(cmd.split())
