# Проект парсинга pep

## Описание проекта
### Проект парсинга pep

С помощью данного парсера пользователь может получить список PEP их тип, статус, количество и общее число Pep.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/ravimb06/scrapy_parser_pep.git
```

```
cd scrapy_parser_pep
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source env/scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Запустить парсер:

```
scrapy crawl pep
```

Файл с результатом выводится в директорию /results.

### Использованные технологии:
- Python 3
- Scrapy

---
## Автор
**[Али Богатырев](https://github.com/ravimb06)**
