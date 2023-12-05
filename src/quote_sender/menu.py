# menu_actions.py
from PyQt5.QtWidgets import QAction, QDialog
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.uic import loadUi
from .LibraryDialog import DocumentLibraryDialog


class QQDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = loadUi("./ui/qq.ui", self)
        self.ui.show()


class MenuActions:
    def __init__(self, main_window):
        self.main_window = main_window

        # 创建 Github 菜单项
        github_action = QAction("GitHub", main_window)
        github_action.triggered.connect(self.github_triggered)
        main_window.ui.menu_github.addAction(github_action)

        # 创建 QQ 菜单项
        qq_action = QAction("QQ", main_window)
        qq_action.triggered.connect(self.qq_triggered)
        main_window.ui.menu_qq.addAction(qq_action)

        # 绑定词库
        default_quotes_action = QAction("默认词库", main_window)
        default_quotes_action.triggered.connect(self.bind_default_quotes)
        main_window.ui.menusetting.addAction(default_quotes_action)

        custom_quotes_action = QAction("自定义词库", main_window)
        custom_quotes_action.triggered.connect(self.bind_custom_quotes)
        main_window.ui.menusetting.addAction(custom_quotes_action)

        test_quotes_action = QAction("测试词库", main_window)
        test_quotes_action.triggered.connect(self.bind_test_quotes)
        main_window.ui.menusetting.addAction(test_quotes_action)

    def github_triggered(self):
        # 打开 GitHub 页面
        url = QUrl("https://github.com/your_github_repo")  # 请替换为你的 GitHub 仓库链接
        QDesktopServices.openUrl(url)

    def qq_triggered(self):
        # 打开 QQ页面
        dialog = QQDialog()
        dialog.exec_()

    def bind_default_quotes(self):
        dialog = DocumentLibraryDialog('default_quotes')
        dialog.exec_()

    def bind_custom_quotes(self):
        dialog = DocumentLibraryDialog('custom_quotes')
        dialog.exec_()

    def bind_test_quotes(self):
        dialog = DocumentLibraryDialog('test_quotes')
        dialog.exec_()







