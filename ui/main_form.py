# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.change_ui import ChangeUI
from models import *

class MainForm(object):
    def __init__(self, form):
        self.form = form

    def setupUi(self, Form):
        Form.setObjectName("Интерфейс к БД")
        Form.resize(700, 600)
        Form.setMinimumSize(QtCore.QSize(700, 600))
        Form.setMaximumSize(QtCore.QSize(700, 600))

        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 700, 600))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 100)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.OrganizationTypeButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.OrganizationTypeButton.setObjectName("OrganizationTypeButton")
        self.verticalLayout.addWidget(self.OrganizationTypeButton)
        self.TypeOfEventButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.TypeOfEventButton.setObjectName("TypeOfEventButton")
        self.verticalLayout.addWidget(self.TypeOfEventButton)
        self.TypeOfWindowButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.TypeOfWindowButton.setObjectName("TypeOfWindowButton")
        self.verticalLayout.addWidget(self.TypeOfWindowButton)
        self.BuildingButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.BuildingButton.setObjectName("BuildingButton")
        self.verticalLayout.addWidget(self.BuildingButton)
        self.ResourceButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ResourceButton.setObjectName("ResourceButton")
        self.verticalLayout.addWidget(self.ResourceButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 100)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.MeterButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.MeterButton.setObjectName("MeterButton")
        self.verticalLayout_2.addWidget(self.MeterButton)
        self.EObjectButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.EObjectButton.setObjectName("EObjectButton")
        self.verticalLayout_2.addWidget(self.EObjectButton)
        self.VehicleButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.VehicleButton.setObjectName("VehicleButton")
        self.verticalLayout_2.addWidget(self.VehicleButton)
        self.TypeOfResourceButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.TypeOfResourceButton.setObjectName("TypeOfResourceButton")
        self.verticalLayout_2.addWidget(self.TypeOfResourceButton)
        self.AddressButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.AddressButton.setObjectName("AddressButton")
        self.verticalLayout_2.addWidget(self.AddressButton)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 100)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.MeterModelButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.MeterModelButton.setObjectName("MeterModelButton")
        self.verticalLayout_3.addWidget(self.MeterModelButton)
        self.ManagerButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ManagerButton.setObjectName("ManagerButton")
        self.verticalLayout_3.addWidget(self.ManagerButton)
        self.EventButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.EventButton.setObjectName("EventButton")
        self.verticalLayout_3.addWidget(self.EventButton)
        self.TypeOfWallButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.TypeOfWallButton.setObjectName("TypeOfWallButton")
        self.verticalLayout_3.addWidget(self.TypeOfWallButton)
        self.ConsumptionButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ConsumptionButton.setObjectName("ConsumptionButton")
        self.verticalLayout_3.addWidget(self.ConsumptionButton)
        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.connect_slots()

        self.change = QtWidgets.QWidget()
        self.change_ui = ChangeUI(self.form, self.change)
        self.change_ui.setupUi(self.change)


    def connect_slots(self):
        self.OrganizationTypeButton.clicked.connect(self.type_organization_slot)
        self.TypeOfEventButton.clicked.connect(self.type_event_slot)
        self.TypeOfWindowButton.clicked.connect(self.type_window_slot)
        self.BuildingButton.clicked.connect(self.buildings_slot)
        self.ResourceButton.clicked.connect(self.resource_slot)
        self.MeterButton.clicked.connect(self.meters_slot)
        self.EObjectButton.clicked.connect(self.eobjects_slot)
        self.VehicleButton.clicked.connect(self.vehicles_slot)
        self.TypeOfResourceButton.clicked.connect(self.type_resource_slot)
        self.AddressButton.clicked.connect(self.adress_slot)
        self.MeterModelButton.clicked.connect(self.type_meter_slot)
        self.ManagerButton.clicked.connect(self.manager_slot)
        self.EventButton.clicked.connect(self.events_slot)
        self.TypeOfWallButton.clicked.connect(self.type_wall_slot)
        self.ConsumptionButton.clicked.connect(self.consumptions_slot)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Интерфейс к БД"))
        self.OrganizationTypeButton.setText(_translate("Form", "Типы Организации"))
        self.TypeOfEventButton.setText(_translate("Form", "Типы Мероприятий"))
        self.TypeOfWindowButton.setText(_translate("Form", "Типы Оконных Блоков"))
        self.BuildingButton.setText(_translate("Form", "Здания"))
        self.ResourceButton.setText(_translate("Form", "Ресурсы"))
        self.MeterButton.setText(_translate("Form", "Приборы Учета"))
        self.EObjectButton.setText(_translate("Form", "Энерго Объекты"))
        self.VehicleButton.setText(_translate("Form", "Транспорт"))
        self.TypeOfResourceButton.setText(_translate("Form", "Типы Ресурсов"))
        self.AddressButton.setText(_translate("Form", "Адреса"))
        self.MeterModelButton.setText(_translate("Form", "Модели Приборов Учета"))
        self.ManagerButton.setText(_translate("Form", "Управляющие"))
        self.EventButton.setText(_translate("Form", "Мероприятия"))
        self.TypeOfWallButton.setText(_translate("Form", "Типы Стен"))
        self.ConsumptionButton.setText(_translate("Form", "Потребления"))

    def _chage_window(self):
        self.form.hide()
        self.change.show()

    def type_organization_slot(self):
        self.change_ui.set_model(OrganizationType())
        self._chage_window()

    def type_event_slot(self):
        self.change_ui.set_model(TypeOfEvent())
        self._chage_window()

    def type_window_slot(self):
        self.change_ui.set_model(TypeOfWindow())
        self._chage_window()

    def buildings_slot(self):
        self.change_ui.set_model(Building())
        self._chage_window()

    def resource_slot(self):
        self.change_ui.set_model(Resource())
        self._chage_window()

    def meters_slot(self):
        self.change_ui.set_model(Meter())
        self._chage_window()

    def eobjects_slot(self):
        self.change_ui.set_model(EObject())
        self._chage_window()

    def vehicles_slot(self):
        self.change_ui.set_model(Vehicle())
        self._chage_window()

    def type_resource_slot(self):
        self.change_ui.set_model(TypeOfResource())
        self._chage_window()

    def adress_slot(self):
        self.change_ui.set_model(Address())
        self._chage_window()

    def type_meter_slot(self):
        self.change_ui.set_model(MeterModel())
        self._chage_window()

    def manager_slot(self):
        self.change_ui.set_model(Manager())
        self._chage_window()

    def events_slot(self):
        self.change_ui.set_model(Event())
        self._chage_window()

    def type_wall_slot(self):
        self.change_ui.set_model(TypeOfWall())
        self._chage_window()

    def consumptions_slot(self):
        self.change_ui.set_model(Consumption())
        self._chage_window()