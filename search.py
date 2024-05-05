import json

# Завантаження даних з файлів authors.json та quotes.json
with open('authors.json', 'r', encoding='utf-8') as f:
    authors = json.load(f)

with open('quotes.json', 'r', encoding='utf-8') as f:
    quotes = json.load(f)

def search_quotes_by_author(author):
    found_quotes = [quote['quote'] for quote in quotes if quote['author'] == author]
    return found_quotes

def search_quotes_by_tag(tag):
    found_quotes = [quote['quote'] for quote in quotes if tag in quote['tags']]
    return found_quotes

def search_quotes_by_tags(tags):
    tags = tags.split(',')
    found_quotes = [quote['quote'] for quote in quotes if any(tag in quote['tags'] for tag in tags)]
    return found_quotes

while True:
    command = input("Введіть команду (name: <ім'я автора>, tag: <тег>, tags: <теги>, exit): ").strip()
    
    if command.startswith('name:'):
        author_name = command.split(':')[1].strip()
        quotes_by_author = search_quotes_by_author(author_name)
        for quote in quotes_by_author:
            print(quote.encode('utf-8'))
    elif command.startswith('tag:'):
        tag = command.split(':')[1].strip()
        quotes_by_tag = search_quotes_by_tag(tag)
        for quote in quotes_by_tag:
            print(quote.encode('utf-8'))
    elif command.startswith('tags:'):
        tags = command.split(':')[1].strip()
        quotes_by_tags = search_quotes_by_tags(tags)
        for quote in quotes_by_tags:
            print(quote.encode('utf-8'))
    elif command == 'exit':
        break
    else:
        print("Невідома команда. Доступні команди: 'name:', 'tag:', 'tags:', 'exit'")