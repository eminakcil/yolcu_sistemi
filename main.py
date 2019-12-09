import sys
from functools import partial

from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication, pyqtSlot

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
            self.ui.koltuk_1_btn, self.ui.koltuk_2_btn, self.ui.koltuk_3_btn,
            self.ui.koltuk_4_btn, self.ui.koltuk_5_btn, self.ui.koltuk_6_btn,
            self.ui.koltuk_7_btn, self.ui.koltuk_8_btn, self.ui.koltuk_9_btn,
            self.ui.koltuk_10_btn, self.ui.koltuk_11_btn, self.ui.koltuk_12_btn,
            self.ui.koltuk_13_btn, self.ui.koltuk_14_btn, self.ui.koltuk_15_btn,
            self.ui.koltuk_16_btn, self.ui.koltuk_17_btn, self.ui.koltuk_18_btn,
            self.ui.koltuk_19_btn, self.ui.koltuk_20_btn, self.ui.koltuk_21_btn,
            self.ui.koltuk_22_btn, self.ui.koltuk_23_btn, self.ui.koltuk_24_btn,
            self.ui.koltuk_25_btn, self.ui.koltuk_26_btn, self.ui.koltuk_27_btn,
            self.ui.koltuk_28_btn, self.ui.koltuk_29_btn, self.ui.koltuk_30_btn,
            self.ui.koltuk_31_btn, self.ui.koltuk_32_btn, self.ui.koltuk_33_btn,
            self.ui.koltuk_34_btn, self.ui.koltuk_35_btn, self.ui.koltuk_36_btn,
            self.ui.koltuk_37_btn
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

        self.ui.dateEdit.dateChanged.connect(controller.search)
        self.ui.time_cbBox.currentIndexChanged.connect(controller.search)

        #koltuk tiklama fonksiyon koprusu
        for btn in self.koltuklar:
            btn.clicked.connect(
                partial(controller.selectSeat, btn)
            )


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()
sys.exit(app.exec())
