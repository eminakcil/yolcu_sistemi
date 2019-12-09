import sys
from functools import partial

from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication

from views.yolcuEkle import Ui_MainWindow
from controllers.slots import MainController

controller = MainController()


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # temel degiskenler
        self.koltuklar = [
            self.ui.koltuk_1_btn,
            self.ui.koltuk_2_btn,
            self.ui.koltuk_3_btn,
            self.ui.koltuk_4_btn,
            self.ui.koltuk_5_btn,
            self.ui.koltuk_6_btn,
            self.ui.koltuk_7_btn,
            self.ui.koltuk_8_btn,
            self.ui.koltuk_9_btn,
            self.ui.koltuk_10_btn,
            self.ui.koltuk_11_btn,
            self.ui.koltuk_12_btn
        ]

        self.koltuk = ""
        self.itemList = [
            self.ui.ad_txt,
            self.ui.soyad_txt,
            self.ui.cinsiyet_cbBox,
            self.ui.dateEdit,
            self.ui.time_cbBox,
            self.ui.binis_txt,
            self.ui.inis_txt,
            self.koltuk,
            self.koltuklar
        ]

        controller.prepare(items=self.itemList)  # hazırlıklar

        # signals
        self.ui.kaydet_btn.clicked.connect(
            partial(controller.save, items=self.itemList)
        )
        self.ui.temizle_btn.clicked.connect(
            partial(controller.temizle, items=self.itemList)
        )
        self.ui.temizle_btn.clicked.connect(
            partial(controller.search)
        )

        self.ui.iptal_btn.clicked.connect(
            QCoreApplication.instance().quit
        )

        self.ui.koltuk_1_btn.clicked.connect(partial(controller.selectSeat, self.ui.koltuk_1_btn))
        self.ui.koltuk_2_btn.clicked.connect(partial(controller.selectSeat, self.ui.koltuk_2_btn))
        self.ui.koltuk_3_btn.clicked.connect(partial(controller.selectSeat, self.ui.koltuk_3_btn))
        self.ui.koltuk_4_btn.clicked.connect(partial(controller.selectSeat, self.ui.koltuk_4_btn))
        self.ui.koltuk_5_btn.clicked.connect(partial(controller.selectSeat, self.ui.koltuk_5_btn))
        self.ui.koltuk_6_btn.clicked.connect(partial(controller.selectSeat, self.ui.koltuk_6_btn))
        self.ui.koltuk_7_btn.clicked.connect(partial(controller.selectSeat, self.ui.koltuk_7_btn))
        self.ui.koltuk_8_btn.clicked.connect(partial(controller.selectSeat, self.ui.koltuk_8_btn))
        self.ui.koltuk_9_btn.clicked.connect(partial(controller.selectSeat, self.ui.koltuk_9_btn))
        self.ui.koltuk_10_btn.clicked.connect(partial(controller.selectSeat, self.ui.koltuk_10_btn))
        self.ui.koltuk_11_btn.clicked.connect(partial(controller.selectSeat, self.ui.koltuk_11_btn))
        self.ui.koltuk_12_btn.clicked.connect(partial(controller.selectSeat, self.ui.koltuk_12_btn))


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()
sys.exit(app.exec())
