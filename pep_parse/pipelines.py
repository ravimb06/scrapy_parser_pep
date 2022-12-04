# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from collections import defaultdict
from .utils import file_output


pep_in_each_status = defaultdict(lambda: 0)
results = [('Статус', 'Количество')]


class PepParsePipeline:
    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        pep_in_each_status[item['status']] += 1
        return item

    def close_spider(self, spider):
        pep_in_each_status['Total'] = sum(pep_in_each_status.values())
        for k, v in pep_in_each_status.items():
            results.append((k, v))
        file_output(results)
