from PyQt5 import QtWidgets
from wphelper import Ui_Dialog
from PyQt5.QtWidgets import QFileDialog
import mainfunc
# pyuic5 -o srs.py srs1.0.ui


class mywindow(QtWidgets.QWidget, Ui_Dialog):
    def __init__(self):
        super(mywindow, self).__init__()
        self.source_list = ['wallpaperscraft', 'bing']
        self.wallpaperscraft_catalog_list = mainfunc.wallpaperscraft_prepare()

        self.setupUi(self)
        self.progressBar.setValue(0)
        self.DownLoad.clicked.connect(self._download)
        self.comboBox_source.clear()
        self.comboBox_source.currentIndexChanged.connect(self.src_change)
        for index in range(0, len(self.source_list)):
            self.comboBox_source.addItem(self.source_list[index], index)

    def src_change(self):
        src_index = self.comboBox_source.currentIndex()
        if self.source_list[src_index] == "wallpaperscraft":
            self.comboBox_catalog.clear()
            for index in range(0, len(self.wallpaperscraft_catalog_list)):
                self.comboBox_catalog.addItem(self.wallpaperscraft_catalog_list[index], index)
        elif self.source_list[src_index] == "bing":
            self.comboBox_catalog.clear()

    def _download(self):
        # Get config
        src_index = self.comboBox_source.currentIndex()
        if self.source_list[src_index] == "wallpaperscraft":
            catalog_idx = self.comboBox_catalog.currentIndex()
            mainfunc.wallpaperscraft(self.progressBar, self.wallpaperscraft_catalog_list[catalog_idx])
        # num = self.lineEdit_number.text


test = 100

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = mywindow()
    ui.show()
    sys.exit(app.exec_())
