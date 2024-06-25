#  ---------- Base libraries -------------------------------------------------------------------------------------------
#import os
import subprocess as sp

# import logging
import cv2
# import numpy as np
#from numpy._typing import NDArray
from datetime import datetime

from PySide6.QtWidgets import QMainWindow, QWidget, QMessageBox

# from PySide6.QtGui import QKeySequence, QShortcut, QColor
# from PySide6.QtCore import QModelIndex, QDir, Qt

from Custom_UIs.UI_Mainwindow import Ui_MainWindow

path_venv_python = "python3"
#path_venv_python = "/home/pi/.mainvenv/bin/python3"
path_sscan1    = "/home/pi/4Band-Camera/Custom_Libs/sscan1.py"
#path_check_cam = "/home/pi/SpectroSphere/check_cam.py"
path_main_from_gui = "/home/pi/4Band-Camera/py_tab2_8bc_gimbal_manual_2.py"
#path_bno = "/home/pi/SpectroSphere/gry_bno08x.py"

class TheMainWindow(QMainWindow):
    expo_v4l2 = (1, 2, 5, 10, 20, 39, 78, 156, 312, 625, 1250, 2500)

    def __init__(self, parent: QWidget | None = None) -> None:
        super(TheMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.init_expo_dial()
        self.ui.d_azi.valueChanged.connect(lambda: self.ui.sp_azi.setValue(self.ui.d_azi.value()))
        self.ui.d_elv.valueChanged.connect(lambda: self.ui.sp_elv.setValue(self.ui.d_elv.value()))
        self.ui.sp_azi.valueChanged.connect(self.when_manual_azi_changed)
        self.ui.sp_elv.valueChanged.connect(self.when_manual_elv_changed)

        self.ui.hs_azi_0.valueChanged.connect(lambda: self.ui.sb_azi_0.setValue(-self.ui.hs_azi_0.value()))
        self.ui.hs_azi_1.valueChanged.connect(lambda: self.ui.sb_azi_1.setValue( self.ui.hs_azi_1.value()))
        self.ui.hs_elv_0.valueChanged.connect(lambda: self.ui.sb_elv_0.setValue(-(self.ui.hs_elv_0.value()//5*5  )))
        self.ui.hs_elv_1.valueChanged.connect(lambda: self.ui.sb_elv_1.setValue( (self.ui.hs_elv_1.value()//5*5+1)))

        self.ui.sb_azi_0.valueChanged.connect(self.when_measure_cmd_change)
        self.ui.sb_azi_1.valueChanged.connect(self.when_measure_cmd_change)
        self.ui.sb_elv_0.valueChanged.connect(self.when_measure_cmd_change)
        self.ui.sb_elv_1.valueChanged.connect(self.when_measure_cmd_change)
        self.ui.qe_tag.textChanged.connect(self.when_measure_cmd_change)

        self.ui.pb_send_cmd.clicked.connect(self.send_cmd)
        self.ui.pb_get_cam0.clicked.connect(self.download_img_and_show)
        self.ui.b_1shot.clicked.connect(self.when_capture_shot)

    def init_expo_dial(self) -> None:
        self.ui.d_expo_1.valueChanged.connect(lambda: self.ui.sp_expo_1.setValue(self.expo_v4l2[self.ui.d_expo_1.value()]))
        self.ui.d_expo_2.valueChanged.connect(lambda: self.ui.sp_expo_2.setValue(self.expo_v4l2[self.ui.d_expo_2.value()]))
        self.ui.d_expo_3.valueChanged.connect(lambda: self.ui.sp_expo_3.setValue(self.expo_v4l2[self.ui.d_expo_3.value()]))
        self.ui.d_expo_4.valueChanged.connect(lambda: self.ui.sp_expo_4.setValue(self.expo_v4l2[self.ui.d_expo_4.value()]))
        self.ui.d_expo_5.valueChanged.connect(lambda: self.ui.sp_expo_5.setValue(self.expo_v4l2[self.ui.d_expo_5.value()]))
        self.ui.d_expo_6.valueChanged.connect(lambda: self.ui.sp_expo_6.setValue(self.expo_v4l2[self.ui.d_expo_6.value()]))
        self.ui.d_expo_7.valueChanged.connect(lambda: self.ui.sp_expo_7.setValue(self.expo_v4l2[self.ui.d_expo_7.value()]))
        self.ui.d_expo_8.valueChanged.connect(lambda: self.ui.sp_expo_8.setValue(self.expo_v4l2[self.ui.d_expo_8.value()]))
        pass
        self.ui.sp_expo_1.valueChanged.connect(self.when_any_expo_change)
        self.ui.sp_expo_2.valueChanged.connect(self.when_any_expo_change)
        self.ui.sp_expo_3.valueChanged.connect(self.when_any_expo_change)
        self.ui.sp_expo_4.valueChanged.connect(self.when_any_expo_change)
        self.ui.sp_expo_5.valueChanged.connect(self.when_any_expo_change)
        self.ui.sp_expo_6.valueChanged.connect(self.when_any_expo_change)
        self.ui.sp_expo_7.valueChanged.connect(self.when_any_expo_change)
        self.ui.sp_expo_8.valueChanged.connect(self.when_any_expo_change)

    def when_any_expo_change(self) -> None:
        self.ui.le_expo_minus_str.setText(
            f"{self.expo_v4l2[min(11, max(0, (self.ui.d_expo_1.value() + self.ui.spinBox.value())))]},"
            f"{self.expo_v4l2[min(11, max(0, (self.ui.d_expo_2.value() + self.ui.spinBox.value())))]},"
            f"{self.expo_v4l2[min(11, max(0, (self.ui.d_expo_3.value() + self.ui.spinBox.value())))]},"
            f"{self.expo_v4l2[min(11, max(0, (self.ui.d_expo_4.value() + self.ui.spinBox.value())))]},"
            f"{self.expo_v4l2[min(11, max(0, (self.ui.d_expo_5.value() + self.ui.spinBox.value())))]},"
            f"{self.expo_v4l2[min(11, max(0, (self.ui.d_expo_6.value() + self.ui.spinBox.value())))]},"
            f"{self.expo_v4l2[min(11, max(0, (self.ui.d_expo_7.value() + self.ui.spinBox.value())))]},"
            f"{self.expo_v4l2[min(11, max(0, (self.ui.d_expo_8.value() + self.ui.spinBox.value())))]}"
        )


        self.ui.le_expo_base_str.setText(
            f"{self.ui.sp_expo_1.value()},"
            f"{self.ui.sp_expo_2.value()},"
            f"{self.ui.sp_expo_3.value()},"
            f"{self.ui.sp_expo_4.value()},"
            f"{self.ui.sp_expo_5.value()},"
            f"{self.ui.sp_expo_6.value()},"
            f"{self.ui.sp_expo_7.value()},"
            f"{self.ui.sp_expo_8.value()}"
        )

        self.ui.le_expo_plus_str.setText(
            f"{self.expo_v4l2[min(11, max(0, (self.ui.d_expo_1.value() + self.ui.spinBox_2.value())))]},"
            f"{self.expo_v4l2[min(11, max(0, (self.ui.d_expo_2.value() + self.ui.spinBox_2.value())))]},"
            f"{self.expo_v4l2[min(11, max(0, (self.ui.d_expo_3.value() + self.ui.spinBox_2.value())))]},"
            f"{self.expo_v4l2[min(11, max(0, (self.ui.d_expo_4.value() + self.ui.spinBox_2.value())))]},"
            f"{self.expo_v4l2[min(11, max(0, (self.ui.d_expo_5.value() + self.ui.spinBox_2.value())))]},"
            f"{self.expo_v4l2[min(11, max(0, (self.ui.d_expo_6.value() + self.ui.spinBox_2.value())))]},"
            f"{self.expo_v4l2[min(11, max(0, (self.ui.d_expo_7.value() + self.ui.spinBox_2.value())))]},"
            f"{self.expo_v4l2[min(11, max(0, (self.ui.d_expo_8.value() + self.ui.spinBox_2.value())))]}"
        )



    def when_manual_azi_changed(self) -> None:
        self.ui.le_cmd2send.setText(
            f"ssh pi@{self.ui.ip_1.value()}.{self.ui.ip_2.value()}.{self.ui.ip_3.value()}.{self.ui.ip_4.value()}"
            f" {path_venv_python} {path_sscan1} azi={self.ui.sp_azi.value()} elv={self.ui.sp_elv.value()} wait=yes"
            f" expos=0,0,0,0,0,0,0,0"
            f" expos_plus=0,0,0,0,0,0,0,0"
            f" expos_minus=0,0,0,0,0,0,0,0"
        )

    def when_manual_elv_changed(self) -> None:
        self.ui.le_cmd2send.setText(
            f"ssh pi@{self.ui.ip_1.value()}.{self.ui.ip_2.value()}.{self.ui.ip_3.value()}.{self.ui.ip_4.value()}"
            f" {path_venv_python} {path_sscan1} azi={self.ui.sp_azi.value()} elv={self.ui.sp_elv.value()} wait=yes"
            f" expos=0,0,0,0,0,0,0,0"
            f" expos_plus=0,0,0,0,0,0,0,0"
            f" expos_minus=0,0,0,0,0,0,0,0"
        )

    def when_measure_cmd_change(self) -> None:
        self.ui.le_cmd2send.setText(
            f"ssh pi@{self.ui.ip_1.value()}.{self.ui.ip_2.value()}.{self.ui.ip_3.value()}.{self.ui.ip_4.value()}"
            f" tmux send -t py.0 "
            f" '{path_venv_python} {path_main_from_gui}"
            f" azi0={self.ui.sb_azi_0.value()}"
            f" azi1={self.ui.sb_azi_1.value()}"
            f" elv0={-self.ui.sb_elv_0.value()}"
            f" elv1={-self.ui.sb_elv_1.value()}"
            f" expos={self.ui.le_expo_base_str.text()}"
            f" expos_plus={self.ui.le_expo_plus_str.text()}"
            f" expos_minus={self.ui.le_expo_minus_str.text()}"
            f" op_mode=scan"
            f" ddir=/home/pi/{datetime.now().strftime('%y%m%d_%H%M')}_{self.ui.qe_tag.text().replace(' ', '_')}'"
            f" ENTER"
        )


    def when_capture_shot(self) -> None:
        self.ui.le_cmd2send.setText(
            f"ssh pi@{self.ui.ip_1.value()}.{self.ui.ip_2.value()}.{self.ui.ip_3.value()}.{self.ui.ip_4.value()}"
            f" {path_venv_python} {path_main_from_gui}"
            f" elv0=0 elv1=0 azi0=0 azi1=0 ddir=/tmp/asdf op_mode=1shot"
            f" expos={self.ui.le_expo_base_str.text()}"
            f" expos_plus={self.ui.le_expo_plus_str.text()}"
            f" expos_minus={self.ui.le_expo_minus_str.text()}"
        )

    def send_cmd(self) -> None:
        results = sp.run(
            self.ui.le_cmd2send.text().split(),
            capture_output=True,
            text=True,
        )

        self.ui.text_output.setText(
            results.stdout + "--------------------------\n" + results.stderr
        )
        self.subprocess_status(results)

    def download_img_and_show(self) -> None:
        results = sp.run(
            ["scp", f"pi@{self.ui.ip_1.value()}.{self.ui.ip_2.value()}.{self.ui.ip_3.value()}.{self.ui.ip_4.value()}:/tmp/test.png", f"/tmp/test.png"],
            capture_output=True,
            text=True,
        )
        self.subprocess_status(results)

        self.ui.text_output.setText(
            results.stdout + "--------------------------\n" + results.stderr
        )
        img = cv2.imread("/tmp/test.png")
        #np.load(f"/tmp/cam{index}.npy")[:, :, 0].T

        self.ui.image_view.setImage(
            img=img,
            #levels=img.max(),
            axes={"x":1, "y":0, "c":2}
        )

    def subprocess_status(self, results: sp.CompletedProcess[str]):
        dlg = QMessageBox(self)
        if results.returncode == 0:
            dlg.setWindowTitle("Subprocess:")
            dlg.setText(f"stdout: {results.stdout}\n\n stderr: {results.stderr}")
        else:
            dlg.setWindowTitle("Subprocess: (err?)")
            dlg.setText(f"stdout: {results.stdout}\n\n stderr: {results.stderr}")

        button = dlg.exec_()

        if button == QMessageBox.Ok:
            print("OK!")
