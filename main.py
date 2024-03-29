import sys
from functools import partial

from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication

from views.yolcuEkle import Ui_MainWindow
from controllers.slots import MainController


class MyWindow(QtWidgets.QMainWindow):

    def upStart(self):

        self.shower=[
            self.ui.ad_shower_lbl,
            self.ui.ad_shower_txt,
            self.ui.soyad_shower_lbl,
            self.ui.soyad_shower_txt,
            self.ui.telNo_shower_lbl,
            self.ui.telNo_shower_txt,
            self.ui.not_shower_lbl,
            self.ui.not_shower_tEdit
        ]

        controller = MainController()

        # temel degiskenler
        self.koltuklar = [
            self.ui.koltuk_1_btn, self.ui.koltuk_2_btn, self.ui.koltuk_3_btn,
            self.ui.koltuk_4_btn, self.ui.koltuk_5_btn, self.ui.koltuk_6_btn,
            self.ui.koltuk_7_btn, self.ui.koltuk_8_btn, self.ui.koltuk_9_btn,
            self.ui.koltuk_10_btn, self.ui.koltuk_11_btn, self.ui.koltuk_12_btn,
            self.ui.koltuk_13_btn, self.ui.koltuk_14_btn, self.ui.koltuk_15_btn,
            self.ui.koltuk_16_btn, self.ui.koltuk_17_btn, self.ui.koltuk_18_btn,
            self.ui.koltuk_19_btn, self.ui.koltuk_20_btn
        ]

        self.koltuk = ""
        self.itemList = [
            self.ui.ad_txt,
            self.ui.soyad_txt,
            self.ui.cinsiyet_cbBox,
            self.ui.dateEdit,
            self.ui.time_cbBox,
            self.ui.telNo_txt,
            self.ui.durak_cbBox,
            self.koltuk,
            self.koltuklar,
            self.shower
        ]

        controller.prepare(items=self.itemList)  # hazırlıklar
        # signals
        self.ui.kaydet_btn.clicked.connect(
            partial(controller.save, items=self.itemList)
        )
        self.ui.dateEdit.clicked.connect(controller.search)
        self.ui.time_cbBox.currentIndexChanged.connect(controller.search)

        for btn in self.koltuklar:
            btn.clicked.connect(
                partial(controller.selectSeat, btn)
            )

    def __init__(self):
        if __name__ == "__main__":
            super(MyWindow, self).__init__()

            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)

            self.upStart()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()
    sys.exit(app.exec())
