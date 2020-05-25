from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  
import os
import pandas as pd
import csv
from datetime import date
from datetime import datetime

statewise=pd.read_csv("https://api.covid19india.org/csv/latest/state_wise.csv")
statedaily=pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")
stateDict={"Total":"TT","Andhra Pradesh":"AP","Arunachal Pradesh":"AR","Assam":"AS","Bihar":"BR","Chhattisgarh":"CT","Goa":"GA","Gujarat":"GJ","Haryana":"HR","Himachal Pradesh":"HP","Jharkhand":"JH",
"Karnataka":"KA","Kerala":"KL","Madhya Pradesh":"MP","Maharashtra":"MH","Manipur":"MN","Meghalaya":"ML","Mizoram":"MZ","Nagaland":"NL","Odisha":"OR","Punjab":"PB","Rajasthan":"RJ","Sikkim":"SK",
"Tamil Nadu":"TN","Telangana":"TG","Tripura":"TR","Uttarakhand":"UT","Uttar Pradesh":"UP","West Bengal":"WB","Andaman and Nicobar Islands":"AN","Chandigarh":"CH","Dadra and Nagar Haveli":"DN",
"Daman and Diu":"DD","Delhi":"DL","Jammu and Kashmir":"JK","Ladakh":"LA","Lakshadweep":"LD","Puducherry":"PY","Dadra and Nagar Haveli and Daman and Diu":"DN","State Unassigned":"UN"}
StateList=list(statewise['State'].dropna())

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class TimeAxisItem(pg.AxisItem):
    def tickStrings(self, values, scale, spacing):
        return [datetime.fromtimestamp(value) for value in values]
class Ui_StateWise(object):
    def setupUi(self, StateWise):
        QtGui.QFontDatabase.addApplicationFont(resource_path("Pictures/BankGothic Md BT.ttf"))
        StateWise.setObjectName("StateWise")
        StateWise.resize(546, 539)
        StateWise.setFixedSize(StateWise.size())
        self.centralwidget = QtWidgets.QWidget(StateWise)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 546, 60))
        font = QtGui.QFont()
        font.setFamily("BankGothic Md BT")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 300, 41))
        font = QtGui.QFont()
        font.setFamily("BankGothic Md BT")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(360, 110, 161, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 126, 60))
        font = QtGui.QFont()
        font.setFamily("BankGothic Md BT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(100)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(145, 150, 126, 60))
        font = QtGui.QFont()
        font.setFamily("BankGothic Md BT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(100)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 150, 126, 60))
        font = QtGui.QFont()
        font.setFamily("BankGothic Md BT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(100)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(395, 150, 126, 60))
        font = QtGui.QFont()
        font.setFamily("BankGothic Md BT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(100)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.graphWidget = PlotWidget(self.centralwidget)
        self.graphWidget.setGeometry(QtCore.QRect(20, 230, 501, 251))
        self.graphWidget.setObjectName("graphWidget")
        StateWise.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StateWise)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 546, 26))
        self.menubar.setObjectName("menubar")
        StateWise.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StateWise)
        self.statusbar.setObjectName("statusbar")
        StateWise.setStatusBar(self.statusbar)
        self.comboBox.currentIndexChanged.connect(self.updates)
        StateWise.setStyleSheet("background-color:#fff9ea")
        self.comboBox_2= QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(360, 485, 161, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.currentIndexChanged.connect(self.updateGraph)
        self.retranslateUi(StateWise)
        QtCore.QMetaObject.connectSlotsByName(StateWise)
    def updateGraph(self):
        val=self.comboBox.currentText()
       
        stateCode=stateDict[val]
        stateDC=statedaily.loc[statedaily["Status"]=="Confirmed"]
        stateDR=statedaily.loc[statedaily["Status"]=="Recovered"]
        stateDD=statedaily.loc[statedaily["Status"]=="Deceased"]
        stateDCVal=list(stateDC[stateCode])
        stateDRVal=list(stateDR[stateCode])
        stateDDVal=list(stateDD[stateCode])
        stateDates=list(stateDC["Date"])
        tmp=self.comboBox_2.currentText()
        if(tmp=="Confirmed"):
            self.plot(stateDates,stateDCVal)
        if(tmp=="Recovered"):
            self.plot(stateDates,stateDRVal,c1='#C0E5C8',c2='#E4F4E8',c3='#29A746')
        if(tmp=="Deceased"):
            self.plot(stateDates,stateDDVal,c1='#706CC3',c2='#E3E2F3',c3='#3D37AD')
        
    def updates(self):
        _translate = QtCore.QCoreApplication.translate
        val=self.comboBox.currentText()
        state=statewise.loc[statewise['State']==val]
        confirmed=int(state['Confirmed'])
        recovered=int(state['Recovered'])
        deaths=int(state['Deaths'])
        active=int(state['Active'])
        self.label_3.setText(_translate("StateWise", "Confirmed:"+"\n"+str(confirmed)))
        self.label_4.setText(_translate("StateWise", "Active:"+"\n"+str(active)))
        self.label_5.setText(_translate("StateWise", "Recovered:"+"\n"+str(recovered)))
        self.label_6.setText(_translate("StateWise", "Deceased:"+"\n"+str(deaths)))
        stateCode=stateDict[val]
        stateDC=statedaily.loc[statedaily["Status"]=="Confirmed"]
        stateDR=statedaily.loc[statedaily["Status"]=="Recovered"]
        stateDD=statedaily.loc[statedaily["Status"]=="Deceased"]
        stateDCVal=list(stateDC[stateCode])
        stateDRVal=list(stateDR[stateCode])
        stateDDVal=list(stateDD[stateCode])
        stateDates=list(stateDC["Date"])
        self.plot(stateDates,stateDCVal)
        self.updateGraph()
    def plot(self, x, y,c1="#FF6282",c2="#FFE0E6",c3="#FF083B"):
        xdict = dict(enumerate(x))
        xax = self.graphWidget.getAxis('bottom')
        xax.setTicks([xdict.items()])
        pen=pg.mkPen(color=c1,width=5,)
        self.graphWidget.clear()
        #self.graphWidget.setLabel('left', "<span style=\"color:#017CFF;font-size:20px;background-color:#EFF7FF\">&nbsp;Active </span>")
        #self.graphWidget.setLabel('bottom',"<span style=\"color:#29A746;font-size:20px;background-color:#E4F4E8\">&nbsp;Recovered </span>")
        self.data_line=self.graphWidget.plot(list(xdict),y,pen=pen, symbol='o', symbolSize=10, symbolBrush=(c3))
        self.graphWidget.setBackground(c2)
    def retranslateUi(self, StateWise):
        _translate = QtCore.QCoreApplication.translate
        StateWise.setWindowTitle(_translate("StateWise", "Statewise Analysis"))
        self.label.setText(_translate("StateWise", "Statewise Analysis"))
        self.label.setStyleSheet('color: #FD7F15;background-color: #FFF3D0;background-image:url("");qproperty-alignment: AlignCenter;')
        self.label_2.setText(_translate("StateWise", " Select a State/U.T  :"))
        self.label_2.setStyleSheet('color: #FC9274;background-color: #FEE5D9;background-image:url("");')
        self.label_3.setStyleSheet('color: #FF2D58;background-color: #F8CCCA;background-image:url("");qproperty-alignment: AlignCenter;')
        self.label_4.setStyleSheet('color: #017CFF;background-color: #EFF7FF;background-image:url("");qproperty-alignment: AlignCenter;')
        self.label_5.setStyleSheet('color:#29A746;background-color: #E4F4E8;background-image:url("");qproperty-alignment: AlignCenter;')
        self.label_6.setStyleSheet('color:#767E85;background-color: #F6F6F7;background-image:url("");qproperty-alignment: AlignCenter;')
        self.comboBox.addItems(StateList)
        self.comboBox_2.addItems(["Confirmed","Recovered","Deceased"])
        self.comboBox_2.setStyleSheet("background-color:white")
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(resource_path('Pictures/virus.ico')))
    StateWise = QtWidgets.QMainWindow()
    ui = Ui_StateWise()
    ui.setupUi(StateWise)
    StateWise.show()
    sys.exit(app.exec_())
