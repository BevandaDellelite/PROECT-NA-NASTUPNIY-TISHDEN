from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
from googletrans import Translator

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.translator = Translator()
        self.dictonaty = {'англійська':'en','іспанська':'es','французька':'fr','німецька':'de','італійська':'it'}
        self.ui.comboBox.addItems(['англійська','іспанська','французька','німецька','італійська',])
        self.ui.pushButton.clicked.connect(self.translate_text)
        self.ui.pushButton_2.clicked.connect(self.button_click)
        self.ui.pushButton_3.clicked.connect(self.button_click)
        self.ui.pushButton_4.clicked.connect(self.button_click)
        self.ui.pushButton_5.clicked.connect(self.button_click)
        self.ui.pushButton_6.clicked.connect(self.button_click)
        self.ui.pushButton_7.clicked.connect(self.button_click) 
        self.ui.pushButton_8.clicked.connect(self.button_click)
        self.ui.pushButton_9.clicked.connect(self.button_click)
        self.ui.pushButton_10.clicked.connect(self.button_click)
        self.ui.pushButton_11.clicked.connect(self.button_click)
        self.ui.pushButton_12.clicked.connect(self.button_click)
        self.ui.pushButton_13.clicked.connect(self.button_click)
        self.ui.pushButton_14.clicked.connect(self.button_click)
        self.ui.pushButton_15.clicked.connect(self.button_click)
        self.ui.pushButton_16.clicked.connect(self.button_click)
        self.ui.pushButton_17.clicked.connect(self.button_click)



    def translate_text(self):
        text = self.ui.lineEdit.text()
        l = self.ui.comboBox.currentText()
        lang = self.dictonaty[l]
        if text:
            translated = self.translator.translate(text,dest=lang)
            self.ui.textEdit.setPlainText(translated.text)

    def button_click(self):
        button = self.sender()
        text = button.text()
        if text == 'ce':
            self.ui.lineEdit_2.clear()
        elif text == '=':
            try:
                result = eval(self.ui.lineEdit_2.text())
                self.ui.lineEdit_2.setText(str(result))
            except:
                self.ui.lineEdit_2.setText('Помилка: ')
        else:
            self.ui.lineEdit_2.insert(text)

                

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()