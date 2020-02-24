# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MBTI.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(606, 471)
        self.stackedWidget = QStackedWidget(Dialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(70, 150, 491, 272))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.E = QRadioButton(self.page)
        self.E.setObjectName(u"E")
        self.E.setGeometry(QRect(1, 93, 16, 16))
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(29, 67, 441, 65))
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setWordWrap(True)
        self.I = QRadioButton(self.page)
        self.I.setObjectName(u"I")
        self.I.setGeometry(QRect(1, 157, 16, 16))
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(29, 138, 441, 52))
        self.label_3.setTextFormat(Qt.AutoText)
        self.label_3.setWordWrap(True)
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(1, 1, 471, 52))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(Qt.AutoText)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.b1 = QPushButton(self.page)
        self.b1.setObjectName(u"b1")
        self.b1.setGeometry(QRect(260, 220, 75, 23))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(11, 1, 451, 26))
        self.label_5.setFont(font)
        self.label_5.setTextFormat(Qt.AutoText)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_6 = QLabel(self.page_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(36, 134, 401, 39))
        self.label_6.setTextFormat(Qt.AutoText)
        self.label_6.setWordWrap(True)
        self.N = QRadioButton(self.page_2)
        self.N.setObjectName(u"N")
        self.N.setGeometry(QRect(11, 147, 16, 16))
        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(31, 89, 411, 39))
        self.label_7.setTextFormat(Qt.AutoText)
        self.label_7.setWordWrap(True)
        self.S = QRadioButton(self.page_2)
        self.S.setObjectName(u"S")
        self.S.setGeometry(QRect(11, 102, 16, 16))
        self.b2 = QPushButton(self.page_2)
        self.b2.setObjectName(u"b2")
        self.b2.setGeometry(QRect(270, 200, 75, 23))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_8 = QLabel(self.page_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 21, 420, 85))
        self.label_8.setFont(font)
        self.label_8.setTextFormat(Qt.AutoText)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setWordWrap(True)
        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 157, 420, 16))
        self.label_9.setTextFormat(Qt.AutoText)
        self.label_9.setWordWrap(True)
        self.T = QRadioButton(self.page_3)
        self.T.setObjectName(u"T")
        self.T.setGeometry(QRect(1, 125, 16, 16))
        self.label_10 = QLabel(self.page_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 112, 420, 39))
        self.label_10.setTextFormat(Qt.AutoText)
        self.label_10.setWordWrap(True)
        self.F = QRadioButton(self.page_3)
        self.F.setObjectName(u"F")
        self.F.setGeometry(QRect(1, 157, 16, 16))
        self.b3 = QPushButton(self.page_3)
        self.b3.setObjectName(u"b3")
        self.b3.setGeometry(QRect(280, 210, 75, 23))
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_11 = QLabel(self.page_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(122, 35, 219, 39))
        self.label_11.setFont(font)
        self.label_11.setTextFormat(Qt.AutoText)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_11.setWordWrap(True)
        self.J = QRadioButton(self.page_4)
        self.J.setObjectName(u"J")
        self.J.setGeometry(QRect(12, 105, 16, 16))
        self.label_12 = QLabel(self.page_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(40, 170, 432, 26))
        self.label_12.setTextFormat(Qt.AutoText)
        self.label_12.setWordWrap(True)
        self.label_13 = QLabel(self.page_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(41, 102, 431, 52))
        self.label_13.setTextFormat(Qt.AutoText)
        self.label_13.setWordWrap(True)
        self.P = QRadioButton(self.page_4)
        self.P.setObjectName(u"P")
        self.P.setGeometry(QRect(12, 175, 16, 16))
        self.b4 = QPushButton(self.page_4)
        self.b4.setObjectName(u"b4")
        self.b4.setGeometry(QRect(280, 220, 75, 23))
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label = QLabel(self.page_5)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 471, 221))
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_14 = QLabel(self.page_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(0, 0, 471, 221))
        self.label_14.setTextFormat(Qt.AutoText)
        self.label_14.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_14.setWordWrap(True)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.label_15 = QLabel(self.page_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(0, 0, 471, 221))
        self.label_15.setTextFormat(Qt.AutoText)
        self.label_15.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_15.setWordWrap(True)
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.label_16 = QLabel(self.page_8)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(0, 10, 471, 221))
        self.label_16.setTextFormat(Qt.AutoText)
        self.label_16.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_16.setWordWrap(True)
        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.label_17 = QLabel(self.page_9)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(0, 0, 471, 221))
        self.label_17.setTextFormat(Qt.AutoText)
        self.label_17.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_17.setWordWrap(True)
        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.label_18 = QLabel(self.page_10)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(0, 0, 471, 221))
        self.label_18.setTextFormat(Qt.AutoText)
        self.label_18.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_18.setWordWrap(True)
        self.stackedWidget.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.label_19 = QLabel(self.page_11)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(0, 10, 471, 221))
        self.label_19.setTextFormat(Qt.AutoText)
        self.label_19.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_19.setWordWrap(True)
        self.stackedWidget.addWidget(self.page_11)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.label_20 = QLabel(self.page_12)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(0, 0, 471, 221))
        self.label_20.setTextFormat(Qt.AutoText)
        self.label_20.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_20.setWordWrap(True)
        self.stackedWidget.addWidget(self.page_12)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.label_21 = QLabel(self.page_13)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(0, 0, 471, 221))
        self.label_21.setTextFormat(Qt.AutoText)
        self.label_21.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_21.setWordWrap(True)
        self.stackedWidget.addWidget(self.page_13)
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.label_22 = QLabel(self.page_14)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(0, 0, 471, 221))
        self.label_22.setTextFormat(Qt.AutoText)
        self.label_22.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_22.setWordWrap(True)
        self.stackedWidget.addWidget(self.page_14)
        self.page_15 = QWidget()
        self.page_15.setObjectName(u"page_15")
        self.label_23 = QLabel(self.page_15)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(0, 0, 471, 221))
        self.label_23.setTextFormat(Qt.AutoText)
        self.label_23.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_23.setWordWrap(True)
        self.stackedWidget.addWidget(self.page_15)
        self.page_16 = QWidget()
        self.page_16.setObjectName(u"page_16")
        self.label_24 = QLabel(self.page_16)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(0, 10, 471, 221))
        self.label_24.setTextFormat(Qt.AutoText)
        self.label_24.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_24.setWordWrap(True)
        self.stackedWidget.addWidget(self.page_16)
        self.page_17 = QWidget()
        self.page_17.setObjectName(u"page_17")
        self.label_25 = QLabel(self.page_17)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(0, 10, 471, 221))
        self.label_25.setTextFormat(Qt.AutoText)
        self.label_25.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_25.setWordWrap(True)
        self.stackedWidget.addWidget(self.page_17)
        self.page_18 = QWidget()
        self.page_18.setObjectName(u"page_18")
        self.label_26 = QLabel(self.page_18)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(0, 10, 471, 221))
        self.label_26.setTextFormat(Qt.AutoText)
        self.label_26.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_26.setWordWrap(True)
        self.stackedWidget.addWidget(self.page_18)
        self.page_19 = QWidget()
        self.page_19.setObjectName(u"page_19")
        self.label_27 = QLabel(self.page_19)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 10, 471, 221))
        self.label_27.setTextFormat(Qt.AutoText)
        self.label_27.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_27.setWordWrap(True)
        self.stackedWidget.addWidget(self.page_19)
        self.page_20 = QWidget()
        self.page_20.setObjectName(u"page_20")
        self.label_28 = QLabel(self.page_20)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(10, 10, 471, 221))
        self.label_28.setTextFormat(Qt.AutoText)
        self.label_28.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_28.setWordWrap(True)
        self.stackedWidget.addWidget(self.page_20)
        self.l2 = QLabel(Dialog)
        self.l2.setObjectName(u"l2")
        self.l2.setGeometry(QRect(80, 70, 451, 81))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.l2.setFont(font1)
        self.l2.setAlignment(Qt.AlignCenter)
        self.un = QTextEdit(Dialog)
        self.un.setObjectName(u"un")
        self.un.setGeometry(QRect(290, 40, 171, 31))
        self.l1 = QLabel(Dialog)
        self.l1.setObjectName(u"l1")
        self.l1.setGeometry(QRect(230, 40, 41, 31))
        self.l1.setFont(font)
        self.dis = QLabel(Dialog)
        self.dis.setObjectName(u"dis")
        self.dis.setGeometry(QRect(80, 100, 181, 41))

        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(19)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.E.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"I\u2019ll call my friends to ask about their plans. I heard that a new restaurant opened / a nice comedy is playing in the cinemas / there are big discounts at the paintball club. We should all go out together.", None))
        self.I.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"I\u2019ll switch on the \"Don\u2019t disturb\" mode on my phone and stay at home. I\u2019ll watch a new episode of my favorite TV show, do a puzzle, and take a long bath with a book.", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"You are totally exhausted because your week was endless and less than great. How are you going to spend your weekend?", None))
        self.b1.setText(QCoreApplication.translate("Dialog", u"next", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Which of these 2 descriptions suits you more?", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Facts are boring. I love to dream and play over upcoming events in my mind. I rely more on intuition than information", None))
        self.N.setText("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"The most important thing for me is what\u2019s happening here and now. I assess real situations and pay attention to details.", None))
        self.S.setText("")
        self.b2.setText(QCoreApplication.translate("Dialog", u"next", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"A competitor of your current employer is trying to entice you. You have doubts because the salary is much higher there, but the staff here is great. Moreover, the head of your department hinted that he will recommend you to the bosses when he retires. How are you going to make a decision?", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"I\u2019ll listen to my feelings. I always try to follow my heart.", None))
        self.T.setText("")
        self.label_10.setText(QCoreApplication.translate("Dialog", u"I\u2019ll learn all the available information about the competitor, ask my HR manager for advice, and draw a chart with all the pros and cons. In such cases, it\u2019s important to weigh up all the arguments and assess the situation with a cold mind.", None))
        self.F.setText("")
        self.b3.setText(QCoreApplication.translate("Dialog", u"next", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Only 2 weeks are left before your close friends\u2019 wedding. How are the preparations going?", None))
        self.J.setText("")
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Why prepare? I\u2019ll be having fun and enjoying myself at the party. I\u2019ll improvise my wedding speech. The best things happen spontaneously.", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"One month ago, I chose the saxophonist who will play a medley of our school songs / collected the couple\u2019s photo love story / composed a poem / pressed my suit / made appointments with the stylist and makeup master. I prefer to be fully armed.", None))
        self.P.setText("")
        self.b4.setText(QCoreApplication.translate("Dialog", u"Show Results", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"ESTJ \u2014 MANAGER\n"
"Practical and consistent, you like to have order everywhere by planning and organizing everything. But most of all, you like to convince people of your rightness and make them think the way you think. You look at life soberly and, above all, trust facts.\n"
"\n"
"You are open for communication, meeting new people, and spending time at parties. You never forget to take care of your close ones and can express your love very well.\n"
"\n"
"11% men, 6% women", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"ENTJ \u2014 COMMANDER\n"
"Life for you is a struggle and extreme. This is how you know yourself and others. Being risky and brave, you are easily inspired to start something new. At the same time, you assess your abilities, both strengths and weaknesses, quite adequately.\n"
"\n"
"You feel new tendencies very well and are open to new ideas. You think positively and adore sport and everything connected to it.\n"
"\n"
"3% men, 1% women", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"ESFJ \u2014 TEACHER\n"
"You get along with people very well, and you are the life of any party. You are attentive, caring, and always ready to help, even if you have to sacrifice your personal interests for others.\n"
"\n"
"Yet you are very independent in your deals and, as a rule, you get everything without any side help. You only wait for emotional support from your close ones.\n"
"\n"
"17% women, 8% men", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"ESTP \u2014 MARSHAL\n"
"\"Participation is more important than victory.\" This is not about you. You strive to reach your goals by any means, even if you have to use physical strength. You stick to an exact plan, and you can\u2019t stand dependence and compromises.\n"
"\n"
"You\u2019re a born fighter, very active and self-organized. You can objectively evaluate even the most stressful situation and give a quick and exact response.\n"
"\n"
"6% men, 3% women", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"ENFJ \u2014 MENTOR\n"
"You are emotional and talkative with rich facial expressions and gesticulations. You are very empathetic to other people\u2019s emotions, and you can spot even the tiniest insincerity. You are very jealous and distrustful in love relationships.\n"
"\n"
"Very often, you are ready to face upcoming events because of your ability to feel them in advance.\n"
"\n"
"3% women, 2% men", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"ENTP \u2014 INVENTOR\n"
"The generator of ideas, you are always seeking to create something new. You adapt easily to nonfamiliar environments and master different methods of work easily.\n"
"\n"
"Due to your dislike of traditions and routine, you very often change your professional spheres and hobbies, becoming an innovator and a pioneer. What is important about you is that not only can you create new ideas but you are also able to convey them to others and make them come true.\n"
"\n"
"4% men, 2% women", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"ESFP \u2014 POLITICIAN\n"
"You can professionally determine the opportunities of your surroundings, and very often you use this skill to manipulate people. In communication with people, you primarily follow your personal interests. However, you try to impress everybody and create the image of a simple person.\n"
"\n"
"You stand firmly in the present moment, and you don\u2019t like to waste time. You want quick results, disliking bureaucracy and red tape.\n"
"\n"
"10% women, 7% men", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"ENFP \u2014 CHAMPION\n"
"You are energetic and inquisitive, with very clear creative skills. You combine the features of both introverts and extroverts, which is why not only do you get along with people easily but you also empathize well. You are very good at advising.\n"
"\n"
"You perceive life with all the diversity of its possibilities. You have a very rich imagination and a very high IQ. You\u2019re a very harmonious person, able to keep the balance even in a very quickly changing environment.\n"
"\n"
"10% women, 6% men", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"INFP \u2014 HEALER\n"
"A lyricist and dreamer, your inner harmony and self-agreement are always in first place. Most of your thinking happens deep inside of you. Nevertheless, you are able to foresee events and understand people well.\n"
"\n"
"You like to dress up and try to look good in all circumstances. You can\u2019t be called thrifty, and you often lose sense of time and reality.\n"
"\n"
"5% women, 4% men", None))
        self.label_22.setText(QCoreApplication.translate("Dialog", u"ISFP \u2014 COMPOSER\n"
"You can find joy in simple things, handling routine and monotony easily. You like to feel needed, which is why you always help other people but never interfere with their comfort zone. You can\u2019t stand conflicts, and you can always entertain people and make them laugh.\n"
"\n"
"You\u2019re a very down-to-earth, practical, caring, tender, reliable, and faithful partner. You take this world as it is, never trying to lead and manipulate.\n"
"\n"
"10% women, 8% men", None))
        self.label_23.setText(QCoreApplication.translate("Dialog", u"INTP \u2014 ARCHITECT\n"
"An egghead and philosopher, you don\u2019t like too much expressiveness. You always seek calm emotions and comfort. You\u2019re very careful when making decisions, preferring to analyze and find connections between the past, present, and future.\n"
"\n"
"You are very sensitive to changes, and you don\u2019t handle them easily. You always try to collect all of your facts, thoughts, and ideas, and that\u2019s why you are very often tense.\n"
"\n"
"5% men, 2% women", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"INFJ \u2014 ADVISOR\n"
"You are perfect at sensing people and their relationships. You can easily identify moods and hidden talents, which is why people seek advice from you. However, you are very vulnerable and can\u2019t stand aggression and lack of love.\n"
"\n"
"Your driving force is intuition, aimed not outside but inside. This type of person never stops learning, considering self-development to be a main priority. By getting to know yourself, you help others.\n"
"\n"
"2% women, 1% men", None))
        self.label_25.setText(QCoreApplication.translate("Dialog", u"INTJ \u2014 INSPIRER\n"
"You have the richest inner world from where you get your incredible ideas. You strive for excellence and want to improve everything and everybody.\n"
"\n"
"However, you have some difficulties in relationships with people, very often distancing yourself intentionally to demonstrate your independence. You can set priorities and trust your intuition.\n"
"\n"
"3% men, 1% women", None))
        self.label_26.setText(QCoreApplication.translate("Dialog", u"ISFJ \u2014 PROTECTOR\n"
"You can\u2019t stand falseness and insincerity in relationships. You distinguish \u201cstrangers\u201c and keep them at a distance right away. For the people \u201dinside your circle,\" you do anything and never ask for anything in return.\n"
"\n"
"You are observant and very careful with words and deeds. Kind and caring, you see your main goal as helping people and making them happier.\n"
"\n"
"19% women, 8% men", None))
        self.label_27.setText(QCoreApplication.translate("Dialog", u"ISTP \u2014 HANDYMAN\n"
"The handyman, as a rule, has a technical mindset and likes to make things by hand. You don\u2019t hurry with taking decisions and think that it is better twice measured than once wrong. However, you always meet deadlines and you are very punctual by nature. You perceive this world through feelings, and your opinion of things happening around you is very objective and specific. By nature, you are communicative, but you will refuse communication once you feel insincerity.\n"
"\n"
"9% men, 2% women", None))
        self.label_28.setText(QCoreApplication.translate("Dialog", u"ISTJ \u2014 INSPECTOR\n"
"Thoughtful, pensive, responsible. You are trustworthy, but you never take things as they are, always analyzing the incoming information. You are not interested in long-term communication and prefer official communication only during companionship. You are aimed at the final result.\n"
"\n"
"You like strictness and order, and very often you are pedantic. You don\u2019t live in your dreams, only in the \"here and now.\"\n"
"\n"
"15% men, 7% women", None))
        self.l2.setText(QCoreApplication.translate("Dialog", u"Which of the following suits you best ?", None))
        self.l1.setText(QCoreApplication.translate("Dialog", u"Name ", None))
        self.dis.setText("")
    # retranslateUi

