from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from db_functions import db


class NoteInfo(object):
    """
        Класс для работы с окном NoteInfo
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
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.textBrowser = QtWidgets.QTextBrowser(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textBrowser)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 180, 381, 33))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.clicked.connect(self.click_delete_note)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        
        self.load_info_note()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def load_info_note(self) -> None:
        """
            Функция load_info_note загружает информацию заметки.

            :param self: Текущий экземпляр объекта.
            :return: None
        """
        db_handler: db.DatabaseHandler = db.DatabaseHandler('./database.db')
        note: list = db_handler.get_note_from_id(self.id_note)
        
        self.label_3.setText(note[1])
        self.textBrowser.setText(note[2])

    def click_delete_note(self) -> None: 
        """
            Функция click_delete_note обрабатывает клик на кнопку delete_note.

            :param self: Текущий экземпляр объекта.
            :return: None
        """
        
        # подключение базы данных
        db_handler: db.DatabaseHandler = db.DatabaseHandler('./database.db')

        # удаление заметки по ID
        db_handler.delete_note(self.id_note)

        # обновление таблицы для получения актуальной информации
        self.note_manager_instance.load_notes()

        return QMessageBox.about(self, 'NoteManager', 'Заметка успешно удалена!')


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "NoteInfo"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">NoteManager</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Title</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\">Note</p></body></html>"))
        self.pushButton.setText(_translate("Form", "Delete Note"))


class NoteInfoWindow(QtWidgets.QMainWindow, NoteInfo):
    """
        Класс для инициализации окна
    """

    def __init__(self, note_manager_instance, *args, obj=None, id_note: int, **kwargs):
        self.id_note = id_note 
        self.note_manager_instance = note_manager_instance
        super(NoteInfoWindow, self).__init__(*args,  **kwargs)
        self.setupUi(self)
