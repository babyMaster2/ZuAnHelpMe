from PyQt5.QtWidgets import QDialog, QMessageBox, QInputDialog, QApplication
from PyQt5.uic import loadUi


class DocumentLibraryDialog(QDialog):
    def __init__(self, quote):
        self.quote = quote
        self.quote_path = self.get_path()
        super().__init__()
        loadUi("./ui/quotes.ui", self)
        self.load_quotes()
        self.toolButton.clicked.connect(self.add_item)
        self.toolButton_2.clicked.connect(self.delete_item)
        self.toolButton_3.clicked.connect(self.edit_item)
        self.toolButton_4.clicked.connect(self.copy_item)
        self.toolButton_5.clicked.connect(self.push_item)
        self.toolButton_6.clicked.connect(self.paste_item)

    def get_path(self):
        quote_path = './quotes/default_quotes.txt'
        if self.quote == 'test_quotes':
            quote_path = './quotes/test_quotes.txt'
        elif self.quote == 'custom_quotes':
            quote_path = './quotes/custom_quotes.txt'
        return quote_path

    def load_quotes(self):
        try:
            with open(self.quote_path, 'r', encoding='utf-8') as f:
                quotes = [line.strip() for line in f.readlines()]
                self.listWidget.addItems(quotes)
        except FileNotFoundError:
            QMessageBox.warning(self, 'Warning', 'test_quotes.txt not found. No items loaded.')

    def add_item(self):
        # Implement the logic to add an item to the list
        text, ok = QInputDialog.getText(self, '添加', '输入语料:')
        if ok:
            self.listWidget.addItem(text)

            with open(self.quote_path, 'a', encoding='utf-8') as f:
                f.write(text + '\n')

    def delete_item(self):
        # Implement the logic to delete the selected item from the list
        selected_item = self.listWidget.currentItem()
        if selected_item:
            # 获取要删除的文本
            deleted_text = selected_item.text()
            # 从界面上删除选定的项
            self.listWidget.takeItem(self.listWidget.row(selected_item))
            # 从文件中删除对应的文本
            self.remove_text_from_file(deleted_text)

    def remove_text_from_file(self, deleted_text):
        # 根据删除的文本从文件中删除对应的行
        with open(self.quote_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        with open(self.quote_path, 'w', encoding='utf-8') as f:
            for line in lines:
                if line.strip() != deleted_text:
                    f.write(line)

    def edit_item(self):
        # Implement the logic to edit the selected item in the list
        selected_item = self.listWidget.currentItem()
        if selected_item:
            # 获取原始文本
            original_text = selected_item.text()
            # 弹出对话框获取新文本
            new_text, ok = QInputDialog.getText(self, '编辑', '输入语料:', text=original_text)
            if ok:
                # 在界面上更新文本
                selected_item.setText(new_text)
                # 在文件中更新文本
                self.edit_text_in_file(original_text, new_text)

    def edit_text_in_file(self, original_text, new_text):
        # 在内存中读取文件内容
        with open(self.quote_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # 在内存中替换原始文本为新文本
        lines = [line.replace(original_text, new_text) for line in lines]

        # 将更新后的内容写回文件
        with open(self.quote_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)

    def copy_item(self):
        # Implement the logic to copy the selected item from the list
        selected_item = self.listWidget.currentItem()
        if selected_item:
            copied_text = selected_item.text()
            # 将文本复制到剪贴板
            clipboard = QApplication.clipboard()
            clipboard.setText(copied_text)

    def push_item(self):
        # Implement the logic to push the clipboard text to a custom TXT file
        selected_item = self.listWidget.currentItem()
        if selected_item:
            with open('./quotes/custom_quotes.txt', 'a', encoding='utf-8') as f:
                f.write(selected_item.text() + '\n')

    def paste_item(self):
        # Implement the logic to paste the selected item from the list
        clipboard = QApplication.clipboard()
        clipboard_text = clipboard.text()

        if clipboard_text:
            # 添加验证逻辑，确保文本长度少于二十个字
            if len(clipboard_text) <= 20:
                with open(self.quote_path, 'a', encoding='utf-8') as f:
                    f.write(clipboard_text + '\n')

                self.listWidget.addItem(clipboard_text)

            else:
                QMessageBox.warning(self, 'Warning', '长度必须少于二十个字符')
