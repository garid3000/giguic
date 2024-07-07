# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_Mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.12
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

from pyqtgraph import ImageView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow: QMainWindow) -> None:
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1057, 695)
        MainWindow.setStyleSheet(u".QLabel { font-size: 12pt;}\n"
".QSpinBox { font-size: 15pt;}\n"
".QComboBox { font-size: 15pt;}\n"
".QCheckBox { font-size: 15pt;}\n"
".QCheckBox::indicator {\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
".QPushButton { font-size: 15pt;}\n"
".QTabWidget { font-size: 14pt;}\n"
".QLineEdit { font-size: 12pt;}\n"
".QSpinBox::down-button{ width: 30;}\n"
".QSpinBox::up-button{ width: 30;  }\n"
"/*.QSplitter::handle {\n"
"    image: url(/tmp/sit.svg);\n"
"}*/\n"
".QSplitter::handle:horizontal {\n"
"    width: 20px;\n"
"}\n"
".QSplitter::handle:vertical {\n"
"    height: 20px;\n"
"}")
        self.actionOpen_Directory = QAction(MainWindow)
        self.actionOpen_Directory.setObjectName(u"actionOpen_Directory")
        self.action_cur_jpeg_export = QAction(MainWindow)
        self.action_cur_jpeg_export.setObjectName(u"action_cur_jpeg_export")
        self.action_geometry_load = QAction(MainWindow)
        self.action_geometry_load.setObjectName(u"action_geometry_load")
        self.action_help = QAction(MainWindow)
        self.action_help.setObjectName(u"action_help")
        self.actionRead_Dependencies = QAction(MainWindow)
        self.actionRead_Dependencies.setObjectName(u"actionRead_Dependencies")
        self.actionContact_information = QAction(MainWindow)
        self.actionContact_information.setObjectName(u"actionContact_information")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.actionContact = QAction(MainWindow)
        self.actionContact.setObjectName(u"actionContact")
        self.action_cur_jpeg_preview = QAction(MainWindow)
        self.action_cur_jpeg_preview.setObjectName(u"action_cur_jpeg_preview")
        self.action_dir_goto_parent = QAction(MainWindow)
        self.action_dir_goto_parent.setObjectName(u"action_dir_goto_parent")
        self.action_dir_goto_cur_child = QAction(MainWindow)
        self.action_dir_goto_cur_child.setObjectName(u"action_dir_goto_cur_child")
        self.action_dir_cur_child_fold = QAction(MainWindow)
        self.action_dir_cur_child_fold.setObjectName(u"action_dir_cur_child_fold")
        self.action_dir_cur_child_unfold = QAction(MainWindow)
        self.action_dir_cur_child_unfold.setObjectName(u"action_dir_cur_child_unfold")
        self.action_cur_file_open = QAction(MainWindow)
        self.action_cur_file_open.setObjectName(u"action_cur_file_open")
        self.actionsdf = QAction(MainWindow)
        self.actionsdf.setObjectName(u"actionsdf")
        self.actionSave_geometry_configuration_Ctrl_Shift_L = QAction(MainWindow)
        self.actionSave_geometry_configuration_Ctrl_Shift_L.setObjectName(u"actionSave_geometry_configuration_Ctrl_Shift_L")
        self.action_dir_ft_filter_toggle = QAction(MainWindow)
        self.action_dir_ft_filter_toggle.setObjectName(u"action_dir_ft_filter_toggle")
        self.action_tabs_show_tab1 = QAction(MainWindow)
        self.action_tabs_show_tab1.setObjectName(u"action_tabs_show_tab1")
        self.action_tabs_show_tab2 = QAction(MainWindow)
        self.action_tabs_show_tab2.setObjectName(u"action_tabs_show_tab2")
        self.action_tabs_show_tab3 = QAction(MainWindow)
        self.action_tabs_show_tab3.setObjectName(u"action_tabs_show_tab3")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.le_cmd2send = QLineEdit(self.centralwidget)
        self.le_cmd2send.setObjectName(u"le_cmd2send")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_cmd2send.sizePolicy().hasHeightForWidth())
        self.le_cmd2send.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Monospace")
        font.setPointSize(12)
        self.le_cmd2send.setFont(font)

        self.gridLayout.addWidget(self.le_cmd2send, 2, 0, 1, 1)

        self.pb_send_cmd = QPushButton(self.centralwidget)
        self.pb_send_cmd.setObjectName(u"pb_send_cmd")
        self.pb_send_cmd.setMinimumSize(QSize(100, 60))

        self.gridLayout.addWidget(self.pb_send_cmd, 2, 1, 1, 1)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setFrameShadow(QFrame.Shadow.Raised)
        self.splitter.setMidLineWidth(0)
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.groupBox = QGroupBox(self.splitter)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.groupBox)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 50))
        self.tabWidget.setStyleSheet(u"QTabBar::tab { height: 35px;  }\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 1px;\n"
"    height: 3px;\n"
"    margin: 0px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"    background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 40px;\n"
"    width: 40px;\n"
"    margin: -20px 0;\n"
"    border-radius: 20px;\n"
"    padding: -20px 0px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(155, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 255, 195);\n"
"}")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setIconSize(QSize(16, 16))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_4 = QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.b_this_pc_get_ip = QPushButton(self.tab)
        self.b_this_pc_get_ip.setObjectName(u"b_this_pc_get_ip")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.b_this_pc_get_ip.sizePolicy().hasHeightForWidth())
        self.b_this_pc_get_ip.setSizePolicy(sizePolicy1)
        self.b_this_pc_get_ip.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_4.addWidget(self.b_this_pc_get_ip)

        self._l_4 = QLabel(self.tab)
        self._l_4.setObjectName(u"_l_4")

        self.horizontalLayout_4.addWidget(self._l_4)

        self.cb_this_pc_network_devices = QComboBox(self.tab)
        self.cb_this_pc_network_devices.setObjectName(u"cb_this_pc_network_devices")

        self.horizontalLayout_4.addWidget(self.cb_this_pc_network_devices)

        self.l_this_pc_ip = QLabel(self.tab)
        self.l_this_pc_ip.setObjectName(u"l_this_pc_ip")
        self.l_this_pc_ip.setFont(font)

        self.horizontalLayout_4.addWidget(self.l_this_pc_ip)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.line = QFrame(self.tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.ip_1 = QSpinBox(self.tab)
        self.ip_1.setObjectName(u"ip_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ip_1.sizePolicy().hasHeightForWidth())
        self.ip_1.setSizePolicy(sizePolicy2)
        self.ip_1.setMinimumSize(QSize(100, 50))
        font1 = QFont()
        font1.setFamily(u"Monospace")
        font1.setPointSize(15)
        font1.setBold(False)
        font1.setItalic(False)
        self.ip_1.setFont(font1)
        self.ip_1.setWrapping(False)
        self.ip_1.setFrame(True)
        self.ip_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ip_1.setReadOnly(False)
        self.ip_1.setMaximum(255)
        self.ip_1.setSingleStep(1)
        self.ip_1.setValue(192)

        self.horizontalLayout_3.addWidget(self.ip_1)

        self.ip_2 = QSpinBox(self.tab)
        self.ip_2.setObjectName(u"ip_2")
        sizePolicy2.setHeightForWidth(self.ip_2.sizePolicy().hasHeightForWidth())
        self.ip_2.setSizePolicy(sizePolicy2)
        self.ip_2.setMinimumSize(QSize(100, 50))
        self.ip_2.setFont(font1)
        self.ip_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ip_2.setMaximum(255)
        self.ip_2.setValue(168)

        self.horizontalLayout_3.addWidget(self.ip_2)

        self.ip_3 = QSpinBox(self.tab)
        self.ip_3.setObjectName(u"ip_3")
        sizePolicy2.setHeightForWidth(self.ip_3.sizePolicy().hasHeightForWidth())
        self.ip_3.setSizePolicy(sizePolicy2)
        self.ip_3.setMinimumSize(QSize(100, 50))
        self.ip_3.setFont(font1)
        self.ip_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ip_3.setMaximum(255)
        self.ip_3.setValue(83)

        self.horizontalLayout_3.addWidget(self.ip_3)

        self.ip_4 = QSpinBox(self.tab)
        self.ip_4.setObjectName(u"ip_4")
        sizePolicy2.setHeightForWidth(self.ip_4.sizePolicy().hasHeightForWidth())
        self.ip_4.setSizePolicy(sizePolicy2)
        self.ip_4.setMinimumSize(QSize(100, 50))
        self.ip_4.setFont(font1)
        self.ip_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ip_4.setMaximum(255)
        self.ip_4.setValue(59)

        self.horizontalLayout_3.addWidget(self.ip_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.b_search_ip_for_pi = QPushButton(self.tab)
        self.b_search_ip_for_pi.setObjectName(u"b_search_ip_for_pi")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.b_search_ip_for_pi.sizePolicy().hasHeightForWidth())
        self.b_search_ip_for_pi.setSizePolicy(sizePolicy3)
        self.b_search_ip_for_pi.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_5.addWidget(self.b_search_ip_for_pi)

        self.b_ssh_copy_id = QPushButton(self.tab)
        self.b_ssh_copy_id.setObjectName(u"b_ssh_copy_id")
        sizePolicy2.setHeightForWidth(self.b_ssh_copy_id.sizePolicy().hasHeightForWidth())
        self.b_ssh_copy_id.setSizePolicy(sizePolicy2)
        self.b_ssh_copy_id.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_5.addWidget(self.b_ssh_copy_id)

        self.b_check_ssh_connection = QPushButton(self.tab)
        self.b_check_ssh_connection.setObjectName(u"b_check_ssh_connection")
        sizePolicy3.setHeightForWidth(self.b_check_ssh_connection.sizePolicy().hasHeightForWidth())
        self.b_check_ssh_connection.setSizePolicy(sizePolicy3)
        self.b_check_ssh_connection.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_5.addWidget(self.b_check_ssh_connection)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.line_2 = QFrame(self.tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.b_soft_reboot = QPushButton(self.tab)
        self.b_soft_reboot.setObjectName(u"b_soft_reboot")
        sizePolicy3.setHeightForWidth(self.b_soft_reboot.sizePolicy().hasHeightForWidth())
        self.b_soft_reboot.setSizePolicy(sizePolicy3)
        self.b_soft_reboot.setMinimumSize(QSize(0, 40))

        self.gridLayout_5.addWidget(self.b_soft_reboot, 2, 0, 1, 1)

        self.b_hard_reboot = QPushButton(self.tab)
        self.b_hard_reboot.setObjectName(u"b_hard_reboot")
        sizePolicy3.setHeightForWidth(self.b_hard_reboot.sizePolicy().hasHeightForWidth())
        self.b_hard_reboot.setSizePolicy(sizePolicy3)
        self.b_hard_reboot.setMinimumSize(QSize(0, 40))

        self.gridLayout_5.addWidget(self.b_hard_reboot, 1, 0, 1, 1)

        self.b_tmux_init = QPushButton(self.tab)
        self.b_tmux_init.setObjectName(u"b_tmux_init")
        sizePolicy3.setHeightForWidth(self.b_tmux_init.sizePolicy().hasHeightForWidth())
        self.b_tmux_init.setSizePolicy(sizePolicy3)
        self.b_tmux_init.setMinimumSize(QSize(0, 40))

        self.gridLayout_5.addWidget(self.b_tmux_init, 1, 1, 1, 1)

        self.b_terminate_python_processes = QPushButton(self.tab)
        self.b_terminate_python_processes.setObjectName(u"b_terminate_python_processes")
        sizePolicy3.setHeightForWidth(self.b_terminate_python_processes.sizePolicy().hasHeightForWidth())
        self.b_terminate_python_processes.setSizePolicy(sizePolicy3)
        self.b_terminate_python_processes.setMinimumSize(QSize(0, 40))

        self.gridLayout_5.addWidget(self.b_terminate_python_processes, 3, 0, 1, 1)

        self.b_info_dump = QPushButton(self.tab)
        self.b_info_dump.setObjectName(u"b_info_dump")
        sizePolicy3.setHeightForWidth(self.b_info_dump.sizePolicy().hasHeightForWidth())
        self.b_info_dump.setSizePolicy(sizePolicy3)
        self.b_info_dump.setMinimumSize(QSize(0, 40))

        self.gridLayout_5.addWidget(self.b_info_dump, 2, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_5)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setStyleSheet(u"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: right; /* position at the top right corner */\n"
"    width: 30px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
"	height: 25px;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: left; /* position at bottom right corner */\n"
"    width: 30px;\n"
"	height: 25px;\n"
"}\n"
"")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.sp_elv = QSpinBox(self.tab_2)
        self.sp_elv.setObjectName(u"sp_elv")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.sp_elv.sizePolicy().hasHeightForWidth())
        self.sp_elv.setSizePolicy(sizePolicy4)
        self.sp_elv.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.sp_elv.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sp_elv.setMinimum(-90)
        self.sp_elv.setMaximum(90)

        self.horizontalLayout_2.addWidget(self.sp_elv)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.d_elv = QDial(self.tab_2)
        self.d_elv.setObjectName(u"d_elv")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.d_elv.sizePolicy().hasHeightForWidth())
        self.d_elv.setSizePolicy(sizePolicy5)
        self.d_elv.setMinimum(-90)
        self.d_elv.setMaximum(90)
        self.d_elv.setSingleStep(5)
        self.d_elv.setPageStep(1)
        self.d_elv.setValue(-45)
        self.d_elv.setSliderPosition(-45)
        self.d_elv.setOrientation(Qt.Orientation.Vertical)
        self.d_elv.setInvertedAppearance(False)
        self.d_elv.setInvertedControls(True)
        self.d_elv.setWrapping(False)
        self.d_elv.setNotchTarget(10.000000000000000)
        self.d_elv.setNotchesVisible(True)

        self.verticalLayout_3.addWidget(self.d_elv)


        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.sp_azi = QSpinBox(self.tab_2)
        self.sp_azi.setObjectName(u"sp_azi")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(1)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.sp_azi.sizePolicy().hasHeightForWidth())
        self.sp_azi.setSizePolicy(sizePolicy6)
        self.sp_azi.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sp_azi.setMinimum(-180)
        self.sp_azi.setMaximum(180)

        self.horizontalLayout.addWidget(self.sp_azi)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.d_azi = QDial(self.tab_2)
        self.d_azi.setObjectName(u"d_azi")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(10)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.d_azi.sizePolicy().hasHeightForWidth())
        self.d_azi.setSizePolicy(sizePolicy7)
        self.d_azi.setMinimum(-180)
        self.d_azi.setMaximum(180)
        self.d_azi.setSingleStep(5)
        self.d_azi.setPageStep(10)
        self.d_azi.setOrientation(Qt.Orientation.Horizontal)
        self.d_azi.setInvertedAppearance(False)
        self.d_azi.setWrapping(True)
        self.d_azi.setNotchTarget(10.000000000000000)
        self.d_azi.setNotchesVisible(True)

        self.verticalLayout.addWidget(self.d_azi)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.pb_motor_zeroing = QPushButton(self.tab_2)
        self.pb_motor_zeroing.setObjectName(u"pb_motor_zeroing")

        self.gridLayout_3.addWidget(self.pb_motor_zeroing, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_10 = QGridLayout(self.tab_7)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self._l1 = QLabel(self.tab_7)
        self._l1.setObjectName(u"_l1")

        self.gridLayout_8.addWidget(self._l1, 0, 0, 1, 1)

        self.sp_expo_1 = QSpinBox(self.tab_7)
        self.sp_expo_1.setObjectName(u"sp_expo_1")
        self.sp_expo_1.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sp_expo_1.setMaximum(2500)

        self.gridLayout_8.addWidget(self.sp_expo_1, 0, 1, 1, 1)

        self.d_expo_1 = QDial(self.tab_7)
        self.d_expo_1.setObjectName(u"d_expo_1")
        sizePolicy7.setHeightForWidth(self.d_expo_1.sizePolicy().hasHeightForWidth())
        self.d_expo_1.setSizePolicy(sizePolicy7)
        self.d_expo_1.setMinimum(0)
        self.d_expo_1.setMaximum(11)
        self.d_expo_1.setValue(8)
        self.d_expo_1.setOrientation(Qt.Orientation.Horizontal)
        self.d_expo_1.setInvertedAppearance(False)
        self.d_expo_1.setWrapping(False)
        self.d_expo_1.setNotchTarget(10.000000000000000)
        self.d_expo_1.setNotchesVisible(True)

        self.gridLayout_8.addWidget(self.d_expo_1, 1, 0, 1, 2)


        self.gridLayout_10.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self._l1_2 = QLabel(self.tab_7)
        self._l1_2.setObjectName(u"_l1_2")

        self.gridLayout_18.addWidget(self._l1_2, 0, 0, 1, 1)

        self.sp_expo_2 = QSpinBox(self.tab_7)
        self.sp_expo_2.setObjectName(u"sp_expo_2")
        self.sp_expo_2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sp_expo_2.setMaximum(2500)

        self.gridLayout_18.addWidget(self.sp_expo_2, 0, 1, 1, 1)

        self.d_expo_2 = QDial(self.tab_7)
        self.d_expo_2.setObjectName(u"d_expo_2")
        sizePolicy7.setHeightForWidth(self.d_expo_2.sizePolicy().hasHeightForWidth())
        self.d_expo_2.setSizePolicy(sizePolicy7)
        self.d_expo_2.setMinimum(0)
        self.d_expo_2.setMaximum(11)
        self.d_expo_2.setValue(8)
        self.d_expo_2.setOrientation(Qt.Orientation.Horizontal)
        self.d_expo_2.setInvertedAppearance(False)
        self.d_expo_2.setWrapping(False)
        self.d_expo_2.setNotchTarget(10.000000000000000)
        self.d_expo_2.setNotchesVisible(True)

        self.gridLayout_18.addWidget(self.d_expo_2, 1, 0, 1, 2)


        self.gridLayout_10.addLayout(self.gridLayout_18, 0, 1, 1, 1)

        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self._l1_3 = QLabel(self.tab_7)
        self._l1_3.setObjectName(u"_l1_3")

        self.gridLayout_19.addWidget(self._l1_3, 0, 0, 1, 1)

        self.sp_expo_3 = QSpinBox(self.tab_7)
        self.sp_expo_3.setObjectName(u"sp_expo_3")
        self.sp_expo_3.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sp_expo_3.setMaximum(2500)

        self.gridLayout_19.addWidget(self.sp_expo_3, 0, 1, 1, 1)

        self.d_expo_3 = QDial(self.tab_7)
        self.d_expo_3.setObjectName(u"d_expo_3")
        sizePolicy7.setHeightForWidth(self.d_expo_3.sizePolicy().hasHeightForWidth())
        self.d_expo_3.setSizePolicy(sizePolicy7)
        self.d_expo_3.setMinimum(0)
        self.d_expo_3.setMaximum(11)
        self.d_expo_3.setValue(8)
        self.d_expo_3.setOrientation(Qt.Orientation.Horizontal)
        self.d_expo_3.setInvertedAppearance(False)
        self.d_expo_3.setWrapping(False)
        self.d_expo_3.setNotchTarget(10.000000000000000)
        self.d_expo_3.setNotchesVisible(True)

        self.gridLayout_19.addWidget(self.d_expo_3, 1, 0, 1, 2)


        self.gridLayout_10.addLayout(self.gridLayout_19, 0, 2, 1, 1)

        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self._l1_4 = QLabel(self.tab_7)
        self._l1_4.setObjectName(u"_l1_4")

        self.gridLayout_20.addWidget(self._l1_4, 0, 0, 1, 1)

        self.sp_expo_4 = QSpinBox(self.tab_7)
        self.sp_expo_4.setObjectName(u"sp_expo_4")
        self.sp_expo_4.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sp_expo_4.setMaximum(2500)

        self.gridLayout_20.addWidget(self.sp_expo_4, 0, 1, 1, 1)

        self.d_expo_4 = QDial(self.tab_7)
        self.d_expo_4.setObjectName(u"d_expo_4")
        sizePolicy7.setHeightForWidth(self.d_expo_4.sizePolicy().hasHeightForWidth())
        self.d_expo_4.setSizePolicy(sizePolicy7)
        self.d_expo_4.setMinimum(0)
        self.d_expo_4.setMaximum(11)
        self.d_expo_4.setValue(8)
        self.d_expo_4.setOrientation(Qt.Orientation.Horizontal)
        self.d_expo_4.setInvertedAppearance(False)
        self.d_expo_4.setWrapping(False)
        self.d_expo_4.setNotchTarget(10.000000000000000)
        self.d_expo_4.setNotchesVisible(True)

        self.gridLayout_20.addWidget(self.d_expo_4, 1, 0, 1, 2)


        self.gridLayout_10.addLayout(self.gridLayout_20, 0, 3, 1, 1)

        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self._l1_5 = QLabel(self.tab_7)
        self._l1_5.setObjectName(u"_l1_5")

        self.gridLayout_21.addWidget(self._l1_5, 0, 0, 1, 1)

        self.sp_expo_5 = QSpinBox(self.tab_7)
        self.sp_expo_5.setObjectName(u"sp_expo_5")
        self.sp_expo_5.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sp_expo_5.setMaximum(2500)

        self.gridLayout_21.addWidget(self.sp_expo_5, 0, 1, 1, 1)

        self.d_expo_5 = QDial(self.tab_7)
        self.d_expo_5.setObjectName(u"d_expo_5")
        sizePolicy7.setHeightForWidth(self.d_expo_5.sizePolicy().hasHeightForWidth())
        self.d_expo_5.setSizePolicy(sizePolicy7)
        self.d_expo_5.setMinimum(0)
        self.d_expo_5.setMaximum(11)
        self.d_expo_5.setValue(8)
        self.d_expo_5.setOrientation(Qt.Orientation.Horizontal)
        self.d_expo_5.setInvertedAppearance(False)
        self.d_expo_5.setWrapping(False)
        self.d_expo_5.setNotchTarget(10.000000000000000)
        self.d_expo_5.setNotchesVisible(True)

        self.gridLayout_21.addWidget(self.d_expo_5, 1, 0, 1, 2)


        self.gridLayout_10.addLayout(self.gridLayout_21, 1, 0, 1, 1)

        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self._l1_6 = QLabel(self.tab_7)
        self._l1_6.setObjectName(u"_l1_6")

        self.gridLayout_22.addWidget(self._l1_6, 0, 0, 1, 1)

        self.sp_expo_6 = QSpinBox(self.tab_7)
        self.sp_expo_6.setObjectName(u"sp_expo_6")
        self.sp_expo_6.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sp_expo_6.setMaximum(2500)

        self.gridLayout_22.addWidget(self.sp_expo_6, 0, 1, 1, 1)

        self.d_expo_6 = QDial(self.tab_7)
        self.d_expo_6.setObjectName(u"d_expo_6")
        sizePolicy7.setHeightForWidth(self.d_expo_6.sizePolicy().hasHeightForWidth())
        self.d_expo_6.setSizePolicy(sizePolicy7)
        self.d_expo_6.setMinimum(0)
        self.d_expo_6.setMaximum(11)
        self.d_expo_6.setValue(8)
        self.d_expo_6.setOrientation(Qt.Orientation.Horizontal)
        self.d_expo_6.setInvertedAppearance(False)
        self.d_expo_6.setWrapping(False)
        self.d_expo_6.setNotchTarget(10.000000000000000)
        self.d_expo_6.setNotchesVisible(True)

        self.gridLayout_22.addWidget(self.d_expo_6, 1, 0, 1, 2)


        self.gridLayout_10.addLayout(self.gridLayout_22, 1, 1, 1, 1)

        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self._l1_7 = QLabel(self.tab_7)
        self._l1_7.setObjectName(u"_l1_7")

        self.gridLayout_23.addWidget(self._l1_7, 0, 0, 1, 1)

        self.sp_expo_7 = QSpinBox(self.tab_7)
        self.sp_expo_7.setObjectName(u"sp_expo_7")
        self.sp_expo_7.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sp_expo_7.setMaximum(2500)

        self.gridLayout_23.addWidget(self.sp_expo_7, 0, 1, 1, 1)

        self.d_expo_7 = QDial(self.tab_7)
        self.d_expo_7.setObjectName(u"d_expo_7")
        sizePolicy7.setHeightForWidth(self.d_expo_7.sizePolicy().hasHeightForWidth())
        self.d_expo_7.setSizePolicy(sizePolicy7)
        self.d_expo_7.setMinimum(0)
        self.d_expo_7.setMaximum(11)
        self.d_expo_7.setValue(8)
        self.d_expo_7.setOrientation(Qt.Orientation.Horizontal)
        self.d_expo_7.setInvertedAppearance(False)
        self.d_expo_7.setWrapping(False)
        self.d_expo_7.setNotchTarget(10.000000000000000)
        self.d_expo_7.setNotchesVisible(True)

        self.gridLayout_23.addWidget(self.d_expo_7, 1, 0, 1, 2)


        self.gridLayout_10.addLayout(self.gridLayout_23, 1, 2, 1, 1)

        self.gridLayout_24 = QGridLayout()
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self._l1_8 = QLabel(self.tab_7)
        self._l1_8.setObjectName(u"_l1_8")

        self.gridLayout_24.addWidget(self._l1_8, 0, 0, 1, 1)

        self.sp_expo_8 = QSpinBox(self.tab_7)
        self.sp_expo_8.setObjectName(u"sp_expo_8")
        self.sp_expo_8.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sp_expo_8.setMaximum(2500)

        self.gridLayout_24.addWidget(self.sp_expo_8, 0, 1, 1, 1)

        self.d_expo_8 = QDial(self.tab_7)
        self.d_expo_8.setObjectName(u"d_expo_8")
        sizePolicy7.setHeightForWidth(self.d_expo_8.sizePolicy().hasHeightForWidth())
        self.d_expo_8.setSizePolicy(sizePolicy7)
        self.d_expo_8.setMinimum(0)
        self.d_expo_8.setMaximum(11)
        self.d_expo_8.setValue(8)
        self.d_expo_8.setOrientation(Qt.Orientation.Horizontal)
        self.d_expo_8.setInvertedAppearance(False)
        self.d_expo_8.setWrapping(False)
        self.d_expo_8.setNotchTarget(10.000000000000000)
        self.d_expo_8.setNotchesVisible(True)

        self.gridLayout_24.addWidget(self.d_expo_8, 1, 0, 1, 2)


        self.gridLayout_10.addLayout(self.gridLayout_24, 1, 3, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_4 = QLabel(self.tab_7)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_9.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_3 = QLabel(self.tab_7)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_9.addWidget(self.label_3, 1, 0, 1, 1)

        self.le_expo_plus_str = QLineEdit(self.tab_7)
        self.le_expo_plus_str.setObjectName(u"le_expo_plus_str")

        self.gridLayout_9.addWidget(self.le_expo_plus_str, 2, 1, 1, 1)

        self.le_expo_minus_str = QLineEdit(self.tab_7)
        self.le_expo_minus_str.setObjectName(u"le_expo_minus_str")

        self.gridLayout_9.addWidget(self.le_expo_minus_str, 0, 1, 1, 1)

        self.label_5 = QLabel(self.tab_7)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_9.addWidget(self.label_5, 2, 0, 1, 1)

        self.le_expo_base_str = QLineEdit(self.tab_7)
        self.le_expo_base_str.setObjectName(u"le_expo_base_str")

        self.gridLayout_9.addWidget(self.le_expo_base_str, 1, 1, 1, 1)

        self.spinBox_2 = QSpinBox(self.tab_7)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(3)
        self.spinBox_2.setValue(1)

        self.gridLayout_9.addWidget(self.spinBox_2, 2, 2, 1, 1)

        self.spinBox = QSpinBox(self.tab_7)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spinBox.setMinimum(-3)
        self.spinBox.setMaximum(0)
        self.spinBox.setValue(-1)

        self.gridLayout_9.addWidget(self.spinBox, 0, 2, 1, 1)

        self.b_1shot = QPushButton(self.tab_7)
        self.b_1shot.setObjectName(u"b_1shot")
        sizePolicy2.setHeightForWidth(self.b_1shot.sizePolicy().hasHeightForWidth())
        self.b_1shot.setSizePolicy(sizePolicy2)
        self.b_1shot.setMinimumSize(QSize(120, 0))

        self.gridLayout_9.addWidget(self.b_1shot, 0, 3, 3, 1)


        self.gridLayout_10.addLayout(self.gridLayout_9, 2, 0, 1, 4)

        self.tabWidget.addTab(self.tab_7, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.qe_meas_gimbal_fullpath = QLineEdit(self.tab_3)
        self.qe_meas_gimbal_fullpath.setObjectName(u"qe_meas_gimbal_fullpath")
        self.qe_meas_gimbal_fullpath.setEnabled(False)

        self.gridLayout_12.addWidget(self.qe_meas_gimbal_fullpath, 0, 1, 1, 1)

        self.label_12 = QLabel(self.tab_3)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_12.addWidget(self.label_12, 0, 0, 1, 1)

        self.qe_meas_gimbal_tag = QLineEdit(self.tab_3)
        self.qe_meas_gimbal_tag.setObjectName(u"qe_meas_gimbal_tag")

        self.gridLayout_12.addWidget(self.qe_meas_gimbal_tag, 1, 1, 1, 1)

        self.label_13 = QLabel(self.tab_3)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_12.addWidget(self.label_13, 1, 0, 1, 1)

        self.b_meas_gimbal_refresh = QPushButton(self.tab_3)
        self.b_meas_gimbal_refresh.setObjectName(u"b_meas_gimbal_refresh")
        sizePolicy2.setHeightForWidth(self.b_meas_gimbal_refresh.sizePolicy().hasHeightForWidth())
        self.b_meas_gimbal_refresh.setSizePolicy(sizePolicy2)

        self.gridLayout_12.addWidget(self.b_meas_gimbal_refresh, 0, 2, 2, 1)


        self.gridLayout_4.addLayout(self.gridLayout_12, 4, 0, 1, 1)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.hs_azi_0 = QSlider(self.tab_3)
        self.hs_azi_0.setObjectName(u"hs_azi_0")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.hs_azi_0.sizePolicy().hasHeightForWidth())
        self.hs_azi_0.setSizePolicy(sizePolicy8)
        self.hs_azi_0.setMinimumSize(QSize(0, 0))
        self.hs_azi_0.setStyleSheet(u"")
        self.hs_azi_0.setMinimum(0)
        self.hs_azi_0.setMaximum(180)
        self.hs_azi_0.setValue(180)
        self.hs_azi_0.setOrientation(Qt.Orientation.Horizontal)
        self.hs_azi_0.setInvertedAppearance(True)

        self.gridLayout_13.addWidget(self.hs_azi_0, 0, 0, 1, 1)

        self.sb_azi_0 = QSpinBox(self.tab_3)
        self.sb_azi_0.setObjectName(u"sb_azi_0")
        self.sb_azi_0.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.sb_azi_0.setMinimum(-180)
        self.sb_azi_0.setMaximum(0)
        self.sb_azi_0.setValue(-180)

        self.gridLayout_13.addWidget(self.sb_azi_0, 0, 1, 1, 1)

        self.hs_elv_0 = QSlider(self.tab_3)
        self.hs_elv_0.setObjectName(u"hs_elv_0")
        sizePolicy8.setHeightForWidth(self.hs_elv_0.sizePolicy().hasHeightForWidth())
        self.hs_elv_0.setSizePolicy(sizePolicy8)
        self.hs_elv_0.setMaximum(90)
        self.hs_elv_0.setSingleStep(5)
        self.hs_elv_0.setPageStep(1)
        self.hs_elv_0.setValue(45)
        self.hs_elv_0.setOrientation(Qt.Orientation.Horizontal)
        self.hs_elv_0.setInvertedAppearance(True)
        self.hs_elv_0.setInvertedControls(False)

        self.gridLayout_13.addWidget(self.hs_elv_0, 2, 0, 1, 1)

        self.sb_elv_0 = QSpinBox(self.tab_3)
        self.sb_elv_0.setObjectName(u"sb_elv_0")
        self.sb_elv_0.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.sb_elv_0.setMinimum(-90)
        self.sb_elv_0.setMaximum(0)
        self.sb_elv_0.setSingleStep(1)
        self.sb_elv_0.setValue(0)

        self.gridLayout_13.addWidget(self.sb_elv_0, 2, 1, 1, 1)

        self._l_2 = QLabel(self.tab_3)
        self._l_2.setObjectName(u"_l_2")

        self.gridLayout_13.addWidget(self._l_2, 2, 2, 1, 1)

        self._l = QLabel(self.tab_3)
        self._l.setObjectName(u"_l")

        self.gridLayout_13.addWidget(self._l, 0, 2, 1, 1)

        self.sb_azi_1 = QSpinBox(self.tab_3)
        self.sb_azi_1.setObjectName(u"sb_azi_1")
        self.sb_azi_1.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.sb_azi_1.setMaximum(180)
        self.sb_azi_1.setValue(180)

        self.gridLayout_13.addWidget(self.sb_azi_1, 0, 3, 1, 1)

        self.sb_elv_1 = QSpinBox(self.tab_3)
        self.sb_elv_1.setObjectName(u"sb_elv_1")
        self.sb_elv_1.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.sb_elv_1.setMinimum(-70)
        self.sb_elv_1.setMaximum(45)

        self.gridLayout_13.addWidget(self.sb_elv_1, 2, 3, 1, 1)

        self.hs_azi_1 = QSlider(self.tab_3)
        self.hs_azi_1.setObjectName(u"hs_azi_1")
        sizePolicy8.setHeightForWidth(self.hs_azi_1.sizePolicy().hasHeightForWidth())
        self.hs_azi_1.setSizePolicy(sizePolicy8)
        self.hs_azi_1.setMaximum(180)
        self.hs_azi_1.setValue(90)
        self.hs_azi_1.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_13.addWidget(self.hs_azi_1, 0, 4, 1, 1)

        self.hs_elv_1 = QSlider(self.tab_3)
        self.hs_elv_1.setObjectName(u"hs_elv_1")
        sizePolicy8.setHeightForWidth(self.hs_elv_1.sizePolicy().hasHeightForWidth())
        self.hs_elv_1.setSizePolicy(sizePolicy8)
        self.hs_elv_1.setMinimum(-70)
        self.hs_elv_1.setMaximum(45)
        self.hs_elv_1.setSingleStep(5)
        self.hs_elv_1.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_13.addWidget(self.hs_elv_1, 2, 4, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.verticalSpacer_5, 1, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_13, 1, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.verticalSpacer_6, 2, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.verticalSpacer_7, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_5 = QVBoxLayout(self.tab_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.b_meas_uav_refresh = QPushButton(self.tab_6)
        self.b_meas_uav_refresh.setObjectName(u"b_meas_uav_refresh")
        sizePolicy2.setHeightForWidth(self.b_meas_uav_refresh.sizePolicy().hasHeightForWidth())
        self.b_meas_uav_refresh.setSizePolicy(sizePolicy2)

        self.gridLayout_11.addWidget(self.b_meas_uav_refresh, 0, 2, 2, 1)

        self.label_9 = QLabel(self.tab_6)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_11.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_10 = QLabel(self.tab_6)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_11.addWidget(self.label_10, 1, 0, 1, 1)

        self.qe_meas_uav_fullpath = QLineEdit(self.tab_6)
        self.qe_meas_uav_fullpath.setObjectName(u"qe_meas_uav_fullpath")
        self.qe_meas_uav_fullpath.setEnabled(False)

        self.gridLayout_11.addWidget(self.qe_meas_uav_fullpath, 0, 1, 1, 1)

        self.qe_meas_uav_tag = QLineEdit(self.tab_6)
        self.qe_meas_uav_tag.setObjectName(u"qe_meas_uav_tag")

        self.gridLayout_11.addWidget(self.qe_meas_uav_tag, 1, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_11)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_6, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.splitter.addWidget(self.groupBox)
        self.groupBox_2 = QGroupBox(self.splitter)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_6 = QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tabWidget_2 = QTabWidget(self.groupBox_2)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_14 = QGridLayout(self.tab_4)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.b_check_dir_tree = QPushButton(self.tab_4)
        self.b_check_dir_tree.setObjectName(u"b_check_dir_tree")
        sizePolicy2.setHeightForWidth(self.b_check_dir_tree.sizePolicy().hasHeightForWidth())
        self.b_check_dir_tree.setSizePolicy(sizePolicy2)

        self.gridLayout_14.addWidget(self.b_check_dir_tree, 1, 1, 1, 1)

        self.b_check_tmux = QPushButton(self.tab_4)
        self.b_check_tmux.setObjectName(u"b_check_tmux")
        self.b_check_tmux.setMinimumSize(QSize(0, 80))

        self.gridLayout_14.addWidget(self.b_check_tmux, 1, 0, 1, 1)

        self.b_check_stroge = QPushButton(self.tab_4)
        self.b_check_stroge.setObjectName(u"b_check_stroge")
        sizePolicy2.setHeightForWidth(self.b_check_stroge.sizePolicy().hasHeightForWidth())
        self.b_check_stroge.setSizePolicy(sizePolicy2)

        self.gridLayout_14.addWidget(self.b_check_stroge, 1, 2, 1, 1)

        self.text_output = QTextBrowser(self.tab_4)
        self.text_output.setObjectName(u"text_output")
        font2 = QFont()
        font2.setFamily(u"Monospace")
        self.text_output.setFont(font2)

        self.gridLayout_14.addWidget(self.text_output, 3, 0, 1, 3)

        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_7 = QGridLayout(self.tab_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pb_get_cam0 = QPushButton(self.tab_5)
        self.pb_get_cam0.setObjectName(u"pb_get_cam0")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.pb_get_cam0.sizePolicy().hasHeightForWidth())
        self.pb_get_cam0.setSizePolicy(sizePolicy9)
        self.pb_get_cam0.setMinimumSize(QSize(0, 80))

        self.gridLayout_7.addWidget(self.pb_get_cam0, 0, 0, 1, 2)

        self.image_view = ImageView(self.tab_5)
        self.image_view.setObjectName(u"image_view")

        self.gridLayout_7.addWidget(self.image_view, 3, 0, 1, 2)

        self.tabWidget_2.addTab(self.tab_5, "")

        self.gridLayout_6.addWidget(self.tabWidget_2, 0, 0, 1, 1)

        self.splitter.addWidget(self.groupBox_2)

        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow: QMainWindow) -> None:
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen_Directory.setText(QCoreApplication.translate("MainWindow", u"Open Directory", None))
        self.action_cur_jpeg_export.setText(QCoreApplication.translate("MainWindow", u"Export (Ctlr-E)", None))
        self.action_geometry_load.setText(QCoreApplication.translate("MainWindow", u"Load geometry configuration (Ctrl + L)", None))
        self.action_help.setText(QCoreApplication.translate("MainWindow", u"Help (Ctrl+H)", None))
        self.actionRead_Dependencies.setText(QCoreApplication.translate("MainWindow", u"Read Dependencies", None))
        self.actionContact_information.setText(QCoreApplication.translate("MainWindow", u"Contact information", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"About (Ctrl+A)", None))
        self.actionContact.setText(QCoreApplication.translate("MainWindow", u"Contact", None))
        self.action_cur_jpeg_preview.setText(QCoreApplication.translate("MainWindow", u"Preview (Space)", None))
        self.action_dir_goto_parent.setText(QCoreApplication.translate("MainWindow", u"Go to Parent Directory (Backspace)", None))
        self.action_dir_goto_cur_child.setText(QCoreApplication.translate("MainWindow", u"Go inside Selected Directory (Enter)", None))
        self.action_dir_cur_child_fold.setText(QCoreApplication.translate("MainWindow", u"Fold Selected Directory (Left Arrow)", None))
        self.action_dir_cur_child_unfold.setText(QCoreApplication.translate("MainWindow", u"Unfold Selected Directory (Right Arrow)", None))
        self.action_cur_file_open.setText(QCoreApplication.translate("MainWindow", u"Open with an external app (Ctrl+O)", None))
        self.actionsdf.setText(QCoreApplication.translate("MainWindow", u"sdf", None))
        self.actionSave_geometry_configuration_Ctrl_Shift_L.setText(QCoreApplication.translate("MainWindow", u"Save geometry configuration (Ctrl + Shift + L)", None))
        self.action_dir_ft_filter_toggle.setText(QCoreApplication.translate("MainWindow", u"File type filter toggle (Ctrl+F)", None))
        self.action_tabs_show_tab1.setText(QCoreApplication.translate("MainWindow", u"Raw Bayer Tab (Ctrl+1) or (Alt+1)", None))
        self.action_tabs_show_tab2.setText(QCoreApplication.translate("MainWindow", u"Spectrum-Raw Tab (Ctrl+2) or (Alt+2)", None))
        self.action_tabs_show_tab3.setText(QCoreApplication.translate("MainWindow", u"Spectrum-Reflectance Tab (Ctrl+3) or (Alt+3)", None))
        self.pb_send_cmd.setText(QCoreApplication.translate("MainWindow", u"SEND", None))
        self.groupBox.setTitle("")
        self.b_this_pc_get_ip.setText(QCoreApplication.translate("MainWindow", u"(Re)-check\n"
" computer IP", None))
        self._l_4.setText(QCoreApplication.translate("MainWindow", u"Network interface", None))
        self.l_this_pc_ip.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Enter Device IP address", None))
        self.b_search_ip_for_pi.setText(QCoreApplication.translate("MainWindow", u"Scan IPs", None))
        self.b_ssh_copy_id.setText(QCoreApplication.translate("MainWindow", u"ssh-copy-id", None))
        self.b_check_ssh_connection.setText(QCoreApplication.translate("MainWindow", u"Check SSH \n"
"Connection", None))
        self.b_soft_reboot.setText(QCoreApplication.translate("MainWindow", u"Soft-reboot \n"
"(Back to handheld mode)", None))
        self.b_hard_reboot.setText(QCoreApplication.translate("MainWindow", u"Hard-Reboot", None))
        self.b_tmux_init.setText(QCoreApplication.translate("MainWindow", u"Init TMUX", None))
        self.b_terminate_python_processes.setText(QCoreApplication.translate("MainWindow", u"Softer-reboot\n"
"(kill tmux + python)", None))
        self.b_info_dump.setText(QCoreApplication.translate("MainWindow", u"Info Dump", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Connection", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Motor-Elevation", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Motor-Azimuth", None))
        self.sp_azi.setSuffix("")
        self.pb_motor_zeroing.setText(QCoreApplication.translate("MainWindow", u"Set curret to 0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Motor", None))
        self._l1.setText(QCoreApplication.translate("MainWindow", u"Cam1", None))
        self._l1_2.setText(QCoreApplication.translate("MainWindow", u"Cam2", None))
        self._l1_3.setText(QCoreApplication.translate("MainWindow", u"Cam3", None))
        self._l1_4.setText(QCoreApplication.translate("MainWindow", u"Cam4", None))
        self._l1_5.setText(QCoreApplication.translate("MainWindow", u"Cam5", None))
        self._l1_6.setText(QCoreApplication.translate("MainWindow", u"Cam6", None))
        self._l1_7.setText(QCoreApplication.translate("MainWindow", u"Cam7", None))
        self._l1_8.setText(QCoreApplication.translate("MainWindow", u"Cam8", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Lower", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Base", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Higher", None))
        self.b_1shot.setText(QCoreApplication.translate("MainWindow", u"1shot", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Exposure", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Data full Path", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Data tag", None))
        self.b_meas_gimbal_refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh\n"
" command", None))
        self._l_2.setText(QCoreApplication.translate("MainWindow", u"Elevation", None))
        self._l.setText(QCoreApplication.translate("MainWindow", u"Azimuth ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Meas-Gimbal", None))
        self.b_meas_uav_refresh.setText(QCoreApplication.translate("MainWindow", u" Refresh\n"
"cmd", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Data Full Directory:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Data Tag:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Meas-UAV", None))
        self.groupBox_2.setTitle("")
        self.b_check_dir_tree.setText(QCoreApplication.translate("MainWindow", u"Dir-Tree", None))
        self.b_check_tmux.setText(QCoreApplication.translate("MainWindow", u"Check TMUX", None))
        self.b_check_stroge.setText(QCoreApplication.translate("MainWindow", u"Storage", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Raw Text", None))
        self.pb_get_cam0.setText(QCoreApplication.translate("MainWindow", u"Download and Show Photo", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Visual", None))
    # retranslateUi

