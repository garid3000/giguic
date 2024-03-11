# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_Mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (
    QCoreApplication,
    QMetaObject,
    QSize,
    Qt,
)
from PySide2.QtGui import (
    QFont,
)
from PySide2.QtWidgets import (
    QAction, 
    QAbstractSpinBox,
    QCheckBox,
    QDial,
    QFrame,
    QGridLayout,
    QGroupBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QSizePolicy,
    QSlider,
    QSpinBox,
    QSplitter,
    QTabWidget,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

from pyqtgraph import PlotWidget
from pyqtgraph.opengl import GLViewWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow: QMainWindow) -> None:
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
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setMinimumSize(QSize(100, 60))

        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)

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
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(16, 16))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_5 = QGridLayout(self.tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.ip_1 = QSpinBox(self.tab)
        self.ip_1.setObjectName("ip_1")
        self.ip_1.setMinimumSize(QSize(100, 50))
        font = QFont()
        font.setFamilies(["Monospace"])
        font.setPointSize(12)
        self.ip_1.setFont(font)
        self.ip_1.setWrapping(False)
        self.ip_1.setFrame(True)
        self.ip_1.setReadOnly(False)
        self.ip_1.setMaximum(255)
        self.ip_1.setSingleStep(1)
        self.ip_1.setValue(192)

        self.gridLayout_5.addWidget(self.ip_1, 0, 0, 1, 1)

        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName("label_7")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.label_7, 0, 1, 1, 1)

        self.ip_2 = QSpinBox(self.tab)
        self.ip_2.setObjectName("ip_2")
        self.ip_2.setMinimumSize(QSize(100, 50))
        self.ip_2.setFont(font)
        self.ip_2.setMaximum(255)
        self.ip_2.setValue(168)

        self.gridLayout_5.addWidget(self.ip_2, 0, 2, 1, 1)

        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName("label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.label_8, 0, 3, 1, 1)

        self.ip_3 = QSpinBox(self.tab)
        self.ip_3.setObjectName("ip_3")
        self.ip_3.setMinimumSize(QSize(100, 50))
        self.ip_3.setFont(font)
        self.ip_3.setMaximum(255)
        self.ip_3.setValue(11)

        self.gridLayout_5.addWidget(self.ip_3, 0, 4, 1, 1)

        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName("label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.label_9, 0, 5, 1, 1)

        self.ip_4 = QSpinBox(self.tab)
        self.ip_4.setObjectName("ip_4")
        self.ip_4.setMinimumSize(QSize(100, 50))
        self.ip_4.setFont(font)
        self.ip_4.setMaximum(255)
        self.ip_4.setValue(2)

        self.gridLayout_5.addWidget(self.ip_4, 0, 6, 1, 1)

        self.Set = QPushButton(self.tab)
        self.Set.setObjectName("Set")
        self.Set.setMinimumSize(QSize(0, 100))

        self.gridLayout_5.addWidget(self.Set, 1, 0, 1, 7)

        self.progressBar = QProgressBar(self.tab)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setValue(24)

        self.gridLayout_5.addWidget(self.progressBar, 2, 0, 1, 7)

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
        self.sp_expo = QSpinBox(self.tab_2)
        self.sp_expo.setObjectName("sp_expo")
        self.sp_expo.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.sp_expo.setMaximum(2500)

        self.gridLayout_3.addWidget(self.sp_expo, 0, 4, 1, 1)

        self.label = QLabel(self.tab_2)
        self.label.setObjectName("label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.sp_gain = QSpinBox(self.tab_2)
        self.sp_gain.setObjectName("sp_gain")
        self.sp_gain.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.sp_gain.setMaximum(33)

        self.gridLayout_3.addWidget(self.sp_gain, 3, 4, 1, 1)

        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")

        self.gridLayout_3.addWidget(self.label_2, 3, 0, 1, 1)

        self.d_expo = QDial(self.tab_2)
        self.d_expo.setObjectName("d_expo")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding
        )
        sizePolicy1.setHorizontalStretch(10)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.d_expo.sizePolicy().hasHeightForWidth())
        self.d_expo.setSizePolicy(sizePolicy1)
        self.d_expo.setMinimum(0)
        self.d_expo.setMaximum(12)
        self.d_expo.setOrientation(Qt.Orientation.Horizontal)
        self.d_expo.setInvertedAppearance(False)
        self.d_expo.setWrapping(False)
        self.d_expo.setNotchTarget(10.000000000000000)
        self.d_expo.setNotchesVisible(True)

        self.gridLayout_3.addWidget(self.d_expo, 1, 3, 1, 2)

        self.line = QFrame(self.tab_2)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line, 0, 2, 5, 1)

        self.line_3 = QFrame(self.tab_2)
        self.line_3.setObjectName("line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_3, 2, 3, 1, 2)

        self.sp_elv = QSpinBox(self.tab_2)
        self.sp_elv.setObjectName("sp_elv")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sp_elv.sizePolicy().hasHeightForWidth())
        self.sp_elv.setSizePolicy(sizePolicy2)
        self.sp_elv.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.sp_elv.setMinimum(-90)
        self.sp_elv.setMaximum(90)

        self.gridLayout_3.addWidget(self.sp_elv, 3, 1, 1, 1)

        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName("label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 3, 1, 1)

        self.d_azi = QDial(self.tab_2)
        self.d_azi.setObjectName("d_azi")
        sizePolicy1.setHeightForWidth(self.d_azi.sizePolicy().hasHeightForWidth())
        self.d_azi.setSizePolicy(sizePolicy1)
        self.d_azi.setMinimum(-180)
        self.d_azi.setMaximum(180)
        self.d_azi.setOrientation(Qt.Orientation.Horizontal)
        self.d_azi.setInvertedAppearance(False)
        self.d_azi.setWrapping(True)
        self.d_azi.setNotchTarget(10.000000000000000)
        self.d_azi.setNotchesVisible(True)

        self.gridLayout_3.addWidget(self.d_azi, 1, 0, 1, 2)

        self.d_gain = QDial(self.tab_2)
        self.d_gain.setObjectName("d_gain")
        sizePolicy1.setHeightForWidth(self.d_gain.sizePolicy().hasHeightForWidth())
        self.d_gain.setSizePolicy(sizePolicy1)
        self.d_gain.setMinimum(1)
        self.d_gain.setMaximum(33)
        self.d_gain.setPageStep(1)
        self.d_gain.setOrientation(Qt.Orientation.Horizontal)
        self.d_gain.setInvertedAppearance(False)
        self.d_gain.setWrapping(False)
        self.d_gain.setNotchTarget(33.000000000000000)
        self.d_gain.setNotchesVisible(True)

        self.gridLayout_3.addWidget(self.d_gain, 4, 3, 1, 2)

        self.pushButton_3 = QPushButton(self.tab_2)
        self.pushButton_3.setObjectName("pushButton_3")

        self.gridLayout_3.addWidget(self.pushButton_3, 6, 3, 1, 2)

        self.line_2 = QFrame(self.tab_2)
        self.line_2.setObjectName("line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_2, 2, 0, 1, 2)

        self.sp_azi = QSpinBox(self.tab_2)
        self.sp_azi.setObjectName("sp_azi")
        sizePolicy2.setHeightForWidth(self.sp_azi.sizePolicy().hasHeightForWidth())
        self.sp_azi.setSizePolicy(sizePolicy2)
        self.sp_azi.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.sp_azi.setMinimum(-180)
        self.sp_azi.setMaximum(180)

        self.gridLayout_3.addWidget(self.sp_azi, 0, 1, 1, 1)

        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("")

        self.gridLayout_3.addWidget(self.label_3, 3, 3, 1, 1)

        self.line_4 = QFrame(self.tab_2)
        self.line_4.setObjectName("line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_4, 5, 0, 1, 2)

        self.line_5 = QFrame(self.tab_2)
        self.line_5.setObjectName("line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_5, 5, 3, 1, 2)

        self.pushButton_2 = QPushButton(self.tab_2)
        self.pushButton_2.setObjectName("pushButton_2")

        self.gridLayout_3.addWidget(self.pushButton_2, 6, 0, 1, 2)

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

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.spinBox_6 = QSpinBox(self.tab_3)
        self.spinBox_6.setObjectName("spinBox_6")
        self.spinBox_6.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_6.setMaximum(180)
        self.spinBox_6.setValue(180)

        self.gridLayout_4.addWidget(self.spinBox_6, 1, 3, 1, 1)

        self.spinBox_5 = QSpinBox(self.tab_3)
        self.spinBox_5.setObjectName("spinBox_5")
        self.spinBox_5.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_5.setMaximum(0)

        self.gridLayout_4.addWidget(self.spinBox_5, 1, 1, 1, 1)

        self.label_5 = QLabel(self.tab_3)
        self.label_5.setObjectName("label_5")

        self.gridLayout_4.addWidget(self.label_5, 1, 2, 1, 1)

        self.horizontalSlider_4 = QSlider(self.tab_3)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.horizontalSlider_4.setMaximum(90)
        self.horizontalSlider_4.setPageStep(1)
        self.horizontalSlider_4.setValue(45)
        self.horizontalSlider_4.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_4.setInvertedAppearance(True)
        self.horizontalSlider_4.setInvertedControls(False)

        self.gridLayout_4.addWidget(self.horizontalSlider_4, 3, 0, 1, 1)

        self.horizontalSlider_2 = QSlider(self.tab_3)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_2.setMinimum(0)
        self.horizontalSlider_2.setMaximum(180)
        self.horizontalSlider_2.setValue(180)
        self.horizontalSlider_2.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_2.setInvertedAppearance(True)

        self.gridLayout_4.addWidget(self.horizontalSlider_2, 1, 0, 1, 1)

        self.spinBox_7 = QSpinBox(self.tab_3)
        self.spinBox_7.setObjectName("spinBox_7")
        self.spinBox_7.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_7.setMinimum(-90)
        self.spinBox_7.setMaximum(0)
        self.spinBox_7.setSingleStep(1)
        self.spinBox_7.setValue(-45)

        self.gridLayout_4.addWidget(self.spinBox_7, 3, 1, 1, 1)

        self.label_6 = QLabel(self.tab_3)
        self.label_6.setObjectName("label_6")

        self.gridLayout_4.addWidget(self.label_6, 3, 2, 1, 1)

        self.spinBox_8 = QSpinBox(self.tab_3)
        self.spinBox_8.setObjectName("spinBox_8")
        self.spinBox_8.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_8.setMaximum(45)

        self.gridLayout_4.addWidget(self.spinBox_8, 3, 3, 1, 1)

        self.horizontalSlider_3 = QSlider(self.tab_3)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalSlider_3.setMinimum(0)
        self.horizontalSlider_3.setMaximum(45)
        self.horizontalSlider_3.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_4.addWidget(self.horizontalSlider_3, 3, 4, 1, 1)

        self.horizontalSlider = QSlider(self.tab_3)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setMaximum(180)
        self.horizontalSlider.setValue(90)
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_4.addWidget(self.horizontalSlider, 1, 4, 1, 1)

        self.widget = GLViewWidget(self.tab_3)
        self.widget.setObjectName("widget")

        self.gridLayout_4.addWidget(self.widget, 0, 3, 1, 2)

        self.tabWidget.addTab(self.tab_3, "")

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
        self.textBrowser = QTextBrowser(self.tab_4)
        self.textBrowser.setObjectName("textBrowser")

        self.verticalLayout_2.addWidget(self.textBrowser)

        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout = QVBoxLayout(self.tab_5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QCheckBox(self.tab_5)
        self.checkBox.setObjectName("checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.widget_2 = PlotWidget(self.tab_5)
        self.widget_2.setObjectName("widget_2")

        self.verticalLayout.addWidget(self.widget_2)

        self.tabWidget_2.addTab(self.tab_5, "")

        self.gridLayout_6.addWidget(self.tabWidget_2, 0, 0, 1, 1)

        self.splitter.addWidget(self.groupBox_2)

        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 2)

        self.le_cmd2send = QLineEdit(self.centralwidget)
        self.le_cmd2send.setObjectName("le_cmd2send")
        self.le_cmd2send.setFont(font)

        self.gridLayout.addWidget(self.le_cmd2send, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(1)

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
        self.pushButton.setText(QCoreApplication.translate("MainWindow", "SEND", None))
        self.groupBox.setTitle(
            QCoreApplication.translate("MainWindow", "Control", None)
        )
        self.label_7.setText(QCoreApplication.translate("MainWindow", ".", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", ".", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", ".", None))
        self.Set.setText(QCoreApplication.translate("MainWindow", "PushButton", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            QCoreApplication.translate("MainWindow", "Connection", None),
        )
        self.label.setText(
            QCoreApplication.translate("MainWindow", "Motor-Azimuth", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", "Motor-Elevation", None)
        )
        self.label_4.setText(
            QCoreApplication.translate("MainWindow", "Camera-Exposure", None)
        )
        self.pushButton_3.setText(
            QCoreApplication.translate("MainWindow", "Camera", None)
        )
        self.sp_azi.setSuffix("")
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", "Camera-Gain", None)
        )
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", "Orientation Sensor", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            QCoreApplication.translate("MainWindow", "Manual", None),
        )
        self.label_5.setText(QCoreApplication.translate("MainWindow", "Azimuth ", None))
        self.label_6.setText(
            QCoreApplication.translate("MainWindow", "Elevation", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_3),
            QCoreApplication.translate("MainWindow", "Measurement", None),
        )
        self.groupBox_2.setTitle(
            QCoreApplication.translate("MainWindow", "Monitor", None)
        )
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.tab_4),
            QCoreApplication.translate("MainWindow", "Raw Text", None),
        )
        self.checkBox.setText(QCoreApplication.translate("MainWindow", "Show", None))
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.tab_5),
            QCoreApplication.translate("MainWindow", "Visual", None),
        )

    # retranslateUi
