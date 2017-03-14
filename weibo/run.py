from scrapy import cmdline

name = 'weibo'
cmd = 'scrapy crawl {0} -a uid=1669282904'.format(name)
cmdline.execute(cmd.split())
