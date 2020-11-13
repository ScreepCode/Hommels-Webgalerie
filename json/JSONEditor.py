# -*- coding: utf-8 -*-

import json
import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class JSONTool(object):
    def __init__(self):
       self.dateipfad = os.path.abspath(".")+ "/ImgDetails.js"
       #self.dateipfad = "Users/detlefhommel/Desktop/WebSeites/json/ImgDetails.js"
    
    def openJSON(self):
        # Datei öffnen
        f = open(self.dateipfad, "r")
        rawJS = f.read()
        f.close()
        
        # Bisheriges Einlesen
        linesJS = rawJS.split("+")
        tmp = "["

        tmp += rawJS.replace("+", "")
        tmp = tmp.replace("'", "")
        tmp = tmp.replace('var data = "["', "")
        tmp = tmp.replace("\n", "")
        tmp = tmp.replace("        ", "")
        tmp = tmp.replace('"]"', "")

        tmp += "]"

        jsonData = json.loads(tmp)
        return jsonData

    def appendNewJSON(self, newJsonString):
        data = self.openJSON()

        dataStr = str(data)[:-1]
        dataStr += "," + newJsonString + "]"
        
        jsonData = json.loads(dataStr.replace("'", '"'))

        f = open(self.dateipfad, "w")
        out = '\nvar data = "[" + \n'
        for x in jsonData:
            y = str(x).replace("'", '"')
            out +=  "        '" + y + ",' + \n"
        out = out[:-6] + "' + \n"   
        out += '        "]"'
        f.write(out)

    def editJSON(self, index, editJsonString):
        jsonData = self.openJSON()

        jsonData[index] = editJsonString

        f = open(self.dateipfad, "w")
        out = '\nvar data = "[" + \n'
        for x in jsonData:
            y = str(x).replace("'", '"')
            out +=  "        '" + y + ",' + \n"
        out = out[:-6] + "' + \n"   
        out += '        "]"'
        f.write(out)

    def deleteJSON(self, title):
        jsonData = self.openJSON()
        tempJSON = []

        for x in jsonData:
            if(x["title"] != title):
                tempJSON.append(str(x))

        f = open(self.dateipfad, "w")
        out = '\nvar test = "[" + \n'
        for x in tempJSON:
            y = str(x).replace("'", '"')
            out +=  "        '" + y + ",' + \n"
        out = out[:-6] + "' + \n"   
        out += '        "]"'
        f.write(out)

    def appendNewJSONWithPictureName(self, pictureName):

        pictureNameSplit = pictureName.split("_")

        title = ""
        year = ""
        format = ""
        technic = ""

        next = 0

        for x in range(len(pictureNameSplit)):
            if len(pictureNameSplit[x]) != 4:
                title += pictureNameSplit[x] + " "
            else:
                next = x
                break

        year = pictureNameSplit[next]
        next += 1
        formatArr = pictureNameSplit[next:(next+4)]
        format = " ".join(formatArr)
        next += 4
        technicArr = pictureNameSplit[next:]
        technic = " ".join(technicArr)
        
        jsonData = '{"title": "'+ title[:-1] +'", "year": "'+ year +'", "format": "'+ format +'", "technic": "'+ technic +'"}'
        self.appendNewJSON(jsonData)

class JSONOpen(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "JSON Parser"
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 400, 600)
        
        #Button
        self.button1 = QPushButton("Neuen JSON String hinzufügen", self)
        self.button1.move(50, 100)
        self.button1.resize(300, 50)

        self.button2 = QPushButton("Bestehenden JSON String bearbeiten", self)
        self.button2.move(50, 200)
        self.button2.resize(300, 50)
        

class JSONAdd(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "JSON Parser"
        self.initUI()

        self.tool = JSONTool()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 400, 600)

        #Textfelder
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(50,100)
        self.textbox1.resize(300, 50)

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(50,200)
        self.textbox2.resize(300, 50)

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(50,300)
        self.textbox3.resize(300, 50)

        self.textbox4 = QLineEdit(self)
        self.textbox4.move(50,400)
        self.textbox4.resize(300, 50)

        #Button
        self.button = QPushButton("Bestätigen", self)
        self.button.move(50, 500)
        self.button.resize(300, 50)
        self.button.clicked.connect(self.on_button_clicked)

        #Label
        self.label1 = QLabel("Title", self)
        self.label1.move(50, 75)
        self.label1.setFont(QFont("Arial", 18))

        self.label2 = QLabel("Year", self)
        self.label2.move(50, 175)
        self.label2.setFont(QFont("Arial", 18))

        self.label3 = QLabel("Format", self)
        self.label3.move(50, 275)
        self.label3.setFont(QFont("Arial", 18))

        self.label4 = QLabel("Technic", self)
        self.label4.move(50, 375)
        self.label4.setFont(QFont("Arial", 18))

        self.label5 = QLabel("", self)
        self.label5.move(50, 550)
        self.label5.setFont(QFont("Arial", 10))
        self.label5.resize(300, 50)

        self.homeButton = QPushButton("Home", self)
        self.homeButton.move(0, 0)
        self.homeButton.resize(60, 25)

    def on_button_clicked(self):
        if(self.textbox1.text() != "" and self.textbox2.text() != "" and self.textbox3.text() != "" and self.textbox4.text() != ""):
            jsonData = '{"title": "'+ self.textbox1.text() +'", "year": "'+ self.textbox2.text() +'", "format": "'+ self.textbox3.text() +'", "technic": "'+ self.textbox4.text() +'"}'
            self.tool.appendNewJSON(jsonData)
            self.textbox1.setText("")
            self.textbox2.setText("")
            self.textbox3.setText("")
            self.textbox4.setText("")
            self.label5.setText("JSON String erfolgreich erstellt und hinzugefügt")
        else:
            self.label5.setText("Bitte fülle alle Felder aus")

class JSONEditTable(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "JSON Parser"
        self.initUI()

        self.tool = JSONTool()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 700, 600)

        self.table = QTableWidget(self)
        self.table.resize(700, 500)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Title", "Year", "Format", "Technic"])

        self.button = QPushButton("Ausgewählte Reihe ändern", self)
        self.button.move(50, 500)
        self.button.resize(300, 50)

        self.label = QLabel("", self)
        self.label.move(50, 550)
        self.label.setFont(QFont("Arial", 10))
        self.label.resize(300, 50)

        self.homeButton = QPushButton("Home", self)
        self.homeButton.move(0, 0)
        self.homeButton.resize(60, 25)

    def addTableRow(self):
        while (self.table.rowCount() > 0):
            self.table.removeRow(0)

        jsonData = self.tool.openJSON()

        for x in jsonData:
            row = self.table.rowCount()
            self.table.setRowCount(row+1)
            self.table.setItem(row, 0, QTableWidgetItem(str(x["title"])))
            self.table.setItem(row, 1, QTableWidgetItem(str(x["year"])))
            self.table.setItem(row, 2, QTableWidgetItem(str(x["format"])))
            self.table.setItem(row, 3, QTableWidgetItem(str(x["technic"])))
        self.table.resizeColumnsToContents()
    

class JSONEditString(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "JSON Parser"
        self.initUI()

        self.tool = JSONTool()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 450, 600)


        #Textfelder
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(50,100)
        self.textbox1.resize(300, 50)

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(50,200)
        self.textbox2.resize(300, 50)

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(50,300)
        self.textbox3.resize(300, 50)

        self.textbox4 = QLineEdit(self)
        self.textbox4.move(50,400)
        self.textbox4.resize(300, 50)

        #Button
        self.button = QPushButton("Bestätigen", self)
        self.button.move(50, 500)
        self.button.resize(300, 50)

        #Label
        self.label1 = QLabel("Title", self)
        self.label1.move(50, 75)
        self.label1.setFont(QFont("Arial", 18))

        self.label2 = QLabel("Year", self)
        self.label2.move(50, 175)
        self.label2.setFont(QFont("Arial", 18))

        self.label3 = QLabel("Format", self)
        self.label3.move(50, 275)
        self.label3.setFont(QFont("Arial", 18))

        self.label4 = QLabel("Technic", self)
        self.label4.move(50, 375)
        self.label4.setFont(QFont("Arial", 18))

        self.label5 = QLabel("", self)
        self.label5.move(50, 550)
        self.label5.setFont(QFont("Arial", 10))
        self.label5.resize(300, 50)

        self.homeButton = QPushButton("Home", self)
        self.homeButton.move(0, 0)
        self.homeButton.resize(60, 25)

    def loadString(self, number):
        self.number = number
        jsonData = self.tool.openJSON()
        self.textbox1.setText(jsonData[number]["title"])
        self.textbox2.setText(jsonData[number]["year"])
        self.textbox3.setText(jsonData[number]["format"])
        self.textbox4.setText(jsonData[number]["technic"])

    def buttonFunction(self):
        if(self.textbox1.text() != "" and self.textbox2.text() != "" and self.textbox3.text() != "" and self.textbox4.text() != ""):
            editJsonData = '{"title": "'+ self.textbox1.text() +'", "year": "'+ self.textbox2.text() +'", "format": "'+ self.textbox3.text() +'", "technic": "'+ self.textbox4.text() +'"}'
            self.tool.editJSON(self.number, editJsonData)
            self.textbox1.setText("")
            self.textbox2.setText("")
            self.textbox3.setText("")
            self.textbox4.setText("")

            self.label5.setText("JSON String erfolgreich geändert")
            return True
        else:
            self.label5.setText("Es darf kein Textfeld leer sein")
            return False


if __name__ == "__main__":
    App = QApplication(sys.argv)

    openGui = JSONOpen()
    addGui = JSONAdd()
    editTableGui = JSONEditTable()
    editStringGui = JSONEditString()

    def on_click_add():
        addGui.show()
        openGui.hide()

    def on_click_edit():
        editTableGui.show()
        editTableGui.addTableRow()
        openGui.hide()

    def on_click_home():
        openGui.show()
        try:
            editTableGui.hide()
        except:
            pass
        try:
            editStringGui.hide()
        except:
            pass
        try:
            addGui.hide()
        except:
            pass

    def on_click_editRow():
        indexes = editTableGui.table.selectionModel().selectedRows()
        if len(indexes) > 0:
            for index in sorted(indexes):
                #print('Row %d is selected' % index.row())
                editStringGui.loadString(int("%d" % index.row()))

            editStringGui.show()
            editTableGui.hide()
            editTableGui.label.setText("")
            
        else:
            editTableGui.label.setText("Bitte wähle ein Reihe aus")
    
    def on_click_editString():
        if(editStringGui.buttonFunction()):
            editStringGui.button.setEnabled(False)
            timer = QTimer()
            timer.singleShot(2000, afterTimerTask)

    def afterTimerTask():
        editTableGui.show()
        editTableGui.addTableRow()
        editStringGui.hide()
        editStringGui.label5.setText("")
        editStringGui.button.setEnabled(True)


    openGui.button1.clicked.connect(on_click_add)
    openGui.button2.clicked.connect(on_click_edit)
    editTableGui.button.clicked.connect(on_click_editRow)
    editStringGui.button.clicked.connect(on_click_editString)

    editTableGui.homeButton.clicked.connect(on_click_home)
    editStringGui.homeButton.clicked.connect(on_click_home)
    addGui.homeButton.clicked.connect(on_click_home)



    openGui.show()
    #editTableGui.show()
    sys.exit(App.exec_())
