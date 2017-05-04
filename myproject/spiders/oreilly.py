import scrapy

from myproject.books import OreillyBook


class NewsSpider(scrapy.Spider):
    name = "oreilly"  # Spiderの名前
    # クロール対象とするドメインのリスト
    allowed_domains = ["www.oreilly.co.jp"]
    start_urls = ['https://www.oreilly.co.jp/catalog']

    def parse(self, response):
        # 発売済みの本一覧から個々の本のリンク先を取得する
        i = 0
        for url in response.css('td.title a::attr("href")').extract():
            i += 1
            yield scrapy.Request(response.urljoin(url), self.parse_books)

    def parse_books(self, response):
        # 本の詳細ページから必要な情報をパースする
        item = OreillyBook()
        item['publisher'] = "O'Reilly"
        item['url'] = response.url
        item['title'] = response.css('title::text').extract_first()
        item['subtitle'] = response.css('subtitle::text').extract_first()
        item['imgurl'] = response.xpath(
            '/html/head/meta[@property="og:image"]').re_first("http.*jpeg")
        yield item
