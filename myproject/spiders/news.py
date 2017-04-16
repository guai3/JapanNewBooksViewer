import scrapy


class NewsSpider(scrapy.Spider):
    name = "news" # Spiderの名前
    # クロール対象とするドメインのリスト
    allowed_domains = ["news.yahoo.co.jp"]
    start_urls = ['http://news.yahoo.co.jp/']

    def parse(self, response):
        """
        トップページのトピックス一覧から個々のトピックスへのリンクを抜き出して表示する。
        """
        print(response.css('ul.topics a::attr("href")').extract())
