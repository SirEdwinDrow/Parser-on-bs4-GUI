# Parser-on-bs4-GUI
Paser on bs4 with GUI/Парсер на bs4 с GUI

# Web Parser Application / Веб-парсер

## ⚠️ Disclaimer / Отказ от ответственности

### English
**Important Legal Notice**:  
This software is provided for educational and legitimate web scraping purposes only. The developers and contributors are not responsible for any misuse of this application. Users are solely responsible for complying with:
- Website terms of service
- robots.txt files
- Copyright laws
- Data protection regulations (GDPR, CCPA, etc.)
- Any other applicable laws

Always obtain proper authorization before scraping any website. Unauthorized scraping may violate laws and website terms.

### Русский
**Важное юридическое уведомление**:  
Данное программное обеспечение предоставляется только в образовательных целях и для законного веб-скрапинга. Разработчики и участники проекта не несут ответственности за неправомерное использование этого приложения. Пользователи самостоятельно несут ответственность за соблюдение:
- Условий использования веб-сайтов
- Файлов robots.txt
- Законов об авторском праве
- Регламентов защиты данных (GDPR, CCPA и др.)
- Иных применимых законов

Всегда получайте соответствующее разрешение перед сканированием веб-сайтов. Несанкционированный парсинг может нарушать законы и условия использования сайтов.

## English Documentation

### Overview
A GUI application for web scraping built with PyQt6 that allows users to:
- Enter any website URL to scrape
- Customize and add new CSS selectors
- View results in a table format
- Save extracted data to a text file

### Features
- **URL Input**: Specify the target website
- **Selector Management**:
  - View existing selectors in a table
  - Add new selectors with custom:
    - Field name
    - HTML tag
    - Class name
    - Attribute (optional)
- **Results Display**: Clean table presentation of scraped data
- **Export**: Save results to a text file with formatting

### Usage
1. Enter the target URL
2. Configure selectors (default selectors are provided)
3. Click "Run Parser" to extract data
4. View results in the table
5. Click "Save to File" to export

### Requirements
- Python 3.x
- PyQt6
- BeautifulSoup4
- urllib

### Installation
```bash
pip install PyQt6 beautifulsoup4
```

## Русская документация

### Обзор
GUI приложение для веб-скрапинга на PyQt6, позволяющее:
- Вводить любой URL сайта для парсинга
- Настраивать и добавлять CSS селекторы
- Просматривать результаты в таблице
- Сохранять извлеченные данные в текстовый файл

### Возможности
- **Ввод URL: Указание целевого сайта
- **Управление селекторами:**:
  - Просмотр существующих селекторов в таблице
  - Добавление новых селекторов с настройкой:
    - Названия поля
    - HTML тега
    - Имени класса
    - Атрибута (опционально)
- **Отображение результатов**: Удобная таблица с данными.
- **Экспорт**: Сохранение в текстовый файл с форматированием

### Использование
1. Введите URL
2. Настройте селекторы (имеются по умолчанию)
3. Нажмите "Запустить парсинг" для извлечения данных
4. Просмотрите результаты в таблице
5. Нажмите "Сохранить в файл" для экспорта

### Требования
- Python 3.x
- PyQt6
- BeautifulSoup4
- urllib

### Установка
```bash
pip install PyQt6 beautifulsoup4
```
