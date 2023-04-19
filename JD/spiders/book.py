import json

import scrapy
from scrapy_redis.spiders import RedisSpider
from JD.items import JdItem

# -----2 继承分布式爬虫
# class BookSpider(scrapy.Spider):
class BookSpider(RedisSpider):
    name = "book"
    redis_key = "py21"

    # allowed_domains = ["jd.com"]
    # allowed_domains = ["jd.com"]
    def __init__(self,*args,**kwargs):
        domain = kwargs.pop('domain',"")
        self.allowed_domains = list(filter(None,domain.split(",")))
        super(BookSpider,self).__init__(*args,**kwargs)


    # def start_requests(self):
    #     headers = {
    #           'authority': 'pjapi.jd.com',
    #           'accept': '*/*',
    #           'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    #           'cache-control': 'no-cache',
    #           'cookie': '__jdu=1679474714050779597376; areaId=19; ipLoc-djd=19-1601-0-0; PCSYCityID=CN_440000_440100_0; shshshfp=d6bb52a3c5920f1c9b95920b81303574; shshshfpa=e6777635-8e0a-42b5-1711-5902563429d4-1681807242; shshshfpx=e6777635-8e0a-42b5-1711-5902563429d4-1681807242; shshshfpb=fLLAOQdi_KWNz90WD0t4KtQ; unpl=JF8EAMhnNSttWE5TAktVHhMTTwoGW1gAGURXbG8DBl0LHlxVSAYaERl7XlVdXxRKEh9vbxRUXFNPVQ4YCisSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAhwUGE5bUVhdDUoTAmlhDVBVXklSAisDKxUge21QX18LShYzblcEZB8MF1EEHwUdFF1LWlJWWA5OEQNqZgFVW15DUA0dAB0VIEptVw; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_1466af4025fc449cbe297c1bd9ab5028|1681872629791; __jdc=122270672; joyytokem=babel_3sAaxodHF7kfo3s95cjxo2UZUxu2MDFqbU9XUDk5MQ==.W1t3ZmhdW3pnYllfeykeMwYKEGc/HQ1vLltBeXthRlwxZS5bEykbHCsiHjM5NSYYGSpTXRgTYB5ZBCMBFBM=.1dd21dd1; joyya=1681876502.1681876505.20.10lpjuh; __jda=122270672.1679474714050779597376.1679474714.1681874571.1681883118.5; jsavif=1; 3AB9D23F7A4B3CSS=jdd03Z4DG4ME4ON2MDJAS5PKMYKR4JV2Z7B3GPFNE2FAANMAMM2VLNCZKDB74LRLFYQGPVP2TJTTFAA36E6Q3SMLUNUUDTEAAAAMHTAHGDLYAAAAACOLJYDHCUWZE5QX; shshshsID=0050d0d33eb7d05b1e796b77ac698b0d_5_1681883388962; 3AB9D23F7A4B3C9B=Z4DG4ME4ON2MDJAS5PKMYKR4JV2Z7B3GPFNE2FAANMAMM2VLNCZKDB74LRLFYQGPVP2TJTTFAA36E6Q3SMLUNUUDTE; __jdb=122270672.12.1679474714050779597376|5.1681883118',
    #           'pragma': 'no-cache',
    #           'referer': 'https://book.jd.com/',
    #           'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    #           'sec-ch-ua-mobile': '?0',
    #           'sec-ch-ua-platform': '"Windows"',
    #           'sec-fetch-dest': 'script',
    #           'sec-fetch-mode': 'no-cors',
    #           'sec-fetch-site': 'same-site',
    #           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    #         }
    #     # start_urls = ["https://pjapi.jd.com/book/sort?source=bookSort"]
    #     for url in start_urls:
    #         yield scrapy.Request(url=url, headers=headers, callback=self.parse)
    def parse(self, response):
        headers = {
            'authority': 'list.jd.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'cookie': '__jdu=1679474714050779597376; areaId=19; ipLoc-djd=19-1601-0-0; PCSYCityID=CN_440000_440100_0; shshshfp=d6bb52a3c5920f1c9b95920b81303574; shshshfpa=e6777635-8e0a-42b5-1711-5902563429d4-1681807242; shshshfpx=e6777635-8e0a-42b5-1711-5902563429d4-1681807242; shshshfpb=fLLAOQdi_KWNz90WD0t4KtQ; unpl=JF8EAMhnNSttWE5TAktVHhMTTwoGW1gAGURXbG8DBl0LHlxVSAYaERl7XlVdXxRKEh9vbxRUXFNPVQ4YCisSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAhwUGE5bUVhdDUoTAmlhDVBVXklSAisDKxUge21QX18LShYzblcEZB8MF1EEHwUdFF1LWlJWWA5OEQNqZgFVW15DUA0dAB0VIEptVw; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_1466af4025fc449cbe297c1bd9ab5028|1681872629791; __jdc=122270672; joyya=1681876502.1681876505.20.10lpjuh; jsavif=1; jsavif=1; __jda=122270672.1679474714050779597376.1679474714.1681883118.1681886199.6; xapieid=jdd03Z4DG4ME4ON2MDJAS5PKMYKR4JV2Z7B3GPFNE2FAANMAMM2VLNCZKDB74LRLFYQGPVP2TJTTFAA36E6Q3SMLUNUUDTEAAAAMHTA5LYIAAAAAAD2455T22WI4PX4X; avif=1; __jdb=122270672.8.1679474714050779597376|6.1681886199; shshshsID=b2a5eb8a9517603c3619c94c85ed5559_4_1681887485112; 3AB9D23F7A4B3CSS=jdd03Z4DG4ME4ON2MDJAS5PKMYKR4JV2Z7B3GPFNE2FAANMAMM2VLNCZKDB74LRLFYQGPVP2TJTTFAA36E6Q3SMLUNUUDTEAAAAMHTBHFZCIAAAAAC3U2EPXJFLM2FEX; 3AB9D23F7A4B3C9B=Z4DG4ME4ON2MDJAS5PKMYKR4JV2Z7B3GPFNE2FAANMAMM2VLNCZKDB74LRLFYQGPVP2TJTTFAA36E6Q3SMLUNUUDTE',
            'pragma': 'no-cache',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        }
        info = json.loads(response.text)
        data = info["data"]
        for book_info in data[:1]:
            big_category_name = book_info["categoryName"]
            big_category_id = book_info["fatherCategoryId"]
            sonList = book_info["sonList"]
            for book_data in sonList[:1]:
                book_item = {}
                book_item["big_category_name"] = big_category_name
                book_item["big_category_id"] = big_category_id
                book_item["small_category_name"] = book_data['categoryName']
                book_item["small_category_id"] = book_data['categoryId']
                url = "https://list.jd.com/list.html?cat={},{}".format(str(int(book_item["big_category_id"])),str(int(book_item["small_category_id"])))
                yield scrapy.Request(url=url, headers=headers, callback=self.parse_book,meta = {"jd_book":book_item})



    def parse_book(self,response):
        meta = response.meta["jd_book"]
        book_list = response.xpath('//*[@id="J_goodsList"]/ul/li/div')
        for book_info in book_list:
            item = JdItem()
            item["big_category"] = meta["big_category_name"]
            item["big_category_id"] = meta["big_category_id"]
            item["small_category"] = meta["small_category_name"]
            item["small_category_id"] = meta["small_category_id"]
            item["price"] = book_info.xpath('./div[2]/strong/i/text()').extract_first()
            item["book_name"] = book_info.xpath('./div[3]/a/em/text()').extract_first()
            item["link"] = book_info.xpath('./div[1]/a/@href').extract_first()
            item["author"] = book_info.xpath('./div[4]/span[1]/a/text()').extract_first()
            yield json.dumps(item)


