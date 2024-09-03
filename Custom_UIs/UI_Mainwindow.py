# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_Mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
    QDial,
    QFrame,
    QGridLayout,
    QGroupBox,
    QLabel,
    QLineEdit,
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
from pyqtgraph.opengl import GLViewWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        MainWindow.setStyleSheet(
            ".QLabel { font-size: 12pt;}\n"
            ".QSpinBox { font-size: 12pt;}\n"
            ".QCheckBox { font-size: 12pt;}\n"
            ".QCheckBox::indicator {\n"
            "    width: 25px;\n"
            "    height: 25px;\n"
            "}\n"
            ".QPushButton { font-size: 12pt;}\n"
            ".QTabWidget { font-size: 12pt;}\n"
            ".QLineEdit { font-size: 12pt;}\n"
            ".QSpinBox::down-button{ width: 30;}\n"
            ".QSpinBox::up-button{ width: 30;  }\n"
            ".QSplitter::handle {\n"
            "    image: url(/tmp/sit.svg);\n"
            "}\n"
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

        self.pb_send_cmd = QPushButton(self.centralwidget)
        self.pb_send_cmd.setObjectName("pb_send_cmd")
        self.pb_send_cmd.setMinimumSize(QSize(100, 60))

        self.gridLayout.addWidget(self.pb_send_cmd, 2, 1, 1, 1)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName("splitter")
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
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName("label_8")

        self.gridLayout_5.addWidget(self.label_8, 2, 0, 1, 1)

        self.ip_sky_4 = QSpinBox(self.tab)
        self.ip_sky_4.setObjectName("ip_sky_4")
        self.ip_sky_4.setMinimumSize(QSize(100, 50))
        self.ip_sky_4.setFont(font)
        self.ip_sky_4.setMaximum(255)
        self.ip_sky_4.setValue(171)

        self.gridLayout_5.addWidget(self.ip_sky_4, 2, 4, 1, 1)

        self.ip_2 = QSpinBox(self.tab)
        self.ip_2.setObjectName("ip_2")
        self.ip_2.setMinimumSize(QSize(100, 50))
        self.ip_2.setFont(font)
        self.ip_2.setMaximum(255)
        self.ip_2.setValue(168)

        self.gridLayout_5.addWidget(self.ip_2, 0, 2, 1, 1)

        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName("label_7")

        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)

        self.ip_4 = QSpinBox(self.tab)
        self.ip_4.setObjectName("ip_4")
        self.ip_4.setMinimumSize(QSize(100, 50))
        self.ip_4.setFont(font)
        self.ip_4.setMaximum(255)
        self.ip_4.setValue(2)

        self.gridLayout_5.addWidget(self.ip_4, 0, 4, 1, 1)

        self.ip_sky_3 = QSpinBox(self.tab)
        self.ip_sky_3.setObjectName("ip_sky_3")
        self.ip_sky_3.setMinimumSize(QSize(100, 50))
        self.ip_sky_3.setFont(font)
        self.ip_sky_3.setMaximum(255)
        self.ip_sky_3.setValue(12)

        self.gridLayout_5.addWidget(self.ip_sky_3, 2, 3, 1, 1)

        self.ip_1 = QSpinBox(self.tab)
        self.ip_1.setObjectName("ip_1")
        self.ip_1.setMinimumSize(QSize(100, 50))
        self.ip_1.setFont(font)
        self.ip_1.setWrapping(False)
        self.ip_1.setFrame(True)
        self.ip_1.setReadOnly(False)
        self.ip_1.setMaximum(255)
        self.ip_1.setSingleStep(1)
        self.ip_1.setValue(192)

        self.gridLayout_5.addWidget(self.ip_1, 0, 1, 1, 1)

        self.ip_3 = QSpinBox(self.tab)
        self.ip_3.setObjectName("ip_3")
        self.ip_3.setMinimumSize(QSize(100, 50))
        self.ip_3.setFont(font)
        self.ip_3.setMaximum(255)
        self.ip_3.setValue(11)

        self.gridLayout_5.addWidget(self.ip_3, 0, 3, 1, 1)

        self.ip_sky_1 = QSpinBox(self.tab)
        self.ip_sky_1.setObjectName("ip_sky_1")
        self.ip_sky_1.setMinimumSize(QSize(100, 50))
        self.ip_sky_1.setFont(font)
        self.ip_sky_1.setWrapping(False)
        self.ip_sky_1.setFrame(True)
        self.ip_sky_1.setReadOnly(False)
        self.ip_sky_1.setMaximum(255)
        self.ip_sky_1.setSingleStep(1)
        self.ip_sky_1.setValue(192)

        self.gridLayout_5.addWidget(self.ip_sky_1, 2, 1, 1, 1)

        self.ip_sky_2 = QSpinBox(self.tab)
        self.ip_sky_2.setObjectName("ip_sky_2")
        self.ip_sky_2.setMinimumSize(QSize(100, 50))
        self.ip_sky_2.setFont(font)
        self.ip_sky_2.setMaximum(255)
        self.ip_sky_2.setValue(168)

        self.gridLayout_5.addWidget(self.ip_sky_2, 2, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.gridLayout_5.addItem(self.verticalSpacer_5, 1, 2, 1, 1)

        self.verticalLayout_3.addLayout(self.gridLayout_5)

        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

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
        self.line_2 = QFrame(self.tab_2)
        self.line_2.setObjectName("line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_2, 2, 0, 1, 2)

        self.d_gain = QDial(self.tab_2)
        self.d_gain.setObjectName("d_gain")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding
        )
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d_gain.sizePolicy().hasHeightForWidth())
        self.d_gain.setSizePolicy(sizePolicy)
        self.d_gain.setMinimum(1)
        self.d_gain.setMaximum(33)
        self.d_gain.setPageStep(1)
        self.d_gain.setOrientation(Qt.Orientation.Horizontal)
        self.d_gain.setInvertedAppearance(False)
        self.d_gain.setWrapping(False)
        self.d_gain.setNotchTarget(33.000000000000000)
        self.d_gain.setNotchesVisible(True)

        self.gridLayout_3.addWidget(self.d_gain, 4, 3, 1, 2)

        self.sp_azi = QSpinBox(self.tab_2)
        self.sp_azi.setObjectName("sp_azi")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sp_azi.sizePolicy().hasHeightForWidth())
        self.sp_azi.setSizePolicy(sizePolicy1)
        self.sp_azi.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sp_azi.setMinimum(-180)
        self.sp_azi.setMaximum(180)

        self.gridLayout_3.addWidget(self.sp_azi, 0, 1, 1, 1)

        self.label = QLabel(self.tab_2)
        self.label.setObjectName("label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.pb_motor_zeroing = QPushButton(self.tab_2)
        self.pb_motor_zeroing.setObjectName("pb_motor_zeroing")
        self.pb_motor_zeroing.setMinimumSize(QSize(0, 45))

        self.gridLayout_3.addWidget(self.pb_motor_zeroing, 6, 0, 1, 2)

        self.d_elv = QDial(self.tab_2)
        self.d_elv.setObjectName("d_elv")
        self.d_elv.setMinimum(-90)
        self.d_elv.setMaximum(90)
        self.d_elv.setSingleStep(1)
        self.d_elv.setPageStep(1)
        self.d_elv.setValue(-45)
        self.d_elv.setSliderPosition(-45)
        self.d_elv.setOrientation(Qt.Orientation.Vertical)
        self.d_elv.setInvertedAppearance(False)
        self.d_elv.setInvertedControls(True)
        self.d_elv.setWrapping(False)
        self.d_elv.setNotchTarget(10.000000000000000)
        self.d_elv.setNotchesVisible(True)

        self.gridLayout_3.addWidget(self.d_elv, 4, 0, 1, 2)

        self.line = QFrame(self.tab_2)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line, 0, 2, 5, 1)

        self.pb_bno_check = QPushButton(self.tab_2)
        self.pb_bno_check.setObjectName("pb_bno_check")
        self.pb_bno_check.setMinimumSize(QSize(0, 45))

        self.gridLayout_3.addWidget(self.pb_bno_check, 7, 0, 1, 2)

        self.line_4 = QFrame(self.tab_2)
        self.line_4.setObjectName("line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_4, 5, 0, 1, 2)

        self.sp_expo = QSpinBox(self.tab_2)
        self.sp_expo.setObjectName("sp_expo")
        self.sp_expo.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sp_expo.setMaximum(2500)

        self.gridLayout_3.addWidget(self.sp_expo, 0, 4, 1, 1)

        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("")

        self.gridLayout_3.addWidget(self.label_3, 3, 3, 1, 1)

        self.d_expo = QDial(self.tab_2)
        self.d_expo.setObjectName("d_expo")
        sizePolicy.setHeightForWidth(self.d_expo.sizePolicy().hasHeightForWidth())
        self.d_expo.setSizePolicy(sizePolicy)
        self.d_expo.setMinimum(0)
        self.d_expo.setMaximum(11)
        self.d_expo.setOrientation(Qt.Orientation.Horizontal)
        self.d_expo.setInvertedAppearance(False)
        self.d_expo.setWrapping(False)
        self.d_expo.setNotchTarget(10.000000000000000)
        self.d_expo.setNotchesVisible(True)

        self.gridLayout_3.addWidget(self.d_expo, 1, 3, 1, 2)

        self.sp_gain = QSpinBox(self.tab_2)
        self.sp_gain.setObjectName("sp_gain")
        self.sp_gain.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sp_gain.setMaximum(33)

        self.gridLayout_3.addWidget(self.sp_gain, 3, 4, 1, 1)

        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName("label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 3, 1, 1)

        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")

        self.gridLayout_3.addWidget(self.label_2, 3, 0, 1, 1)

        self.sp_elv = QSpinBox(self.tab_2)
        self.sp_elv.setObjectName("sp_elv")
        sizePolicy1.setHeightForWidth(self.sp_elv.sizePolicy().hasHeightForWidth())
        self.sp_elv.setSizePolicy(sizePolicy1)
        self.sp_elv.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sp_elv.setMinimum(-90)
        self.sp_elv.setMaximum(90)

        self.gridLayout_3.addWidget(self.sp_elv, 3, 1, 1, 1)

        self.line_5 = QFrame(self.tab_2)
        self.line_5.setObjectName("line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_5, 5, 3, 1, 2)

        self.line_3 = QFrame(self.tab_2)
        self.line_3.setObjectName("line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_3, 2, 3, 1, 2)

        self.d_azi = QDial(self.tab_2)
        self.d_azi.setObjectName("d_azi")
        sizePolicy.setHeightForWidth(self.d_azi.sizePolicy().hasHeightForWidth())
        self.d_azi.setSizePolicy(sizePolicy)
        self.d_azi.setMinimum(-180)
        self.d_azi.setMaximum(180)
        self.d_azi.setOrientation(Qt.Orientation.Horizontal)
        self.d_azi.setInvertedAppearance(False)
        self.d_azi.setWrapping(True)
        self.d_azi.setNotchTarget(10.000000000000000)
        self.d_azi.setNotchesVisible(True)

        self.gridLayout_3.addWidget(self.d_azi, 1, 0, 1, 2)

        self.pb_capture_shot = QPushButton(self.tab_2)
        self.pb_capture_shot.setObjectName("pb_capture_shot")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.pb_capture_shot.sizePolicy().hasHeightForWidth()
        )
        self.pb_capture_shot.setSizePolicy(sizePolicy2)
        self.pb_capture_shot.setMinimumSize(QSize(0, 45))

        self.gridLayout_3.addWidget(self.pb_capture_shot, 6, 3, 1, 2)

        self.pb_webcam_shot = QPushButton(self.tab_2)
        self.pb_webcam_shot.setObjectName("pb_webcam_shot")
        self.pb_webcam_shot.setMinimumSize(QSize(0, 45))

        self.gridLayout_3.addWidget(self.pb_webcam_shot, 7, 3, 1, 2)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.hs_azi_0 = QSlider(self.tab_3)
        self.hs_azi_0.setObjectName("hs_azi_0")
        self.hs_azi_0.setMinimum(0)
        self.hs_azi_0.setMaximum(180)
        self.hs_azi_0.setValue(180)
        self.hs_azi_0.setOrientation(Qt.Orientation.Horizontal)
        self.hs_azi_0.setInvertedAppearance(True)

        self.gridLayout_4.addWidget(self.hs_azi_0, 2, 0, 1, 1)

        self.hs_azi_1 = QSlider(self.tab_3)
        self.hs_azi_1.setObjectName("hs_azi_1")
        self.hs_azi_1.setMaximum(180)
        self.hs_azi_1.setValue(90)
        self.hs_azi_1.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_4.addWidget(self.hs_azi_1, 2, 4, 1, 1)

        self.sb_elv_1 = QSpinBox(self.tab_3)
        self.sb_elv_1.setObjectName("sb_elv_1")
        self.sb_elv_1.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.sb_elv_1.setMinimum(-70)
        self.sb_elv_1.setMaximum(45)

        self.gridLayout_4.addWidget(self.sb_elv_1, 4, 3, 1, 1)

        self.widget = GLViewWidget(self.tab_3)
        self.widget.setObjectName("widget")

        self.gridLayout_4.addWidget(self.widget, 1, 3, 1, 2)

        self.sb_elv_0 = QSpinBox(self.tab_3)
        self.sb_elv_0.setObjectName("sb_elv_0")
        self.sb_elv_0.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.sb_elv_0.setMinimum(-90)
        self.sb_elv_0.setMaximum(0)
        self.sb_elv_0.setSingleStep(1)
        self.sb_elv_0.setValue(-45)

        self.gridLayout_4.addWidget(self.sb_elv_0, 4, 1, 1, 1)

        self.sb_azi_0 = QSpinBox(self.tab_3)
        self.sb_azi_0.setObjectName("sb_azi_0")
        self.sb_azi_0.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.sb_azi_0.setMinimum(-180)
        self.sb_azi_0.setMaximum(0)
        self.sb_azi_0.setValue(-180)

        self.gridLayout_4.addWidget(self.sb_azi_0, 2, 1, 1, 1)

        self.qe_tag = QLineEdit(self.tab_3)
        self.qe_tag.setObjectName("qe_tag")

        self.gridLayout_4.addWidget(self.qe_tag, 5, 0, 1, 1)

        self.hs_elv_1 = QSlider(self.tab_3)
        self.hs_elv_1.setObjectName("hs_elv_1")
        self.hs_elv_1.setMinimum(-70)
        self.hs_elv_1.setMaximum(45)
        self.hs_elv_1.setSingleStep(5)
        self.hs_elv_1.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_4.addWidget(self.hs_elv_1, 4, 4, 1, 1)

        self.sb_azi_1 = QSpinBox(self.tab_3)
        self.sb_azi_1.setObjectName("sb_azi_1")
        self.sb_azi_1.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.sb_azi_1.setMaximum(180)
        self.sb_azi_1.setValue(180)

        self.gridLayout_4.addWidget(self.sb_azi_1, 2, 3, 1, 1)

        self.hs_elv_0 = QSlider(self.tab_3)
        self.hs_elv_0.setObjectName("hs_elv_0")
        self.hs_elv_0.setMaximum(90)
        self.hs_elv_0.setSingleStep(5)
        self.hs_elv_0.setPageStep(1)
        self.hs_elv_0.setValue(45)
        self.hs_elv_0.setOrientation(Qt.Orientation.Horizontal)
        self.hs_elv_0.setInvertedAppearance(True)
        self.hs_elv_0.setInvertedControls(False)

        self.gridLayout_4.addWidget(self.hs_elv_0, 4, 0, 1, 1)

        self._l_2 = QLabel(self.tab_3)
        self._l_2.setObjectName("_l_2")

        self.gridLayout_4.addWidget(self._l_2, 4, 2, 1, 1)

        self._l = QLabel(self.tab_3)
        self._l.setObjectName("_l")

        self.gridLayout_4.addWidget(self._l, 2, 2, 1, 1)

        self.pb_bno_save = QPushButton(self.tab_3)
        self.pb_bno_save.setObjectName("pb_bno_save")

        self.gridLayout_4.addWidget(self.pb_bno_save, 0, 3, 1, 2)

        self.le_bno_save_path = QLineEdit(self.tab_3)
        self.le_bno_save_path.setObjectName("le_bno_save_path")

        self.gridLayout_4.addWidget(self.le_bno_save_path, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout = QVBoxLayout(self.tab_6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.b_tmux_starter = QPushButton(self.tab_6)
        self.b_tmux_starter.setObjectName("b_tmux_starter")

        self.verticalLayout.addWidget(self.b_tmux_starter)

        self.verticalSpacer = QSpacerItem(
            20, 431, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_5 = QLabel(self.tab_6)
        self.label_5.setObjectName("label_5")

        self.gridLayout_8.addWidget(self.label_5, 0, 0, 1, 1)

        self.le_tag = QLineEdit(self.tab_6)
        self.le_tag.setObjectName("le_tag")

        self.gridLayout_8.addWidget(self.le_tag, 0, 1, 1, 1)

        self.drone_starter = QPushButton(self.tab_6)
        self.drone_starter.setObjectName("drone_starter")
        self.drone_starter.setMinimumSize(QSize(0, 80))

        self.gridLayout_8.addWidget(self.drone_starter, 0, 2, 2, 1)

        self.label_6 = QLabel(self.tab_6)
        self.label_6.setObjectName("label_6")

        self.gridLayout_8.addWidget(self.label_6, 1, 0, 1, 1)

        self.sp_drone_meas_dur = QSpinBox(self.tab_6)
        self.sp_drone_meas_dur.setObjectName("sp_drone_meas_dur")
        self.sp_drone_meas_dur.setMinimum(5)
        self.sp_drone_meas_dur.setMaximum(7200)
        self.sp_drone_meas_dur.setValue(1200)

        self.gridLayout_8.addWidget(self.sp_drone_meas_dur, 1, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout_8)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_12 = QGridLayout(self.tab_7)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.verticalSpacer_4 = QSpacerItem(
            20, 187, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.gridLayout_12.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_12 = QLabel(self.tab_7)
        self.label_12.setObjectName("label_12")
        self.label_12.setStyleSheet("")

        self.gridLayout_11.addWidget(self.label_12, 0, 0, 1, 1)

        self.sp_sky_gain = QSpinBox(self.tab_7)
        self.sp_sky_gain.setObjectName("sp_sky_gain")
        self.sp_sky_gain.setEnabled(False)
        self.sp_sky_gain.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sp_sky_gain.setMaximum(33)

        self.gridLayout_11.addWidget(self.sp_sky_gain, 0, 1, 1, 1)

        self.d_sky_gain = QDial(self.tab_7)
        self.d_sky_gain.setObjectName("d_sky_gain")
        sizePolicy.setHeightForWidth(self.d_sky_gain.sizePolicy().hasHeightForWidth())
        self.d_sky_gain.setSizePolicy(sizePolicy)
        self.d_sky_gain.setMinimum(1)
        self.d_sky_gain.setMaximum(33)
        self.d_sky_gain.setPageStep(1)
        self.d_sky_gain.setOrientation(Qt.Orientation.Horizontal)
        self.d_sky_gain.setInvertedAppearance(False)
        self.d_sky_gain.setWrapping(False)
        self.d_sky_gain.setNotchTarget(33.000000000000000)
        self.d_sky_gain.setNotchesVisible(True)

        self.gridLayout_11.addWidget(self.d_sky_gain, 1, 0, 1, 2)

        self.gridLayout_12.addLayout(self.gridLayout_11, 0, 1, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_11 = QLabel(self.tab_7)
        self.label_11.setObjectName("label_11")

        self.gridLayout_10.addWidget(self.label_11, 2, 0, 1, 1)

        self.label_10 = QLabel(self.tab_7)
        self.label_10.setObjectName("label_10")

        self.gridLayout_10.addWidget(self.label_10, 1, 0, 1, 1)

        self.b_sky_measure = QPushButton(self.tab_7)
        self.b_sky_measure.setObjectName("b_sky_measure")
        sizePolicy2.setHeightForWidth(
            self.b_sky_measure.sizePolicy().hasHeightForWidth()
        )
        self.b_sky_measure.setSizePolicy(sizePolicy2)
        self.b_sky_measure.setMinimumSize(QSize(0, 45))

        self.gridLayout_10.addWidget(self.b_sky_measure, 2, 2, 1, 1)

        self.sp_sky_duration = QSpinBox(self.tab_7)
        self.sp_sky_duration.setObjectName("sp_sky_duration")
        self.sp_sky_duration.setMaximum(7200)
        self.sp_sky_duration.setValue(3600)

        self.gridLayout_10.addWidget(self.sp_sky_duration, 2, 1, 1, 1)

        self.b_sky_preview = QPushButton(self.tab_7)
        self.b_sky_preview.setObjectName("b_sky_preview")
        sizePolicy2.setHeightForWidth(
            self.b_sky_preview.sizePolicy().hasHeightForWidth()
        )
        self.b_sky_preview.setSizePolicy(sizePolicy2)
        self.b_sky_preview.setMinimumSize(QSize(0, 45))

        self.gridLayout_10.addWidget(self.b_sky_preview, 1, 1, 1, 1)

        self.b_sky_tmux_starter = QPushButton(self.tab_7)
        self.b_sky_tmux_starter.setObjectName("b_sky_tmux_starter")
        self.b_sky_tmux_starter.setMinimumSize(QSize(0, 45))

        self.gridLayout_10.addWidget(self.b_sky_tmux_starter, 0, 1, 1, 1)

        self.label_13 = QLabel(self.tab_7)
        self.label_13.setObjectName("label_13")

        self.gridLayout_10.addWidget(self.label_13, 0, 0, 1, 1)

        self.b_sky_reboot = QPushButton(self.tab_7)
        self.b_sky_reboot.setObjectName("b_sky_reboot")
        self.b_sky_reboot.setMinimumSize(QSize(0, 45))

        self.gridLayout_10.addWidget(self.b_sky_reboot, 0, 2, 1, 1)

        self.gridLayout_12.addLayout(self.gridLayout_10, 2, 0, 1, 2)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.sp_sky_expo = QSpinBox(self.tab_7)
        self.sp_sky_expo.setObjectName("sp_sky_expo")
        self.sp_sky_expo.setEnabled(False)
        self.sp_sky_expo.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sp_sky_expo.setMaximum(2500)

        self.gridLayout_9.addWidget(self.sp_sky_expo, 0, 1, 1, 1)

        self.d_sky_expo = QDial(self.tab_7)
        self.d_sky_expo.setObjectName("d_sky_expo")
        sizePolicy.setHeightForWidth(self.d_sky_expo.sizePolicy().hasHeightForWidth())
        self.d_sky_expo.setSizePolicy(sizePolicy)
        self.d_sky_expo.setMinimum(0)
        self.d_sky_expo.setMaximum(11)
        self.d_sky_expo.setOrientation(Qt.Orientation.Horizontal)
        self.d_sky_expo.setInvertedAppearance(False)
        self.d_sky_expo.setWrapping(False)
        self.d_sky_expo.setNotchTarget(10.000000000000000)
        self.d_sky_expo.setNotchesVisible(True)

        self.gridLayout_9.addWidget(self.d_sky_expo, 1, 0, 1, 2)

        self.label_9 = QLabel(self.tab_7)
        self.label_9.setObjectName("label_9")

        self.gridLayout_9.addWidget(self.label_9, 0, 0, 1, 1)

        self.gridLayout_12.addLayout(self.gridLayout_9, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_7, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 2, 1, 1)

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
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.b_tmux_output = QPushButton(self.tab_4)
        self.b_tmux_output.setObjectName("b_tmux_output")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding
        )
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.b_tmux_output.sizePolicy().hasHeightForWidth()
        )
        self.b_tmux_output.setSizePolicy(sizePolicy3)

        self.gridLayout_13.addWidget(self.b_tmux_output, 0, 0, 1, 1)

        self.b_get_cam_info = QPushButton(self.tab_4)
        self.b_get_cam_info.setObjectName("b_get_cam_info")
        sizePolicy3.setHeightForWidth(
            self.b_get_cam_info.sizePolicy().hasHeightForWidth()
        )
        self.b_get_cam_info.setSizePolicy(sizePolicy3)

        self.gridLayout_13.addWidget(self.b_get_cam_info, 0, 1, 1, 1)

        self.b_data_dir = QPushButton(self.tab_4)
        self.b_data_dir.setObjectName("b_data_dir")
        sizePolicy3.setHeightForWidth(self.b_data_dir.sizePolicy().hasHeightForWidth())
        self.b_data_dir.setSizePolicy(sizePolicy3)

        self.gridLayout_13.addWidget(self.b_data_dir, 1, 0, 1, 1)

        self.b_sky_tmux_output = QPushButton(self.tab_4)
        self.b_sky_tmux_output.setObjectName("b_sky_tmux_output")
        sizePolicy3.setHeightForWidth(
            self.b_sky_tmux_output.sizePolicy().hasHeightForWidth()
        )
        self.b_sky_tmux_output.setSizePolicy(sizePolicy3)

        self.gridLayout_13.addWidget(self.b_sky_tmux_output, 2, 0, 1, 1)

        self.b_sky_data_dir = QPushButton(self.tab_4)
        self.b_sky_data_dir.setObjectName("b_sky_data_dir")
        sizePolicy3.setHeightForWidth(
            self.b_sky_data_dir.sizePolicy().hasHeightForWidth()
        )
        self.b_sky_data_dir.setSizePolicy(sizePolicy3)

        self.gridLayout_13.addWidget(self.b_sky_data_dir, 2, 1, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout_13)

        self.text_output = QTextBrowser(self.tab_4)
        self.text_output.setObjectName("text_output")
        font1 = QFont()
        font1.setFamilies(["Iosevka"])
        font1.setPointSize(10)
        self.text_output.setFont(font1)

        self.verticalLayout_2.addWidget(self.text_output)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 4)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_7 = QGridLayout(self.tab_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pb_get_cam0 = QPushButton(self.tab_5)
        self.pb_get_cam0.setObjectName("pb_get_cam0")

        self.gridLayout_7.addWidget(self.pb_get_cam0, 0, 0, 1, 1)

        self.pb_get_cam1 = QPushButton(self.tab_5)
        self.pb_get_cam1.setObjectName("pb_get_cam1")

        self.gridLayout_7.addWidget(self.pb_get_cam1, 0, 1, 1, 1)

        self.image_view = ImageView(self.tab_5)
        self.image_view.setObjectName("image_view")

        self.gridLayout_7.addWidget(self.image_view, 1, 0, 1, 2)

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

    def retranslateUi(self, MainWindow):
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
        self.pb_send_cmd.setText(QCoreApplication.translate("MainWindow", "SEND", None))
        self.groupBox.setTitle(
            QCoreApplication.translate("MainWindow", "Control", None)
        )
        self.label_8.setText(
            QCoreApplication.translate("MainWindow", "SkyLogger IP", None)
        )
        self.label_7.setText(QCoreApplication.translate("MainWindow", "Main IP", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            QCoreApplication.translate("MainWindow", "Connection", None),
        )
        self.sp_azi.setSuffix("")
        self.label.setText(
            QCoreApplication.translate("MainWindow", "Motor-Azimuth", None)
        )
        self.pb_motor_zeroing.setText(
            QCoreApplication.translate("MainWindow", "Set curret to 0", None)
        )
        self.pb_bno_check.setText(
            QCoreApplication.translate("MainWindow", "BNO check", None)
        )
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", "Camera-Gain", None)
        )
        self.label_4.setText(
            QCoreApplication.translate("MainWindow", "Camera-Exposure", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", "Motor-Elevation", None)
        )
        self.pb_capture_shot.setText(
            QCoreApplication.translate(
                "MainWindow", "Spectral cam Shot (set props & preview)", None
            )
        )
        self.pb_webcam_shot.setText(
            QCoreApplication.translate("MainWindow", "Webcam Shot (preview)", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            QCoreApplication.translate("MainWindow", "Manual", None),
        )
        self._l_2.setText(QCoreApplication.translate("MainWindow", "Elevation", None))
        self._l.setText(QCoreApplication.translate("MainWindow", "Azimuth ", None))
        self.pb_bno_save.setText(
            QCoreApplication.translate("MainWindow", "BNO save", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_3),
            QCoreApplication.translate(
                "MainWindow", "Measurement (Spectrosphere)", None
            ),
        )
        self.b_tmux_starter.setText(
            QCoreApplication.translate("MainWindow", "TMUX Starter (once)", None)
        )
        self.label_5.setText(QCoreApplication.translate("MainWindow", "Dir. Tag", None))
        self.le_tag.setText(
            QCoreApplication.translate("MainWindow", "Hokuden_measure1", None)
        )
        self.drone_starter.setText(
            QCoreApplication.translate("MainWindow", "Refresh", None)
        )
        self.label_6.setText(
            QCoreApplication.translate("MainWindow", "Duration (sec)", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_6),
            QCoreApplication.translate(
                "MainWindow", "Continuos Measurement (Drone)", None
            ),
        )
        self.label_12.setText(
            QCoreApplication.translate("MainWindow", "SKY-Spectral-cam-Gain", None)
        )
        self.label_11.setText(
            QCoreApplication.translate("MainWindow", "Measurement", None)
        )
        self.label_10.setText(QCoreApplication.translate("MainWindow", "Preview", None))
        self.b_sky_measure.setText(
            QCoreApplication.translate("MainWindow", "Measurement", None)
        )
        self.b_sky_preview.setText(
            QCoreApplication.translate("MainWindow", "1shot (Preview)", None)
        )
        self.b_sky_tmux_starter.setText(
            QCoreApplication.translate("MainWindow", "TMUX Starter (once)", None)
        )
        self.label_13.setText(
            QCoreApplication.translate("MainWindow", "Need to start TMUX", None)
        )
        self.b_sky_reboot.setText(
            QCoreApplication.translate("MainWindow", "Reboot (sky)", None)
        )
        self.label_9.setText(
            QCoreApplication.translate("MainWindow", "SKY-Spectral-Cam-Exposure", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_7),
            QCoreApplication.translate("MainWindow", "Sky Logger", None),
        )
        self.groupBox_2.setTitle(
            QCoreApplication.translate("MainWindow", "Monitor", None)
        )
        self.b_tmux_output.setText(
            QCoreApplication.translate("MainWindow", "Get TMUX outputs (main)", None)
        )
        self.b_get_cam_info.setText(
            QCoreApplication.translate("MainWindow", "Get camera info", None)
        )
        self.b_data_dir.setText(
            QCoreApplication.translate("MainWindow", "Get data directory", None)
        )
        self.b_sky_tmux_output.setText(
            QCoreApplication.translate("MainWindow", "Get TMUX outputs (sky)", None)
        )
        self.b_sky_data_dir.setText(
            QCoreApplication.translate("MainWindow", "Get Data Direc (sky)", None)
        )
        self.text_output.setHtml(
            QCoreApplication.translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                'li.unchecked::marker { content: "\\2610"; }\n'
                'li.checked::marker { content: "\\2612"; }\n'
                "</style></head><body style=\" font-family:'Iosevka'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">........</p>\n'
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
                None,
            )
        )
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.tab_4),
            QCoreApplication.translate("MainWindow", "Raw Text", None),
        )
        self.pb_get_cam0.setText(
            QCoreApplication.translate("MainWindow", "Show Cam 0", None)
        )
        self.pb_get_cam1.setText(
            QCoreApplication.translate("MainWindow", "Show Cam 1", None)
        )
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.tab_5),
            QCoreApplication.translate("MainWindow", "Visual", None),
        )

    # retranslateUi
