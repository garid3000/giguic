#  ---------- Base libraries -------------------------------------------------------------------------------------------
#import os
import subprocess as sp

# import logging
import numpy as np
#from numpy._typing import NDArray

from PySide2.QtWidgets import QMainWindow, QWidget, QMessageBox

# from PySide2.QtGui import QKeySequence, QShortcut, QColor
# from PySide2.QtCore import QModelIndex, QDir, Qt

from Custom_UIs.UI_Mainwindow import Ui_MainWindow


path_sscan1    = "/home/pi/SpecSphere/sscan1.py"
path_check_cam = "/home/pi/SpecSphere/check_cam.py"
path_main_from_gui = "/home/pi/SpecSphere/main_from_gui.py"
path_bno = "/home/pi/SpecSphere/gry_bno08x.py"

class TheMainWindow(QMainWindow):
    expo_v4l2 = (1, 2, 5, 10, 20, 39, 78, 156, 312, 625, 1250, 2500)

    def __init__(self, parent: QWidget | None = None) -> None:
        super(TheMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.d_azi.valueChanged.connect(lambda: self.ui.sp_azi.setValue(self.ui.d_azi.value()))
        self.ui.d_elv.valueChanged.connect(lambda: self.ui.sp_elv.setValue(self.ui.d_elv.value()))
        self.ui.d_expo.valueChanged.connect(lambda: self.ui.sp_expo.setValue(self.expo_v4l2[self.ui.d_expo.value()]))
        self.ui.d_gain.valueChanged.connect(lambda: self.ui.sp_gain.setValue(self.ui.d_gain.value()))

        self.ui.sp_azi.valueChanged.connect(self.when_manual_azi_changed)
        self.ui.sp_elv.valueChanged.connect(self.when_manual_elv_changed)
        self.ui.sp_expo.valueChanged.connect(self.when_manual_expo_changed)
        self.ui.sp_gain.valueChanged.connect(self.when_manual_gain_changed)

        self.ui.hs_azi_0.valueChanged.connect(lambda: self.ui.sb_azi_0.setValue(-self.ui.hs_azi_0.value()))
        self.ui.hs_azi_1.valueChanged.connect(lambda: self.ui.sb_azi_1.setValue( self.ui.hs_azi_1.value()))
        self.ui.hs_elv_0.valueChanged.connect(lambda: self.ui.sb_elv_0.setValue(-self.ui.hs_elv_0.value()))
        self.ui.hs_elv_1.valueChanged.connect(lambda: self.ui.sb_elv_1.setValue( self.ui.hs_elv_1.value()))

        self.ui.sb_azi_0.valueChanged.connect(self.when_measure_cmd_change)
        self.ui.sb_azi_1.valueChanged.connect(self.when_measure_cmd_change)
        self.ui.sb_elv_0.valueChanged.connect(self.when_measure_cmd_change)
        self.ui.sb_elv_1.valueChanged.connect(self.when_measure_cmd_change)
        self.ui.qe_tag.textChanged.connect(self.when_measure_cmd_change)

        self.ui.pb_send_cmd.clicked.connect(self.send_cmd)
        self.ui.pb_capture_shot.clicked.connect(self.when_capture_shot)


        self.ui.pb_get_cam0.clicked.connect(lambda: self.download_img_and_show(0))
        self.ui.pb_get_cam1.clicked.connect(lambda: self.download_img_and_show(2))


    def when_manual_azi_changed(self) -> None:
        self.ui.le_cmd2send.setText(
            f"ssh pi@{self.ui.ip_1.value()}.{self.ui.ip_2.value()}.{self.ui.ip_3.value()}.{self.ui.ip_4.value()}"
            f" python3 {path_sscan1} azi={self.ui.sp_azi.value()} elv={self.ui.sp_elv.value()} wait=yes"
        )

    def when_manual_elv_changed(self) -> None:
        self.ui.le_cmd2send.setText(
            f"ssh pi@{self.ui.ip_1.value()}.{self.ui.ip_2.value()}.{self.ui.ip_3.value()}.{self.ui.ip_4.value()}"
            f" python3 {path_sscan1} azi={self.ui.sp_azi.value()} elv={self.ui.sp_elv.value()} wait=yes"
        )

    def when_manual_expo_changed(self) -> None:
        self.ui.le_cmd2send.setText(
            f"ssh pi@{self.ui.ip_1.value()}.{self.ui.ip_2.value()}.{self.ui.ip_3.value()}.{self.ui.ip_4.value()}" 
            f" v4l2-ctl -d0 -c exposure_time_absolute={self.ui.sp_expo.value()}"
        )

    def when_manual_gain_changed(self) -> None:
        self.ui.le_cmd2send.setText(
            f"ssh pi@{self.ui.ip_1.value()}.{self.ui.ip_2.value()}.{self.ui.ip_3.value()}.{self.ui.ip_4.value()}" 
            f" v4l2-ctl -d0 -c gain={self.ui.sp_gain.value()}"
        )

    def when_measure_cmd_change(self) -> None:
        self.ui.le_cmd2send.setText(
            f"ssh pi@{self.ui.ip_1.value()}.{self.ui.ip_2.value()}.{self.ui.ip_3.value()}.{self.ui.ip_4.value()}" 
            f" tmux send -t py.0 "
            f" 'python3 {path_main_from_gui}" 
            f" azi0={self.ui.sb_azi_0.value()}"
            f" azi1={self.ui.sb_azi_1.value()} "
            f" elv0={self.ui.sb_elv_0.value()}" 
            f" elv1={self.ui.sb_elv_1.value()} "
            f" ddir={self.ui.qe_tag.text().replace(' ', '_')}'"
            f" ENTER"
        )

    def when_capture_shot(self) -> None:
        self.ui.le_cmd2send.setText(
            f"ssh pi@{self.ui.ip_1.value()}.{self.ui.ip_2.value()}.{self.ui.ip_3.value()}.{self.ui.ip_4.value()}" 
            f" python3 {path_check_cam}" 
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

    def download_img_and_show(self, index:int) -> None:
        results = sp.run(
            ["scp", f"pi@{self.ui.ip_1.value()}.{self.ui.ip_2.value()}.{self.ui.ip_3.value()}.{self.ui.ip_4.value()}:/tmp/cam{index}.npy", f"/tmp/cam{index}.npy"],
            capture_output=True,
            text=True,
        )
        self.subprocess_status(results)

        self.ui.text_output.setText(
            results.stdout + "--------------------------\n" + results.stderr
        )
        img = np.load(f"/tmp/cam{index}.npy")[:, :, 0].T#.reshape(480, 640, 1, 3)

        self.ui.image_view.setImage(
            img=img,
            #levels=img.max(),
            #axes={"x":1, "y":0, "c":2}
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


        
