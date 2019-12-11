from PyQt5.QtCore import QDateTime
import sqlite3

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
            "binis" TEXT,
            "inis" TEXT,
            "koltuk" TEXT
            )""")  # veritabni tabloları kontrol ettik.
        self.db.commit()  # veritabanina isle
        print("veritabanı hazır")

        for item in items:  # itemleri cektik !!Gelistirilecek
            self.items.append(item)
        print("itemler hazır")

        self.items[3].setDateTime(QDateTime.currentDateTime())  # Guncel tarih

        self.search()

    def clear(self, items):  # itemleri temizle
        items[0].clear()  # ad
        items[1].clear()  # soyad
        items[2].setCurrentIndex(0)  # cinsiyet
        items[3].setDateTime(QDateTime.currentDateTime())  # tarih
        items[4].setCurrentIndex(0)  # sefer
        items[5].clear()  # binis
        items[6].clear()  # inis
        items[7] = ""  # koltuk

    def save(self, items):
        global selectedSeat  # degiskenin degisimden etkilenmesi

        if selectedSeat == "":  # eger koltuk secilmediyse
            self.autoPlace() # otomatik yerlestir

        ad = items[0].text()
        soyad = items[1].text()
        cinsiyet = items[2].currentText()
        tarih = items[3].text()
        saat = items[4].currentText()
        binis = items[5].text()
        inis = items[6].text()
        koltuk = selectedSeat

        selectedSeat = ""  # kaydettikten sonra bosa dusmesi icin

        veri = (ad, soyad, cinsiyet, tarih, saat, binis, inis, koltuk)

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
            , "binis > " + binis
            , "inis > " + inis
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
            [self.items[3].text(), self.items[4].currentText()]
        )

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
            button.setStyleSheet("font: 75 17pt 'Consolas';"
                                 "border: 0px;"
                                 "background-image: url(:/img/img/selected-seat.png);"
                                 "background-position: center;"
                                 "background-repeat: no-repeat;")

    def search(self):
        for koltuk in self.items[8]:
            koltuk.setStyleSheet("font: 75 17pt 'Consolas';"
                                 "border: 0px;"
                                 "background-image: url(:/img/img/free-seat.png);"
                                 "background-position: center;"
                                 "background-repeat: no-repeat;")

        self.im.execute(
            "SELECT * FROM yolcular WHERE tarih = ? AND saat = ?",
            [self.items[3].text(), self.items[4].currentText()]
        )

        for s in self.im.fetchall():
            for koltuk in self.items[8]:
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

    def autoPlace(self):
        global selectedSeat
        self.im.execute(
            "SELECT * FROM yolcular WHERE tarih = ? AND saat = ? ORDER BY koltuk",
            [self.items[3].text(), self.items[4].currentText()]
        )
        self.results = []

        for s in self.im.fetchall():
            self.results.append(s[8])

        print("autoplace >", self.results)

        for koltuk in self.items[8]:
            if koltuk.objectName() in self.results:
                print(koltuk.objectName(), "dolu")
            else:
                print(koltuk.objectName(), "boş")
                selectedSeat = koltuk.objectName()  # veritabanı kayıt için
                print("autoPlace > secildi", selectedSeat)
                break
