import sqlite3
from datetime import datetime

from PyQt5.QtCore import QDate

selectedSeat = ""  # secili koltuk degiskeni etki alanından dolayı burda tanımlandı.


class MainController:
    db = sqlite3.connect("database/vt.sqlite")  # veritabani baglantisi
    im = db.cursor()  # veritabani imleci

    items = []  # tasarimdan cekilen itemler  (label,button vs)

    def prepare(self, items):  # hazirlik
        self.im.execute("""
            CREATE TABLE IF NOT EXISTS yolcular
            (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            "ad" TEXT,
            "soyad" TEXT,
            "cinsiyet" TEXT,
            "tarih" TEXT,
            "saat" TEXT,
            "telNo" TEXT,
            "durak" TEXT,
            "koltuk" TEXT
            )""")  # veritabni tabloları kontrol ettik.
        self.db.commit()  # veritabanina isle
        print("veritabanı hazır")

        for item in items:  # itemleri cektik !!Gelistirilecek *
            self.items.append(item)

        self.item = {
            "ad": self.items[0],
            "soyad": self.items[1],
            "cinsiyet": self.items[2],
            "tarih": self.items[3],
            "saat": self.items[4],
            "telNo": self.items[5],
            "durak": self.items[6],
            "koltuk": self.items[7],
            "koltuklar": self.items[8],
            "shower": self.items[9]
        }

        print("itemler hazır")

        self.items[3].setSelectedDate(
            QDate(datetime.now().year, datetime.now().month, 1)
        )  # Guncel tarih

        self.search()

    def clear(self, items):  # itemleri temizle
        self.item["ad"].clear()  # ad
        self.item["soyad"].clear()  # soyad
        self.item["cinsiyet"].setCurrentIndex(0)  # cinsiyet
        # self.item["tarih"].setDateTime(QDateTime.currentDateTime())  # tarih
        self.item["saat"].setCurrentIndex(0)  # saat
        self.item["durak"].setCurrentIndex(0)  # durak
        self.item["koltuk"] = ""  # koltuk

    def save(self, items):
        global selectedSeat  # degiskenin degisimden etkilenmesi

        ad = self.item["ad"].text()
        soyad = self.item["soyad"].text()
        cinsiyet = self.item["cinsiyet"].currentText()
        tarih = self.item["tarih"].selectedDate().toString()
        saat = self.item["saat"].currentText()
        telNo = self.item["telNo"].text()
        durak = self.item["durak"].currentText()
        koltuk = selectedSeat

        selectedSeat = ""  # kaydettikten sonra bosa dusmesi icin

        veri = (ad, soyad, cinsiyet, tarih, saat, telNo, durak, koltuk)

        print(veri)
        self.im.execute(
            """INSERT INTO yolcular
                (ad,soyad,cinsiyet,tarih,saat,binis,inis,koltuk)
                VALUES(?,?,?,?,?,?,?,?)""", veri)  # verileri veritabanina gonderdik

        self.db.commit()  # veritabanina isle

        print(
            'ad > ' + ad
            , "soyad > " + soyad
            , "cinsiyet >" + cinsiyet
            , "tarih > " + tarih
            , "saat > " + saat
            , "telNo > " + telNo
            , "durak > " + durak
            , "koltuk > " + koltuk
            , sep="\n"
        )

        self.clear(items)  # itemlerin degerini sifirla
        self.search()  #

    def selectSeat(self, button):
        global selectedSeat
        print("seçiliydi", selectedSeat)
        dolu = False
        self.search()

        self.im.execute(
            "SELECT * FROM yolcular WHERE tarih = ? AND saat = ?",
            [self.item["tarih"].selectedDate().toString(), self.item["saat"].currentText()]
        )

        for s in self.im.fetchall():
            if s[8] == button.objectName():
                print("dolu")
                dolu = True
                self.showDetails(ad=s[1], soyad=s[2], telNO=s[6])
                break
            else:
                print("bos")
                dolu = False
        if not dolu:
            selectedSeat = button.objectName()  # veritabanı kayıt için
            print("secildi", selectedSeat)
            button.setStyleSheet("font: 75 17pt 'Consolas';"
                                 "border: 0px;"
                                 "background-image: url(:/img/img/selected-seat.png);"
                                 "background-position: center;"
                                 "background-repeat: no-repeat;")

    def search(self):
        self.hideDetails()

        for koltuk in self.item["koltuklar"]:
            koltuk.setStyleSheet("font: 75 17pt 'Consolas';"
                                 "border: 0px;"
                                 "background-image: url(:/img/img/free-seat.png);"
                                 "background-position: center;"
                                 "background-repeat: no-repeat;")

        self.im.execute(
            "SELECT * FROM yolcular WHERE tarih = ? AND saat = ?",
            [self.item["tarih"].selectedDate().toString(), self.item["saat"].currentText()]
        )

        for s in self.im.fetchall():
            for koltuk in self.item["koltuklar"]:
                if koltuk.objectName() == s[8]:
                    if s[3] == "Erkek":
                        koltuk.setStyleSheet("font: 75 17pt 'Consolas';"
                                             "border: 0px;"
                                             "background-image: url(:/img/img/male-seat.png);"
                                             "background-position: center;"
                                             "background-repeat: no-repeat;")
                    elif s[3] == "Kadın":
                        koltuk.setStyleSheet("font: 75 17pt 'Consolas';"
                                             "border: 0px;"
                                             "background-image: url(:/img/img/female-seat.png);"
                                             "background-position: center;"
                                             "background-repeat: no-repeat;")
        print("arandı")

    def showDetails(self, ad, soyad, telNO):
        print("Detaylar")
        self.item["shower"][1].setText(ad)
        self.item["shower"][3].setText(soyad)
        self.item["shower"][5].setText(telNO)

        for show in self.item["shower"]:
            show.setHidden(False)

    def hideDetails(self):
        self.item["shower"][1].setText("")
        self.item["shower"][3].setText("")
        self.item["shower"][5].setText("")

        for show in self.item["shower"]:
            show.setHidden(True)

    def autoPlace(self):
        global selectedSeat
        self.im.execute(
            "SELECT * FROM yolcular WHERE tarih = ? AND saat = ? ORDER BY koltuk",
            [self.item["tarih"].selectedDate().toString(), self.item["saat"].currentText()]
        )
        self.results = []

        for s in self.im.fetchall():
            self.results.append(s[8])

        print("autoplace >", self.results)

        for koltuk in self.item["koltuklar"]:
            if koltuk.objectName() in self.results:
                print(koltuk.objectName(), "dolu")
            else:
                print(koltuk.objectName(), "boş")
                selectedSeat = koltuk.objectName()  # veritabanı kayıt için
                print("autoPlace > secildi", selectedSeat)
                break
