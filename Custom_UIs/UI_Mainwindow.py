# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_Mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QSize,
    Qt,
)
from PySide6.QtGui import (
    QAction,
    QFont,
)
from PySide6.QtWidgets import (
    QAbstractSpinBox,
    QComboBox,
    QDial,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSlider,
    QSpacerItem,
    QSpinBox,
    QSplitter,
    QTabWidget,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

from pyqtgraph import ImageView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow: QMainWindow) -> None:
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1057, 695)
        MainWindow.setStyleSheet(
            ".QLabel { font-size: 12pt;}\n"
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
            "}"
        )
        self.actionOpen_Directory = QAction(MainWindow)
        self.actionOpen_Directory.setObjectName("actionOpen_Directory")
        self.action_cur_jpeg_export = QAction(MainWindow)
        self.action_cur_jpeg_export.setObjectName("action_cur_jpeg_export")
        self.action_geometry_load = QAction(MainWindow)
        self.action_geometry_load.setObjectName("action_geometry_load")
        self.action_help = QAction(MainWindow)
        self.action_help.setObjectName("action_help")
        self.actionRead_Dependencies = QAction(MainWindow)
        self.actionRead_Dependencies.setObjectName("actionRead_Dependencies")
        self.actionContact_information = QAction(MainWindow)
        self.actionContact_information.setObjectName("actionContact_information")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.actionContact = QAction(MainWindow)
        self.actionContact.setObjectName("actionContact")
        self.action_cur_jpeg_preview = QAction(MainWindow)
        self.action_cur_jpeg_preview.setObjectName("action_cur_jpeg_preview")
        self.action_dir_goto_parent = QAction(MainWindow)
        self.action_dir_goto_parent.setObjectName("action_dir_goto_parent")
        self.action_dir_goto_cur_child = QAction(MainWindow)
        self.action_dir_goto_cur_child.setObjectName("action_dir_goto_cur_child")
        self.action_dir_cur_child_fold = QAction(MainWindow)
        self.action_dir_cur_child_fold.setObjectName("action_dir_cur_child_fold")
        self.action_dir_cur_child_unfold = QAction(MainWindow)
        self.action_dir_cur_child_unfold.setObjectName("action_dir_cur_child_unfold")
        self.action_cur_file_open = QAction(MainWindow)
        self.action_cur_file_open.setObjectName("action_cur_file_open")
        self.actionsdf = QAction(MainWindow)
        self.actionsdf.setObjectName("actionsdf")
        self.actionSave_geometry_configuration_Ctrl_Shift_L = QAction(MainWindow)
        self.actionSave_geometry_configuration_Ctrl_Shift_L.setObjectName(
            "actionSave_geometry_configuration_Ctrl_Shift_L"
        )
        self.action_dir_ft_filter_toggle = QAction(MainWindow)
        self.action_dir_ft_filter_toggle.setObjectName("action_dir_ft_filter_toggle")
        self.action_tabs_show_tab1 = QAction(MainWindow)
        self.action_tabs_show_tab1.setObjectName("action_tabs_show_tab1")
        self.action_tabs_show_tab2 = QAction(MainWindow)
        self.action_tabs_show_tab2.setObjectName("action_tabs_show_tab2")
        self.action_tabs_show_tab3 = QAction(MainWindow)
        self.action_tabs_show_tab3.setObjectName("action_tabs_show_tab3")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.le_cmd2send = QLineEdit(self.centralwidget)
        self.le_cmd2send.setObjectName("le_cmd2send")
        font = QFont()
        font.setFamilies(["Monospace"])
        font.setPointSize(12)
        self.le_cmd2send.setFont(font)

        self.gridLayout.addWidget(self.le_cmd2send, 2, 0, 1, 1)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName("splitter")
        self.splitter.setFrameShadow(QFrame.Shadow.Raised)
        self.splitter.setMidLineWidth(0)
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.groupBox = QGroupBox(self.splitter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QTabWidget(self.groupBox)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 50))
        self.tabWidget.setStyleSheet("QTabBar::tab { height: 35px;  }")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setIconSize(QSize(16, 16))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self._l_4 = QLabel(self.tab)
        self._l_4.setObjectName("_l_4")

        self.horizontalLayout_4.addWidget(self._l_4)

        self.cb_this_pc_network_devices = QComboBox(self.tab)
        self.cb_this_pc_network_devices.setObjectName("cb_this_pc_network_devices")

        self.horizontalLayout_4.addWidget(self.cb_this_pc_network_devices)

        self._l_3 = QLabel(self.tab)
        self._l_3.setObjectName("_l_3")

        self.horizontalLayout_4.addWidget(self._l_3)

        self.l_this_pc_ip = QLabel(self.tab)
        self.l_this_pc_ip.setObjectName("l_this_pc_ip")
        self.l_this_pc_ip.setFont(font)

        self.horizontalLayout_4.addWidget(self.l_this_pc_ip)

        self.b_this_pc_get_ip = QPushButton(self.tab)
        self.b_this_pc_get_ip.setObjectName("b_this_pc_get_ip")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.b_this_pc_get_ip.sizePolicy().hasHeightForWidth()
        )
        self.b_this_pc_get_ip.setSizePolicy(sizePolicy)
        self.b_this_pc_get_ip.setMinimumSize(QSize(0, 59))

        self.horizontalLayout_4.addWidget(self.b_this_pc_get_ip)

        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_4 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName("label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.ip_1 = QSpinBox(self.tab)
        self.ip_1.setObjectName("ip_1")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ip_1.sizePolicy().hasHeightForWidth())
        self.ip_1.setSizePolicy(sizePolicy1)
        self.ip_1.setMinimumSize(QSize(100, 50))
        font1 = QFont()
        font1.setFamilies(["Monospace"])
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
        self.ip_2.setObjectName("ip_2")
        sizePolicy1.setHeightForWidth(self.ip_2.sizePolicy().hasHeightForWidth())
        self.ip_2.setSizePolicy(sizePolicy1)
        self.ip_2.setMinimumSize(QSize(100, 50))
        self.ip_2.setFont(font1)
        self.ip_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ip_2.setMaximum(255)
        self.ip_2.setValue(168)

        self.horizontalLayout_3.addWidget(self.ip_2)

        self.ip_3 = QSpinBox(self.tab)
        self.ip_3.setObjectName("ip_3")
        sizePolicy1.setHeightForWidth(self.ip_3.sizePolicy().hasHeightForWidth())
        self.ip_3.setSizePolicy(sizePolicy1)
        self.ip_3.setMinimumSize(QSize(100, 50))
        self.ip_3.setFont(font1)
        self.ip_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ip_3.setMaximum(255)
        self.ip_3.setValue(83)

        self.horizontalLayout_3.addWidget(self.ip_3)

        self.ip_4 = QSpinBox(self.tab)
        self.ip_4.setObjectName("ip_4")
        sizePolicy1.setHeightForWidth(self.ip_4.sizePolicy().hasHeightForWidth())
        self.ip_4.setSizePolicy(sizePolicy1)
        self.ip_4.setMinimumSize(QSize(100, 50))
        self.ip_4.setFont(font1)
        self.ip_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ip_4.setMaximum(255)
        self.ip_4.setValue(59)

        self.horizontalLayout_3.addWidget(self.ip_4)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.b_search_ip_for_pi = QPushButton(self.tab)
        self.b_search_ip_for_pi.setObjectName("b_search_ip_for_pi")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.b_search_ip_for_pi.sizePolicy().hasHeightForWidth()
        )
        self.b_search_ip_for_pi.setSizePolicy(sizePolicy2)
        self.b_search_ip_for_pi.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_5.addWidget(self.b_search_ip_for_pi)

        self.b_ssh_copy_id = QPushButton(self.tab)
        self.b_ssh_copy_id.setObjectName("b_ssh_copy_id")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding
        )
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.b_ssh_copy_id.sizePolicy().hasHeightForWidth()
        )
        self.b_ssh_copy_id.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.b_ssh_copy_id)

        self.b_check_ssh_connection = QPushButton(self.tab)
        self.b_check_ssh_connection.setObjectName("b_check_ssh_connection")
        sizePolicy2.setHeightForWidth(
            self.b_check_ssh_connection.sizePolicy().hasHeightForWidth()
        )
        self.b_check_ssh_connection.setSizePolicy(sizePolicy2)
        self.b_check_ssh_connection.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_5.addWidget(self.b_check_ssh_connection)

        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.b_soft_reboot = QPushButton(self.tab)
        self.b_soft_reboot.setObjectName("b_soft_reboot")
        sizePolicy2.setHeightForWidth(
            self.b_soft_reboot.sizePolicy().hasHeightForWidth()
        )
        self.b_soft_reboot.setSizePolicy(sizePolicy2)
        self.b_soft_reboot.setMinimumSize(QSize(0, 40))

        self.gridLayout_5.addWidget(self.b_soft_reboot, 2, 0, 1, 1)

        self.b_terminate_python_processes = QPushButton(self.tab)
        self.b_terminate_python_processes.setObjectName("b_terminate_python_processes")
        sizePolicy2.setHeightForWidth(
            self.b_terminate_python_processes.sizePolicy().hasHeightForWidth()
        )
        self.b_terminate_python_processes.setSizePolicy(sizePolicy2)
        self.b_terminate_python_processes.setMinimumSize(QSize(0, 40))

        self.gridLayout_5.addWidget(self.b_terminate_python_processes, 2, 1, 1, 1)

        self.b_hard_reboot = QPushButton(self.tab)
        self.b_hard_reboot.setObjectName("b_hard_reboot")
        sizePolicy2.setHeightForWidth(
            self.b_hard_reboot.sizePolicy().hasHeightForWidth()
        )
        self.b_hard_reboot.setSizePolicy(sizePolicy2)
        self.b_hard_reboot.setMinimumSize(QSize(0, 40))

        self.gridLayout_5.addWidget(self.b_hard_reboot, 1, 0, 1, 1)

        self.b_tmux_init = QPushButton(self.tab)
        self.b_tmux_init.setObjectName("b_tmux_init")
        sizePolicy2.setHeightForWidth(self.b_tmux_init.sizePolicy().hasHeightForWidth())
        self.b_tmux_init.setSizePolicy(sizePolicy2)
        self.b_tmux_init.setMinimumSize(QSize(0, 40))

        self.gridLayout_5.addWidget(self.b_tmux_init, 1, 1, 1, 1)

        self.b_info_dump = QPushButton(self.tab)
        self.b_info_dump.setObjectName("b_info_dump")
        sizePolicy2.setHeightForWidth(self.b_info_dump.sizePolicy().hasHeightForWidth())
        self.b_info_dump.setSizePolicy(sizePolicy2)
        self.b_info_dump.setMinimumSize(QSize(0, 40))

        self.gridLayout_5.addWidget(self.b_info_dump, 3, 0, 1, 2)

        self.verticalLayout_4.addLayout(self.gridLayout_5)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tab_2.setStyleSheet(
            "\n"
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
            ""
        )
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        sizePolicy4 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.sp_elv = QSpinBox(self.tab_2)
        self.sp_elv.setObjectName("sp_elv")
        sizePolicy5 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed
        )
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.sp_elv.sizePolicy().hasHeightForWidth())
        self.sp_elv.setSizePolicy(sizePolicy5)
        self.sp_elv.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.sp_elv.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sp_elv.setMinimum(-90)
        self.sp_elv.setMaximum(90)

        self.horizontalLayout_2.addWidget(self.sp_elv)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.d_elv = QDial(self.tab_2)
        self.d_elv.setObjectName("d_elv")
        sizePolicy6 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding
        )
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.d_elv.sizePolicy().hasHeightForWidth())
        self.d_elv.setSizePolicy(sizePolicy6)
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
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(self.tab_2)
        self.label.setObjectName("label")

        self.horizontalLayout.addWidget(self.label)

        self.sp_azi = QSpinBox(self.tab_2)
        self.sp_azi.setObjectName("sp_azi")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(1)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.sp_azi.sizePolicy().hasHeightForWidth())
        self.sp_azi.setSizePolicy(sizePolicy7)
        self.sp_azi.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sp_azi.setMinimum(-180)
        self.sp_azi.setMaximum(180)

        self.horizontalLayout.addWidget(self.sp_azi)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.d_azi = QDial(self.tab_2)
        self.d_azi.setObjectName("d_azi")
        sizePolicy8 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding
        )
        sizePolicy8.setHorizontalStretch(10)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.d_azi.sizePolicy().hasHeightForWidth())
        self.d_azi.setSizePolicy(sizePolicy8)
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
        self.pb_motor_zeroing.setObjectName("pb_motor_zeroing")

        self.gridLayout_3.addWidget(self.pb_motor_zeroing, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_10 = QGridLayout(self.tab_7)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self._l1 = QLabel(self.tab_7)
        self._l1.setObjectName("_l1")

        self.gridLayout_8.addWidget(self._l1, 0, 0, 1, 1)

        self.sp_expo_1 = QSpinBox(self.tab_7)
        self.sp_expo_1.setObjectName("sp_expo_1")
        self.sp_expo_1.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sp_expo_1.setMaximum(2500)

        self.gridLayout_8.addWidget(self.sp_expo_1, 0, 1, 1, 1)

        self.d_expo_1 = QDial(self.tab_7)
        self.d_expo_1.setObjectName("d_expo_1")
        sizePolicy8.setHeightForWidth(self.d_expo_1.sizePolicy().hasHeightForWidth())
        self.d_expo_1.setSizePolicy(sizePolicy8)
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
        self.gridLayout_18.setObjectName("gridLayout_18")
        self._l1_2 = QLabel(self.tab_7)
        self._l1_2.setObjectName("_l1_2")

        self.gridLayout_18.addWidget(self._l1_2, 0, 0, 1, 1)

        self.sp_expo_2 = QSpinBox(self.tab_7)
        self.sp_expo_2.setObjectName("sp_expo_2")
        self.sp_expo_2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sp_expo_2.setMaximum(2500)

        self.gridLayout_18.addWidget(self.sp_expo_2, 0, 1, 1, 1)

        self.d_expo_2 = QDial(self.tab_7)
        self.d_expo_2.setObjectName("d_expo_2")
        sizePolicy8.setHeightForWidth(self.d_expo_2.sizePolicy().hasHeightForWidth())
        self.d_expo_2.setSizePolicy(sizePolicy8)
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
        self.gridLayout_19.setObjectName("gridLayout_19")
        self._l1_3 = QLabel(self.tab_7)
        self._l1_3.setObjectName("_l1_3")

        self.gridLayout_19.addWidget(self._l1_3, 0, 0, 1, 1)

        self.sp_expo_3 = QSpinBox(self.tab_7)
        self.sp_expo_3.setObjectName("sp_expo_3")
        self.sp_expo_3.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sp_expo_3.setMaximum(2500)

        self.gridLayout_19.addWidget(self.sp_expo_3, 0, 1, 1, 1)

        self.d_expo_3 = QDial(self.tab_7)
        self.d_expo_3.setObjectName("d_expo_3")
        sizePolicy8.setHeightForWidth(self.d_expo_3.sizePolicy().hasHeightForWidth())
        self.d_expo_3.setSizePolicy(sizePolicy8)
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
        self.gridLayout_20.setObjectName("gridLayout_20")
        self._l1_4 = QLabel(self.tab_7)
        self._l1_4.setObjectName("_l1_4")

        self.gridLayout_20.addWidget(self._l1_4, 0, 0, 1, 1)

        self.sp_expo_4 = QSpinBox(self.tab_7)
        self.sp_expo_4.setObjectName("sp_expo_4")
        self.sp_expo_4.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sp_expo_4.setMaximum(2500)

        self.gridLayout_20.addWidget(self.sp_expo_4, 0, 1, 1, 1)

        self.d_expo_4 = QDial(self.tab_7)
        self.d_expo_4.setObjectName("d_expo_4")
        sizePolicy8.setHeightForWidth(self.d_expo_4.sizePolicy().hasHeightForWidth())
        self.d_expo_4.setSizePolicy(sizePolicy8)
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
        self.gridLayout_21.setObjectName("gridLayout_21")
        self._l1_5 = QLabel(self.tab_7)
        self._l1_5.setObjectName("_l1_5")

        self.gridLayout_21.addWidget(self._l1_5, 0, 0, 1, 1)

        self.sp_expo_5 = QSpinBox(self.tab_7)
        self.sp_expo_5.setObjectName("sp_expo_5")
        self.sp_expo_5.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sp_expo_5.setMaximum(2500)

        self.gridLayout_21.addWidget(self.sp_expo_5, 0, 1, 1, 1)

        self.d_expo_5 = QDial(self.tab_7)
        self.d_expo_5.setObjectName("d_expo_5")
        sizePolicy8.setHeightForWidth(self.d_expo_5.sizePolicy().hasHeightForWidth())
        self.d_expo_5.setSizePolicy(sizePolicy8)
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
        self.gridLayout_22.setObjectName("gridLayout_22")
        self._l1_6 = QLabel(self.tab_7)
        self._l1_6.setObjectName("_l1_6")

        self.gridLayout_22.addWidget(self._l1_6, 0, 0, 1, 1)

        self.sp_expo_6 = QSpinBox(self.tab_7)
        self.sp_expo_6.setObjectName("sp_expo_6")
        self.sp_expo_6.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sp_expo_6.setMaximum(2500)

        self.gridLayout_22.addWidget(self.sp_expo_6, 0, 1, 1, 1)

        self.d_expo_6 = QDial(self.tab_7)
        self.d_expo_6.setObjectName("d_expo_6")
        sizePolicy8.setHeightForWidth(self.d_expo_6.sizePolicy().hasHeightForWidth())
        self.d_expo_6.setSizePolicy(sizePolicy8)
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
        self.gridLayout_23.setObjectName("gridLayout_23")
        self._l1_7 = QLabel(self.tab_7)
        self._l1_7.setObjectName("_l1_7")

        self.gridLayout_23.addWidget(self._l1_7, 0, 0, 1, 1)

        self.sp_expo_7 = QSpinBox(self.tab_7)
        self.sp_expo_7.setObjectName("sp_expo_7")
        self.sp_expo_7.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sp_expo_7.setMaximum(2500)

        self.gridLayout_23.addWidget(self.sp_expo_7, 0, 1, 1, 1)

        self.d_expo_7 = QDial(self.tab_7)
        self.d_expo_7.setObjectName("d_expo_7")
        sizePolicy8.setHeightForWidth(self.d_expo_7.sizePolicy().hasHeightForWidth())
        self.d_expo_7.setSizePolicy(sizePolicy8)
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
        self.gridLayout_24.setObjectName("gridLayout_24")
        self._l1_8 = QLabel(self.tab_7)
        self._l1_8.setObjectName("_l1_8")

        self.gridLayout_24.addWidget(self._l1_8, 0, 0, 1, 1)

        self.sp_expo_8 = QSpinBox(self.tab_7)
        self.sp_expo_8.setObjectName("sp_expo_8")
        self.sp_expo_8.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sp_expo_8.setMaximum(2500)

        self.gridLayout_24.addWidget(self.sp_expo_8, 0, 1, 1, 1)

        self.d_expo_8 = QDial(self.tab_7)
        self.d_expo_8.setObjectName("d_expo_8")
        sizePolicy8.setHeightForWidth(self.d_expo_8.sizePolicy().hasHeightForWidth())
        self.d_expo_8.setSizePolicy(sizePolicy8)
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
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_4 = QLabel(self.tab_7)
        self.label_4.setObjectName("label_4")

        self.gridLayout_9.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_3 = QLabel(self.tab_7)
        self.label_3.setObjectName("label_3")

        self.gridLayout_9.addWidget(self.label_3, 1, 0, 1, 1)

        self.le_expo_plus_str = QLineEdit(self.tab_7)
        self.le_expo_plus_str.setObjectName("le_expo_plus_str")

        self.gridLayout_9.addWidget(self.le_expo_plus_str, 2, 1, 1, 1)

        self.le_expo_minus_str = QLineEdit(self.tab_7)
        self.le_expo_minus_str.setObjectName("le_expo_minus_str")

        self.gridLayout_9.addWidget(self.le_expo_minus_str, 0, 1, 1, 1)

        self.label_5 = QLabel(self.tab_7)
        self.label_5.setObjectName("label_5")

        self.gridLayout_9.addWidget(self.label_5, 2, 0, 1, 1)

        self.le_expo_base_str = QLineEdit(self.tab_7)
        self.le_expo_base_str.setObjectName("le_expo_base_str")

        self.gridLayout_9.addWidget(self.le_expo_base_str, 1, 1, 1, 1)

        self.spinBox_2 = QSpinBox(self.tab_7)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_2.setMaximum(3)
        self.spinBox_2.setValue(1)

        self.gridLayout_9.addWidget(self.spinBox_2, 2, 2, 1, 1)

        self.spinBox = QSpinBox(self.tab_7)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spinBox.setMinimum(-3)
        self.spinBox.setMaximum(0)
        self.spinBox.setValue(-1)

        self.gridLayout_9.addWidget(self.spinBox, 0, 2, 1, 1)

        self.b_1shot = QPushButton(self.tab_7)
        self.b_1shot.setObjectName("b_1shot")
        sizePolicy1.setHeightForWidth(self.b_1shot.sizePolicy().hasHeightForWidth())
        self.b_1shot.setSizePolicy(sizePolicy1)
        self.b_1shot.setMinimumSize(QSize(120, 0))

        self.gridLayout_9.addWidget(self.b_1shot, 0, 3, 3, 1)

        self.gridLayout_10.addLayout(self.gridLayout_9, 2, 0, 1, 4)

        self.tabWidget.addTab(self.tab_7, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.lineEdit_3 = QLineEdit(self.tab_3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setEnabled(False)

        self.gridLayout_12.addWidget(self.lineEdit_3, 0, 1, 1, 1)

        self.label_12 = QLabel(self.tab_3)
        self.label_12.setObjectName("label_12")

        self.gridLayout_12.addWidget(self.label_12, 0, 0, 1, 1)

        self.qe_tag = QLineEdit(self.tab_3)
        self.qe_tag.setObjectName("qe_tag")

        self.gridLayout_12.addWidget(self.qe_tag, 1, 1, 1, 1)

        self.label_13 = QLabel(self.tab_3)
        self.label_13.setObjectName("label_13")

        self.gridLayout_12.addWidget(self.label_13, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.tab_3)
        self.pushButton.setObjectName("pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)

        self.gridLayout_12.addWidget(self.pushButton, 0, 2, 2, 1)

        self.gridLayout_4.addLayout(self.gridLayout_12, 3, 0, 1, 1)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.hs_azi_0 = QSlider(self.tab_3)
        self.hs_azi_0.setObjectName("hs_azi_0")
        sizePolicy9 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.hs_azi_0.sizePolicy().hasHeightForWidth())
        self.hs_azi_0.setSizePolicy(sizePolicy9)
        self.hs_azi_0.setMinimum(0)
        self.hs_azi_0.setMaximum(180)
        self.hs_azi_0.setValue(180)
        self.hs_azi_0.setOrientation(Qt.Orientation.Horizontal)
        self.hs_azi_0.setInvertedAppearance(True)

        self.gridLayout_13.addWidget(self.hs_azi_0, 0, 0, 1, 1)

        self.sb_azi_0 = QSpinBox(self.tab_3)
        self.sb_azi_0.setObjectName("sb_azi_0")
        self.sb_azi_0.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.sb_azi_0.setMinimum(-180)
        self.sb_azi_0.setMaximum(0)
        self.sb_azi_0.setValue(-180)

        self.gridLayout_13.addWidget(self.sb_azi_0, 0, 1, 1, 1)

        self.hs_elv_0 = QSlider(self.tab_3)
        self.hs_elv_0.setObjectName("hs_elv_0")
        self.hs_elv_0.setMaximum(90)
        self.hs_elv_0.setSingleStep(5)
        self.hs_elv_0.setPageStep(1)
        self.hs_elv_0.setValue(45)
        self.hs_elv_0.setOrientation(Qt.Orientation.Horizontal)
        self.hs_elv_0.setInvertedAppearance(True)
        self.hs_elv_0.setInvertedControls(False)

        self.gridLayout_13.addWidget(self.hs_elv_0, 2, 0, 1, 1)

        self.sb_elv_0 = QSpinBox(self.tab_3)
        self.sb_elv_0.setObjectName("sb_elv_0")
        self.sb_elv_0.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.sb_elv_0.setMinimum(-90)
        self.sb_elv_0.setMaximum(0)
        self.sb_elv_0.setSingleStep(1)
        self.sb_elv_0.setValue(0)

        self.gridLayout_13.addWidget(self.sb_elv_0, 2, 1, 1, 1)

        self._l_2 = QLabel(self.tab_3)
        self._l_2.setObjectName("_l_2")

        self.gridLayout_13.addWidget(self._l_2, 2, 2, 1, 1)

        self._l = QLabel(self.tab_3)
        self._l.setObjectName("_l")

        self.gridLayout_13.addWidget(self._l, 0, 2, 1, 1)

        self.sb_azi_1 = QSpinBox(self.tab_3)
        self.sb_azi_1.setObjectName("sb_azi_1")
        self.sb_azi_1.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.sb_azi_1.setMaximum(180)
        self.sb_azi_1.setValue(180)

        self.gridLayout_13.addWidget(self.sb_azi_1, 0, 3, 1, 1)

        self.sb_elv_1 = QSpinBox(self.tab_3)
        self.sb_elv_1.setObjectName("sb_elv_1")
        self.sb_elv_1.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.sb_elv_1.setMinimum(-70)
        self.sb_elv_1.setMaximum(45)

        self.gridLayout_13.addWidget(self.sb_elv_1, 2, 3, 1, 1)

        self.hs_azi_1 = QSlider(self.tab_3)
        self.hs_azi_1.setObjectName("hs_azi_1")
        sizePolicy9.setHeightForWidth(self.hs_azi_1.sizePolicy().hasHeightForWidth())
        self.hs_azi_1.setSizePolicy(sizePolicy9)
        self.hs_azi_1.setMaximum(180)
        self.hs_azi_1.setValue(90)
        self.hs_azi_1.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_13.addWidget(self.hs_azi_1, 0, 4, 1, 1)

        self.hs_elv_1 = QSlider(self.tab_3)
        self.hs_elv_1.setObjectName("hs_elv_1")
        self.hs_elv_1.setMinimum(-70)
        self.hs_elv_1.setMaximum(45)
        self.hs_elv_1.setSingleStep(5)
        self.hs_elv_1.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_13.addWidget(self.hs_elv_1, 2, 4, 1, 1)

        self.gridLayout_4.addLayout(self.gridLayout_13, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout_5 = QVBoxLayout(self.tab_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.pushButton_7 = QPushButton(self.tab_6)
        self.pushButton_7.setObjectName("pushButton_7")
        sizePolicy1.setHeightForWidth(
            self.pushButton_7.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_7.setSizePolicy(sizePolicy1)

        self.gridLayout_11.addWidget(self.pushButton_7, 0, 2, 2, 1)

        self.label_9 = QLabel(self.tab_6)
        self.label_9.setObjectName("label_9")

        self.gridLayout_11.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_10 = QLabel(self.tab_6)
        self.label_10.setObjectName("label_10")

        self.gridLayout_11.addWidget(self.label_10, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.tab_6)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEnabled(False)

        self.gridLayout_11.addWidget(self.lineEdit_2, 0, 1, 1, 1)

        self.lineEdit = QLineEdit(self.tab_6)
        self.lineEdit.setObjectName("lineEdit")

        self.gridLayout_11.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.verticalLayout_5.addLayout(self.gridLayout_11)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_6, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.splitter.addWidget(self.groupBox)
        self.groupBox_2 = QGroupBox(self.splitter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_6 = QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tabWidget_2 = QTabWidget(self.groupBox_2)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_2 = QVBoxLayout(self.tab_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_8 = QPushButton(self.tab_4)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 80))

        self.verticalLayout_2.addWidget(self.pushButton_8)

        self.text_output = QTextBrowser(self.tab_4)
        self.text_output.setObjectName("text_output")

        self.verticalLayout_2.addWidget(self.text_output)

        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_7 = QGridLayout(self.tab_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pb_get_cam0 = QPushButton(self.tab_5)
        self.pb_get_cam0.setObjectName("pb_get_cam0")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(
            self.pb_get_cam0.sizePolicy().hasHeightForWidth()
        )
        self.pb_get_cam0.setSizePolicy(sizePolicy10)
        self.pb_get_cam0.setMinimumSize(QSize(0, 80))

        self.gridLayout_7.addWidget(self.pb_get_cam0, 0, 0, 1, 2)

        self.image_view = ImageView(self.tab_5)
        self.image_view.setObjectName("image_view")

        self.gridLayout_7.addWidget(self.image_view, 3, 0, 1, 2)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tabWidget_2.addTab(self.tab_8, "")

        self.gridLayout_6.addWidget(self.tabWidget_2, 0, 0, 1, 1)

        self.splitter.addWidget(self.groupBox_2)

        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 2)

        self.pb_send_cmd = QPushButton(self.centralwidget)
        self.pb_send_cmd.setObjectName("pb_send_cmd")
        self.pb_send_cmd.setMinimumSize(QSize(100, 60))

        self.gridLayout.addWidget(self.pb_send_cmd, 2, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(2)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow: QMainWindow) -> None:
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.actionOpen_Directory.setText(
            QCoreApplication.translate("MainWindow", "Open Directory", None)
        )
        self.action_cur_jpeg_export.setText(
            QCoreApplication.translate("MainWindow", "Export (Ctlr-E)", None)
        )
        self.action_geometry_load.setText(
            QCoreApplication.translate(
                "MainWindow", "Load geometry configuration (Ctrl + L)", None
            )
        )
        self.action_help.setText(
            QCoreApplication.translate("MainWindow", "Help (Ctrl+H)", None)
        )
        self.actionRead_Dependencies.setText(
            QCoreApplication.translate("MainWindow", "Read Dependencies", None)
        )
        self.actionContact_information.setText(
            QCoreApplication.translate("MainWindow", "Contact information", None)
        )
        self.action_about.setText(
            QCoreApplication.translate("MainWindow", "About (Ctrl+A)", None)
        )
        self.actionContact.setText(
            QCoreApplication.translate("MainWindow", "Contact", None)
        )
        self.action_cur_jpeg_preview.setText(
            QCoreApplication.translate("MainWindow", "Preview (Space)", None)
        )
        self.action_dir_goto_parent.setText(
            QCoreApplication.translate(
                "MainWindow", "Go to Parent Directory (Backspace)", None
            )
        )
        self.action_dir_goto_cur_child.setText(
            QCoreApplication.translate(
                "MainWindow", "Go inside Selected Directory (Enter)", None
            )
        )
        self.action_dir_cur_child_fold.setText(
            QCoreApplication.translate(
                "MainWindow", "Fold Selected Directory (Left Arrow)", None
            )
        )
        self.action_dir_cur_child_unfold.setText(
            QCoreApplication.translate(
                "MainWindow", "Unfold Selected Directory (Right Arrow)", None
            )
        )
        self.action_cur_file_open.setText(
            QCoreApplication.translate(
                "MainWindow", "Open with an external app (Ctrl+O)", None
            )
        )
        self.actionsdf.setText(QCoreApplication.translate("MainWindow", "sdf", None))
        self.actionSave_geometry_configuration_Ctrl_Shift_L.setText(
            QCoreApplication.translate(
                "MainWindow", "Save geometry configuration (Ctrl + Shift + L)", None
            )
        )
        self.action_dir_ft_filter_toggle.setText(
            QCoreApplication.translate(
                "MainWindow", "File type filter toggle (Ctrl+F)", None
            )
        )
        self.action_tabs_show_tab1.setText(
            QCoreApplication.translate(
                "MainWindow", "Raw Bayer Tab (Ctrl+1) or (Alt+1)", None
            )
        )
        self.action_tabs_show_tab2.setText(
            QCoreApplication.translate(
                "MainWindow", "Spectrum-Raw Tab (Ctrl+2) or (Alt+2)", None
            )
        )
        self.action_tabs_show_tab3.setText(
            QCoreApplication.translate(
                "MainWindow", "Spectrum-Reflectance Tab (Ctrl+3) or (Alt+3)", None
            )
        )
        self.groupBox.setTitle(
            QCoreApplication.translate("MainWindow", "Control", None)
        )
        self._l_4.setText(
            QCoreApplication.translate("MainWindow", "This PC IP on", None)
        )
        self._l_3.setText(QCoreApplication.translate("MainWindow", "is", None))
        self.l_this_pc_ip.setText(
            QCoreApplication.translate("MainWindow", "..................", None)
        )
        self.b_this_pc_get_ip.setText(
            QCoreApplication.translate("MainWindow", "Recheck PC ip", None)
        )
        self.label_6.setText(
            QCoreApplication.translate("MainWindow", "Enter Device IP address", None)
        )
        self.b_search_ip_for_pi.setText(
            QCoreApplication.translate("MainWindow", "Search for IP (1~2min)", None)
        )
        self.b_ssh_copy_id.setText(
            QCoreApplication.translate("MainWindow", "ssh-copy-ip", None)
        )
        self.b_check_ssh_connection.setText(
            QCoreApplication.translate("MainWindow", "Check SSH Connection", None)
        )
        self.b_soft_reboot.setText(
            QCoreApplication.translate("MainWindow", "Soft Reboot", None)
        )
        self.b_terminate_python_processes.setText(
            QCoreApplication.translate(
                "MainWindow", "Terminal All Tmux & Python processes", None
            )
        )
        self.b_hard_reboot.setText(
            QCoreApplication.translate("MainWindow", "Reboot", None)
        )
        self.b_tmux_init.setText(
            QCoreApplication.translate("MainWindow", "Initialize TMUX", None)
        )
        self.b_info_dump.setText(
            QCoreApplication.translate("MainWindow", "Info Dump", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            QCoreApplication.translate("MainWindow", "Connection", None),
        )
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", "Motor-Elevation", None)
        )
        self.label.setText(
            QCoreApplication.translate("MainWindow", "Motor-Azimuth", None)
        )
        self.sp_azi.setSuffix("")
        self.pb_motor_zeroing.setText(
            QCoreApplication.translate("MainWindow", "Set curret to 0", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            QCoreApplication.translate("MainWindow", "Motor", None),
        )
        self._l1.setText(QCoreApplication.translate("MainWindow", "Cam1", None))
        self._l1_2.setText(QCoreApplication.translate("MainWindow", "Cam2", None))
        self._l1_3.setText(QCoreApplication.translate("MainWindow", "Cam3", None))
        self._l1_4.setText(QCoreApplication.translate("MainWindow", "Cam4", None))
        self._l1_5.setText(QCoreApplication.translate("MainWindow", "Cam5", None))
        self._l1_6.setText(QCoreApplication.translate("MainWindow", "Cam6", None))
        self._l1_7.setText(QCoreApplication.translate("MainWindow", "Cam7", None))
        self._l1_8.setText(QCoreApplication.translate("MainWindow", "Cam8", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", "Lower", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", "Base", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", "Higher", None))
        self.b_1shot.setText(QCoreApplication.translate("MainWindow", "1shot", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_7),
            QCoreApplication.translate("MainWindow", "Exposure", None),
        )
        self.label_12.setText(
            QCoreApplication.translate("MainWindow", "Data full Path", None)
        )
        self.label_13.setText(
            QCoreApplication.translate("MainWindow", "Data tag", None)
        )
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", "PushButton", None)
        )
        self._l_2.setText(QCoreApplication.translate("MainWindow", "Elevation", None))
        self._l.setText(QCoreApplication.translate("MainWindow", "Azimuth ", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_3),
            QCoreApplication.translate("MainWindow", "Meas-Gimbal", None),
        )
        self.pushButton_7.setText(
            QCoreApplication.translate("MainWindow", "Start Measurement", None)
        )
        self.label_9.setText(
            QCoreApplication.translate("MainWindow", "Data Full Directory:", None)
        )
        self.label_10.setText(
            QCoreApplication.translate("MainWindow", "Data Tag:", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_6),
            QCoreApplication.translate("MainWindow", "Meas-UAV", None),
        )
        self.groupBox_2.setTitle(
            QCoreApplication.translate("MainWindow", "Monitor", None)
        )
        self.pushButton_8.setText(
            QCoreApplication.translate("MainWindow", "Check TMUX", None)
        )
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.tab_4),
            QCoreApplication.translate("MainWindow", "Raw Text", None),
        )
        self.pb_get_cam0.setText(
            QCoreApplication.translate("MainWindow", "Download and Show Photo", None)
        )
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.tab_5),
            QCoreApplication.translate("MainWindow", "Visual", None),
        )
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.tab_8),
            QCoreApplication.translate("MainWindow", "Page", None),
        )
        self.pb_send_cmd.setText(QCoreApplication.translate("MainWindow", "SEND", None))

    # retranslateUi
