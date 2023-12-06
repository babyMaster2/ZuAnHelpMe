import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import random
import keyboard
import time
from .menu import MenuActions


class MyMainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = loadUi("./ui/main.ui", self)
        self.ui.show()
        # 初始化计数器值
        self.lcdNumber_1_count = 0
        self.lcdNumber_2_count = 0
        self.lcdNumber_3_count = 0
        # 注册全局热键 F2
        keyboard.add_hotkey('F2', self.on_f2_pressed)
        # 注册全局热键 F3
        keyboard.add_hotkey('F3', self.on_f3_pressed)
        # 注册全局热键 F12
        keyboard.add_hotkey('F12', self.on_f12_pressed)

        # 创建菜单项
        self.menu_actions = MenuActions(self)

    def keyPressEvent(self, event):
        # 处理其他按键的逻辑
        pass

    def on_f2_pressed(self):
        # 处理按下 F2 键的逻辑
        random_text = self.get_random_text_from_file('F2')  # 从文件中随机抽取一条文本
        self.send_text(random_text)  # 发送文本
        self.increment_counter_lcd_1()  # 计数器值加一
        self.update_counter_display('F2')  # 更新计数器显示

    def on_f3_pressed(self):
        random_text = self.get_random_text_from_file('F3')  # 从文件中随机抽取一条文本
        self.send_text(random_text)  # 发送文本
        self.increment_counter_lcd_2()  # 计数器值加一
        self.update_counter_display('F3')  # 更新计数器显示

    def on_f12_pressed(self):
        random_text = self.get_random_text_from_file('F12')  # 从文件中随机抽取一条文本
        self.send_text(random_text)  # 发送文本
        self.increment_counter_lcd_3()  # 计数器值加一
        self.update_counter_display('F12')  # 更新计数器显示

    def get_random_text_from_file(self, hotkey):
        path = './quotes/test_quotes.txt'
        # 从文件中随机抽取一条文本
        if hotkey == 'F2':
            path = './quotes/default_quotes.txt'
        elif hotkey == 'F3':
            path = './quotes/custom_quotes.txt'
        with open(path, 'r+', encoding='utf-8') as f:
            text_library = [line.strip() for line in f.readlines()]
        return random.choice(text_library)

    def send_text(self, text):
        # 在这里实现发送文本的逻辑
        keyboard.press_and_release('enter')
        time.sleep(0.1)
        keyboard.write(text)
        keyboard.press_and_release('enter')

    def increment_counter_lcd_1(self):
        # 计数器值加一
        self.lcdNumber_1_count += 1

    def increment_counter_lcd_2(self):
        self.lcdNumber_2_count += 1

    def increment_counter_lcd_3(self):
        self.lcdNumber_3_count += 1

    def update_counter_display(self, hotkey):
        if hotkey == 'F2':
            # 更新计数器显示
            self.ui.lcdNumber_1.display(self.lcdNumber_1_count)
        elif hotkey == 'F3':
            self.ui.lcdNumber_2.display(self.lcdNumber_2_count)
        elif hotkey == 'F12':
            self.ui.lcdNumber_3.display(self.lcdNumber_3_count)

