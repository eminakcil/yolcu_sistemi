from PyQt5.QtCore import QDateTime
import sqlite3

selectedSeat = ""


class MainController:
    db = sqlite3.connect("database/vt.sqlite")
    im = db.cursor()

    items = []

    def prepare(self, items):
        self.im.execute("""
            CREATE TABLE IF NOT EXISTS yolcular
            (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            "ad" TEXT,
            "soyad" TEXT,
            "cinsiyet" TEXT,
            "tarih" TEXT,
            "saat" TEXT,
            "binis" TEXT,
            "inis" TEXT,
            "koltuk" TEXT
            )""")
        self.db.commit()
        print("veritabanı hazır")

        for item in items:
            self.items.append(item)
        print("itemler hazır")

        print(self.items[7])
        self.search()

    def temizle(self, items):
        items[0].clear()
        items[1].clear()
        items[2].setCurrentIndex(0)
        items[3].setDateTime(QDateTime.currentDateTime())
        items[4].setCurrentIndex(0)
        items[5].clear()
        items[6].clear()
        items[7] = ""

    def save(self, items):
        ad = items[0].text()
        soyad = items[1].text()
        cinsiyet = items[2].currentText()
        tarih = items[3].text()
        saat = items[4].currentText()
        binis = items[5].toPlainText()
        inis = items[6].toPlainText()
        koltuk = selectedSeat
        veri = (ad, soyad, cinsiyet, tarih, saat, binis, inis, koltuk)

        print(veri)
        self.im.execute(
            """INSERT INTO yolcular
                (ad,soyad,cinsiyet,tarih,saat,binis,inis,koltuk)
                VALUES(?,?,?,?,?,?,?,?)""", veri)

        self.db.commit()

        print(
            'ad > ' + ad
            , "soyad > " + soyad
            , "cinsiyet >" + cinsiyet
            , "tarih > " + tarih
            , "saat > " + saat
            , "binis > " + binis
            , "inis > " + inis
            , "koltuk > " + koltuk
            , sep="\n"
        )

        self.temizle(items)
        self.search()

    def selectSeat(self, button):
        global selectedSeat
        print("seçiliydi", selectedSeat)
        dolu = False
        self.search()

        self.im.execute("SELECT * FROM yolcular WHERE tarih = '07.12.2019'")

        for s in self.im.fetchall():
            if s[8] == button.objectName():
                print("dolu")
                dolu = True
                break
            else:
                print("bos")
                dolu = False
        if not dolu:
            selectedSeat = button.objectName()  # veritabanı kayıt için
            print("secildi", selectedSeat)
            button.setStyleSheet("background-image: url(resources/img/selected-seat.png);\n"
                                 "background-position:center;\n"
                                 "background-repeat: no-repeat;")

    def search(self):
        for koltuk in self.items[8]:
            koltuk.setStyleSheet("background-image: url(resources/img/free-seat.png);\n"
                                 "background-position:center;\n"
                                 "background-repeat: no-repeat;")

        self.im.execute("SELECT * FROM yolcular WHERE tarih = '07.12.2019'")

        for s in self.im.fetchall():
            # print(s[8],s[3])

            for koltuk in self.items[8]:
                if koltuk.objectName() == s[8]:
                    if s[3] == "Erkek":
                        koltuk.setStyleSheet("background-image: url(resources/img/male-seat.png);\n"
                                             "background-position:center;\n"
                                             "background-repeat: no-repeat;")
                    elif s[3] == "Kadın":
                        koltuk.setStyleSheet("background-image: url(resources/img/female-seat.png);\n"
                                             "background-position:center;\n"
                                             "background-repeat: no-repeat;")
        print("arandı")