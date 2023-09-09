import sys, qdarktheme
from PyQt5 import QtWidgets
from vendor.NoteManagerWindow import NoteManagerWindow

# Подключение стилей окна
app = QtWidgets.QApplication(sys.argv)
qdarktheme.setup_theme(custom_colors={"primary": "#D0BCFF"}) 

# Инициализация окна и его показ
window = NoteManagerWindow()
window.show()
app.exec_() 