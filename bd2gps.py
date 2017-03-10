# -*- coding: utf-8 -*-

try:
    from PyQt5.QtWidgets import (QDialog, QApplication)
    from ui_main5 import Ui_Dialog

    def unicode(s):
        return s
except ImportError:
    from PyQt4.QtGui import (QDialog, QApplication)
    from ui_main4 import Ui_Dialog

from convertor import (
    bd09togcj02,
    gcj02towgs84,
    wgs84togcj02,
    gcj02tobd09)


def bd09towgs84(lng, lat):
    lng, lat = bd09togcj02(lng, lat)
    return gcj02towgs84(lng, lat)


def wgs84tobd09(lng, lat):
    lng, lat = wgs84togcj02(lng, lat)
    return gcj02tobd09(lng, lat)


class MainDlg(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MainDlg, self).__init__(parent)
        self.setupUi(self)

    def start_convert(self):
        self.textEditDst.clear()
        src = unicode(self.textEditSrc.toPlainText())
        lines = src.splitlines()
        for line in lines:
            try:
                line = line.strip()
                lng, lat = line.split(",")
                lng, lat = float(lng.strip()), float(lat.strip())
                if self.bd2Gps.checkState():
                    lng, lat = bd09towgs84(lng, lat)
                else:
                    lng, lat = wgs84tobd09(lng, lat)
                self.textEditDst.insertPlainText("%f,%f\n" % (lng, lat))
            except:
                self.textEditDst.insertPlainText("%s\n" % line)
            # QtWidgets.qApp.processEvents()


def main():
    import sys

    app = QApplication([])
    dialog = MainDlg()
    dialog.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
