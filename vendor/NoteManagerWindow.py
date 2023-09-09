from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from vendor.AddNoteWindow import AddNoteWindow
from db_functions import db


class NoteManager(object):
    """
        Класс для работы с основным окном NoteManager
    """
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(730, 464)
        Form.setFixedSize(730, 464)
        self.setWindowIcon(QtGui.QIcon('./icon/ico.ico'))
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 711, 51))
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
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(180, 70, 391, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.clicked.connect(self.click_add_note)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textChanged.connect(self.search_table)
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(23, 119, 690, 341))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Roboto")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Roboto")
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.clicked.connect(self.click_note_title)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(327)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(23)
        self.verticalLayout_2.addWidget(self.tableWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.load_notes()

    def load_notes(self) -> None:
        """
            Функция load_notes подгружает актуальные заметки в таблицу.

            :param self: Текущий экземпляр объекта.
            :return: None
        """

        # подключение базы данных и получение списка заметок
        db_handler: db.DatabaseHandler = db.DatabaseHandler('./database.db')
        notes: list = db_handler.notes_list()
        
        # получение количества элементов в базе данных
        required_rows: int = len(notes)
        
        # удаление неактуальных элементов из таблицы
        while self.tableWidget.rowCount() > required_rows:
            self.tableWidget.removeRow(self.tableWidget.rowCount() - 1)

        row: int = 0  
        col: int = 0  

        # добавление актуальных элементов в таблицу
        for note in notes:
            if row >= self.tableWidget.rowCount():
                self.tableWidget.insertRow(row)  

            date_item: QTableWidgetItem = QTableWidgetItem()
            date_item.setText(str(note[3]))
            self.tableWidget.setItem(row, col, date_item)

            title_item: QTableWidgetItem = QTableWidgetItem()
            title_item.setText(note[1])
            self.tableWidget.setItem(row, col + 1, title_item)

            col += 2  

            if col >= self.tableWidget.columnCount():
                col = 0  
                row += 1



    def click_note_title(self, item: object) -> None:
        """
            Функция click_note_title обрабатывает клики на items.

            :param self: Текущий экземпляр объекта.
            :return: None
        """

        # проверка на какой столбец из таблицы идет клик
        if item.column() != 1: 
            return 
        
        # подключение базы данных
        db_handler: db.DatabaseHandler = db.DatabaseHandler('./database.db')

        # получение столбца и ряда, по которому произошел клик
        get_item_title: QTableWidgetItem = self.tableWidget.item(item.row(), item.column())
        get_item_date: QTableWidgetItem = self.tableWidget.item(item.row(), 0)

        # получение даты и заголовка 
        date: str = get_item_date.text()
        title: str = get_item_title.text()

        # проверка заголовка и даты на пустоту 
        if title is not None and date is not None: 
            id_note: int = db_handler.get_note(get_item_title.text(), get_item_date.text())[0]
        
        # открытие окна с информацией о заметке
        from vendor.NoteInfoWindow import NoteInfoWindow
        self.window = NoteInfoWindow(self, id_note = id_note)
        self.window.show()

    def search_table(self):
        """
            Функция search_table обрабатывает поле ввода для поиска заметок.

            :param self: Текущий экземпляр объекта.
            :return: None
        """

        # получение текста из QLineEdit
        search_text: str = self.lineEdit.text().lower()

        for row in range(self.tableWidget.rowCount()):
            item_name = self.tableWidget.item(row, 0).text().lower()
            item_value = self.tableWidget.item(row, 1).text().lower()
            if search_text in item_name or search_text in item_value:
                self.tableWidget.setRowHidden(row, False)
            else:
                self.tableWidget.setRowHidden(row, True)


    def click_add_note(self) -> None:
        """
            Функция click_add_note обрабатывает клик на кнопку AddNote и открывает окно AddNoteWindow.

            :param self: Текущий экземпляр объекта.
            :return: None
        """

        self.window = AddNoteWindow(self)
        self.window.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("NoteManager", "NoteManager"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Note Manager</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Add Note"))
        self.label_2.setText(_translate("Form", "Search"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Form", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Form", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Form", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Form", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Form", "10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Date"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Title"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)


class NoteManagerWindow(QtWidgets.QMainWindow, NoteManager):
    """
        Класс для инициализации окна
    """

    def __init__(self, *args, obj=None, **kwargs):
        super(NoteManagerWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.add_note_window = AddNoteWindow(self)