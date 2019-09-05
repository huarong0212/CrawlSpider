scrapy startproject  项目名

进入项目目录

CrawlSpider类通过一些规则（rules），使对于链接（网页）的爬取更具有通用性，换句话说，CrawlSpider爬虫为通用性的爬虫，而Spider爬虫更像是为一些特殊网站制定的爬虫。

那我们开始正式的讲解一下CrawlSpider爬虫。。。。

首先我们建立一个爬虫工程：

scrapy startproject crawlspider

这个我们很熟悉，接下来创建一个CrawlSpider爬虫

scrapy genspider -t crawl Crawlspider domain.com

注意上面，我们比Spider爬虫建立时多了一个’-t crawl’,这是值爬虫的类 
