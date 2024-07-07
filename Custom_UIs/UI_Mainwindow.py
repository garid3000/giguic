/********************************************************************************
** Form generated from reading UI file 'UI_Mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.15.12
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDial>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSlider>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QSplitter>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QTextBrowser>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>
#include "pyqtgraph"

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionOpen_Directory;
    QAction *action_cur_jpeg_export;
    QAction *action_geometry_load;
    QAction *action_help;
    QAction *actionRead_Dependencies;
    QAction *actionContact_information;
    QAction *action_about;
    QAction *actionContact;
    QAction *action_cur_jpeg_preview;
    QAction *action_dir_goto_parent;
    QAction *action_dir_goto_cur_child;
    QAction *action_dir_cur_child_fold;
    QAction *action_dir_cur_child_unfold;
    QAction *action_cur_file_open;
    QAction *actionsdf;
    QAction *actionSave_geometry_configuration_Ctrl_Shift_L;
    QAction *action_dir_ft_filter_toggle;
    QAction *action_tabs_show_tab1;
    QAction *action_tabs_show_tab2;
    QAction *action_tabs_show_tab3;
    QWidget *centralwidget;
    QGridLayout *gridLayout;
    QLineEdit *le_cmd2send;
    QPushButton *pb_send_cmd;
    QSplitter *splitter;
    QGroupBox *groupBox;
    QGridLayout *gridLayout_2;
    QTabWidget *tabWidget;
    QWidget *tab;
    QVBoxLayout *verticalLayout_4;
    QHBoxLayout *horizontalLayout_4;
    QPushButton *b_this_pc_get_ip;
    QLabel *_l_4;
    QComboBox *cb_this_pc_network_devices;
    QLabel *l_this_pc_ip;
    QSpacerItem *verticalSpacer_4;
    QFrame *line;
    QHBoxLayout *horizontalLayout_3;
    QLabel *label_6;
    QSpinBox *ip_1;
    QSpinBox *ip_2;
    QSpinBox *ip_3;
    QSpinBox *ip_4;
    QHBoxLayout *horizontalLayout_5;
    QPushButton *b_search_ip_for_pi;
    QPushButton *b_ssh_copy_id;
    QPushButton *b_check_ssh_connection;
    QSpacerItem *verticalSpacer_3;
    QFrame *line_2;
    QGridLayout *gridLayout_5;
    QPushButton *b_soft_reboot;
    QPushButton *b_hard_reboot;
    QPushButton *b_tmux_init;
    QPushButton *b_terminate_python_processes;
    QPushButton *b_info_dump;
    QWidget *tab_2;
    QGridLayout *gridLayout_3;
    QVBoxLayout *verticalLayout_3;
    QHBoxLayout *horizontalLayout_2;
    QLabel *label_2;
    QSpinBox *sp_elv;
    QDial *d_elv;
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QLabel *label;
    QSpinBox *sp_azi;
    QDial *d_azi;
    QPushButton *pb_motor_zeroing;
    QWidget *tab_7;
    QGridLayout *gridLayout_10;
    QGridLayout *gridLayout_8;
    QLabel *_l1;
    QSpinBox *sp_expo_1;
    QDial *d_expo_1;
    QGridLayout *gridLayout_18;
    QLabel *_l1_2;
    QSpinBox *sp_expo_2;
    QDial *d_expo_2;
    QGridLayout *gridLayout_19;
    QLabel *_l1_3;
    QSpinBox *sp_expo_3;
    QDial *d_expo_3;
    QGridLayout *gridLayout_20;
    QLabel *_l1_4;
    QSpinBox *sp_expo_4;
    QDial *d_expo_4;
    QGridLayout *gridLayout_21;
    QLabel *_l1_5;
    QSpinBox *sp_expo_5;
    QDial *d_expo_5;
    QGridLayout *gridLayout_22;
    QLabel *_l1_6;
    QSpinBox *sp_expo_6;
    QDial *d_expo_6;
    QGridLayout *gridLayout_23;
    QLabel *_l1_7;
    QSpinBox *sp_expo_7;
    QDial *d_expo_7;
    QGridLayout *gridLayout_24;
    QLabel *_l1_8;
    QSpinBox *sp_expo_8;
    QDial *d_expo_8;
    QGridLayout *gridLayout_9;
    QLabel *label_4;
    QLabel *label_3;
    QLineEdit *le_expo_plus_str;
    QLineEdit *le_expo_minus_str;
    QLabel *label_5;
    QLineEdit *le_expo_base_str;
    QSpinBox *spinBox_2;
    QSpinBox *spinBox;
    QPushButton *b_1shot;
    QWidget *tab_3;
    QGridLayout *gridLayout_4;
    QGridLayout *gridLayout_12;
    QLineEdit *qe_meas_gimbal_fullpath;
    QLabel *label_12;
    QLineEdit *qe_meas_gimbal_tag;
    QLabel *label_13;
    QPushButton *b_meas_gimbal_refresh;
    QGridLayout *gridLayout_13;
    QSlider *hs_azi_0;
    QSpinBox *sb_azi_0;
    QSlider *hs_elv_0;
    QSpinBox *sb_elv_0;
    QLabel *_l_2;
    QLabel *_l;
    QSpinBox *sb_azi_1;
    QSpinBox *sb_elv_1;
    QSlider *hs_azi_1;
    QSlider *hs_elv_1;
    QSpacerItem *verticalSpacer_5;
    QSpacerItem *verticalSpacer_6;
    QSpacerItem *verticalSpacer_7;
    QWidget *tab_6;
    QVBoxLayout *verticalLayout_5;
    QSpacerItem *verticalSpacer_2;
    QGridLayout *gridLayout_11;
    QPushButton *b_meas_uav_refresh;
    QLabel *label_9;
    QLabel *label_10;
    QLineEdit *qe_meas_uav_fullpath;
    QLineEdit *qe_meas_uav_tag;
    QSpacerItem *verticalSpacer;
    QGroupBox *groupBox_2;
    QGridLayout *gridLayout_6;
    QTabWidget *tabWidget_2;
    QWidget *tab_4;
    QGridLayout *gridLayout_14;
    QPushButton *b_check_dir_tree;
    QPushButton *b_check_tmux;
    QPushButton *b_check_stroge;
    QTextBrowser *text_output;
    QWidget *tab_5;
    QGridLayout *gridLayout_7;
    QPushButton *pb_get_cam0;
    ImageView *image_view;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(1057, 695);
        MainWindow->setStyleSheet(QString::fromUtf8(".QLabel { font-size: 12pt;}\n"
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
"}"));
        actionOpen_Directory = new QAction(MainWindow);
        actionOpen_Directory->setObjectName(QString::fromUtf8("actionOpen_Directory"));
        action_cur_jpeg_export = new QAction(MainWindow);
        action_cur_jpeg_export->setObjectName(QString::fromUtf8("action_cur_jpeg_export"));
        action_geometry_load = new QAction(MainWindow);
        action_geometry_load->setObjectName(QString::fromUtf8("action_geometry_load"));
        action_help = new QAction(MainWindow);
        action_help->setObjectName(QString::fromUtf8("action_help"));
        actionRead_Dependencies = new QAction(MainWindow);
        actionRead_Dependencies->setObjectName(QString::fromUtf8("actionRead_Dependencies"));
        actionContact_information = new QAction(MainWindow);
        actionContact_information->setObjectName(QString::fromUtf8("actionContact_information"));
        action_about = new QAction(MainWindow);
        action_about->setObjectName(QString::fromUtf8("action_about"));
        actionContact = new QAction(MainWindow);
        actionContact->setObjectName(QString::fromUtf8("actionContact"));
        action_cur_jpeg_preview = new QAction(MainWindow);
        action_cur_jpeg_preview->setObjectName(QString::fromUtf8("action_cur_jpeg_preview"));
        action_dir_goto_parent = new QAction(MainWindow);
        action_dir_goto_parent->setObjectName(QString::fromUtf8("action_dir_goto_parent"));
        action_dir_goto_cur_child = new QAction(MainWindow);
        action_dir_goto_cur_child->setObjectName(QString::fromUtf8("action_dir_goto_cur_child"));
        action_dir_cur_child_fold = new QAction(MainWindow);
        action_dir_cur_child_fold->setObjectName(QString::fromUtf8("action_dir_cur_child_fold"));
        action_dir_cur_child_unfold = new QAction(MainWindow);
        action_dir_cur_child_unfold->setObjectName(QString::fromUtf8("action_dir_cur_child_unfold"));
        action_cur_file_open = new QAction(MainWindow);
        action_cur_file_open->setObjectName(QString::fromUtf8("action_cur_file_open"));
        actionsdf = new QAction(MainWindow);
        actionsdf->setObjectName(QString::fromUtf8("actionsdf"));
        actionSave_geometry_configuration_Ctrl_Shift_L = new QAction(MainWindow);
        actionSave_geometry_configuration_Ctrl_Shift_L->setObjectName(QString::fromUtf8("actionSave_geometry_configuration_Ctrl_Shift_L"));
        action_dir_ft_filter_toggle = new QAction(MainWindow);
        action_dir_ft_filter_toggle->setObjectName(QString::fromUtf8("action_dir_ft_filter_toggle"));
        action_tabs_show_tab1 = new QAction(MainWindow);
        action_tabs_show_tab1->setObjectName(QString::fromUtf8("action_tabs_show_tab1"));
        action_tabs_show_tab2 = new QAction(MainWindow);
        action_tabs_show_tab2->setObjectName(QString::fromUtf8("action_tabs_show_tab2"));
        action_tabs_show_tab3 = new QAction(MainWindow);
        action_tabs_show_tab3->setObjectName(QString::fromUtf8("action_tabs_show_tab3"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        gridLayout = new QGridLayout(centralwidget);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        le_cmd2send = new QLineEdit(centralwidget);
        le_cmd2send->setObjectName(QString::fromUtf8("le_cmd2send"));
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(le_cmd2send->sizePolicy().hasHeightForWidth());
        le_cmd2send->setSizePolicy(sizePolicy);
        QFont font;
        font.setFamily(QString::fromUtf8("Monospace"));
        font.setPointSize(12);
        le_cmd2send->setFont(font);

        gridLayout->addWidget(le_cmd2send, 2, 0, 1, 1);

        pb_send_cmd = new QPushButton(centralwidget);
        pb_send_cmd->setObjectName(QString::fromUtf8("pb_send_cmd"));
        pb_send_cmd->setMinimumSize(QSize(100, 60));

        gridLayout->addWidget(pb_send_cmd, 2, 1, 1, 1);

        splitter = new QSplitter(centralwidget);
        splitter->setObjectName(QString::fromUtf8("splitter"));
        splitter->setFrameShadow(QFrame::Shadow::Raised);
        splitter->setMidLineWidth(0);
        splitter->setOrientation(Qt::Orientation::Horizontal);
        groupBox = new QGroupBox(splitter);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        gridLayout_2 = new QGridLayout(groupBox);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        tabWidget = new QTabWidget(groupBox);
        tabWidget->setObjectName(QString::fromUtf8("tabWidget"));
        tabWidget->setMinimumSize(QSize(0, 50));
        tabWidget->setStyleSheet(QString::fromUtf8("QTabBar::tab { height: 35px;  }\n"
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
"}"));
        tabWidget->setTabPosition(QTabWidget::TabPosition::North);
        tabWidget->setTabShape(QTabWidget::TabShape::Rounded);
        tabWidget->setIconSize(QSize(16, 16));
        tabWidget->setDocumentMode(false);
        tabWidget->setTabsClosable(false);
        tabWidget->setTabBarAutoHide(false);
        tab = new QWidget();
        tab->setObjectName(QString::fromUtf8("tab"));
        verticalLayout_4 = new QVBoxLayout(tab);
        verticalLayout_4->setObjectName(QString::fromUtf8("verticalLayout_4"));
        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        b_this_pc_get_ip = new QPushButton(tab);
        b_this_pc_get_ip->setObjectName(QString::fromUtf8("b_this_pc_get_ip"));
        QSizePolicy sizePolicy1(QSizePolicy::Minimum, QSizePolicy::Minimum);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(b_this_pc_get_ip->sizePolicy().hasHeightForWidth());
        b_this_pc_get_ip->setSizePolicy(sizePolicy1);
        b_this_pc_get_ip->setMinimumSize(QSize(0, 0));

        horizontalLayout_4->addWidget(b_this_pc_get_ip);

        _l_4 = new QLabel(tab);
        _l_4->setObjectName(QString::fromUtf8("_l_4"));

        horizontalLayout_4->addWidget(_l_4);

        cb_this_pc_network_devices = new QComboBox(tab);
        cb_this_pc_network_devices->setObjectName(QString::fromUtf8("cb_this_pc_network_devices"));

        horizontalLayout_4->addWidget(cb_this_pc_network_devices);

        l_this_pc_ip = new QLabel(tab);
        l_this_pc_ip->setObjectName(QString::fromUtf8("l_this_pc_ip"));
        l_this_pc_ip->setFont(font);

        horizontalLayout_4->addWidget(l_this_pc_ip);


        verticalLayout_4->addLayout(horizontalLayout_4);

        verticalSpacer_4 = new QSpacerItem(20, 40, QSizePolicy::Expanding, QSizePolicy::Minimum);

        verticalLayout_4->addItem(verticalSpacer_4);

        line = new QFrame(tab);
        line->setObjectName(QString::fromUtf8("line"));
        line->setFrameShape(QFrame::HLine);
        line->setFrameShadow(QFrame::Sunken);

        verticalLayout_4->addWidget(line);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        label_6 = new QLabel(tab);
        label_6->setObjectName(QString::fromUtf8("label_6"));

        horizontalLayout_3->addWidget(label_6);

        ip_1 = new QSpinBox(tab);
        ip_1->setObjectName(QString::fromUtf8("ip_1"));
        QSizePolicy sizePolicy2(QSizePolicy::Minimum, QSizePolicy::Preferred);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(ip_1->sizePolicy().hasHeightForWidth());
        ip_1->setSizePolicy(sizePolicy2);
        ip_1->setMinimumSize(QSize(100, 50));
        QFont font1;
        font1.setFamily(QString::fromUtf8("Monospace"));
        font1.setPointSize(15);
        font1.setBold(false);
        font1.setItalic(false);
        ip_1->setFont(font1);
        ip_1->setWrapping(false);
        ip_1->setFrame(true);
        ip_1->setAlignment(Qt::AlignmentFlag::AlignCenter);
        ip_1->setReadOnly(false);
        ip_1->setMaximum(255);
        ip_1->setSingleStep(1);
        ip_1->setValue(192);

        horizontalLayout_3->addWidget(ip_1);

        ip_2 = new QSpinBox(tab);
        ip_2->setObjectName(QString::fromUtf8("ip_2"));
        sizePolicy2.setHeightForWidth(ip_2->sizePolicy().hasHeightForWidth());
        ip_2->setSizePolicy(sizePolicy2);
        ip_2->setMinimumSize(QSize(100, 50));
        ip_2->setFont(font1);
        ip_2->setAlignment(Qt::AlignmentFlag::AlignCenter);
        ip_2->setMaximum(255);
        ip_2->setValue(168);

        horizontalLayout_3->addWidget(ip_2);

        ip_3 = new QSpinBox(tab);
        ip_3->setObjectName(QString::fromUtf8("ip_3"));
        sizePolicy2.setHeightForWidth(ip_3->sizePolicy().hasHeightForWidth());
        ip_3->setSizePolicy(sizePolicy2);
        ip_3->setMinimumSize(QSize(100, 50));
        ip_3->setFont(font1);
        ip_3->setAlignment(Qt::AlignmentFlag::AlignCenter);
        ip_3->setMaximum(255);
        ip_3->setValue(83);

        horizontalLayout_3->addWidget(ip_3);

        ip_4 = new QSpinBox(tab);
        ip_4->setObjectName(QString::fromUtf8("ip_4"));
        sizePolicy2.setHeightForWidth(ip_4->sizePolicy().hasHeightForWidth());
        ip_4->setSizePolicy(sizePolicy2);
        ip_4->setMinimumSize(QSize(100, 50));
        ip_4->setFont(font1);
        ip_4->setAlignment(Qt::AlignmentFlag::AlignCenter);
        ip_4->setMaximum(255);
        ip_4->setValue(59);

        horizontalLayout_3->addWidget(ip_4);


        verticalLayout_4->addLayout(horizontalLayout_3);

        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setObjectName(QString::fromUtf8("horizontalLayout_5"));
        b_search_ip_for_pi = new QPushButton(tab);
        b_search_ip_for_pi->setObjectName(QString::fromUtf8("b_search_ip_for_pi"));
        QSizePolicy sizePolicy3(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy3.setHorizontalStretch(0);
        sizePolicy3.setVerticalStretch(0);
        sizePolicy3.setHeightForWidth(b_search_ip_for_pi->sizePolicy().hasHeightForWidth());
        b_search_ip_for_pi->setSizePolicy(sizePolicy3);
        b_search_ip_for_pi->setMinimumSize(QSize(0, 40));

        horizontalLayout_5->addWidget(b_search_ip_for_pi);

        b_ssh_copy_id = new QPushButton(tab);
        b_ssh_copy_id->setObjectName(QString::fromUtf8("b_ssh_copy_id"));
        sizePolicy2.setHeightForWidth(b_ssh_copy_id->sizePolicy().hasHeightForWidth());
        b_ssh_copy_id->setSizePolicy(sizePolicy2);
        b_ssh_copy_id->setMinimumSize(QSize(0, 40));

        horizontalLayout_5->addWidget(b_ssh_copy_id);

        b_check_ssh_connection = new QPushButton(tab);
        b_check_ssh_connection->setObjectName(QString::fromUtf8("b_check_ssh_connection"));
        sizePolicy3.setHeightForWidth(b_check_ssh_connection->sizePolicy().hasHeightForWidth());
        b_check_ssh_connection->setSizePolicy(sizePolicy3);
        b_check_ssh_connection->setMinimumSize(QSize(0, 40));

        horizontalLayout_5->addWidget(b_check_ssh_connection);


        verticalLayout_4->addLayout(horizontalLayout_5);

        verticalSpacer_3 = new QSpacerItem(20, 40, QSizePolicy::Expanding, QSizePolicy::Minimum);

        verticalLayout_4->addItem(verticalSpacer_3);

        line_2 = new QFrame(tab);
        line_2->setObjectName(QString::fromUtf8("line_2"));
        line_2->setFrameShape(QFrame::HLine);
        line_2->setFrameShadow(QFrame::Sunken);

        verticalLayout_4->addWidget(line_2);

        gridLayout_5 = new QGridLayout();
        gridLayout_5->setObjectName(QString::fromUtf8("gridLayout_5"));
        b_soft_reboot = new QPushButton(tab);
        b_soft_reboot->setObjectName(QString::fromUtf8("b_soft_reboot"));
        sizePolicy3.setHeightForWidth(b_soft_reboot->sizePolicy().hasHeightForWidth());
        b_soft_reboot->setSizePolicy(sizePolicy3);
        b_soft_reboot->setMinimumSize(QSize(0, 40));

        gridLayout_5->addWidget(b_soft_reboot, 2, 0, 1, 1);

        b_hard_reboot = new QPushButton(tab);
        b_hard_reboot->setObjectName(QString::fromUtf8("b_hard_reboot"));
        sizePolicy3.setHeightForWidth(b_hard_reboot->sizePolicy().hasHeightForWidth());
        b_hard_reboot->setSizePolicy(sizePolicy3);
        b_hard_reboot->setMinimumSize(QSize(0, 40));

        gridLayout_5->addWidget(b_hard_reboot, 1, 0, 1, 1);

        b_tmux_init = new QPushButton(tab);
        b_tmux_init->setObjectName(QString::fromUtf8("b_tmux_init"));
        sizePolicy3.setHeightForWidth(b_tmux_init->sizePolicy().hasHeightForWidth());
        b_tmux_init->setSizePolicy(sizePolicy3);
        b_tmux_init->setMinimumSize(QSize(0, 40));

        gridLayout_5->addWidget(b_tmux_init, 1, 1, 1, 1);

        b_terminate_python_processes = new QPushButton(tab);
        b_terminate_python_processes->setObjectName(QString::fromUtf8("b_terminate_python_processes"));
        sizePolicy3.setHeightForWidth(b_terminate_python_processes->sizePolicy().hasHeightForWidth());
        b_terminate_python_processes->setSizePolicy(sizePolicy3);
        b_terminate_python_processes->setMinimumSize(QSize(0, 40));

        gridLayout_5->addWidget(b_terminate_python_processes, 3, 0, 1, 1);

        b_info_dump = new QPushButton(tab);
        b_info_dump->setObjectName(QString::fromUtf8("b_info_dump"));
        sizePolicy3.setHeightForWidth(b_info_dump->sizePolicy().hasHeightForWidth());
        b_info_dump->setSizePolicy(sizePolicy3);
        b_info_dump->setMinimumSize(QSize(0, 40));

        gridLayout_5->addWidget(b_info_dump, 2, 1, 1, 1);


        verticalLayout_4->addLayout(gridLayout_5);

        tabWidget->addTab(tab, QString());
        tab_2 = new QWidget();
        tab_2->setObjectName(QString::fromUtf8("tab_2"));
        tab_2->setStyleSheet(QString::fromUtf8("\n"
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
""));
        gridLayout_3 = new QGridLayout(tab_2);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        verticalLayout_3 = new QVBoxLayout();
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        label_2 = new QLabel(tab_2);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        sizePolicy3.setHeightForWidth(label_2->sizePolicy().hasHeightForWidth());
        label_2->setSizePolicy(sizePolicy3);

        horizontalLayout_2->addWidget(label_2);

        sp_elv = new QSpinBox(tab_2);
        sp_elv->setObjectName(QString::fromUtf8("sp_elv"));
        QSizePolicy sizePolicy4(QSizePolicy::Preferred, QSizePolicy::Fixed);
        sizePolicy4.setHorizontalStretch(1);
        sizePolicy4.setVerticalStretch(0);
        sizePolicy4.setHeightForWidth(sp_elv->sizePolicy().hasHeightForWidth());
        sp_elv->setSizePolicy(sizePolicy4);
        sp_elv->setLayoutDirection(Qt::LayoutDirection::LeftToRight);
        sp_elv->setButtonSymbols(QAbstractSpinBox::ButtonSymbols::PlusMinus);
        sp_elv->setMinimum(-90);
        sp_elv->setMaximum(90);

        horizontalLayout_2->addWidget(sp_elv);


        verticalLayout_3->addLayout(horizontalLayout_2);

        d_elv = new QDial(tab_2);
        d_elv->setObjectName(QString::fromUtf8("d_elv"));
        QSizePolicy sizePolicy5(QSizePolicy::Preferred, QSizePolicy::Expanding);
        sizePolicy5.setHorizontalStretch(0);
        sizePolicy5.setVerticalStretch(0);
        sizePolicy5.setHeightForWidth(d_elv->sizePolicy().hasHeightForWidth());
        d_elv->setSizePolicy(sizePolicy5);
        d_elv->setMinimum(-90);
        d_elv->setMaximum(90);
        d_elv->setSingleStep(5);
        d_elv->setPageStep(1);
        d_elv->setValue(-45);
        d_elv->setSliderPosition(-45);
        d_elv->setOrientation(Qt::Orientation::Vertical);
        d_elv->setInvertedAppearance(false);
        d_elv->setInvertedControls(true);
        d_elv->setWrapping(false);
        d_elv->setNotchTarget(10.000000000000000);
        d_elv->setNotchesVisible(true);

        verticalLayout_3->addWidget(d_elv);


        gridLayout_3->addLayout(verticalLayout_3, 0, 1, 1, 1);

        verticalLayout = new QVBoxLayout();
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        label = new QLabel(tab_2);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout->addWidget(label);

        sp_azi = new QSpinBox(tab_2);
        sp_azi->setObjectName(QString::fromUtf8("sp_azi"));
        QSizePolicy sizePolicy6(QSizePolicy::Minimum, QSizePolicy::Fixed);
        sizePolicy6.setHorizontalStretch(1);
        sizePolicy6.setVerticalStretch(0);
        sizePolicy6.setHeightForWidth(sp_azi->sizePolicy().hasHeightForWidth());
        sp_azi->setSizePolicy(sizePolicy6);
        sp_azi->setButtonSymbols(QAbstractSpinBox::ButtonSymbols::PlusMinus);
        sp_azi->setMinimum(-180);
        sp_azi->setMaximum(180);

        horizontalLayout->addWidget(sp_azi);


        verticalLayout->addLayout(horizontalLayout);

        d_azi = new QDial(tab_2);
        d_azi->setObjectName(QString::fromUtf8("d_azi"));
        QSizePolicy sizePolicy7(QSizePolicy::Preferred, QSizePolicy::Expanding);
        sizePolicy7.setHorizontalStretch(10);
        sizePolicy7.setVerticalStretch(0);
        sizePolicy7.setHeightForWidth(d_azi->sizePolicy().hasHeightForWidth());
        d_azi->setSizePolicy(sizePolicy7);
        d_azi->setMinimum(-180);
        d_azi->setMaximum(180);
        d_azi->setSingleStep(5);
        d_azi->setPageStep(10);
        d_azi->setOrientation(Qt::Orientation::Horizontal);
        d_azi->setInvertedAppearance(false);
        d_azi->setWrapping(true);
        d_azi->setNotchTarget(10.000000000000000);
        d_azi->setNotchesVisible(true);

        verticalLayout->addWidget(d_azi);


        gridLayout_3->addLayout(verticalLayout, 0, 0, 1, 1);

        pb_motor_zeroing = new QPushButton(tab_2);
        pb_motor_zeroing->setObjectName(QString::fromUtf8("pb_motor_zeroing"));

        gridLayout_3->addWidget(pb_motor_zeroing, 1, 0, 1, 1);

        tabWidget->addTab(tab_2, QString());
        tab_7 = new QWidget();
        tab_7->setObjectName(QString::fromUtf8("tab_7"));
        gridLayout_10 = new QGridLayout(tab_7);
        gridLayout_10->setObjectName(QString::fromUtf8("gridLayout_10"));
        gridLayout_8 = new QGridLayout();
        gridLayout_8->setObjectName(QString::fromUtf8("gridLayout_8"));
        _l1 = new QLabel(tab_7);
        _l1->setObjectName(QString::fromUtf8("_l1"));

        gridLayout_8->addWidget(_l1, 0, 0, 1, 1);

        sp_expo_1 = new QSpinBox(tab_7);
        sp_expo_1->setObjectName(QString::fromUtf8("sp_expo_1"));
        sp_expo_1->setButtonSymbols(QAbstractSpinBox::ButtonSymbols::PlusMinus);
        sp_expo_1->setMaximum(2500);

        gridLayout_8->addWidget(sp_expo_1, 0, 1, 1, 1);

        d_expo_1 = new QDial(tab_7);
        d_expo_1->setObjectName(QString::fromUtf8("d_expo_1"));
        sizePolicy7.setHeightForWidth(d_expo_1->sizePolicy().hasHeightForWidth());
        d_expo_1->setSizePolicy(sizePolicy7);
        d_expo_1->setMinimum(0);
        d_expo_1->setMaximum(11);
        d_expo_1->setValue(8);
        d_expo_1->setOrientation(Qt::Orientation::Horizontal);
        d_expo_1->setInvertedAppearance(false);
        d_expo_1->setWrapping(false);
        d_expo_1->setNotchTarget(10.000000000000000);
        d_expo_1->setNotchesVisible(true);

        gridLayout_8->addWidget(d_expo_1, 1, 0, 1, 2);


        gridLayout_10->addLayout(gridLayout_8, 0, 0, 1, 1);

        gridLayout_18 = new QGridLayout();
        gridLayout_18->setObjectName(QString::fromUtf8("gridLayout_18"));
        _l1_2 = new QLabel(tab_7);
        _l1_2->setObjectName(QString::fromUtf8("_l1_2"));

        gridLayout_18->addWidget(_l1_2, 0, 0, 1, 1);

        sp_expo_2 = new QSpinBox(tab_7);
        sp_expo_2->setObjectName(QString::fromUtf8("sp_expo_2"));
        sp_expo_2->setButtonSymbols(QAbstractSpinBox::ButtonSymbols::PlusMinus);
        sp_expo_2->setMaximum(2500);

        gridLayout_18->addWidget(sp_expo_2, 0, 1, 1, 1);

        d_expo_2 = new QDial(tab_7);
        d_expo_2->setObjectName(QString::fromUtf8("d_expo_2"));
        sizePolicy7.setHeightForWidth(d_expo_2->sizePolicy().hasHeightForWidth());
        d_expo_2->setSizePolicy(sizePolicy7);
        d_expo_2->setMinimum(0);
        d_expo_2->setMaximum(11);
        d_expo_2->setValue(8);
        d_expo_2->setOrientation(Qt::Orientation::Horizontal);
        d_expo_2->setInvertedAppearance(false);
        d_expo_2->setWrapping(false);
        d_expo_2->setNotchTarget(10.000000000000000);
        d_expo_2->setNotchesVisible(true);

        gridLayout_18->addWidget(d_expo_2, 1, 0, 1, 2);


        gridLayout_10->addLayout(gridLayout_18, 0, 1, 1, 1);

        gridLayout_19 = new QGridLayout();
        gridLayout_19->setObjectName(QString::fromUtf8("gridLayout_19"));
        _l1_3 = new QLabel(tab_7);
        _l1_3->setObjectName(QString::fromUtf8("_l1_3"));

        gridLayout_19->addWidget(_l1_3, 0, 0, 1, 1);

        sp_expo_3 = new QSpinBox(tab_7);
        sp_expo_3->setObjectName(QString::fromUtf8("sp_expo_3"));
        sp_expo_3->setButtonSymbols(QAbstractSpinBox::ButtonSymbols::PlusMinus);
        sp_expo_3->setMaximum(2500);

        gridLayout_19->addWidget(sp_expo_3, 0, 1, 1, 1);

        d_expo_3 = new QDial(tab_7);
        d_expo_3->setObjectName(QString::fromUtf8("d_expo_3"));
        sizePolicy7.setHeightForWidth(d_expo_3->sizePolicy().hasHeightForWidth());
        d_expo_3->setSizePolicy(sizePolicy7);
        d_expo_3->setMinimum(0);
        d_expo_3->setMaximum(11);
        d_expo_3->setValue(8);
        d_expo_3->setOrientation(Qt::Orientation::Horizontal);
        d_expo_3->setInvertedAppearance(false);
        d_expo_3->setWrapping(false);
        d_expo_3->setNotchTarget(10.000000000000000);
        d_expo_3->setNotchesVisible(true);

        gridLayout_19->addWidget(d_expo_3, 1, 0, 1, 2);


        gridLayout_10->addLayout(gridLayout_19, 0, 2, 1, 1);

        gridLayout_20 = new QGridLayout();
        gridLayout_20->setObjectName(QString::fromUtf8("gridLayout_20"));
        _l1_4 = new QLabel(tab_7);
        _l1_4->setObjectName(QString::fromUtf8("_l1_4"));

        gridLayout_20->addWidget(_l1_4, 0, 0, 1, 1);

        sp_expo_4 = new QSpinBox(tab_7);
        sp_expo_4->setObjectName(QString::fromUtf8("sp_expo_4"));
        sp_expo_4->setButtonSymbols(QAbstractSpinBox::ButtonSymbols::PlusMinus);
        sp_expo_4->setMaximum(2500);

        gridLayout_20->addWidget(sp_expo_4, 0, 1, 1, 1);

        d_expo_4 = new QDial(tab_7);
        d_expo_4->setObjectName(QString::fromUtf8("d_expo_4"));
        sizePolicy7.setHeightForWidth(d_expo_4->sizePolicy().hasHeightForWidth());
        d_expo_4->setSizePolicy(sizePolicy7);
        d_expo_4->setMinimum(0);
        d_expo_4->setMaximum(11);
        d_expo_4->setValue(8);
        d_expo_4->setOrientation(Qt::Orientation::Horizontal);
        d_expo_4->setInvertedAppearance(false);
        d_expo_4->setWrapping(false);
        d_expo_4->setNotchTarget(10.000000000000000);
        d_expo_4->setNotchesVisible(true);

        gridLayout_20->addWidget(d_expo_4, 1, 0, 1, 2);


        gridLayout_10->addLayout(gridLayout_20, 0, 3, 1, 1);

        gridLayout_21 = new QGridLayout();
        gridLayout_21->setObjectName(QString::fromUtf8("gridLayout_21"));
        _l1_5 = new QLabel(tab_7);
        _l1_5->setObjectName(QString::fromUtf8("_l1_5"));

        gridLayout_21->addWidget(_l1_5, 0, 0, 1, 1);

        sp_expo_5 = new QSpinBox(tab_7);
        sp_expo_5->setObjectName(QString::fromUtf8("sp_expo_5"));
        sp_expo_5->setButtonSymbols(QAbstractSpinBox::ButtonSymbols::PlusMinus);
        sp_expo_5->setMaximum(2500);

        gridLayout_21->addWidget(sp_expo_5, 0, 1, 1, 1);

        d_expo_5 = new QDial(tab_7);
        d_expo_5->setObjectName(QString::fromUtf8("d_expo_5"));
        sizePolicy7.setHeightForWidth(d_expo_5->sizePolicy().hasHeightForWidth());
        d_expo_5->setSizePolicy(sizePolicy7);
        d_expo_5->setMinimum(0);
        d_expo_5->setMaximum(11);
        d_expo_5->setValue(8);
        d_expo_5->setOrientation(Qt::Orientation::Horizontal);
        d_expo_5->setInvertedAppearance(false);
        d_expo_5->setWrapping(false);
        d_expo_5->setNotchTarget(10.000000000000000);
        d_expo_5->setNotchesVisible(true);

        gridLayout_21->addWidget(d_expo_5, 1, 0, 1, 2);


        gridLayout_10->addLayout(gridLayout_21, 1, 0, 1, 1);

        gridLayout_22 = new QGridLayout();
        gridLayout_22->setObjectName(QString::fromUtf8("gridLayout_22"));
        _l1_6 = new QLabel(tab_7);
        _l1_6->setObjectName(QString::fromUtf8("_l1_6"));

        gridLayout_22->addWidget(_l1_6, 0, 0, 1, 1);

        sp_expo_6 = new QSpinBox(tab_7);
        sp_expo_6->setObjectName(QString::fromUtf8("sp_expo_6"));
        sp_expo_6->setButtonSymbols(QAbstractSpinBox::ButtonSymbols::PlusMinus);
        sp_expo_6->setMaximum(2500);

        gridLayout_22->addWidget(sp_expo_6, 0, 1, 1, 1);

        d_expo_6 = new QDial(tab_7);
        d_expo_6->setObjectName(QString::fromUtf8("d_expo_6"));
        sizePolicy7.setHeightForWidth(d_expo_6->sizePolicy().hasHeightForWidth());
        d_expo_6->setSizePolicy(sizePolicy7);
        d_expo_6->setMinimum(0);
        d_expo_6->setMaximum(11);
        d_expo_6->setValue(8);
        d_expo_6->setOrientation(Qt::Orientation::Horizontal);
        d_expo_6->setInvertedAppearance(false);
        d_expo_6->setWrapping(false);
        d_expo_6->setNotchTarget(10.000000000000000);
        d_expo_6->setNotchesVisible(true);

        gridLayout_22->addWidget(d_expo_6, 1, 0, 1, 2);


        gridLayout_10->addLayout(gridLayout_22, 1, 1, 1, 1);

        gridLayout_23 = new QGridLayout();
        gridLayout_23->setObjectName(QString::fromUtf8("gridLayout_23"));
        _l1_7 = new QLabel(tab_7);
        _l1_7->setObjectName(QString::fromUtf8("_l1_7"));

        gridLayout_23->addWidget(_l1_7, 0, 0, 1, 1);

        sp_expo_7 = new QSpinBox(tab_7);
        sp_expo_7->setObjectName(QString::fromUtf8("sp_expo_7"));
        sp_expo_7->setButtonSymbols(QAbstractSpinBox::ButtonSymbols::PlusMinus);
        sp_expo_7->setMaximum(2500);

        gridLayout_23->addWidget(sp_expo_7, 0, 1, 1, 1);

        d_expo_7 = new QDial(tab_7);
        d_expo_7->setObjectName(QString::fromUtf8("d_expo_7"));
        sizePolicy7.setHeightForWidth(d_expo_7->sizePolicy().hasHeightForWidth());
        d_expo_7->setSizePolicy(sizePolicy7);
        d_expo_7->setMinimum(0);
        d_expo_7->setMaximum(11);
        d_expo_7->setValue(8);
        d_expo_7->setOrientation(Qt::Orientation::Horizontal);
        d_expo_7->setInvertedAppearance(false);
        d_expo_7->setWrapping(false);
        d_expo_7->setNotchTarget(10.000000000000000);
        d_expo_7->setNotchesVisible(true);

        gridLayout_23->addWidget(d_expo_7, 1, 0, 1, 2);


        gridLayout_10->addLayout(gridLayout_23, 1, 2, 1, 1);

        gridLayout_24 = new QGridLayout();
        gridLayout_24->setObjectName(QString::fromUtf8("gridLayout_24"));
        _l1_8 = new QLabel(tab_7);
        _l1_8->setObjectName(QString::fromUtf8("_l1_8"));

        gridLayout_24->addWidget(_l1_8, 0, 0, 1, 1);

        sp_expo_8 = new QSpinBox(tab_7);
        sp_expo_8->setObjectName(QString::fromUtf8("sp_expo_8"));
        sp_expo_8->setButtonSymbols(QAbstractSpinBox::ButtonSymbols::PlusMinus);
        sp_expo_8->setMaximum(2500);

        gridLayout_24->addWidget(sp_expo_8, 0, 1, 1, 1);

        d_expo_8 = new QDial(tab_7);
        d_expo_8->setObjectName(QString::fromUtf8("d_expo_8"));
        sizePolicy7.setHeightForWidth(d_expo_8->sizePolicy().hasHeightForWidth());
        d_expo_8->setSizePolicy(sizePolicy7);
        d_expo_8->setMinimum(0);
        d_expo_8->setMaximum(11);
        d_expo_8->setValue(8);
        d_expo_8->setOrientation(Qt::Orientation::Horizontal);
        d_expo_8->setInvertedAppearance(false);
        d_expo_8->setWrapping(false);
        d_expo_8->setNotchTarget(10.000000000000000);
        d_expo_8->setNotchesVisible(true);

        gridLayout_24->addWidget(d_expo_8, 1, 0, 1, 2);


        gridLayout_10->addLayout(gridLayout_24, 1, 3, 1, 1);

        gridLayout_9 = new QGridLayout();
        gridLayout_9->setObjectName(QString::fromUtf8("gridLayout_9"));
        label_4 = new QLabel(tab_7);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        gridLayout_9->addWidget(label_4, 0, 0, 1, 1);

        label_3 = new QLabel(tab_7);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        gridLayout_9->addWidget(label_3, 1, 0, 1, 1);

        le_expo_plus_str = new QLineEdit(tab_7);
        le_expo_plus_str->setObjectName(QString::fromUtf8("le_expo_plus_str"));

        gridLayout_9->addWidget(le_expo_plus_str, 2, 1, 1, 1);

        le_expo_minus_str = new QLineEdit(tab_7);
        le_expo_minus_str->setObjectName(QString::fromUtf8("le_expo_minus_str"));

        gridLayout_9->addWidget(le_expo_minus_str, 0, 1, 1, 1);

        label_5 = new QLabel(tab_7);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        gridLayout_9->addWidget(label_5, 2, 0, 1, 1);

        le_expo_base_str = new QLineEdit(tab_7);
        le_expo_base_str->setObjectName(QString::fromUtf8("le_expo_base_str"));

        gridLayout_9->addWidget(le_expo_base_str, 1, 1, 1, 1);

        spinBox_2 = new QSpinBox(tab_7);
        spinBox_2->setObjectName(QString::fromUtf8("spinBox_2"));
        spinBox_2->setMaximum(3);
        spinBox_2->setValue(1);

        gridLayout_9->addWidget(spinBox_2, 2, 2, 1, 1);

        spinBox = new QSpinBox(tab_7);
        spinBox->setObjectName(QString::fromUtf8("spinBox"));
        spinBox->setLayoutDirection(Qt::LayoutDirection::LeftToRight);
        spinBox->setButtonSymbols(QAbstractSpinBox::ButtonSymbols::UpDownArrows);
        spinBox->setMinimum(-3);
        spinBox->setMaximum(0);
        spinBox->setValue(-1);

        gridLayout_9->addWidget(spinBox, 0, 2, 1, 1);

        b_1shot = new QPushButton(tab_7);
        b_1shot->setObjectName(QString::fromUtf8("b_1shot"));
        sizePolicy2.setHeightForWidth(b_1shot->sizePolicy().hasHeightForWidth());
        b_1shot->setSizePolicy(sizePolicy2);
        b_1shot->setMinimumSize(QSize(120, 0));

        gridLayout_9->addWidget(b_1shot, 0, 3, 3, 1);


        gridLayout_10->addLayout(gridLayout_9, 2, 0, 1, 4);

        tabWidget->addTab(tab_7, QString());
        tab_3 = new QWidget();
        tab_3->setObjectName(QString::fromUtf8("tab_3"));
        gridLayout_4 = new QGridLayout(tab_3);
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
        gridLayout_12 = new QGridLayout();
        gridLayout_12->setObjectName(QString::fromUtf8("gridLayout_12"));
        qe_meas_gimbal_fullpath = new QLineEdit(tab_3);
        qe_meas_gimbal_fullpath->setObjectName(QString::fromUtf8("qe_meas_gimbal_fullpath"));
        qe_meas_gimbal_fullpath->setEnabled(false);

        gridLayout_12->addWidget(qe_meas_gimbal_fullpath, 0, 1, 1, 1);

        label_12 = new QLabel(tab_3);
        label_12->setObjectName(QString::fromUtf8("label_12"));

        gridLayout_12->addWidget(label_12, 0, 0, 1, 1);

        qe_meas_gimbal_tag = new QLineEdit(tab_3);
        qe_meas_gimbal_tag->setObjectName(QString::fromUtf8("qe_meas_gimbal_tag"));

        gridLayout_12->addWidget(qe_meas_gimbal_tag, 1, 1, 1, 1);

        label_13 = new QLabel(tab_3);
        label_13->setObjectName(QString::fromUtf8("label_13"));

        gridLayout_12->addWidget(label_13, 1, 0, 1, 1);

        b_meas_gimbal_refresh = new QPushButton(tab_3);
        b_meas_gimbal_refresh->setObjectName(QString::fromUtf8("b_meas_gimbal_refresh"));
        sizePolicy2.setHeightForWidth(b_meas_gimbal_refresh->sizePolicy().hasHeightForWidth());
        b_meas_gimbal_refresh->setSizePolicy(sizePolicy2);

        gridLayout_12->addWidget(b_meas_gimbal_refresh, 0, 2, 2, 1);


        gridLayout_4->addLayout(gridLayout_12, 4, 0, 1, 1);

        gridLayout_13 = new QGridLayout();
        gridLayout_13->setObjectName(QString::fromUtf8("gridLayout_13"));
        hs_azi_0 = new QSlider(tab_3);
        hs_azi_0->setObjectName(QString::fromUtf8("hs_azi_0"));
        QSizePolicy sizePolicy8(QSizePolicy::Expanding, QSizePolicy::MinimumExpanding);
        sizePolicy8.setHorizontalStretch(0);
        sizePolicy8.setVerticalStretch(0);
        sizePolicy8.setHeightForWidth(hs_azi_0->sizePolicy().hasHeightForWidth());
        hs_azi_0->setSizePolicy(sizePolicy8);
        hs_azi_0->setMinimumSize(QSize(0, 0));
        hs_azi_0->setStyleSheet(QString::fromUtf8(""));
        hs_azi_0->setMinimum(0);
        hs_azi_0->setMaximum(180);
        hs_azi_0->setValue(180);
        hs_azi_0->setOrientation(Qt::Orientation::Horizontal);
        hs_azi_0->setInvertedAppearance(true);

        gridLayout_13->addWidget(hs_azi_0, 0, 0, 1, 1);

        sb_azi_0 = new QSpinBox(tab_3);
        sb_azi_0->setObjectName(QString::fromUtf8("sb_azi_0"));
        sb_azi_0->setButtonSymbols(QAbstractSpinBox::ButtonSymbols::NoButtons);
        sb_azi_0->setMinimum(-180);
        sb_azi_0->setMaximum(0);
        sb_azi_0->setValue(-180);

        gridLayout_13->addWidget(sb_azi_0, 0, 1, 1, 1);

        hs_elv_0 = new QSlider(tab_3);
        hs_elv_0->setObjectName(QString::fromUtf8("hs_elv_0"));
        sizePolicy8.setHeightForWidth(hs_elv_0->sizePolicy().hasHeightForWidth());
        hs_elv_0->setSizePolicy(sizePolicy8);
        hs_elv_0->setMaximum(90);
        hs_elv_0->setSingleStep(5);
        hs_elv_0->setPageStep(1);
        hs_elv_0->setValue(45);
        hs_elv_0->setOrientation(Qt::Orientation::Horizontal);
        hs_elv_0->setInvertedAppearance(true);
        hs_elv_0->setInvertedControls(false);

        gridLayout_13->addWidget(hs_elv_0, 2, 0, 1, 1);

        sb_elv_0 = new QSpinBox(tab_3);
        sb_elv_0->setObjectName(QString::fromUtf8("sb_elv_0"));
        sb_elv_0->setButtonSymbols(QAbstractSpinBox::ButtonSymbols::NoButtons);
        sb_elv_0->setMinimum(-90);
        sb_elv_0->setMaximum(0);
        sb_elv_0->setSingleStep(1);
        sb_elv_0->setValue(0);

        gridLayout_13->addWidget(sb_elv_0, 2, 1, 1, 1);

        _l_2 = new QLabel(tab_3);
        _l_2->setObjectName(QString::fromUtf8("_l_2"));

        gridLayout_13->addWidget(_l_2, 2, 2, 1, 1);

        _l = new QLabel(tab_3);
        _l->setObjectName(QString::fromUtf8("_l"));

        gridLayout_13->addWidget(_l, 0, 2, 1, 1);

        sb_azi_1 = new QSpinBox(tab_3);
        sb_azi_1->setObjectName(QString::fromUtf8("sb_azi_1"));
        sb_azi_1->setButtonSymbols(QAbstractSpinBox::ButtonSymbols::NoButtons);
        sb_azi_1->setMaximum(180);
        sb_azi_1->setValue(180);

        gridLayout_13->addWidget(sb_azi_1, 0, 3, 1, 1);

        sb_elv_1 = new QSpinBox(tab_3);
        sb_elv_1->setObjectName(QString::fromUtf8("sb_elv_1"));
        sb_elv_1->setButtonSymbols(QAbstractSpinBox::ButtonSymbols::NoButtons);
        sb_elv_1->setMinimum(-70);
        sb_elv_1->setMaximum(45);

        gridLayout_13->addWidget(sb_elv_1, 2, 3, 1, 1);

        hs_azi_1 = new QSlider(tab_3);
        hs_azi_1->setObjectName(QString::fromUtf8("hs_azi_1"));
        sizePolicy8.setHeightForWidth(hs_azi_1->sizePolicy().hasHeightForWidth());
        hs_azi_1->setSizePolicy(sizePolicy8);
        hs_azi_1->setMaximum(180);
        hs_azi_1->setValue(90);
        hs_azi_1->setOrientation(Qt::Orientation::Horizontal);

        gridLayout_13->addWidget(hs_azi_1, 0, 4, 1, 1);

        hs_elv_1 = new QSlider(tab_3);
        hs_elv_1->setObjectName(QString::fromUtf8("hs_elv_1"));
        sizePolicy8.setHeightForWidth(hs_elv_1->sizePolicy().hasHeightForWidth());
        hs_elv_1->setSizePolicy(sizePolicy8);
        hs_elv_1->setMinimum(-70);
        hs_elv_1->setMaximum(45);
        hs_elv_1->setSingleStep(5);
        hs_elv_1->setOrientation(Qt::Orientation::Horizontal);

        gridLayout_13->addWidget(hs_elv_1, 2, 4, 1, 1);

        verticalSpacer_5 = new QSpacerItem(20, 40, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_13->addItem(verticalSpacer_5, 1, 0, 1, 1);


        gridLayout_4->addLayout(gridLayout_13, 1, 0, 1, 1);

        verticalSpacer_6 = new QSpacerItem(20, 40, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_4->addItem(verticalSpacer_6, 2, 0, 1, 1);

        verticalSpacer_7 = new QSpacerItem(20, 40, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_4->addItem(verticalSpacer_7, 0, 0, 1, 1);

        tabWidget->addTab(tab_3, QString());
        tab_6 = new QWidget();
        tab_6->setObjectName(QString::fromUtf8("tab_6"));
        verticalLayout_5 = new QVBoxLayout(tab_6);
        verticalLayout_5->setObjectName(QString::fromUtf8("verticalLayout_5"));
        verticalSpacer_2 = new QSpacerItem(20, 40, QSizePolicy::Expanding, QSizePolicy::Minimum);

        verticalLayout_5->addItem(verticalSpacer_2);

        gridLayout_11 = new QGridLayout();
        gridLayout_11->setObjectName(QString::fromUtf8("gridLayout_11"));
        b_meas_uav_refresh = new QPushButton(tab_6);
        b_meas_uav_refresh->setObjectName(QString::fromUtf8("b_meas_uav_refresh"));
        sizePolicy2.setHeightForWidth(b_meas_uav_refresh->sizePolicy().hasHeightForWidth());
        b_meas_uav_refresh->setSizePolicy(sizePolicy2);

        gridLayout_11->addWidget(b_meas_uav_refresh, 0, 2, 2, 1);

        label_9 = new QLabel(tab_6);
        label_9->setObjectName(QString::fromUtf8("label_9"));

        gridLayout_11->addWidget(label_9, 0, 0, 1, 1);

        label_10 = new QLabel(tab_6);
        label_10->setObjectName(QString::fromUtf8("label_10"));

        gridLayout_11->addWidget(label_10, 1, 0, 1, 1);

        qe_meas_uav_fullpath = new QLineEdit(tab_6);
        qe_meas_uav_fullpath->setObjectName(QString::fromUtf8("qe_meas_uav_fullpath"));
        qe_meas_uav_fullpath->setEnabled(false);

        gridLayout_11->addWidget(qe_meas_uav_fullpath, 0, 1, 1, 1);

        qe_meas_uav_tag = new QLineEdit(tab_6);
        qe_meas_uav_tag->setObjectName(QString::fromUtf8("qe_meas_uav_tag"));

        gridLayout_11->addWidget(qe_meas_uav_tag, 1, 1, 1, 1);


        verticalLayout_5->addLayout(gridLayout_11);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Expanding, QSizePolicy::Minimum);

        verticalLayout_5->addItem(verticalSpacer);

        tabWidget->addTab(tab_6, QString());

        gridLayout_2->addWidget(tabWidget, 0, 0, 1, 1);

        splitter->addWidget(groupBox);
        groupBox_2 = new QGroupBox(splitter);
        groupBox_2->setObjectName(QString::fromUtf8("groupBox_2"));
        gridLayout_6 = new QGridLayout(groupBox_2);
        gridLayout_6->setObjectName(QString::fromUtf8("gridLayout_6"));
        tabWidget_2 = new QTabWidget(groupBox_2);
        tabWidget_2->setObjectName(QString::fromUtf8("tabWidget_2"));
        tab_4 = new QWidget();
        tab_4->setObjectName(QString::fromUtf8("tab_4"));
        gridLayout_14 = new QGridLayout(tab_4);
        gridLayout_14->setObjectName(QString::fromUtf8("gridLayout_14"));
        b_check_dir_tree = new QPushButton(tab_4);
        b_check_dir_tree->setObjectName(QString::fromUtf8("b_check_dir_tree"));
        sizePolicy2.setHeightForWidth(b_check_dir_tree->sizePolicy().hasHeightForWidth());
        b_check_dir_tree->setSizePolicy(sizePolicy2);

        gridLayout_14->addWidget(b_check_dir_tree, 1, 1, 1, 1);

        b_check_tmux = new QPushButton(tab_4);
        b_check_tmux->setObjectName(QString::fromUtf8("b_check_tmux"));
        b_check_tmux->setMinimumSize(QSize(0, 80));

        gridLayout_14->addWidget(b_check_tmux, 1, 0, 1, 1);

        b_check_stroge = new QPushButton(tab_4);
        b_check_stroge->setObjectName(QString::fromUtf8("b_check_stroge"));
        sizePolicy2.setHeightForWidth(b_check_stroge->sizePolicy().hasHeightForWidth());
        b_check_stroge->setSizePolicy(sizePolicy2);

        gridLayout_14->addWidget(b_check_stroge, 1, 2, 1, 1);

        text_output = new QTextBrowser(tab_4);
        text_output->setObjectName(QString::fromUtf8("text_output"));
        QFont font2;
        font2.setFamily(QString::fromUtf8("Monospace"));
        text_output->setFont(font2);

        gridLayout_14->addWidget(text_output, 3, 0, 1, 3);

        tabWidget_2->addTab(tab_4, QString());
        tab_5 = new QWidget();
        tab_5->setObjectName(QString::fromUtf8("tab_5"));
        gridLayout_7 = new QGridLayout(tab_5);
        gridLayout_7->setObjectName(QString::fromUtf8("gridLayout_7"));
        pb_get_cam0 = new QPushButton(tab_5);
        pb_get_cam0->setObjectName(QString::fromUtf8("pb_get_cam0"));
        QSizePolicy sizePolicy9(QSizePolicy::Minimum, QSizePolicy::Fixed);
        sizePolicy9.setHorizontalStretch(0);
        sizePolicy9.setVerticalStretch(0);
        sizePolicy9.setHeightForWidth(pb_get_cam0->sizePolicy().hasHeightForWidth());
        pb_get_cam0->setSizePolicy(sizePolicy9);
        pb_get_cam0->setMinimumSize(QSize(0, 80));

        gridLayout_7->addWidget(pb_get_cam0, 0, 0, 1, 2);

        image_view = new ImageView(tab_5);
        image_view->setObjectName(QString::fromUtf8("image_view"));

        gridLayout_7->addWidget(image_view, 3, 0, 1, 2);

        tabWidget_2->addTab(tab_5, QString());

        gridLayout_6->addWidget(tabWidget_2, 0, 0, 1, 1);

        splitter->addWidget(groupBox_2);

        gridLayout->addWidget(splitter, 1, 0, 1, 2);

        MainWindow->setCentralWidget(centralwidget);

        retranslateUi(MainWindow);

        tabWidget->setCurrentIndex(0);
        tabWidget_2->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        actionOpen_Directory->setText(QCoreApplication::translate("MainWindow", "Open Directory", nullptr));
        action_cur_jpeg_export->setText(QCoreApplication::translate("MainWindow", "Export (Ctlr-E)", nullptr));
        action_geometry_load->setText(QCoreApplication::translate("MainWindow", "Load geometry configuration (Ctrl + L)", nullptr));
        action_help->setText(QCoreApplication::translate("MainWindow", "Help (Ctrl+H)", nullptr));
        actionRead_Dependencies->setText(QCoreApplication::translate("MainWindow", "Read Dependencies", nullptr));
        actionContact_information->setText(QCoreApplication::translate("MainWindow", "Contact information", nullptr));
        action_about->setText(QCoreApplication::translate("MainWindow", "About (Ctrl+A)", nullptr));
        actionContact->setText(QCoreApplication::translate("MainWindow", "Contact", nullptr));
        action_cur_jpeg_preview->setText(QCoreApplication::translate("MainWindow", "Preview (Space)", nullptr));
        action_dir_goto_parent->setText(QCoreApplication::translate("MainWindow", "Go to Parent Directory (Backspace)", nullptr));
        action_dir_goto_cur_child->setText(QCoreApplication::translate("MainWindow", "Go inside Selected Directory (Enter)", nullptr));
        action_dir_cur_child_fold->setText(QCoreApplication::translate("MainWindow", "Fold Selected Directory (Left Arrow)", nullptr));
        action_dir_cur_child_unfold->setText(QCoreApplication::translate("MainWindow", "Unfold Selected Directory (Right Arrow)", nullptr));
        action_cur_file_open->setText(QCoreApplication::translate("MainWindow", "Open with an external app (Ctrl+O)", nullptr));
        actionsdf->setText(QCoreApplication::translate("MainWindow", "sdf", nullptr));
        actionSave_geometry_configuration_Ctrl_Shift_L->setText(QCoreApplication::translate("MainWindow", "Save geometry configuration (Ctrl + Shift + L)", nullptr));
        action_dir_ft_filter_toggle->setText(QCoreApplication::translate("MainWindow", "File type filter toggle (Ctrl+F)", nullptr));
        action_tabs_show_tab1->setText(QCoreApplication::translate("MainWindow", "Raw Bayer Tab (Ctrl+1) or (Alt+1)", nullptr));
        action_tabs_show_tab2->setText(QCoreApplication::translate("MainWindow", "Spectrum-Raw Tab (Ctrl+2) or (Alt+2)", nullptr));
        action_tabs_show_tab3->setText(QCoreApplication::translate("MainWindow", "Spectrum-Reflectance Tab (Ctrl+3) or (Alt+3)", nullptr));
        pb_send_cmd->setText(QCoreApplication::translate("MainWindow", "SEND", nullptr));
        groupBox->setTitle(QString());
        b_this_pc_get_ip->setText(QCoreApplication::translate("MainWindow", "(Re)-check\n"
" computer IP", nullptr));
        _l_4->setText(QCoreApplication::translate("MainWindow", "Network interface", nullptr));
        l_this_pc_ip->setText(QCoreApplication::translate("MainWindow", "..................", nullptr));
        label_6->setText(QCoreApplication::translate("MainWindow", "Enter Device IP address", nullptr));
        b_search_ip_for_pi->setText(QCoreApplication::translate("MainWindow", "Scan IPs", nullptr));
        b_ssh_copy_id->setText(QCoreApplication::translate("MainWindow", "ssh-copy-id", nullptr));
        b_check_ssh_connection->setText(QCoreApplication::translate("MainWindow", "Check SSH \n"
"Connection", nullptr));
        b_soft_reboot->setText(QCoreApplication::translate("MainWindow", "Soft-reboot \n"
"(Back to handheld mode)", nullptr));
        b_hard_reboot->setText(QCoreApplication::translate("MainWindow", "Hard-Reboot", nullptr));
        b_tmux_init->setText(QCoreApplication::translate("MainWindow", "Init TMUX", nullptr));
        b_terminate_python_processes->setText(QCoreApplication::translate("MainWindow", "Softer-reboot\n"
"(kill tmux + python)", nullptr));
        b_info_dump->setText(QCoreApplication::translate("MainWindow", "Info Dump", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab), QCoreApplication::translate("MainWindow", "Connection", nullptr));
        label_2->setText(QCoreApplication::translate("MainWindow", "Motor-Elevation", nullptr));
        label->setText(QCoreApplication::translate("MainWindow", "Motor-Azimuth", nullptr));
        sp_azi->setSuffix(QString());
        pb_motor_zeroing->setText(QCoreApplication::translate("MainWindow", "Set curret to 0", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab_2), QCoreApplication::translate("MainWindow", "Motor", nullptr));
        _l1->setText(QCoreApplication::translate("MainWindow", "Cam1", nullptr));
        _l1_2->setText(QCoreApplication::translate("MainWindow", "Cam2", nullptr));
        _l1_3->setText(QCoreApplication::translate("MainWindow", "Cam3", nullptr));
        _l1_4->setText(QCoreApplication::translate("MainWindow", "Cam4", nullptr));
        _l1_5->setText(QCoreApplication::translate("MainWindow", "Cam5", nullptr));
        _l1_6->setText(QCoreApplication::translate("MainWindow", "Cam6", nullptr));
        _l1_7->setText(QCoreApplication::translate("MainWindow", "Cam7", nullptr));
        _l1_8->setText(QCoreApplication::translate("MainWindow", "Cam8", nullptr));
        label_4->setText(QCoreApplication::translate("MainWindow", "Lower", nullptr));
        label_3->setText(QCoreApplication::translate("MainWindow", "Base", nullptr));
        label_5->setText(QCoreApplication::translate("MainWindow", "Higher", nullptr));
        b_1shot->setText(QCoreApplication::translate("MainWindow", "1shot", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab_7), QCoreApplication::translate("MainWindow", "Exposure", nullptr));
        label_12->setText(QCoreApplication::translate("MainWindow", "Data full Path", nullptr));
        label_13->setText(QCoreApplication::translate("MainWindow", "Data tag", nullptr));
        b_meas_gimbal_refresh->setText(QCoreApplication::translate("MainWindow", "Refresh\n"
" command", nullptr));
        _l_2->setText(QCoreApplication::translate("MainWindow", "Elevation", nullptr));
        _l->setText(QCoreApplication::translate("MainWindow", "Azimuth ", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab_3), QCoreApplication::translate("MainWindow", "Meas-Gimbal", nullptr));
        b_meas_uav_refresh->setText(QCoreApplication::translate("MainWindow", " Refresh\n"
"cmd", nullptr));
        label_9->setText(QCoreApplication::translate("MainWindow", "Data Full Directory:", nullptr));
        label_10->setText(QCoreApplication::translate("MainWindow", "Data Tag:", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab_6), QCoreApplication::translate("MainWindow", "Meas-UAV", nullptr));
        groupBox_2->setTitle(QString());
        b_check_dir_tree->setText(QCoreApplication::translate("MainWindow", "Dir-Tree", nullptr));
        b_check_tmux->setText(QCoreApplication::translate("MainWindow", "Check TMUX", nullptr));
        b_check_stroge->setText(QCoreApplication::translate("MainWindow", "Storage", nullptr));
        tabWidget_2->setTabText(tabWidget_2->indexOf(tab_4), QCoreApplication::translate("MainWindow", "Raw Text", nullptr));
        pb_get_cam0->setText(QCoreApplication::translate("MainWindow", "Download and Show Photo", nullptr));
        tabWidget_2->setTabText(tabWidget_2->indexOf(tab_5), QCoreApplication::translate("MainWindow", "Visual", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
