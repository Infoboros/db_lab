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
        Form.resize(1200, 600)
        Form.setMinimumSize(QtCore.QSize(1200, 600))
        Form.setMaximumSize(QtCore.QSize(1200, 600))

        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1200, 600))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 100)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.organizationTypeButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.organizationTypeButton.setObjectName("OrganizationTypeButton")
        self.verticalLayout.addWidget(self.organizationTypeButton)
        self.typeOfEventButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.typeOfEventButton.setObjectName("TypeOfEventButton")
        self.verticalLayout.addWidget(self.typeOfEventButton)
        self.typeOfWindowButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.typeOfWindowButton.setObjectName("TypeOfWindowButton")
        self.verticalLayout.addWidget(self.typeOfWindowButton)
        self.buildingButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buildingButton.setObjectName("BuildingButton")
        self.verticalLayout.addWidget(self.buildingButton)
        self.resourceButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.resourceButton.setObjectName("ResourceButton")
        self.verticalLayout.addWidget(self.resourceButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 100)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.meterButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.meterButton.setObjectName("MeterButton")
        self.verticalLayout_2.addWidget(self.meterButton)
        self.eobjectButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.eobjectButton.setObjectName("EObjectButton")
        self.verticalLayout_2.addWidget(self.eobjectButton)
        self.vehicleButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.vehicleButton.setObjectName("VehicleButton")
        self.verticalLayout_2.addWidget(self.vehicleButton)
        self.typeOfResourceButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.typeOfResourceButton.setObjectName("TypeOfResourceButton")
        self.verticalLayout_2.addWidget(self.typeOfResourceButton)
        self.addressButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addressButton.setObjectName("AddressButton")
        self.verticalLayout_2.addWidget(self.addressButton)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 100)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.meterModelButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.meterModelButton.setObjectName("MeterModelButton")
        self.verticalLayout_3.addWidget(self.meterModelButton)
        self.managerButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.managerButton.setObjectName("ManagerButton")
        self.verticalLayout_3.addWidget(self.managerButton)
        self.eventButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.eventButton.setObjectName("EventButton")
        self.verticalLayout_3.addWidget(self.eventButton)
        self.typeOfWallButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.typeOfWallButton.setObjectName("TypeOfWallButton")
        self.verticalLayout_3.addWidget(self.typeOfWallButton)
        self.consumptionButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.consumptionButton.setObjectName("ConsumptionButton")
        self.verticalLayout_3.addWidget(self.consumptionButton)
        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.connect_slots()

        self.change = QtWidgets.QWidget()
        self.change_ui = ChangeUI(self.form, self.change)
        self.change_ui.setupUi(self.change)


    def connect_slots(self):
        self.organizationTypeButton.clicked.connect(self.type_organization_slot)
        self.typeOfEventButton.clicked.connect(self.type_event_slot)
        self.typeOfWindowButton.clicked.connect(self.type_window_slot)
        self.buildingButton.clicked.connect(self.buildings_slot)
        self.resourceButton.clicked.connect(self.resource_slot)
        self.meterButton.clicked.connect(self.meters_slot)
        self.eobjectButton.clicked.connect(self.eobjects_slot)
        self.vehicleButton.clicked.connect(self.vehicles_slot)
        self.typeOfResourceButton.clicked.connect(self.type_resource_slot)
        self.addressButton.clicked.connect(self.adress_slot)
        self.meterModelButton.clicked.connect(self.type_meter_slot)
        self.managerButton.clicked.connect(self.manager_slot)
        self.eventButton.clicked.connect(self.events_slot)
        self.typeOfWallButton.clicked.connect(self.type_wall_slot)
        self.consumptionButton.clicked.connect(self.consumptions_slot)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Интерфейс к БД"))
        self.organizationTypeButton.setText(_translate("Form", "Типы Организации"))
        self.typeOfEventButton.setText(_translate("Form", "Типы Мероприятий"))
        self.typeOfWindowButton.setText(_translate("Form", "Типы Оконных Блоков"))
        self.buildingButton.setText(_translate("Form", "Здания"))
        self.resourceButton.setText(_translate("Form", "Ресурсы"))
        self.meterButton.setText(_translate("Form", "Приборы Учета"))
        self.eobjectButton.setText(_translate("Form", "Энерго Объекты"))
        self.vehicleButton.setText(_translate("Form", "Транспорт"))
        self.typeOfResourceButton.setText(_translate("Form", "Типы Ресурсов"))
        self.addressButton.setText(_translate("Form", "Адреса"))
        self.meterModelButton.setText(_translate("Form", "Модели Приборов Учета"))
        self.managerButton.setText(_translate("Form", "Управляющие"))
        self.eventButton.setText(_translate("Form", "Мероприятия"))
        self.typeOfWallButton.setText(_translate("Form", "Типы Стен"))
        self.consumptionButton.setText(_translate("Form", "Потребления"))

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