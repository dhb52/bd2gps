# -*- coding: utf-8 -*-

from ui_main import Ui_Dialog

from PyQt5 import QtWidgets

from convertor import bd09towgs84, wgs84tobd09


class MainDlg(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MainDlg, self).__init__(parent)
        self.setupUi(self)

    def start_convert(self):
        self.textEditDst.clear()
        src = self.textEditSrc.toPlainText()
        lines = src.splitlines()
        for line in lines:
            try:
                line = line.strip()
                lng, lat = line.split(",")
                lng, lat = float(lng.strip()), float(lat.strip())
                lng, lat = bd09towgs84(
                    lng, lat) if self.bd2Gps.checkState() else wgs84tobd09(lng, lat)
                self.textEditDst.insertPlainText("%f,%f\n" % (lng, lat))
            except:
                self.textEditDst.insertPlainText("%s\n" % line)
            QtWidgets.qApp.processEvents()


def main():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    dialog = MainDlg()
    dialog.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
