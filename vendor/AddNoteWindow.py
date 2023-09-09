from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from db_functions import db

class AddNote(object):
    """
        Класс для работы с окном AddNote
    """
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 219)
        self.setWindowIcon(QtGui.QIcon('./icon/ico.ico'))
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 10, 381, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 59, 381, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.textEdit = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 180, 381, 33))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.clicked.connect(self.click_add_note)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def click_add_note(self) -> None: 
        """
            Функция click_add_note обрабатывает клик на кнопку AddNote.

            :param self: Текущий экземпляр объекта.
            :return: None
        """

        # получение заголовка и текста заметки
        title: str = self.lineEdit.text()
        note_text: str = self.textEdit.toPlainText()

        # подключение базы данных
        db_handler: db.DatabaseHandler = db.DatabaseHandler('./database.db')

        # проверка на существование заметки
        if db_handler.is_note_exits(title, note_text): 
            return QMessageBox.about(self, 'NoteManager', 'Такая заметка уже существует!')
        
        # создание заметки
        db_handler.create_note(title, note_text)

        # обновление актуальной информации таблицы
        self.note_manager_instance.load_notes()

        return QMessageBox.about(self, 'NoteManager', 'Заметка успешно создана!')

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Add Note", "Add Note"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">NoteManager</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Title</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\">Note</p></body></html>"))
        self.textEdit.setPlaceholderText(_translate("Form", "Enter your note"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Enter your title note"))
        self.pushButton.setText(_translate("Form", "Add note"))


class AddNoteWindow(QtWidgets.QMainWindow, AddNote):
    """
        Класс для инициализации окна
    """

    def __init__(self, note_manager_instance, *args, obj=None, **kwargs):
        super(AddNoteWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.note_manager_instance = note_manager_instance