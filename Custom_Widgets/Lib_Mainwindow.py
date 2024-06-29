#  ---------- Base libraries -------------------------------------------------------------------------------------------
import os
import subprocess as sp
import logging
import cv2
import tempfile
# import numpy as np
# from numpy._typing import NDArray
from datetime import datetime
from shlex import split as sh_split

from PySide6.QtWidgets import QMainWindow, QWidget, QMessageBox
# from PySide6.QtGui import QKeySequence, QShortcut, QColor
# from PySide6.QtCore import QModelIndex, QDir, Qt

from Custom_UIs.UI_Mainwindow import Ui_MainWindow

path_venv_python = "python3"
# path_venv_python = "/home/pi/.mainvenv/bin/python3" # might needed in the futrue.
# good for the python library updates
path_sscan1    = "/home/pi/4Band-Camera/Custom_Libs/sscan1.py"
path_main_from_gui = "/home/pi/4Band-Camera/py_tab2_8bc_gimbal_manual_2.py"

logging.basicConfig(
    filename=os.path.join(tempfile.gettempdir(), datetime.now().strftime("Influenza_gui_%Y%m%d_%H%M%S.log")),
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.DEBUG,
)

class TheMainWindow(QMainWindow):
    expo_v4l2 = (1, 2, 5, 10, 20, 39, 78, 156, 312, 625, 1250, 2500)

    def __init__(self, parent: QWidget | None = None) -> None:
        super(TheMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.init_this_pc_network_configs()
        self.init_expo_dial_spinbox_callbacks()
        self.init_intial_exposure_values()
        self.init_motor_dial_spinbox_callbacks()
        self.init_measurement_related_ui_callbacks()

        self.ui.pb_send_cmd.clicked.connect(self.send_cmd_over_ssh)
        self.ui.pb_get_cam0.clicked.connect(self.download_img_and_show)
        self.ui.b_check_tmux.clicked.connect(self.check_tmux_pane)
        self.ui.b_check_dir_tree.clicked.connect(self.check_dir_tree)
        self.ui.b_check_stroge.clicked.connect(self.check_storage)
        self.ui.b_1shot.clicked.connect(self.when_exposure_props_changed_update_cmd)

    def init_this_pc_network_configs(self) -> None:
        self.ui.b_this_pc_get_ip.clicked.connect(self.callback_refresh_network_interfacess_ip_addresses)
        self.ui.cb_this_pc_network_devices.currentIndexChanged.connect(self.when_network_interface_changed)
        self.ui.b_search_ip_for_pi.clicked.connect(self.callback_search_ip_for_pi)
        self.ui.b_ssh_copy_id.clicked.connect(self.callback_ssh_copy_id)

        self.ui.b_hard_reboot.clicked.connect(
            lambda: self.ui.le_cmd2send.setText(
                f"ssh pi@{self.ui.ip_1.value()}.{self.ui.ip_2.value()}.{self.ui.ip_3.value()}.{self.ui.ip_4.value()}"
                " 'sudo reboot' ENTER"
            )
        )
        self.ui.b_soft_reboot.clicked.connect(
            lambda: self.ui.le_cmd2send.setText(
                f"ssh pi@{self.ui.ip_1.value()}.{self.ui.ip_2.value()}.{self.ui.ip_3.value()}.{self.ui.ip_4.value()}"
                " 'pidof bash python3 abduco tmux | xargs kill -9'"
            )
        )

        self.ui.b_terminate_python_processes.clicked.connect(
            lambda: self.ui.le_cmd2send.setText(
                f"ssh pi@{self.ui.ip_1.value()}.{self.ui.ip_2.value()}.{self.ui.ip_3.value()}.{self.ui.ip_4.value()}"
                " 'pidof python3 tmux | xargs kill -9'"
            )
        )

        self.ui.b_tmux_init.clicked.connect(
            lambda: self.ui.le_cmd2send.setText(
                f"ssh pi@{self.ui.ip_1.value()}.{self.ui.ip_2.value()}.{self.ui.ip_3.value()}.{self.ui.ip_4.value()}"
                " 'tmux new -s py -d'"
            )
        )

        self.ui.b_info_dump.clicked.connect(
            lambda: self.ui.le_cmd2send.setText(
                f"ssh pi@{self.ui.ip_1.value()}.{self.ui.ip_2.value()}.{self.ui.ip_3.value()}.{self.ui.ip_4.value()}"
                " 'tmux ls'"
            )
        )


    def when_network_interface_changed(self) -> None:
        try:
            self.ui.l_this_pc_ip.setText(
                self.network_interface2ip[self.ui.cb_this_pc_network_devices.currentText()]
            )

            self.ui.ip_1.setValue(
                int(self.network_interface2ip[self.ui.cb_this_pc_network_devices.currentText()].split(".")[0])
            )
            self.ui.ip_2.setValue(
                int(self.network_interface2ip[self.ui.cb_this_pc_network_devices.currentText()].split(".")[1])
            )
            self.ui.ip_3.setValue(
                int(self.network_interface2ip[self.ui.cb_this_pc_network_devices.currentText()].split(".")[2])
            )

        except Exception:
            logging.debug(Exception)

    def callback_refresh_network_interfacess_ip_addresses(self) -> None:
        """Only linux may be wokr, I don't know about the other windows and macos having ip -breif address command"""
        try:
            self.network_interface2ip = {
                each_interface.split()[0] : each_interface.split()[2].split("/")[0]
                for each_interface in sp.check_output(["ip", "-brief", "address"]).decode().strip().split("\n")
            }
            self.ui.cb_this_pc_network_devices.blockSignals(True)
            self.ui.cb_this_pc_network_devices.clear()
            self.ui.cb_this_pc_network_devices.addItems(
                list(self.network_interface2ip.keys())
            )
            self.ui.cb_this_pc_network_devices.blockSignals(False)

        except Exception:
            logging.debug(Exception)

    def callback_search_ip_for_pi(self) -> None:
        tmp_ip123 = f"{self.ui.ip_1.value()}.{self.ui.ip_2.value()}.{self.ui.ip_3.value()}"

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Run in external terminal")
        dlg.setText(
            "Run following command on new terminal, it'll take ~1min\n"
            f"sudo nmap -p 22 {tmp_ip123}.0/24 | grep {tmp_ip123}"
        )

        button = dlg.exec_()

        if button == QMessageBox.StandardButton.Ok:
            print("OK!")
        

    def callback_ssh_copy_id(self) -> None:
        tmp_ip1234 = f"{self.ui.ip_1.value()}.{self.ui.ip_2.value()}.{self.ui.ip_3.value()}.{self.ui.ip_4.value()}"

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Run in external terminal")
        dlg.setText(
            "Run following command on new terminal\n"
            f"ssh-copy-id pi@{tmp_ip1234}"
        )

        button = dlg.exec_()

        if button == QMessageBox.StandardButton.Ok:
            print("OK!")
        pass


    def init_expo_dial_spinbox_callbacks(self) -> None:
        self.ui.d_expo_1.valueChanged.connect(lambda: self.ui.sp_expo_1.setValue(self.expo_v4l2[self.ui.d_expo_1.value()]))
        self.ui.d_expo_2.valueChanged.connect(lambda: self.ui.sp_expo_2.setValue(self.expo_v4l2[self.ui.d_expo_2.value()]))
        self.ui.d_expo_3.valueChanged.connect(lambda: self.ui.sp_expo_3.setValue(self.expo_v4l2[self.ui.d_expo_3.value()]))
        self.ui.d_expo_4.valueChanged.connect(lambda: self.ui.sp_expo_4.setValue(self.expo_v4l2[self.ui.d_expo_4.value()]))
        self.ui.d_expo_5.valueChanged.connect(lambda: self.ui.sp_expo_5.setValue(self.expo_v4l2[self.ui.d_expo_5.value()]))
        self.ui.d_expo_6.valueChanged.connect(lambda: self.ui.sp_expo_6.setValue(self.expo_v4l2[self.ui.d_expo_6.value()]))
        self.ui.d_expo_7.valueChanged.connect(lambda: self.ui.sp_expo_7.setValue(self.expo_v4l2[self.ui.d_expo_7.value()]))
        self.ui.d_expo_8.valueChanged.connect(lambda: self.ui.sp_expo_8.setValue(self.expo_v4l2[self.ui.d_expo_8.value()]))

        self.ui.sp_expo_1.valueChanged.connect(self.when_any_expo_spinbox_changed_update_hdr_exposure_list_strs)
        self.ui.sp_expo_2.valueChanged.connect(self.when_any_expo_spinbox_changed_update_hdr_exposure_list_strs)
        self.ui.sp_expo_3.valueChanged.connect(self.when_any_expo_spinbox_changed_update_hdr_exposure_list_strs)
        self.ui.sp_expo_4.valueChanged.connect(self.when_any_expo_spinbox_changed_update_hdr_exposure_list_strs)
        self.ui.sp_expo_5.valueChanged.connect(self.when_any_expo_spinbox_changed_update_hdr_exposure_list_strs)
        self.ui.sp_expo_6.valueChanged.connect(self.when_any_expo_spinbox_changed_update_hdr_exposure_list_strs)
        self.ui.sp_expo_7.valueChanged.connect(self.when_any_expo_spinbox_changed_update_hdr_exposure_list_strs)
        self.ui.sp_expo_8.valueChanged.connect(self.when_any_expo_spinbox_changed_update_hdr_exposure_list_strs)

    def init_intial_exposure_values(self) -> None:
        # reason why I put it for code is to maintain dial to spinbox conversion
        # initial spinboxes previouly started from 0
        self.ui.d_expo_1.setValue(5)
        self.ui.d_expo_2.setValue(5)
        self.ui.d_expo_3.setValue(5)
        self.ui.d_expo_4.setValue(5)
        self.ui.d_expo_5.setValue(5)
        self.ui.d_expo_6.setValue(5)
        self.ui.d_expo_7.setValue(5)
        self.ui.d_expo_8.setValue(5)

    def init_motor_dial_spinbox_callbacks(self) -> None:
        self.ui.d_azi.valueChanged.connect(lambda: self.ui.sp_azi.setValue(self.ui.d_azi.value()))
        self.ui.d_elv.valueChanged.connect(lambda: self.ui.sp_elv.setValue(self.ui.d_elv.value()))
        self.ui.sp_azi.valueChanged.connect(self.when_motor_azi_or_elv_spinbox_value_changed)
        self.ui.sp_elv.valueChanged.connect(self.when_motor_azi_or_elv_spinbox_value_changed)

    def init_measurement_related_ui_callbacks(self) -> None:
        self.ui.hs_azi_0.valueChanged.connect(lambda: self.ui.sb_azi_0.setValue(-self.ui.hs_azi_0.value()))
        self.ui.hs_azi_1.valueChanged.connect(lambda: self.ui.sb_azi_1.setValue( self.ui.hs_azi_1.value()))
        self.ui.hs_elv_0.valueChanged.connect(lambda: self.ui.sb_elv_0.setValue(-(self.ui.hs_elv_0.value()//5*5  )))
        self.ui.hs_elv_1.valueChanged.connect(lambda: self.ui.sb_elv_1.setValue( (self.ui.hs_elv_1.value()//5*5+1)))

        self.ui.sb_azi_0.valueChanged.connect(self.when_gimbal_measurement_props_changed_update_cmd)
        self.ui.sb_azi_1.valueChanged.connect(self.when_gimbal_measurement_props_changed_update_cmd)
        self.ui.sb_elv_0.valueChanged.connect(self.when_gimbal_measurement_props_changed_update_cmd)
        self.ui.sb_elv_1.valueChanged.connect(self.when_gimbal_measurement_props_changed_update_cmd)
        self.ui.qe_meas_gimbal_tag.textChanged.connect(
            lambda: self.ui.qe_meas_gimbal_fullpath.setText(
                f'/home/pi/data/gimbal_{datetime.now().strftime("%y%m%d_%H%M")}_{self.ui.qe_meas_gimbal_tag.text().replace(" ", "_")}'
            )
        )
        self.ui.qe_meas_gimbal_fullpath.textChanged.connect(self.when_gimbal_measurement_props_changed_update_cmd)

        self.ui.qe_meas_uav_tag.textChanged.connect(
            lambda: self.ui.qe_meas_uav_fullpath.setText(
                f'/home/pi/data/uav_{datetime.now().strftime("%y%m%d_%H%M")}_{self.ui.qe_meas_uav_tag.text().replace(" ", "_")}'
            )
        )
        self.ui.qe_meas_uav_fullpath.textChanged.connect(self.when_uav_measurement_props_changed_update_cmd)



    def when_any_expo_spinbox_changed_update_hdr_exposure_list_strs(self) -> None:
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

        self.when_exposure_props_changed_update_cmd()

    def when_motor_azi_or_elv_spinbox_value_changed(self) -> None:
        self.ui.le_cmd2send.setText(
            f"ssh pi@{self.ui.ip_1.value()}.{self.ui.ip_2.value()}.{self.ui.ip_3.value()}.{self.ui.ip_4.value()}"
            f" {path_venv_python} {path_sscan1} azi={self.ui.sp_azi.value()} elv={self.ui.sp_elv.value()} wait=yes"
            f" expos=0,0,0,0,0,0,0,0"
            f" expos_plus=0,0,0,0,0,0,0,0"
            f" expos_minus=0,0,0,0,0,0,0,0"
        )

    def when_uav_measurement_props_changed_update_cmd(self) -> None:
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
            f" op_mode=drone"
            f" ddir=/home/pi/{datetime.now().strftime('%y%m%d_%H%M')}_{self.ui.qe_meas_uav_fullpath.text().replace(' ', '_')}'"
            f" ENTER"
        )


    def when_gimbal_measurement_props_changed_update_cmd(self) -> None:
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
            f" ddir=/home/pi/{datetime.now().strftime('%y%m%d_%H%M')}_{self.ui.qe_meas_gimbal_fullpath.text().replace(' ', '_')}'"
            f" ENTER"
        )


    def when_exposure_props_changed_update_cmd(self) -> None:
        self.ui.le_cmd2send.setText(
            f"ssh pi@{self.ui.ip_1.value()}.{self.ui.ip_2.value()}.{self.ui.ip_3.value()}.{self.ui.ip_4.value()}"
            f" {path_venv_python} {path_main_from_gui}"
            f" elv0=0 elv1=0 azi0=0 azi1=0 ddir=/tmp/asdf op_mode=1shot"
            f" expos={self.ui.le_expo_base_str.text()}"
            f" expos_plus={self.ui.le_expo_plus_str.text()}"
            f" expos_minus={self.ui.le_expo_minus_str.text()}"
        )

        self.ui.pb_send_cmd.setText("Capture \n single image\n (props changed)")
        self.ui.pb_send_cmd.setStyleSheet("background-color: yellow;") 
        
        # self.ui.pb_send_cmd. TODO: check how to change button color

    def send_cmd_over_ssh(self) -> None:
        results = sp.run(
            sh_split(self.ui.le_cmd2send.text() ), #.split(),
            capture_output=True,
            text=True,
        )

        self.ui.text_output.setText(
            results.stdout + "--------------------------\n" + results.stderr
        )
        self.show_subprocess_return_status_on_dialog(results)
        self.ui.pb_send_cmd.setText("Re-Execute")
        self.ui.pb_send_cmd.setStyleSheet("background-color: #00FF00") 
        # self.ui.pb_send_cmd. TODO: check how to change button color

    def download_img_and_show(self) -> None:
        results = sp.run(
            ["scp", f"pi@{self.ui.ip_1.value()}.{self.ui.ip_2.value()}.{self.ui.ip_3.value()}.{self.ui.ip_4.value()}:/tmp/test.png", f"/tmp/test.png"],
            capture_output=True,
            text=True,
        )
        self.show_subprocess_return_status_on_dialog(results)

        self.ui.text_output.setText(
            results.stdout + "--------------------------\n" + results.stderr
        )
        img = cv2.imread("/tmp/test.png")
        self.ui.image_view.setImage(
            img=img, # levels=img.max(),
            levels=255,
            axes={"x":1, "y":0, "c":2}
        )

    def check_tmux_pane(self) -> None:
        results = sp.run(
            ["ssh", f"pi@{self.ui.ip_1.value()}.{self.ui.ip_2.value()}.{self.ui.ip_3.value()}.{self.ui.ip_4.value()}", "tmux", "capture-pane", "-pt", "py.0"],
            capture_output=True,
            text=True,
        )

        self.ui.text_output.setText(
            results.stdout + "--------------------------\n" + results.stderr
        )

    def check_dir_tree(self) -> None:
        results = sp.run(
            ["ssh", f"pi@{self.ui.ip_1.value()}.{self.ui.ip_2.value()}.{self.ui.ip_3.value()}.{self.ui.ip_4.value()}", "tree", datetime.now().strftime("*%y%m%d*"), "--du", "-h"],
            capture_output=True,
            text=True,
        )

        self.ui.text_output.setText(
            results.stdout + "--------------------------\n" + results.stderr
        )
    
    def check_storage(self) -> None:
        results = sp.run(
            ["ssh", f"pi@{self.ui.ip_1.value()}.{self.ui.ip_2.value()}.{self.ui.ip_3.value()}.{self.ui.ip_4.value()}", "df", "-h"],
            capture_output=True,
            text=True,
        )

        self.ui.text_output.setText(
            results.stdout + "--------------------------\n" + results.stderr
        )


    def show_subprocess_return_status_on_dialog(self, results: sp.CompletedProcess[str]):
        dlg = QMessageBox(self)
        if results.returncode == 0:
            dlg.setWindowTitle("Subprocess:")
            dlg.setText(f"stdout: {results.stdout}\n\n stderr: {results.stderr}")
        else:
            dlg.setWindowTitle("Subprocess: (err?)")
            dlg.setText(f"stdout: {results.stdout}\n\n stderr: {results.stderr}")

        button = dlg.exec_()

        if button == QMessageBox.StandardButton.Ok:
            print("OK!")
