# Scrapy settings for JD project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import os
import time

# 获取当前目录
# PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
BOT_NAME = "JD"

SPIDER_MODULES = ["JD.spiders"]
NEWSPIDER_MODULE = "JD.spiders"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 使用scrapy-redis调度请求队列
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "JD (+http://www.yourdomain.com)"

# 设置item的pipelines
ITEM_PIPELINES = {
    # 'meizitu_crawler.pipelines.BeautySpiderPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400
}
# Obey robots.txt rules
ROBOTSTXT_OBEY = False
REDIS_URL = "redis://127.0.0.1:6379"
# 设置item在redis中的默认存储键
REDIS_ITEMS_KEY = "jd_book:item"
# LOG_LEAVEL = "DEBUG"
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True
DEFAULT_REQUEST_HEADERS = {
              'authority': 'pjapi.jd.com',
              'accept': '*/*',
              'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
              'cache-control': 'no-cache',
              'cookie': '__jdu=1679474714050779597376; areaId=19; ipLoc-djd=19-1601-0-0; PCSYCityID=CN_440000_440100_0; shshshfp=d6bb52a3c5920f1c9b95920b81303574; shshshfpa=e6777635-8e0a-42b5-1711-5902563429d4-1681807242; shshshfpx=e6777635-8e0a-42b5-1711-5902563429d4-1681807242; shshshfpb=fLLAOQdi_KWNz90WD0t4KtQ; unpl=JF8EAMhnNSttWE5TAktVHhMTTwoGW1gAGURXbG8DBl0LHlxVSAYaERl7XlVdXxRKEh9vbxRUXFNPVQ4YCisSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAhwUGE5bUVhdDUoTAmlhDVBVXklSAisDKxUge21QX18LShYzblcEZB8MF1EEHwUdFF1LWlJWWA5OEQNqZgFVW15DUA0dAB0VIEptVw; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_1466af4025fc449cbe297c1bd9ab5028|1681872629791; __jdc=122270672; joyytokem=babel_3sAaxodHF7kfo3s95cjxo2UZUxu2MDFqbU9XUDk5MQ==.W1t3ZmhdW3pnYllfeykeMwYKEGc/HQ1vLltBeXthRlwxZS5bEykbHCsiHjM5NSYYGSpTXRgTYB5ZBCMBFBM=.1dd21dd1; joyya=1681876502.1681876505.20.10lpjuh; __jda=122270672.1679474714050779597376.1679474714.1681874571.1681883118.5; jsavif=1; 3AB9D23F7A4B3CSS=jdd03Z4DG4ME4ON2MDJAS5PKMYKR4JV2Z7B3GPFNE2FAANMAMM2VLNCZKDB74LRLFYQGPVP2TJTTFAA36E6Q3SMLUNUUDTEAAAAMHTAHGDLYAAAAACOLJYDHCUWZE5QX; shshshsID=0050d0d33eb7d05b1e796b77ac698b0d_5_1681883388962; 3AB9D23F7A4B3C9B=Z4DG4ME4ON2MDJAS5PKMYKR4JV2Z7B3GPFNE2FAANMAMM2VLNCZKDB74LRLFYQGPVP2TJTTFAA36E6Q3SMLUNUUDTE; __jdb=122270672.12.1679474714050779597376|5.1681883118',
              'pragma': 'no-cache',
              'referer': 'https://book.jd.com/',
              'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
              'sec-ch-ua-mobile': '?0',
              'sec-ch-ua-platform': '"Windows"',
              'sec-fetch-dest': 'script',
              'sec-fetch-mode': 'no-cors',
              'sec-fetch-site': 'same-site',
              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
            }

DOWNLOAD_DELAY = 1
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "JD.middlewares.JdSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "JD.middlewares.JdDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "JD.pipelines.JdPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"
# LOG_FILE = os.path.join(PROJECT_DIR, 'crawler.log')
# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
