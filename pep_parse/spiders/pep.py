import scrapy
import re
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    # allowed_domains = ['peps.python.org']
    start_urls = ['http://peps.python.org/']

    def parse(self, response):
        all_pep = response.css('[href^="/pep-"]')
        for pep_link in all_pep:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep = response.css('h1.page-title::text').get()
        data = {
            'number': re.search(r'PEP (\d+)...(\w+.+)', pep).group(1),
            'name': re.search(r'PEP (\d+)...(\w+.+)', pep).group(2),
            'status': response.css('abbr::text').get()
        }
        yield PepParseItem(data)
