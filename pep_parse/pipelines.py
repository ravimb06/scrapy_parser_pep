import csv
import datetime as dt

from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.pep_in_each_status = defaultdict(lambda: 0)
        self.results = [('Статус', 'Количество')]

    def process_item(self, item, spider):
        self.pep_in_each_status[item['status']] += 1
        return item

    def close_spider(self, spider):
        self.pep_in_each_status['Total'] = sum(
            self.pep_in_each_status.values())
        for k, v in self.pep_in_each_status.items():
            self.results.append((k, v))
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        now = dt.datetime.now()
        now_formatted = now.strftime('%Y-%m-%dT%H-%M-%S')
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = results_dir / file_name
        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(self.results)
