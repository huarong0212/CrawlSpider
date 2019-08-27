# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from crawlspider.items import CrawlspiderItem
import re


class CrawlspiderSpider(CrawlSpider):
    name = 'Crawlspider'
    allowed_domains = ['sbiquge.com']
    start_urls = ['https://www.sbiquge.com/biqukan/']

    rules = (
        Rule(LinkExtractor(allow=r'/\d+?_\d+?/',unique=True), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        chap_list = response.xpath('.//*[@class="listmain"]/dl/dd')
        for chapter in chap_list:
            print('aaaaa00000000')
            novel_name = chapter.xpath('//*[@id="book"]/div[1]/div/a[2]/text()').extract_first()
            chapter_name = chapter.xpath('./a/text()').extract_first()
            chapter_link = chapter.xpath('./a/@href').extract_first()

            if chapter_name:
                print('a00000000')
                print(chapter_name)
                item = CrawlspiderItem(chapter_title=chapter_name,novel_name=novel_name)
                url = response.urljoin(chapter_link)
                request = scrapy.Request(url=url,callback=self.parse_body)
                request.meta['key'] = item
                yield request

    def parse_body(self,response):
        item = response.meta['key']
        content_list = response.xpath('.//*[@id="content"]') # 匹配到的是一个列表
        print('aaaaaaaaaa')
        print(content_list)
        print('bbbbbbbbbb')
        content_list = content_list.re('([\u4e00-\u9fa5]|<br>)+?')
        print(content_list)
        print('ccccccccc')
        # 利用re直接匹配小说的汉字内容.正则可以匹配标签下的任何内容，这样我们可以提取我们想要的数据
        content_str = ''.join(content_list)
        content = re.sub('<br><br>','\n  ',content_str)
        # 对匹配的章节进行分段
        item['content'] = content
        yield item
        # item = {}
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
