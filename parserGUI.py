import sys
from bs4 import BeautifulSoup
import urllib.request
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QTextEdit, QPushButton, QTableWidget,
                             QTableWidgetItem, QFileDialog, QMessageBox, QTabWidget,
                             QGroupBox, QScrollArea, QFormLayout)
from PyQt6.QtCore import Qt


class ParserApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Web Parser")
        self.setGeometry(100, 100, 800, 600)

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        self.layout = QVBoxLayout()
        self.main_widget.setLayout(self.layout)

        self.create_url_input()
        self.create_selectors_tab()
        self.create_results_section()
        self.create_buttons()

        # Инициализация списка селекторов
        self.selectors = [
            {"name": "title", "selector": "div", "class": "products-view-name products-view-name-default"},
            {"name": "price", "selector": "div", "class": "price"},
            {"name": "href", "selector": "a", "attribute": "href"}
        ]

        self.update_selectors_table()

    def create_url_input(self):
        url_group = QGroupBox("URL для парсинга")
        url_layout = QHBoxLayout()

        self.url_input = QLineEdit("https://example.com")
        self.url_input.setPlaceholderText("Введите URL для парсинга")

        url_layout.addWidget(QLabel("URL:"))
        url_layout.addWidget(self.url_input)

        url_group.setLayout(url_layout)
        self.layout.addWidget(url_group)

    def create_selectors_tab(self):
        self.tabs = QTabWidget()

        # Вкладка существующих селекторов
        self.existing_selectors_tab = QWidget()
        self.existing_layout = QVBoxLayout()

        self.selector_table = QTableWidget()
        self.selector_table.setColumnCount(4)
        self.selector_table.setHorizontalHeaderLabels(["Название", "Тег", "Класс", "Атрибут"])
        self.selector_table.horizontalHeader().setStretchLastSection(True)

        self.existing_layout.addWidget(self.selector_table)
        self.existing_selectors_tab.setLayout(self.existing_layout)

        # Вкладка добавления нового селектора
        self.new_selector_tab = QWidget()
        self.new_selector_layout = QFormLayout()

        self.new_selector_name = QLineEdit()
        self.new_selector_tag = QLineEdit("div")
        self.new_selector_class = QLineEdit()
        self.new_selector_attr = QLineEdit()

        self.new_selector_layout.addRow("Название поля:", self.new_selector_name)
        self.new_selector_layout.addRow("HTML тег:", self.new_selector_tag)
        self.new_selector_layout.addRow("Класс:", self.new_selector_class)
        self.new_selector_layout.addRow("Атрибут (если нужен):", self.new_selector_attr)

        self.add_selector_btn = QPushButton("Добавить селектор")
        self.add_selector_btn.clicked.connect(self.add_new_selector)
        self.new_selector_layout.addRow(self.add_selector_btn)

        self.new_selector_tab.setLayout(self.new_selector_layout)

        self.tabs.addTab(self.existing_selectors_tab, "Существующие селекторы")
        self.tabs.addTab(self.new_selector_tab, "Добавить селектор")

        self.layout.addWidget(self.tabs)

    def create_results_section(self):
        results_group = QGroupBox("Результаты парсинга")
        results_layout = QVBoxLayout()

        self.results_table = QTableWidget()
        self.results_table.setColumnCount(3)
        self.results_table.setHorizontalHeaderLabels(["Название", "Цена", "Ссылка"])
        self.results_table.horizontalHeader().setStretchLastSection(True)

        results_layout.addWidget(self.results_table)
        results_group.setLayout(results_layout)
        self.layout.addWidget(results_group)

    def create_buttons(self):
        buttons_layout = QHBoxLayout()

        self.parse_btn = QPushButton("Запустить парсинг")
        self.parse_btn.clicked.connect(self.run_parser)

        self.save_btn = QPushButton("Сохранить в файл")
        self.save_btn.clicked.connect(self.save_results)

        buttons_layout.addWidget(self.parse_btn)
        buttons_layout.addWidget(self.save_btn)

        self.layout.addLayout(buttons_layout)

    def update_selectors_table(self):
        self.selector_table.setRowCount(len(self.selectors))

        for i, selector in enumerate(self.selectors):
            self.selector_table.setItem(i, 0, QTableWidgetItem(selector["name"]))
            self.selector_table.setItem(i, 1, QTableWidgetItem(selector["selector"]))
            self.selector_table.setItem(i, 2, QTableWidgetItem(selector.get("class", "")))
            self.selector_table.setItem(i, 3, QTableWidgetItem(selector.get("attribute", "")))

    def add_new_selector(self):
        name = self.new_selector_name.text().strip()
        tag = self.new_selector_tag.text().strip()
        class_ = self.new_selector_class.text().strip()
        attr = self.new_selector_attr.text().strip()

        if not name or not tag:
            QMessageBox.warning(self, "Ошибка", "Название и тег обязательны для заполнения")
            return

        new_selector = {"name": name, "selector": tag}
        if class_:
            new_selector["class"] = class_
        if attr:
            new_selector["attribute"] = attr

        self.selectors.append(new_selector)
        self.update_selectors_table()

        # Очищаем поля после добавления
        self.new_selector_name.clear()
        self.new_selector_class.clear()
        self.new_selector_attr.clear()
        self.new_selector_tag.setText("div")

        QMessageBox.information(self, "Успех", "Селектор успешно добавлен")

    def run_parser(self):
        url = self.url_input.text().strip()
        if not url:
            QMessageBox.warning(self, "Ошибка", "Введите URL для парсинга")
            return

        try:
            req = urllib.request.urlopen(url)
            html = req.read()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить страницу: {str(e)}")
            return

        soup = BeautifulSoup(html, 'html.parser')

        # Основной контейнер для элементов
        try:
            news = soup.find_all('div', class_='products-view-item text-static cs-br-1 js-products-view-item')
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось найти основные элементы: {str(e)}")
            return

        results = []

        for item in news:
            result_item = {}
            for selector in self.selectors:
                try:
                    element = item.find(selector["selector"], class_=selector.get("class"))

                    if element:
                        if "attribute" in selector:
                            value = element.get(selector["attribute"])
                        else:
                            value = element.get_text(strip=True)

                        result_item[selector["name"]] = value
                    else:
                        result_item[selector["name"]] = "Не найдено"
                except Exception as e:
                    result_item[selector["name"]] = f"Ошибка: {str(e)}"

            results.append(result_item)

        self.display_results(results)

    def display_results(self, results):
        if not results:
            QMessageBox.information(self, "Информация", "Не найдено ни одного элемента")
            return

        # Определяем заголовки столбцов на основе ключей первого элемента
        headers = list(results[0].keys())
        self.results_table.setColumnCount(len(headers))
        self.results_table.setHorizontalHeaderLabels(headers)

        self.results_table.setRowCount(len(results))

        for row, item in enumerate(results):
            for col, key in enumerate(headers):
                self.results_table.setItem(row, col, QTableWidgetItem(str(item.get(key, ""))))

        QMessageBox.information(self, "Успех", f"Найдено {len(results)} элементов")

    def save_results(self):
        if self.results_table.rowCount() == 0:
            QMessageBox.warning(self, "Ошибка", "Нет данных для сохранения")
            return

        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить результаты", "", "Text Files (*.txt)")
        if not file_path:
            return

        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                headers = [self.results_table.horizontalHeaderItem(i).text() for i in
                           range(self.results_table.columnCount())]

                for row in range(self.results_table.rowCount()):
                    f.write(f'Элемент № {row + 1}\n\n')
                    for col in range(self.results_table.columnCount()):
                        item = self.results_table.item(row, col)
                        f.write(f'{headers[col]}: {item.text() if item else ""}\n')
                    f.write('\n**********************\n')

            QMessageBox.information(self, "Успех", "Результаты успешно сохранены")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить файл: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ParserApp()
    window.show()
    sys.exit(app.exec())