import sys
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
import inflect
import mysql.connector
mydb=mysql.connector.connect(host="localhost",port=3306,user="root",password="123456789",database="BILL")
cus = mydb.cursor()
inf=inflect.engine()


dc=''
dnc=''
x=''
user=''
password=''
valid=''
comp_no=''
state=''


class Ui_OtherWindow(object):
    states=[]
    states.append('Andaman & Nicobar Islands')
    states.append('Andhra Pradesh')
    states.append('Andrapradesh(New)')
    states.append('Arunachal Pradesh')
    states.append('Assam')
    states.append('Bihar')
    states.append('Chandigarh')
    states.append('Chhattisgarh')
    states.append('Dadra & Nagar Haveli')
    states.append('Daman & Diu')
    states.append('Delhi')
    states.append('Goa')
    states.append('Gujarat')
    states.append('Haryana')
    states.append('Himachal Pradesh')
    states.append('Jammu & Kashmir')
    states.append('Jharkhand')
    states.append('Karnataka')
    states.append('Kerala')
    states.append('Lakshadweep')
    states.append('Madhya Pradesh')
    states.append('Maharashtra')
    states.append('Manipur')
    states.append('Meghalaya')
    states.append('Mizoram')
    states.append('Nagaland')
    states.append('Orissa')
    states.append('Puducherry')
    states.append('Punjab')
    states.append('Rajasthan')
    states.append('Sikkim')
    states.append('Tamil Nadu')
    states.append('Telengana')
    states.append('Tripura')
    states.append('Uttarakhand')
    states.append('Uttar Pradesh')
    states.append('West Bengal')
    

    x=-1
    """x for product entry"""
    y=-1
    """y for product modify"""
    z=-1
    """z for add"""
    a=-1
    """a for master modify supplier and customer"""
    b=-1
    """b for debit and credit"""
    c=-1
    p=-1

    d=-1

    e=-1

    f=-1

    g=-1

    h=-1

    i=-1

    
    row=-1
    column=-1
    rowCount=1
    combobox_5=-1
    rowCount2=1

        
    



    
    def master(self):
        INITIALIZE.massForm.show()
        INITIALIZE.compForm.hide()
        INITIALIZE.compForm.hide()

    def master2(self):
        INITIALIZE.massForm.hide()
        INITIALIZE.compForm.hide()
        INITIALIZE.compForm.hide()

    
    #masters   >>>   Add_customer
    def do_this(self):
        self.do_this23()
        self.menubar.setEnabled(False)
        self.z=1
        self.label_49.setText(QtCore.QCoreApplication.translate("OtherWindow", "Customer details"))
        self.stackedWidget.setCurrentIndex(0)

    #Entry   >>>   Sales
    def do_this1(self):
        self.rowCount=1
        global comp_no
        self.p=comp_no
        print(self.p)
        self.stackedWidget.setCurrentIndex(1)
        
        cus.execute("SELECT * FROM PARTY WHERE type='Customer'")
        b=cus.fetchall()
        
        self.e=QtWidgets.QCheckBox()
        self.e.setEnabled(False)
        self.e.setGeometry(QtCore.QRect(200, 0, 10, 10))
        self.tableWidget.setCellWidget(0,0,self.e)
        self.comboBox_3.clear()
        print("hi")
        print(b)
        for i in b:
            self.comboBox_3.addItem(i[1])
        self.comboBox_3.setCurrentIndex(-1)
        self.comboBox_4.setCurrentIndex(-1)
        self.radioButton.setEnabled(False)
        self.radioButton_2.setEnabled(False)
        self.lineEdit_17.setEnabled(False)
        self.comboBox_10.setCurrentIndex(-1)
        self.do_this37()
        self.menubar.setEnabled(False)
        cus.execute("SELECT MAX(v_no) FROM SALES_VOUCHER WHERE c_no='%s'"%comp_no)
        b=cus.fetchall()
        print(b[0][0])
        
        print("how is it")
        if b[0][0]!=None:
            print("hi")
            self.spinBox.setValue(b[0][0]+1)
        else:
            self.spinBox.setValue(1)
        print("bye")

        

    #Products   >>>   Supplier 
    def do_this2(self):
        self.menubar.setEnabled(False)
        self.lineEdit_25.clear()
        self.lineEdit_26.clear()
        self.groupBox_2.setTitle(QtCore.QCoreApplication.translate("OtherWindow", "Supplier products"))
        
        
        self.stackedWidget.setCurrentIndex(2)
        self.comboBox_8.setCurrentIndex(-1)
        
        self.x=0

    #Products   >>>   Customer  
    def do_this3(self):
        self.menubar.setEnabled(False)
        self.lineEdit_25.clear()
        self.lineEdit_26.clear()
        self.groupBox_2.setTitle(QtCore.QCoreApplication.translate("OtherWindow", "Customer products"))
        self.stackedWidget.setCurrentIndex(2)
        self.comboBox_8.setCurrentIndex(-1)
        self.x=1
        
    #Entry   >>>   Purchases  
    def do_this4(self):
        global comp_no
        self.stackedWidget.setCurrentIndex(4)
        self.menubar.setEnabled(False)

        self.h=QtWidgets.QCheckBox()
        self.h.setEnabled(False)
        self.h.setGeometry(QtCore.QRect(200, 0, 10, 10))
        self.tableWidget_2.setCellWidget(0,0,self.h)

        cus.execute("SELECT * FROM PARTY WHERE type='Supplier'")
        b=cus.fetchall()
        for i in b:
            self.comboBox_9.addItem(i[1])
        self.comboBox_9.setCurrentIndex(-1)
        self.do_this50()
        
        cus.execute("SELECT MAX(v_no) FROM PURCHASE_VOUCHER WHERE c_no='%s'"%comp_no)
        b=cus.fetchall()
        print(b[0][0])
        
        print("how is it")
        if b[0][0]!=None:
            print("hi")
            self.spinBox_2.setValue(b[0][0]+1)
        else:
            self.spinBox_2.setValue(1)
        
        
        
        

    #masters   >>>   Add_Supplier  
    def do_this5(self):
        self.do_this23()
        self.menubar.setEnabled(False)
        self.z=0
        self.label_49.setText(QtCore.QCoreApplication.translate("OtherWindow", "Supplier details"))
        self.stackedWidget.setCurrentIndex(0)

    #Products   >>>   Modify   >>>   Supplier  
    def do_this6(self):
        self.y=0
        self.menubar.setEnabled(False)
        
        self.comboBox_5.clear()
        cus.execute("SELECT * FROM PRODUCT WHERE type='Supplier'")
        GOOD=cus.fetchall()
        
        for i in GOOD:
            self.comboBox_5.addItem(i[2])
            
        print(GOOD)
        self.lineEdit_28.clear()
        self.comboBox_5.setCurrentIndex(-1)
        self.comboBox_7.setCurrentIndex(-1)
        
        
        
        
        self.groupBox_3.setTitle(QtCore.QCoreApplication.translate("OtherWindow", "Supplier products"))
        self.stackedWidget.setCurrentIndex(3)


    #Products   >>>   Modify   >>>   Customer  
    def do_this7(self):
        self.y=1
        self.menubar.setEnabled(False)
        
        self.comboBox_5.clear()
        cus.execute("SELECT * FROM PRODUCT WHERE type='Customer'")
        GOOD=cus.fetchall()
        
        for i in GOOD:
            self.comboBox_5.addItem(i[2])
            
        print(GOOD)
        self.lineEdit_28.clear()
        self.comboBox_5.setCurrentIndex(-1)
        self.comboBox_7.setCurrentIndex(-1)
        
        self.groupBox_3.setTitle(QtCore.QCoreApplication.translate("OtherWindow", "Customer products"))
        self.stackedWidget.setCurrentIndex(3)


    #Inventory   >>>   Debit
    def do_this8(self):
        self.b=0
        print("ab")
        self.menubar.setEnabled(False)
        self.comboBox_11.clear()
        self.comboBox_16.clear()
        self.lineEdit_34.clear()
        cus.execute("SELECT DISTINCT(name) FROM PURCHASE_VOUCHER")
        GOOD=cus.fetchall()
        print("bc")
        for i in GOOD:
            self.comboBox_11.addItem(i[0])
        self.comboBox_11.setCurrentIndex(-1)
        self.groupBox_5.setTitle(QtCore.QCoreApplication.translate("OtherWindow", "Debit"))
        print("cd")
        self.stackedWidget.setCurrentIndex(5)


    #Inventory   >>>   Credit
    def do_this9(self):
        print("good")
        self.b=1
        self.menubar.setEnabled(False)
        self.comboBox_11.clear()
        self.comboBox_16.clear()
        self.lineEdit_34.clear()
        cus.execute("SELECT DISTINCT(name) FROM SALES_VOUCHER")
        GOOD=cus.fetchall()
        
        for i in GOOD:
            self.comboBox_11.addItem(i[0])
        self.comboBox_11.setCurrentIndex(-1)
        self.groupBox_5.setTitle(QtCore.QCoreApplication.translate("OtherWindow", "Credit"))
        self.stackedWidget.setCurrentIndex(5)



    #Inventory   >>>   Receivables   >>>   Party
    def do_this10(self):
        self.i=1
        self.menubar.setEnabled(False)
        self.groupBox_6.setTitle(QtCore.QCoreApplication.translate("OtherWindow", "Receivable"))
        self.stackedWidget.setCurrentIndex(6)
        self.comboBox_12.clear()
        
        cus.execute("SELECT DISTINCT(name) FROM SALES_VOUCHER")
        GOOD=cus.fetchall()
        
        for i in GOOD:
            self.comboBox_12.addItem(i[0])
        self.comboBox_12.setCurrentIndex(-1)        
        
        

    #Inventory   >>>   Payables   >>>   Party
    def do_this11(self):
        self.i=0
        self.menubar.setEnabled(False)
        self.groupBox_6.setTitle(QtCore.QCoreApplication.translate("OtherWindow", "Payable"))
        self.stackedWidget.setCurrentIndex(6)
        self.comboBox_12.clear()
        
        cus.execute("SELECT DISTINCT(name) FROM PURCHASE_VOUCHER")
        GOOD=cus.fetchall()
        
        for i in GOOD:
            self.comboBox_12.addItem(i[0])
        self.comboBox_12.setCurrentIndex(-1)


    #Inventory   >>>   Receivables   >>>   All
    def do_this12(self):
        row=0
        self.menubar.setEnabled(False)
        self.groupBox_7.setTitle(QtCore.QCoreApplication.translate("OtherWindow", "All Receivable"))
        self.stackedWidget.setCurrentIndex(7)
        cus.execute("SELECT name,SUM(amount)-SUM(samount) AS A FROM SALES_VOUCHER GROUP BY name ORDER BY A DESC")
        GOOD=cus.fetchall()
        print(GOOD)
        for i in GOOD:
            self.tableWidget_3.insertRow(row)
            m=QtWidgets.QTableWidgetItem(i[0])                                     
            m.setTextAlignment(QtCore.Qt.AlignVCenter)
            self.tableWidget_3.setItem(row,0,m)
            m=QtWidgets.QTableWidgetItem(str(i[1]))
            m.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
            self.tableWidget_3.setItem(row,1,m)
            row=row+1
        
        


    #Inventory   >>>   Payables   >>>   All
    def do_this13(self):
        row=0
        self.menubar.setEnabled(False)
        self.groupBox_7.setTitle(QtCore.QCoreApplication.translate("OtherWindow", "All Payable"))
        self.stackedWidget.setCurrentIndex(7)
        cus.execute("SELECT name,SUM(amount)-SUM(samount) AS A FROM PURCHASE_VOUCHER GROUP BY name ORDER BY A DESC")
        GOOD=cus.fetchall()
        print(GOOD)
        for i in GOOD:
            self.tableWidget_3.insertRow(row)
            m=QtWidgets.QTableWidgetItem(i[0])                                     
            m.setTextAlignment(QtCore.Qt.AlignVCenter)
            self.tableWidget_3.setItem(row,0,m)
            m=QtWidgets.QTableWidgetItem(str(i[1]))
            m.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
            self.tableWidget_3.setItem(row,1,m)
            row=row+1


    #Masters   >>>   Modify   >>>   Supplier
    def do_this14(self):
        self.a=0
        self.menubar.setEnabled(False)
        self.comboBox_14.clear()        
        cus.execute("SELECT * FROM PARTY WHERE type='Supplier'")
        GOOD=cus.fetchall()
        
        for i in GOOD:
            self.comboBox_14.addItem(i[1])
        self.do_this25()
        self.groupBox_8.setTitle(QtCore.QCoreApplication.translate("OtherWindow", "Edit Supplier"))
        self.stackedWidget.setCurrentIndex(8)


    #Masters   >>>   Modify   >>>   Customer
    def do_this15(self):
        self.a=1
        self.menubar.setEnabled(False)
        self.comboBox_14.clear()
        cus.execute("SELECT * FROM PARTY WHERE type='Customer'")
        GOOD=cus.fetchall()
        
        for i in GOOD:
            self.comboBox_14.addItem(i[1])
        self.do_this25()
        self.groupBox_8.setTitle(QtCore.QCoreApplication.translate("OtherWindow", "Edit customer"))
        self.stackedWidget.setCurrentIndex(8)



    
    def do_this16(self):
        self.stackedWidget.setCurrentIndex(9)


    #Inventory  >>>   Summary
    def do_this17(self):
        a=[]
        self.stackedWidget.setCurrentIndex(10)
        x=datetime.datetime.today().strftime('%Y-%m-%d')
        b=x[0:4]
        c=x[5:7]
        b=int(b)
        c=int(c)
        print(b)
        print(c)
        print("Fine")
        cus.execute("SELECT SUM(amount) FROM SALES_VOUCHER WHERE YEAR(date)='%s' AND MONTH(date)='%s'"%(b,c))
        d=cus.fetchall()
        print("Ok")

        for i in d:
            e=str(i[0])
            self.label_106.setText(QtCore.QCoreApplication.translate("OtherWindow", e))


        cus.execute("SELECT SUM(amount) FROM SALES_VOUCHER WHERE YEAR(date)='%s'"%(b))
        d=cus.fetchall()

        for i in d:
            e=str(i[0])
            self.label_105.setText(QtCore.QCoreApplication.translate("OtherWindow", e))

        cus.execute("SELECT SUM(amount) FROM PURCHASE_VOUCHER WHERE YEAR(date)='%s' AND MONTH(date)='%s'"%(b,c))
        d=cus.fetchall()
        print("Ok")

        for i in d:
            e=str(i[0])
            self.label_107.setText(QtCore.QCoreApplication.translate("OtherWindow", e))


        cus.execute("SELECT SUM(amount) FROM PURCHASE_VOUCHER WHERE YEAR(date)='%s'"%(b))
        d=cus.fetchall()

        for i in d:
            e=str(i[0])
            self.label_108.setText(QtCore.QCoreApplication.translate("OtherWindow", e))

        

        
            
        
        a.append(x)
        print(x)
        print(a)
        print(b)
        print(c)


    #Click of ADD Button in product entry
    def do_this18(self):
        if self.lineEdit_25.text()=='':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Enter Product name")       
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif self.lineEdit_26.text()=='':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Enter HSN ")       
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_() 
        elif self.comboBox_8.currentText()=='':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Enter GST")       
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()           
        else:           
            print(self.lineEdit_25.text())
            print(self.lineEdit_26.text())
            print(self.comboBox_8.currentText())
            print(self.x)
            if self.x==1 :
                v1='Customer'
            
            else:
                v1='Supplier'        
            
            v2=self.lineEdit_25.text()
            v3=self.lineEdit_26.text()
            v4=int(self.comboBox_8.currentText())
    
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            if self.x==1 :
                msg.setText("Product %s Added to Customer successfully!"%v2)
                print("running")
            
            else:
                msg.setText("Supplier %s Added to Supplier successfully!"%v2)       
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            print("hi")
            
            cus.execute("INSERT INTO PRODUCT (type,name,HSN,GST) VALUES ('%s','%s','%s','%s')"%(v1,v2,v3,v4))
            mydb.commit()
            print("ho")
            self.lineEdit_25.clear()
            self.lineEdit_26.clear()
            self.comboBox_8.setCurrentIndex(-1)
            
        


    #To enable the menubar
    def do_this19(self):
        self.menubar.setEnabled(True)
        self.stackedWidget.setCurrentIndex(11)


    #Click of Name Dropdown in product modify
    def do_this20(self):
        self.combobox_5=int(self.comboBox_5.currentIndex())
        a=self.comboBox_5.currentText()
        if self.y==1:
            cus.execute("SELECT * FROM PRODUCT WHERE type='Customer' AND name='%s'"%a)
        else :
            cus.execute("SELECT * FROM PRODUCT WHERE type='Supplier' AND name='%s'"%a)
        b=cus.fetchall()
        for i in b:
            print(i[3])
            self.lineEdit_28.setText(i[3])            
            self.comboBox_7.setCurrentText(str(i[4]))



    #Click of Save changes Button in product modify
    def do_this21(self):
        a=self.lineEdit_28.displayText()
        b=int(self.comboBox_7.currentText())
        c=self.comboBox_5.currentText()
        
        cus.execute("UPDATE PRODUCT SET GST = '%s' WHERE name= '%s' "%(b,c))
        cus.execute("UPDATE PRODUCT SET HSN = '%s' WHERE name= '%s' "%(a,c))
        
        mydb.commit()

        print("It is fine")

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("%s Modified successfully!"%c)
        msg.setWindowTitle("Message")        
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

        self.lineEdit_28.clear()
        self.comboBox_5.setCurrentIndex(-1)
        self.comboBox_7.setCurrentIndex(-1)
        


    #Click of OK Button in insertion of customer or supplier
    def do_this22(self):
        if self.lineEdit.text()=='':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            if self.z==1:
                msg.setText("Enter Customer's name")
            else:
                msg.setText("Enter Supplier's name")       
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif self.lineEdit_2.text()=='':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            if self.z==1:
                msg.setText("Enter Customer's GSTIN")
            else:
                msg.setText("Enter Supplier's GSTIN")       
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif self.lineEdit_3.text()=='':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            if self.z==1:
                msg.setText("Enter Customer's Address 1")
            else:
                msg.setText("Enter Supplier's Address 1")       
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif self.lineEdit_6.text()=='':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            if self.z==1:
                msg.setText("Enter Customer's city")
            else:
                msg.setText("Enter Supplier's city")       
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif self.lineEdit_7.text()=='':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            if self.z==1:
                msg.setText("Enter Customer's Pincode")
            else:
                msg.setText("Enter Supplier's Pincode")       
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif self.comboBox.currentText()=='':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            if self.z==1:
                msg.setText("Enter Customer's State")
            else:
                msg.setText("Enter Supplier's State")       
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        else:
            a1=self.lineEdit.text()
            a2=self.lineEdit_2.text()
            a3=self.lineEdit_8.text()
            a4=self.lineEdit_3.text()
            a5=self.lineEdit_4.text()
            a6=self.lineEdit_5.text()
            a7=self.lineEdit_6.text()
            a8=self.lineEdit_7.text()
            a9=self.comboBox.currentText()
            print("Go")
            print("a5="+a5)
            print("a6="+a6)
            if a5=='':
                print("hi")
                if self.z==1:
                    cus.execute("INSERT INTO PARTY (type,name,GSTIN,phno,add1,city,pincode,state) VALUES('%s','%s','%s','%s','%s','%s','%s','%s')"%('Customer',a1,a2,a3,a4,a7,a8,a9))
                else :
                    cus.execute("INSERT INTO PARTY (type,name,GSTIN,phno,add1,city,pincode,state) VALUES('%s','%s','%s','%s','%s','%s','%s','%s')"%('Supplier',a1,a2,a3,a4,a7,a8,a9))
                mydb.commit()
                print("bye")
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                if self.z==1:
                    msg.setText("Customer added successfully")
                else:
                    msg.setText("Supplier added successfully")       
                msg.setWindowTitle("Message")        
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec_()
                
            elif a6=='':
                print(self.z)
                print(a1)
                print(a2)
                print(a3)
                print(a4)
                print(a5)
                print(a6)
                print(a7)
                print(a8)
                print(a9)
                if self.z==1:
                    print("good")
                    cus.execute("INSERT INTO PARTY (type,name,GSTIN,phno,add1,add2,city,pincode,state) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%('Customer',a1,a2,a3,a4,a5,a7,a8,a9))
                    print("very good")
                else :
                    cus.execute("INSERT INTO PARTY (type,name,GSTIN,phno,add1,add2,city,pincode,state) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%('Supplier',a1,a2,a3,a4,a5,a7,a8,a9))
                mydb.commit()
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                if self.z==1:
                    msg.setText("Customer added successfully")
                else:
                    msg.setText("Supplies added successfully")       
                msg.setWindowTitle("Message")        
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec_()

            else:
                if self.z==1:
                    cus.execute("INSERT INTO PARTY (type,name,GSTIN,phno,add1,add2,add3,city,pincode,state) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%('Customer',a1,a2,a3,a4,a5,a6,a7,a8,a9))
                else :
                    cus.execute("INSERT INTO PARTY (type,name,GSTIN,phno,add1,add2,add3,city,pincode,state) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%('Supplier',a1,a2,a3,a4,a5,a6,a7,a8,a9))
                mydb.commit()
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                if self.z==1:
                    msg.setText("Customer added successfully")
                else:
                    msg.setText("Supplies added successfully")       
                msg.setWindowTitle("Message")        
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec_()

            




            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_8.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.lineEdit_7.clear()
            self.comboBox.setCurrentIndex(-1)

            
            
            """ cus.execute("INSERT INTO PARTY (type,name,GSTIN,phno,add1,add2,add3,city,pincode,state)")"""


            """cus.execute("INSERT INTO PRODUCT (type,name,HSN,GST) VALUES('%s','%s','%s','%s')"%(v1,v2,v3,v4))    """
            print("Done with it")

        

    #Click of RESET Button in supplier and customer insertion
    def do_this23(self):
        self.lineEdit_2.clear()
        self.lineEdit.clear()
        self.lineEdit_4.clear()
        self.lineEdit_3.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()        
        self.comboBox.setCurrentIndex(-1)

    #Click of Name Dropdown in master modify for customer and supplier
    def do_this24(self):
        a=self.comboBox_14.currentText()
        if self.a==1:
            cus.execute("SELECT * FROM PARTY WHERE type='Customer' AND name='%s'"%a)
        else :
            cus.execute("SELECT * FROM PARTY WHERE type='Supplier' AND name='%s'"%a)
        b=cus.fetchall()

        for i in b:
            self.lineEdit_39.setText(i[2])
            self.lineEdit_40.setText(i[3])
            self.lineEdit_38.setText(i[4])
            self.lineEdit_41.setText(i[5])
            self.lineEdit_35.setText(i[6])
            self.lineEdit_36.setText(i[7])
            self.lineEdit_42.setText(i[8])
            self.comboBox_13.setCurrentText(i[9])
        
    #To clear everything in master modify menu for supplier and customer
    def do_this25(self):
        self.comboBox_14.setCurrentIndex(-1)
        self.lineEdit_39.clear()
        self.lineEdit_40.clear()
        self.lineEdit_38.clear()
        self.lineEdit_41.clear()
        self.lineEdit_35.clear()
        self.lineEdit_36.clear()
        self.lineEdit_42.clear()
        self.comboBox_13.setCurrentIndex(-1)


    #Reset everything except Name and GSTIN in master modify 
    def do_this26(self):
        self.lineEdit_40.clear()
        self.lineEdit_38.clear()
        self.lineEdit_41.clear()
        self.lineEdit_35.clear()
        self.lineEdit_36.clear()
        self.lineEdit_42.clear()
        self.comboBox_13.setCurrentIndex(-1)

    #Click of OK in master modify
    def do_this27(self):        
        a=self.comboBox_14.currentText()
        b=self.lineEdit_39.displayText()
        c=self.lineEdit_40.displayText()
        d=self.lineEdit_38.displayText()
        e=self.lineEdit_41.displayText()
        f=self.lineEdit_35.displayText()
        g=self.lineEdit_36.displayText()
        h=self.lineEdit_42.displayText()
        i=self.comboBox_13.currentText()

        
        if d=='':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Enter Address1")
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif g=='':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Enter City")
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif h=='':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Enter Pincode")
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif i=='':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Enter State")
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        else:
            cus.execute("UPDATE PARTY SET phno = '%s' WHERE name= '%s' "%(c,a))
            cus.execute("UPDATE PARTY SET add1 = '%s' WHERE name= '%s' "%(d,a))
            cus.execute("UPDATE PARTY SET add2 = '%s' WHERE name= '%s' "%(e,a))
            cus.execute("UPDATE PARTY SET add3 = '%s' WHERE name= '%s' "%(f,a))
            cus.execute("UPDATE PARTY SET city = '%s' WHERE name= '%s' "%(g,a))
            cus.execute("UPDATE PARTY SET pincode = '%s' WHERE name= '%s' "%(h,a))
            cus.execute("UPDATE PARTY SET state = '%s' WHERE name= '%s' "%(i,a))
        
            mydb.commit()
            
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("%s Modified successfully!"%a)
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()

            self.do_this25()



    #Click of Add Button in Debit and Credit
    def do_this28(self):
        global comp_no
        a=comp_no
        print(a)
        b=self.comboBox_16.currentText()
        print(b)
        f=self.comboBox_11.currentText()
        print(f)
        print("Yo")
        if self.b==1:
            cus.execute("SELECT samount FROM SALES_VOUCHER WHERE c_no='%s' AND v_no='%s'"%(a,b))
        else:
            cus.execute("SELECT samount FROM PURCHASE_VOUCHER WHERE c_no='%s' AND v_no='%s'"%(a,b))
        x=cus.fetchall()
        d=float(self.lineEdit_34.displayText())
        for i in x:
            print(i[0])
            c=float(i[0])
        e=d+c
        d=str(d)
        print("good")
        if self.b==1:
            cus.execute("UPDATE SALES_VOUCHER SET samount = '%s' WHERE c_no='%s' AND v_no='%s' "%(e,a,b))
        else:
            cus.execute("UPDATE PURCHASE_VOUCHER SET samount = '%s' WHERE c_no='%s' AND v_no='%s' "%(e,a,b))

        mydb.commit()
        print("What")
        b=str(b)
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        if self.b==1:
            msg.setText("Rs.%s for voucher no %s credited from %s successfully!"%(d,b,f))
        else:
            msg.setText("Rs.%s for voucher no %s debited to %s successfully!"%(d,b,f))
        msg.setWindowTitle("Message")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

        self.comboBox_11.setCurrentIndex(-1)
        self.comboBox_16.setCurrentIndex(-1)
        self.lineEdit_34.clear()



    
    #Click of a cell in Sales Table    
    def do_this29(self,row,column):
        if column==1:
            
            self.c=QtWidgets.QComboBox()
            self.tableWidget.setCellWidget(row,column,self.c)
            cus.execute("SELECT * FROM PRODUCT WHERE type='Customer' ")
            b=cus.fetchall()
            for i in b:
                self.tableWidget.cellWidget(row,column).addItem(i[2])
            self.tableWidget.cellWidget(row,column).setCurrentIndex(-1)
            self.tableWidget.cellWidget(row,column).showPopup()
            self.row=row
            self.column=column
            print(self.row)
            print(self.column)
            self.c.currentTextChanged.connect(self.do_this30)
            x=self.tableWidget.rowCount()
            
            
            

        elif column==3:
            self.d=QtWidgets.QComboBox()
            self.tableWidget.setCellWidget(row,column,self.d)
            self.tableWidget.cellWidget(row,column).addItems(['TONS','BAGS'])
            self.tableWidget.cellWidget(row,column).setCurrentIndex(-1)
            self.tableWidget.cellWidget(row,column).showPopup()
            self.row1=row
            self.column1=column
            print("hi")
            self.d.currentTextChanged.connect(self.do_this31)        
        

    #Selection from Dropdown of products in Sales table
    def do_this30(self):
        
        d=self.c.currentText()
        self.tableWidget.removeCellWidget(self.row,self.column)
        self.tableWidget.setItem(self.row,self.column,QtWidgets.QTableWidgetItem(d))
        self.tableWidget.clearFocus()


    #Selection from Dropdown of products in Sales table
    def do_this31(self):
       
        a=self.d.currentText()
        
        self.tableWidget.removeCellWidget(self.row1,self.column1)
        self.tableWidget.setItem(self.row1,self.column1,QtWidgets.QTableWidgetItem(a))


    
    def do_this32(self):
        self.tableWidget.removeCellWidget(self.row,self.column)


    #Selection of PARTY in Sales
    def do_this33(self):
        
        global state
        a=self.comboBox_3.currentText()
        print("yo")
        cus.execute("SELECT * FROM PARTY WHERE type='Customer' AND name='%s'"%a)
        b=cus.fetchall()
        for i in b:
            self.lineEdit_17.setText(i[2])
            self.lineEdit_20.setText(i[4])
            self.lineEdit_22.setText(i[5])
            self.lineEdit_21.setText(i[6])
            self.lineEdit_23.setText(i[7])
            self.lineEdit_24.setText(i[8])
            self.comboBox_4.setCurrentText(i[9])
            if state==i[9]:
                self.radioButton.setChecked(True)
            else:
                self.radioButton_2.setChecked(True)
                
                

        
        self.lineEdit_20.setEnabled(False)
        self.lineEdit_22.setEnabled(False)
        self.lineEdit_21.setEnabled(False)
        self.lineEdit_23.setEnabled(False)
        self.lineEdit_24.setEnabled(False)
        self.comboBox_4.setEnabled(False)


    #Selection of checkBox in Copy Billing Address
    def do_this34(self):
        if self.checkBox.isChecked()==True:
            a=self.lineEdit_20.displayText()
            self.lineEdit_27.setText(a)
            a=self.lineEdit_22.displayText()
            self.lineEdit_30.setText(a)
            a=self.lineEdit_21.displayText()
            self.lineEdit_31.setText(a)
            a=self.lineEdit_23.displayText()
            self.lineEdit_32.setText(a)
            a=self.lineEdit_24.displayText()
            self.lineEdit_33.setText(a)
            a=self.comboBox_4.currentText()
            self.comboBox_10.setCurrentText(a)


    #A cell is changed in Sales table
    def do_this35(self,row,column):
        a=self.tableWidget.item(row,1)
        b=self.tableWidget.item(row,3)
        c=self.tableWidget.item(row,4)
        d=self.tableWidget.item(row,5)
        l=self.tableWidget.item(row,7)
        if column==1 or column==3 or column==4 or column==5 :
            if a:
                if a.text():
                    e=a.text()
                    cus.execute("SELECT * FROM PRODUCT WHERE type='Customer' AND name='%s'"%e)
                    f=cus.fetchall()
                    print(f)
                    for i in f:
                        x=i[3]
                        self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(x))
                    if b:
                        if b.text():
                            if c:
                                if c.text():
                                    if d:
                                        if d.text():
                                            if  not l:
                                                self.tableWidget.insertRow(row+1)

                                            g=float(c.text())
                                            h=float(d.text())
                                            i=str(g*h*1.0)
                                            m=QtWidgets.QTableWidgetItem(i)                                     
                                            m.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
                                            self.tableWidget.setItem(row,6,m)
                                            
                                            for l in f:
                                                x=l[4]
                                            x=int(x)
                                            j=str(x*g*h/100)
                                            m=QtWidgets.QTableWidgetItem(j)                                     
                                            m.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
                                            self.tableWidget.setItem(row,7,m)
                                            k=str(float(i)+float(j))
                                            m=QtWidgets.QTableWidgetItem(k)
                                            m.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
                                            self.tableWidget.setItem(row,8,m)
                                            
                                            self.e.setCheckState(QtCore.Qt.Checked)
                                            self.e=QtWidgets.QCheckBox()
                                            self.tableWidget.setCellWidget(row+1,0,self.e)
                                            self.e.setEnabled(False)
                                            self.rowCount=self.rowCount+1

                                            n=self.label_38.text()

                                            if n=='':
                                                n=i
                                            else :
                                                n=str(float(n)+float(i))
                                            self.label_38.setText(QtCore.QCoreApplication.translate("OtherWindow", n))

                                            n=self.label_39.text()

                                            if n=='':
                                                n=j
                                            else :
                                                n=str(float(n)+float(j))
                                            self.label_39.setText(QtCore.QCoreApplication.translate("OtherWindow", n))

                                            n=self.label_40.text()

                                            if n=='':
                                                n=k
                                            else :
                                                n=str(float(n)+float(k))
                                            self.label_40.setText(QtCore.QCoreApplication.translate("OtherWindow", n))
                                            
                                            
    #Double clicked a table widget to remove the row
    def do_this36(self,row,column):
        
        print(self.rowCount)
        if row!=(self.rowCount-1):
            n=self.label_38.text()
            i=self.tableWidget.item(row,6).text()
            if n=='':
                n=i
            else :
                print(n)
                n=str(float(n)-float(i))
                print("hi")
            self.label_38.setText(QtCore.QCoreApplication.translate("OtherWindow", n))

            n=self.label_39.text()
            j=self.tableWidget.item(row,7).text()
            print("good")
            if n=='':
                n=j
            else :
                print(n)
                n=str(float(n)-float(j))
            self.label_39.setText(QtCore.QCoreApplication.translate("OtherWindow", n))
            print("Great")

            n=self.label_40.text()
            
            k=self.tableWidget.item(row,8).text()

            if n=='':
                n=k
            else :
                print(n)
                n=str(float(n)-float(k))
            print("Well done")
            self.label_40.setText(QtCore.QCoreApplication.translate("OtherWindow", n))
            
            self.tableWidget.removeRow(row)
            self.rowCount=self.rowCount-1



    #Disable all widgets and set the number of rows to 1 in Sales 
    def do_this37(self):
        self.do_this40()
        self.tabWidget.setTabEnabled(0,False)
        self.tabWidget.setTabEnabled(1,False)
        self.tabWidget.setTabEnabled(2,False)
        self.dateEdit.setEnabled(False)
        #self.comboBox.setEnabled(False)
        self.comboBox_3.setEnabled(False)
        self.lineEdit_17.setEnabled(False)
        self.pushButton.setEnabled(True)
        self.pushButton_18.setEnabled(False)
        self.pushButton_16.setEnabled(False)
        self.pushButton_13.setEnabled(False)
        self.pushButton_15.setEnabled(False)
        self.tabWidget.setCurrentIndex(0)
        self.tableWidget.clearContents
        self.radioButton.setChecked(True)
        self.radioButton_2.setChecked(False)
        self.spinBox.setEnabled(True)
        if self.rowCount>1:
            for i in range(1,self.rowCount):
                self.tableWidget.removeRow(0)
            self.rowCount=1
        self.tableWidget.takeItem(0,1)
        self.tableWidget.takeItem(0,2)
        self.tableWidget.takeItem(0,3)
        self.tableWidget.takeItem(0,4)
        self.tableWidget.takeItem(0,5)
        self.tableWidget.takeItem(0,6)
        self.tableWidget.takeItem(0,7)
        self.tableWidget.takeItem(0,8)


    #Enable the widgets in Sales
    def do_this38(self):
        self.do_this40()
        self.tabWidget.setTabEnabled(0,True)
        self.tabWidget.setTabEnabled(1,True)
        self.tabWidget.setTabEnabled(2,True)
        self.dateEdit.setEnabled(True)
        self.comboBox.setEnabled(True)
        self.comboBox_3.setEnabled(True)
        self.lineEdit_17.setEnabled(False)
        self.pushButton.setEnabled(False)
        self.pushButton_18.setEnabled(True)
        self.pushButton_16.setEnabled(True)
        self.pushButton_13.setEnabled(True)
        self.pushButton_15.setEnabled(True)
        self.spinBox.setEnabled(False)
        self.tabWidget.setCurrentIndex(0)

    #Click of Save Button in Sales
    def do_this39(self):
        global comp_no
        global state
        a1=comp_no
        a2=self.spinBox.value()
        a2=int(a2)
        a3=self.comboBox_3.currentText()
        a4=self.dateEdit.date().toPyDate()
        a5=self.lineEdit_18.displayText()
        a6=self.lineEdit_19.displayText()
        a7=self.lineEdit_20.displayText()
        a8=self.lineEdit_22.displayText()
        
        a9=self.lineEdit_21.displayText()
        a10=self.lineEdit_23.displayText()
        a11=self.lineEdit_24.displayText()
        a12=self.comboBox_4.currentText()
        a13=self.lineEdit_27.displayText()
        
        a14=self.lineEdit_30.displayText()
        a15=self.lineEdit_31.displayText()
        a16=self.lineEdit_32.displayText()
        a17=self.lineEdit_33.displayText()
        a18=self.comboBox_10.currentText()
        a19=self.label_40.text()
        
        
        if a19!='':
            a19=int(float(a19))
        if state==a12:
            print("Within  state")
        else:
            print("Other state")

        print("Amount",a19)

        print("Hi")

        
        if a3=='':
            
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Enter party name")
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif a19=='':
            
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Enter Products")
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()

        else:
            
            cus.execute("SELECT * FROM SALES_VOUCHER WHERE c_no='%s' AND v_no='%s'"%(a1,a2))
            b=cus.fetchall()
            print(b)
            if len(b)==0:
                print(self.rowCount)
                
                cus.execute("INSERT INTO SALES_VOUCHER (c_no,name,v_no,date,amount) VALUES('%s','%s','%s','%s','%s')"%(a1,a3,a2,a4,a19))
                mydb.commit()
                print("perfect")
                cus.execute("SELECT sno FROM SALES_VOUCHER WHERE c_no='%s' AND v_no='%s'"%(a1,a2))
                c=cus.fetchall()
                for i in c:
                    b=i[0]
                
                for i in range(1,self.rowCount):
                    b1=i
                    b2=self.tableWidget.item(i-1,1).text()
                    b3=self.tableWidget.item(i-1,2).text()
                    b4=self.tableWidget.item(i-1,3).text()
                    b5=self.tableWidget.item(i-1,4).text()
                    b6=self.tableWidget.item(i-1,5).text()
                    b7=self.tableWidget.item(i-1,6).text()
                    b8=self.tableWidget.item(i-1,7).text()
                    b9=self.tableWidget.item(i-1,8).text()
                    b5=float(b5)
                    b6=float(b6)
                    b7=float(b7)
                    b8=float(b8)
                    b9=float(b9)
                    

                    cus.execute("INSERT INTO SALES_PRODUCT (pno,sl_no,name,HSN_code,unit,qty,rate,gross,tax,net) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(b,b1,b2,b3,b4,b5,b6,b7,b8,b9))
                    print("It is fine")
            else:
                print(self.rowCount)
                cus.execute("SELECT sno FROM SALES_VOUCHER WHERE c_no='%s' AND v_no='%s'"%(a1,a2))
                c=cus.fetchall()
                for i in c:
                    b=i[0]
                cus.execute("DELETE FROM SALES_PRODUCT WHERE pno='%s'"%b)
                mydb.commit()
                
                for i in range(1,self.rowCount):
                    b1=i
                    b2=self.tableWidget.item(i-1,1).text()
                    b3=self.tableWidget.item(i-1,2).text()
                    b4=self.tableWidget.item(i-1,3).text()
                    b5=self.tableWidget.item(i-1,4).text()
                    b6=self.tableWidget.item(i-1,5).text()
                    b7=self.tableWidget.item(i-1,6).text()
                    b8=self.tableWidget.item(i-1,7).text()
                    b9=self.tableWidget.item(i-1,8).text()
                    b5=float(b5)
                    b6=float(b6)
                    b7=float(b7)
                    b8=float(b8)
                    b9=float(b9)
                    

                    cus.execute("INSERT INTO SALES_PRODUCT (pno,sl_no,name,HSN_code,unit,qty,rate,gross,tax,net) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(b,b1,b2,b3,b4,b5,b6,b7,b8,b9))
                    
                
                cus.execute("UPDATE SALES_VOUCHER SET name = '%s' WHERE c_no = '%s' AND v_no = '%s'"%(a3,a1,a2))
                cus.execute("UPDATE SALES_VOUCHER SET date = '%s' WHERE c_no = '%s' AND v_no = '%s'"%(a4,a1,a2))
                cus.execute("UPDATE SALES_VOUCHER SET amount = '%s' WHERE c_no = '%s' AND v_no = '%s'"%(a19,a1,a2))
                
            
            if a5!='':
                print("hi")
                cus.execute("UPDATE SALES_VOUCHER SET vehicle = '%s' WHERE c_no = '%s' AND v_no = '%s'"%(a5,a1,a2))

            if a6!='':
                 cus.execute("UPDATE SALES_VOUCHER SET doc = '%s' WHERE c_no = '%s' AND v_no = '%s'"%(a6,a1,a2))

            if a7!='':
                 cus.execute("UPDATE SALES_VOUCHER SET badd1 = '%s' WHERE c_no = '%s' AND v_no = '%s'"%(a7,a1,a2))

            if a8!='':
                 cus.execute("UPDATE SALES_VOUCHER SET badd2 = '%s' WHERE c_no = '%s' AND v_no = '%s'"%(a8,a1,a2))
            
            if a9!='':
                 cus.execute("UPDATE SALES_VOUCHER SET badd3 = '%s' WHERE c_no = '%s' AND v_no = '%s'"%(a9,a1,a2))

            if a10!='':
                 cus.execute("UPDATE SALES_VOUCHER SET bcity = '%s' WHERE c_no = '%s' AND v_no = '%s'"%(a10,a1,a2))

            if a11!='':
                 cus.execute("UPDATE SALES_VOUCHER SET bpincode = '%s' WHERE c_no = '%s' AND v_no = '%s'"%(a11,a1,a2))

            if a12!='':
                cus.execute("UPDATE SALES_VOUCHER SET bstate = '%s' WHERE c_no = '%s' AND v_no = '%s'"%(a12,a1,a2))
                if state==a12:
                    cus.execute("UPDATE SALES_VOUCHER SET state = '%s' WHERE c_no = '%s' AND v_no = '%s'"%(1,a1,a2))
                else:
                    cus.execute("UPDATE SALES_VOUCHER SET state = '%s' WHERE c_no = '%s' AND v_no = '%s'"%(0,a1,a2))
            
            if a13!='':
                cus.execute("UPDATE SALES_VOUCHER SET sadd1 = '%s' WHERE c_no = '%s' AND v_no = '%s'"%(a13,a1,a2))

            if a14!='':
                cus.execute("UPDATE SALES_VOUCHER SET sadd2 = '%s' WHERE c_no = '%s' AND v_no = '%s'"%(a14,a1,a2))

            if a15!='':
                cus.execute("UPDATE SALES_VOUCHER SET sadd3 = '%s' WHERE c_no = '%s' AND v_no = '%s'"%(a15,a1,a2))

            if a16!='':
                cus.execute("UPDATE SALES_VOUCHER SET scity = '%s' WHERE c_no = '%s' AND v_no = '%s'"%(a16,a1,a2))
            
            if a17!='':
                cus.execute("UPDATE SALES_VOUCHER SET spincode = '%s' WHERE c_no = '%s' AND v_no = '%s'"%(a17,a1,a2))

            if a18!='':
                cus.execute("UPDATE SALES_VOUCHER SET sstate = '%s' WHERE c_no = '%s' AND v_no = '%s'"%(a18,a1,a2))

            mydb.commit()
            self.spinBox.setValue(self.spinBox.value()+1)
            self.do_this37()


    #Clear content of all widgets in Sales
    def do_this40(self):
        self.comboBox_3.setCurrentIndex(-1)
        
        self.lineEdit_18.clear()
        self.lineEdit_19.clear()
        self.lineEdit_20.clear()
        self.lineEdit_22.clear()
        self.lineEdit_21.clear()
        self.lineEdit_23.clear()
        self.lineEdit_24.clear()
        self.comboBox_4.setCurrentIndex(-1)
        self.lineEdit_27.clear()
        self.lineEdit_30.clear()
        self.lineEdit_31.clear()
        self.lineEdit_32.clear()
        self.lineEdit_33.clear()
        self.comboBox_10.setCurrentIndex(-1)
        self.lineEdit_17.clear()
        self.label_38.clear()
        self.label_39.clear()
        self.label_40.clear()
        self.checkBox.setCheckState(QtCore.Qt.Unchecked)


    #Click of Edit Button in Sales
    def do_this41(self):
        global comp_no
        self.do_this38()
        x=self.spinBox.value()
        cus.execute("SELECT * FROM SALES_VOUCHER WHERE c_no='%s' AND v_no='%s'"%(comp_no,x))
        b=cus.fetchall()
        self.dateEdit.setDate(datetime.date.today())
        print("Edit 1")
        if len(b)!=0:
            for i in b:
                print("Date")
                print(datetime.date.today())
                c=i[1]
                self.comboBox_3.setCurrentText(i[3])

                
                cus.execute("SELECT * FROM PARTY WHERE type='Customer' AND name='%s'"%i[3])
                d=cus.fetchall()
                for j in d:
                    self.lineEdit_17.setText(j[2])
                
                self.dateEdit.setDate(i[4])
                self.lineEdit_18.setText(i[5])
                self.lineEdit_19.setText(i[6])
                
                self.lineEdit_20.setText(i[7])
                self.lineEdit_22.setText(i[8])
                self.lineEdit_21.setText(i[9])
                self.lineEdit_23.setText(i[10])
                self.lineEdit_24.setText(i[11])
                
                self.comboBox_4.setCurrentText(i[12])
                self.lineEdit_27.setText(i[13])
                
                self.lineEdit_30.setText(i[14])
                self.lineEdit_31.setText(i[15])
                
                self.lineEdit_32.setText(i[16])
                self.lineEdit_33.setText(i[17])
                print(i[18])
                
                if i[18]!=None:
                    self.comboBox_10.setCurrentText(i[18])

                if i[21]==0:
                    self.radioButton.setChecked(False)
                    
                else:
                    print(i[21])                    
                    self.radioButton.setChecked(True)

                print("Edit 2")
                
            
            cus.execute("SELECT * FROM SALES_PRODUCT WHERE pno='%s'"%(c))
            b=cus.fetchall()
            
            c=0
            d=0
            e=0
            f=0
            print("Edit 3")
            for i in b:
                
                m=QtWidgets.QTableWidgetItem(i[3])
                self.tableWidget.setItem(c,1,m)
                m=QtWidgets.QTableWidgetItem(i[4])
                self.tableWidget.setItem(c,2,m)
                m=QtWidgets.QTableWidgetItem(i[5])
                self.tableWidget.setItem(c,3,m)
                m=QtWidgets.QTableWidgetItem(str(i[6]))
                self.tableWidget.setItem(c,4,m)
                m=QtWidgets.QTableWidgetItem(str(i[7]))
                self.tableWidget.setItem(c,5,m)
                               
                m=QtWidgets.QTableWidgetItem(str(i[8]))
                m.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
                self.tableWidget.setItem(c,6,m)
                m=QtWidgets.QTableWidgetItem(str(i[9]))                                     
                m.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
                self.tableWidget.setItem(c,7,m)
                m=QtWidgets.QTableWidgetItem(str(i[10]))                                     
                m.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
                self.tableWidget.setItem(c,8,m)
                print("Edit 4")
                if c==0:
                    d=i[8]
                    e=i[9]
                    f=i[10]
                else:
                    d=d+i[8]
                    e=e+i[9]
                    f=f+i[10]               
                c=c+1
                print("Edit 5")
            n=str(d)
            self.label_38.setText(QtCore.QCoreApplication.translate("OtherWindow", n))
            n=str(e)
            self.label_39.setText(QtCore.QCoreApplication.translate("OtherWindow", n))
            n=str(f)
            self.label_40.setText(QtCore.QCoreApplication.translate("OtherWindow", n))
            print("Edit 6")

        self.lineEdit_20.setEnabled(False)
        self.lineEdit_22.setEnabled(False)
        self.lineEdit_21.setEnabled(False)
        self.lineEdit_23.setEnabled(False)
        self.lineEdit_24.setEnabled(False)
        self.comboBox_4.setEnabled(False)
        print("Edit 6")        



    #Click of Undo  Button in Sales
    def do_this42(self):
        
        self.do_this37()
        self.spinBox.setValue(self.spinBox.value()-1)



    #Click of Delete Button in Sales
    def do_this43(self):
        global comp_no
        
        
        
        a1=comp_no
        a2=self.spinBox.value()
        a2=int(a2)
        print(a2)
        cus.execute("SELECT sno FROM SALES_VOUCHER WHERE c_no='%s' AND v_no='%s'"%(a1,a2))
        c=cus.fetchall()
        for i in c:
            b=i[0]
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Do you want to delete this voucher")
        msg.setWindowTitle("Message")        
        msg.setStandardButtons(QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        retval=msg.exec_()
        print("value",retval)
        
        if retval==16384:
            cus.execute("DELETE FROM SALES_PRODUCT WHERE pno='%s'"%b)
            cus.execute("DELETE FROM SALES_VOUCHER WHERE sno='%s'"%b)
            mydb.commit()
            self.do_this42()

    #Click of Close Button in Sales
    def do_this44(self):
        self.do_this19()
        self.do_this37()

    #Click of a Party Drop down Credit/Debit
    def do_this45(self):
        global comp_no
        self.comboBox_16.clear()
        a1=comp_no
        
        a2=self.comboBox_11.currentText()
        if self.b==1:
            cus.execute("SELECT v_no FROM SALES_VOUCHER WHERE c_no='%s' and name='%s' ORDER By v_no" %(a1,a2))
        else:
            cus.execute("SELECT v_no FROM PURCHASE_VOUCHER WHERE c_no='%s' and name='%s' ORDER By v_no" %(a1,a2))
        c=cus.fetchall()
        print(c)
        for i in c:
            print("hi")
            self.comboBox_16.addItem(str(i[0]))

        self.comboBox_16.setCurrentIndex(-1)


    def do_this46(self,row,column):
        if column==1:
            
            self.f=QtWidgets.QComboBox()
            self.tableWidget_2.setCellWidget(row,column,self.f)
            cus.execute("SELECT * FROM PRODUCT WHERE type='Supplier' ")
            b=cus.fetchall()
            for i in b:
                self.tableWidget_2.cellWidget(row,column).addItem(i[2])
            self.tableWidget_2.cellWidget(row,column).setCurrentIndex(-1)
            self.tableWidget_2.cellWidget(row,column).showPopup()
            self.row2=row
            self.column2=column
            print(self.row)
            print(self.column)
            self.f.currentTextChanged.connect(self.do_this47)
            x=self.tableWidget_2.rowCount()
            
            
            

        elif column==3:
            self.g=QtWidgets.QComboBox()
            self.tableWidget_2.setCellWidget(row,column,self.g)
            self.tableWidget_2.cellWidget(row,column).addItems(['TONS','BAGS'])
            self.tableWidget_2.cellWidget(row,column).setCurrentIndex(-1)
            self.tableWidget_2.cellWidget(row,column).showPopup()
            self.row3=row
            self.column3=column
            print("hi")
            self.g.currentTextChanged.connect(self.do_this48)


    #Selection from Dropdown of products in Purchase table
    def do_this47(self):
        
        d=self.f.currentText()
        self.tableWidget_2.removeCellWidget(self.row2,self.column2)
        self.tableWidget_2.setItem(self.row2,self.column2,QtWidgets.QTableWidgetItem(d))
        self.tableWidget_2.clearFocus()


    #Selection from Dropdown of products in Purchase table
    def do_this48(self):
       
        a=self.g.currentText()
        
        self.tableWidget_2.removeCellWidget(self.row3,self.column3)
        self.tableWidget_2.setItem(self.row3,self.column3,QtWidgets.QTableWidgetItem(a))



    #A cell is changed in Sales table
    def do_this49(self,row,column):
        a=self.tableWidget_2.item(row,1)
        b=self.tableWidget_2.item(row,3)
        c=self.tableWidget_2.item(row,4)
        d=self.tableWidget_2.item(row,5)
        l=self.tableWidget_2.item(row,7)
        if column==1 or column==3 or column==4 or column==5 :
            if a:
                if a.text():
                    e=a.text()
                    print("This is"+e)
                    cus.execute("SELECT * FROM PRODUCT WHERE type='Supplier' AND name='%s'"%e)
                    f=cus.fetchall()
                    print(f)
                    for i in f:
                        x=i[3]
                        self.tableWidget_2.setItem(row,2,QtWidgets.QTableWidgetItem(x))
                    if b:
                        if b.text():
                            if c:
                                if c.text():
                                    if d:
                                        if d.text():
                                            if  not l:
                                                self.tableWidget_2.insertRow(row+1)

                                            g=float(c.text())
                                            h=float(d.text())
                                            i=str(g*h*1.0)
                                            m=QtWidgets.QTableWidgetItem(i)                                     
                                            m.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
                                            self.tableWidget_2.setItem(row,6,m)
                                            
                                            for l in f:
                                                x=l[4]
                                            x=int(x)
                                            j=str(x*g*h/100)
                                            m=QtWidgets.QTableWidgetItem(j)                                     
                                            m.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
                                            self.tableWidget_2.setItem(row,7,m)
                                            k=str(float(i)+float(j))
                                            m=QtWidgets.QTableWidgetItem(k)
                                            m.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
                                            self.tableWidget_2.setItem(row,8,m)
                                            
                                            self.h.setCheckState(QtCore.Qt.Checked)
                                            self.h=QtWidgets.QCheckBox()
                                            self.tableWidget_2.setCellWidget(row+1,0,self.h)
                                            self.h.setEnabled(False)
                                            self.rowCount2=self.rowCount2+1

                                            n=self.label_11.text()

                                            if n=='':
                                                n=i
                                            else :
                                                n=str(float(n)+float(i))
                                            self.label_11.setText(QtCore.QCoreApplication.translate("OtherWindow", n))

                                            n=self.label_12.text()

                                            if n=='':
                                                n=j
                                            else :
                                                n=str(float(n)+float(j))
                                            self.label_12.setText(QtCore.QCoreApplication.translate("OtherWindow", n))

                                            n=self.label_13.text()

                                            if n=='':
                                                n=k
                                            else :
                                                n=str(float(n)+float(k))
                                            self.label_13.setText(QtCore.QCoreApplication.translate("OtherWindow", n))



    def do_this50(self):
        self.spinBox_2.setEnabled(True)
        self.pushButton_7.setEnabled(True)
        self.dateEdit_2.setEnabled(False)
        self.comboBox_9.setEnabled(False)
        self.tableWidget_2.setEnabled(False)
        self.pushButton_23.setEnabled(False)
        self.pushButton_22.setEnabled(False)
        self.pushButton_21.setEnabled(False)
        self.label_11.setText(QtCore.QCoreApplication.translate("OtherWindow", ""))
        self.label_12.setText(QtCore.QCoreApplication.translate("OtherWindow", ""))
        self.label_13.setText(QtCore.QCoreApplication.translate("OtherWindow", ""))
        self.comboBox_9.setCurrentIndex(-1)


    #Click of Edit Button in Purchase
    def do_this51(self):
        global comp_no
        self.do_this52()
        x=self.spinBox_2.value()
        cus.execute("SELECT * FROM PURCHASE_VOUCHER WHERE c_no='%s' AND v_no='%s'"%(comp_no,x))
        b=cus.fetchall()
        self.dateEdit_2.setDate(datetime.date.today())
        print("Edit 1")
        print(b)
        if len(b)!=0:
            for i in b:
                print("Date")
                print(datetime.date.today())
                c=i[1]
                self.comboBox_9.setCurrentText(i[3])

                
                
                self.dateEdit_2.setDate(i[4])


            cus.execute("SELECT * FROM PURCHASE_PRODUCT WHERE pno='%s'"%(c))
            b=cus.fetchall()
            
            c=0
            d=0
            e=0
            f=0
            print("Edit 3")
            for i in b:
                
                m=QtWidgets.QTableWidgetItem(i[3])
                self.tableWidget_2.setItem(c,1,m)
                m=QtWidgets.QTableWidgetItem(i[4])
                self.tableWidget_2.setItem(c,2,m)
                m=QtWidgets.QTableWidgetItem(i[5])
                self.tableWidget_2.setItem(c,3,m)
                m=QtWidgets.QTableWidgetItem(str(i[6]))
                self.tableWidget_2.setItem(c,4,m)
                m=QtWidgets.QTableWidgetItem(str(i[7]))
                self.tableWidget_2.setItem(c,5,m)
                m=QtWidgets.QTableWidgetItem(str(i[8]))
                
                m.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
                self.tableWidget_2.setItem(c,6,m)
                m=QtWidgets.QTableWidgetItem(str(i[9]))                                     
                m.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
                self.tableWidget_2.setItem(c,7,m)
                m=QtWidgets.QTableWidgetItem(str(i[10]))                                     
                m.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
                self.tableWidget_2.setItem(c,8,m)
                print("Edit 4")
                if c==0:
                    d=i[8]
                    e=i[9]
                    f=i[10]
                else:
                    d=d+i[8]
                    e=e+i[9]
                    f=f+i[10]               
                c=c+1
                print("Edit 5")
            n=str(d)
            self.label_11.setText(QtCore.QCoreApplication.translate("OtherWindow", n))
            n=str(e)
            self.label_12.setText(QtCore.QCoreApplication.translate("OtherWindow", n))
            n=str(f)
            self.label_13.setText(QtCore.QCoreApplication.translate("OtherWindow", n))
            print("Edit 6")


    def do_this52(self):
        self.spinBox_2.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.dateEdit_2.setEnabled(True)
        self.comboBox_9.setEnabled(True)
        self.tableWidget_2.setEnabled(True)
        self.pushButton_23.setEnabled(True)
        self.pushButton_22.setEnabled(True)
        self.pushButton_21.setEnabled(True)

    #Click of Undo Button in Purchase
    def do_this53(self):
        self.do_this50()
        if self.rowCount2>1:
            for i in range(1,self.rowCount2):
                self.tableWidget_2.removeRow(0)
            self.rowCount2=1
        self.spinBox_2.setValue(self.spinBox_2.value()-1)

    #Click of Save Button in Purchase
    def do_this54(self):
        global comp_no
        a1=comp_no
        a2=self.spinBox_2.value()
        a2=int(a2)
        a3=self.comboBox_9.currentText()
        a4=self.dateEdit_2.date().toPyDate()
        a5=self.label_13.text()
        
        
        
        if a3=='':
            
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Enter party name")
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif a5=='':
            
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Enter Products")
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()

        else :
            cus.execute("SELECT * FROM PURCHASE_VOUCHER WHERE c_no='%s' AND v_no='%s'"%(a1,a2))
            b=cus.fetchall()
            print(b)
            if len(b)==0:
                
                
                cus.execute("INSERT INTO PURCHASE_VOUCHER (c_no,name,v_no,date,amount) VALUES('%s','%s','%s','%s','%s')"%(a1,a3,a2,a4,a5))
                mydb.commit()
                print("perfect")
                cus.execute("SELECT sno FROM PURCHASE_VOUCHER WHERE c_no='%s' AND v_no='%s'"%(a1,a2))
                c=cus.fetchall()
                for i in c:
                    b=i[0]
                
                for i in range(1,self.rowCount2):
                    b1=i
                    b2=self.tableWidget_2.item(i-1,1).text()
                    b3=self.tableWidget_2.item(i-1,2).text()
                    b4=self.tableWidget_2.item(i-1,3).text()
                    b5=self.tableWidget_2.item(i-1,4).text()
                    b6=self.tableWidget_2.item(i-1,5).text()
                    b7=self.tableWidget_2.item(i-1,6).text()
                    b8=self.tableWidget_2.item(i-1,7).text()
                    b9=self.tableWidget_2.item(i-1,8).text()
                    b5=float(b5)
                    b6=float(b6)
                    b7=float(b7)
                    b8=float(b8)
                    b9=float(b9)
                    

                    cus.execute("INSERT INTO PURCHASE_PRODUCT (pno,sl_no,name,HSN_code,unit,qty,rate,gross,tax,net) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(b,b1,b2,b3,b4,b5,b6,b7,b8,b9))
                    print("It is fine")
            else:
                print(self.rowCount2)
                cus.execute("SELECT sno FROM PURCHASE_VOUCHER WHERE c_no='%s' AND v_no='%s'"%(a1,a2))
                c=cus.fetchall()
                for i in c:
                    b=i[0]
                    print(b)
                cus.execute("DELETE FROM PURCHASE_PRODUCT WHERE pno='%s'"%b)
                mydb.commit()
                
                for i in range(1,self.rowCount2):
                    b1=i
                    b2=self.tableWidget_2.item(i-1,1).text()
                    b3=self.tableWidget_2.item(i-1,2).text()
                    b4=self.tableWidget_2.item(i-1,3).text()
                    b5=self.tableWidget_2.item(i-1,4).text()
                    b6=self.tableWidget_2.item(i-1,5).text()
                    b7=self.tableWidget_2.item(i-1,6).text()
                    b8=self.tableWidget_2.item(i-1,7).text()
                    b9=self.tableWidget_2.item(i-1,8).text()
                    b5=float(b5)
                    b6=float(b6)
                    b7=float(b7)
                    b8=float(b8)
                    b9=float(b9)
                    

                    cus.execute("INSERT INTO PURCHASE_PRODUCT (pno,sl_no,name,HSN_code,unit,qty,rate,gross,tax,net) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(b,b1,b2,b3,b4,b5,b6,b7,b8,b9))
                    
                
                cus.execute("UPDATE PURCHASE_VOUCHER SET name = '%s' WHERE c_no = '%s' AND v_no = '%s'"%(a3,a1,a2))
                cus.execute("UPDATE PURCHASE_VOUCHER SET date = '%s' WHERE c_no = '%s' AND v_no = '%s'"%(a4,a1,a2))
                cus.execute("UPDATE PURCHASE_VOUCHER SET amount = '%s' WHERE c_no = '%s' AND v_no = '%s'"%(a5,a1,a2))

            mydb.commit()
            if self.rowCount2>1:
                for i in range(1,self.rowCount2):
                    self.tableWidget_2.removeRow(0)
                self.rowCount2=1
            self.spinBox_2.setValue(self.spinBox_2.value()+1)
            self.do_this50()


    #Click of Close Button in Purchase
    def do_this55(self):
        if self.rowCount2>1:
            for i in range(1,self.rowCount2):
                self.tableWidget_2.removeRow(0)
            self.rowCount2=1
        self.spinBox_2.setValue(self.spinBox_2.value()+1)
        self.comboBox_9.clear()
        self.do_this50()
        self.do_this19()

    #Click of Delete Button in Purchase
    def do_this56(self):
        global comp_no
        
        
        
        a1=comp_no
        a2=self.spinBox_2.value()
        a2=int(a2)
        print(a2)
        cus.execute("SELECT sno FROM PURCHASE_VOUCHER WHERE c_no='%s' AND v_no='%s'"%(a1,a2))
        c=cus.fetchall()
        for i in c:
            b=i[0]
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Do you want to delete this voucher")
        msg.setWindowTitle("Message")        
        msg.setStandardButtons(QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        retval=msg.exec_()
        print("value",retval)
        if retval==16384:
            cus.execute("DELETE FROM PURCHASE_PRODUCT WHERE pno='%s'"%b)
            cus.execute("DELETE FROM PURCHASE_VOUCHER WHERE sno='%s'"%b)
            mydb.commit()
            if self.rowCount2>1:
                for i in range(1,self.rowCount2):
                    self.tableWidget_2.removeRow(0)
                self.rowCount2=1
            self.spinBox_2.setValue(self.spinBox_2.value()-1)
            self.comboBox_9.setCurrentIndex(-1)
            self.do_this50()


    
    def do_this57(self):
        global comp_no
        
        a=self.comboBox_12.currentText()
        if self.i==1:
            cus.execute("SELECT SUM(amount)-SUM(samount) FROM SALES_VOUCHER WHERE name='%s'"%a)
        else:
            cus.execute("SELECT SUM(amount)-SUM(samount) FROM PURCHASE_VOUCHER WHERE name='%s'"%a)
        c=cus.fetchall()
        print(c)
        for i in c:
            x=i[0]
            
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        if self.i==1:
            msg.setText("The Trade receivable from '%s' is Rs.'%s'"%(a,x))
        else:
            msg.setText("The Trade payable to '%s' is Rs.'%s'"%(a,x))
        msg.setWindowTitle("Message")        
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
        self.comboBox_12.setCurrentIndex(-1)


    def do_this58(self):
        q=self.tableWidget_3.rowCount()
        print(q)
        for i in range(q):
            self.tableWidget_3.removeRow(0)
            print(i)
        self.do_this19()


    def do_this59(self):

        INITIALIZE.compForm2.show()

        
    def do_this60(self):
        global comp_no
        global state
        global dc
        global dnc
        printer = QtPrintSupport.QPrinter()

            
        printer.setPaperSize(QtPrintSupport.QPrinter.A4)
        printer.setPageSize(QtPrintSupport.QPrinter.A4)
        printer.setResolution(96)
        printer.setOutputFormat(QtPrintSupport.QPrinter.NativeFormat)
        printer.setCopyCount(dnc)

        qp = QtGui.QPainter()
        
        qp.begin(printer)
        x=13
        y=120
        
        qp.drawLine(x+10,y+100,x+730,y+100)
        qp.drawLine(x+10,y+100,x+10,y+750)
        qp.drawLine(x+730,y+100,x+730,y+750)
        qp.drawLine(x+250,y+100,x+250,y+250)
        qp.drawLine(x+500,y+100,x+500,y+250)
        qp.drawLine(x+10,y+250,x+730,y+250)
        qp.drawLine(x+27,y+250,x+27,y+620)
        qp.drawLine(x+275,y+250,x+275,y+620)
        qp.drawLine(x+319,y+250,x+319,y+620)
        qp.drawLine(x+363,y+250,x+363,y+620)
        qp.drawLine(x+407,y+250,x+407,y+620)
        qp.drawLine(x+460,y+250,x+460,y+620)
        qp.drawLine(x+532,y+250,x+532,y+620)
        qp.drawLine(x+604,y+250,x+604,y+620)
        qp.drawLine(x+676,y+250,x+676,y+620)
        
        qp.drawLine(x+460,y+270,x+676,y+270)

        qp.drawLine(x+492,y+270,x+492,y+620)
        qp.drawLine(x+564,y+270,x+564,y+620)
        qp.drawLine(x+636,y+270,x+636,y+620)
        
        qp.drawLine(x+10,y+290,x+730,y+290)
        qp.drawLine(x+10,y+620,x+730,y+620)

        qp.drawLine(x+605,y+620,x+605,y+750)

        qp.drawLine(x+605,y+733,x+730,y+733)

        qp.drawLine(x+10,y+750,x+730,y+750)

        qp.drawLine(x+10,y+770,x+730,y+770)

        qp.drawLine(x+10,y+750,x+10,y+770)

        qp.drawLine(x+730,y+750,x+730,y+770)








        
        print("print option")
        cus.execute("SELECT * FROM COMPANY WHERE sno='%s'"%comp_no)
        c=cus.fetchall()

        for i in c:
            a1=i[6]
            a2=i[7]
            a3=i[8]
            a4=i[9]
            a5=i[10]
            a6=i[11]
            a7=i[4]
            a8=i[5]
            a9=i[2]
           
            print("hi")
            if a2==None:
               
                b1=[a1,""]
            elif a3==None:
                b1=[a1,a2,""]
             
            else:
                b1=[a1,a2,a3,""]
               

            print(b1)
            b2=",".join(b1)

            b3=[a4,a5]
            b4="-".join(b3)
            b5=str(self.spinBox.value())
            b5="Invoice no : "+b5#Invoice no
            a7="GSTIN : "+a7
            a8="Ph No : "+a8
            
            print(b2)#Total address
            print(b4)#City with pincode
            print(a7)#GSTIN
            print(a8)#Ph no

            c1=self.comboBox_3.currentText()#Party name
            cus.execute("SELECT * FROM PARTY WHERE type='Customer' AND name='%s'"%c1)
            c=cus.fetchall()

            for i in c:
                c23=i[3]
                
            
            c2=self.lineEdit_20.displayText()
            c3=self.lineEdit_22.displayText()
            
            c4=self.lineEdit_21.displayText()
            c5=self.lineEdit_23.displayText()
            c6=self.lineEdit_24.displayText()
            c7=self.comboBox_4.currentText()

            if c3=="":
                c8=[c2]
            elif c4=="":
                c8=[c2,c3]       
            else:
                c8=[c2,c3,c4]

            c10=[c5,c6]
            #Billing
            c9=",".join(c8)#Total address
            c11="-".join(c10)#City with pincode
            c7=c7#State

            c12=self.lineEdit_27.displayText()
        
            c13=self.lineEdit_30.displayText()
            c14=self.lineEdit_31.displayText()
            c15=self.lineEdit_32.displayText()
            c16=self.lineEdit_33.displayText()
            c17=self.comboBox_10.currentText()

            if c13=="":
                c18=[c12]
            elif c14=="":
                c18=[c12,c13]       
            else:
                c18=[c12,c13,c14]

            c20=[c15,c16]
            #Shipping
            c19=",".join(c18)#Total address
            c21="-".join(c20)#City with pincode
            c17=c17#State

            if c17=="":
                c19=""
                c21=""

            c22=self.lineEdit_17.displayText()
            c22="GSTIN : "+c22#GSTIN
            c23=c23
            c23="Phone : "+c23#Ph no

            c24=str(self.dateEdit.date().toPyDate())

            

            c24=c24.split("-")
            c24.reverse()
            c24="-".join(c24)
            c24="Date : " + c24#Date


            
            


            print(c1)
            print(c9)
            print(c11)
            print(c7)
            print(c22)
            print(c23)

            print(c1)
            print(c19)
            print(c21)
            print(c17)
            print(c22)
            print(c23)

            print(b5)
            print(c24)
            print(self.rowCount)
            xx=0
            for i in range(1,self.rowCount):
                d1=i
                d2=self.tableWidget.item(i-1,1).text()
                d3=self.tableWidget.item(i-1,2).text()
                d4=self.tableWidget.item(i-1,3).text()
                d5=self.tableWidget.item(i-1,4).text()
                d6=self.tableWidget.item(i-1,5).text()
                d7=self.tableWidget.item(i-1,6).text()
                d8=self.tableWidget.item(i-1,7).text()
                d9=self.tableWidget.item(i-1,8).text()
                
                
                d5=float(d5)
                d6=float(d6)
                d7=float(d7)
                d8=float(d8)
                d9=float(d9)

                d10=(d8*100)/d7
                d5="%.2f"%d5
                d6="%.2f"%d6
                d7="%.2f"%d7
                d9="%.2f"%d9
                d10="%.2f"%(d10/2)
                print(d1)
                print(d3)
                print(d4)
                print(d5)
                print(d6)
                print(d7)
                print(d8)
                print(d10)
                print(d9)
                print("good" + str(i))


            e1=self.lineEdit_18.displayText()
            e2=self.lineEdit_19.displayText()
            e1="Vehicle No. : "+e1
            e2="Doc. Through : "+e2

            print("ok")
            f1=self.label_38.text()
            f2=self.label_39.text()
            f3=self.label_40.text()
            print("ok")
            print(f1)
            print(f2)
            print(f3)
            f1=float(f1)
            f2=float(f2)
            f3=float(f3)
            print("ok")
            if c7==state:
                f4="%.2f"%(f2/2)
                f5="%.2f"%(f2/2)
                f6=""
            else:
                f4=""
                f5=""
                f6="%.2f"%(f2)
            print("ok")
            f1="%.2f"%(f1)
            f2="%.2f"%(f2)
            f3="%.2f"%(f3)
           
            print("Check 1")
        
            
            
            x1=0
            y1=60
            x2=13
            y2=0
            x3=60
            y3=0
            x4=73
            y4=0
            x5=10
            y5=0
            y2=y2+y1
            y3=y3+y1
            y4=y4+y1
            y5=y5+y1
            x6=10
            y6=130
            x7=40
            y7=130

            y5=y5+20
            
            print("Check 3")

            
            qp.setPen(QtGui.QColor(0, 0, 0))
            qp.setFont(QtGui.QFont('Arial', 15,weight=QtGui.QFont.Bold))
            print("hi")

            qp.drawText(x1+0,y1+0,x1+740,y1+20,0x0084,a9)
            qp.setFont(QtGui.QFont('Arial', 8,weight=QtGui.QFont.Normal))
            y1=52
            text=dc
            qp.drawText(20,15,740,45,0x0081,text)
            qp.drawText(x1+0,y1+20,x1+740,y1+45,0x0084,b2)
            qp.drawText(x1+0,y1+40,x1+740,y1+45,0x0084,b4)
            qp.drawText(x1+0,y1+60,x1+740,y1+45,0x0084,a8)
            qp.drawText(x1+0,y1+80,x1+740,y1+45,0x0084,a7)
            qp.drawText(x1+0,y1+100,x1+740,y1+45,0x0084,"TAX INVOICE")
            qp.setFont(QtGui.QFont('Arial', 7,weight=QtGui.QFont.Normal))
            
            qp.drawText(x2+12,y2+100,x2+180,y2+20,0x0041,"Billing Address")
            
            qp.setFont(QtGui.QFont('Arial', 8,weight=QtGui.QFont.Normal))

            print("Check 4")
            
            qp.drawText(x2+13,y2+122,x2+180,y2+20,0x0041,c1)
            qp.setFont(QtGui.QFont('Arial', 7.5,weight=QtGui.QFont.Normal))
            qp.drawText(x2+13,y2+140,x2+180,y2+20,0x0041,c9)
            qp.drawText(x2+13,y2+158,x2+180,y2+20,0x0041,c11)
            qp.drawText(x2+12,y2+176,x2+180,y2+20,0x0041,c7)
            qp.drawText(x2+12,y2+210,x2+180,y2+20,0x0041,c22)
            qp.drawText(x2+12,y2+230,x2+180,y2+20,0x0041,c23)

            qp.setFont(QtGui.QFont('Arial', 7,weight=QtGui.QFont.Normal))
            qp.drawText(x3+204,y3+100,x3+180,y3+20,0x0041,"Shipping Address")
            qp.setFont(QtGui.QFont('Arial', 8,weight=QtGui.QFont.Normal))
            qp.drawText(x3+205,y3+122,x3+180,y3+20,0x0041,c1)
            qp.setFont(QtGui.QFont('Arial', 7.5,weight=QtGui.QFont.Normal))
            qp.drawText(x3+205,y3+140,x3+180,y3+20,0x0041,c19)
            qp.drawText(x3+205,y3+158,x3+180,y3+20,0x0041,c21)
            qp.drawText(x3+205,y3+176,x3+180,y3+20,0x0041,c17)
            qp.drawText(x3+205,y3+210,x3+180,y3+20,0x0041,c22)
            qp.drawText(x3+205,y3+230,x3+180,y3+20,0x0041,c23)

            print("Check 5")
            
            qp.setFont(QtGui.QFont('Arial', 8,weight=QtGui.QFont.Normal))
            qp.drawText(x4+445,y4+100,x4+180,y4+20,0x0041,b5)
            qp.drawText(x4+445,y4+120,x4+180,y4+20,0x0041,c24)
            qp.drawText(x4+445,y4+140,x4+180,y4+20,0x0041,e1)
            qp.drawText(x4+445,y4+160,x4+180,y4+20,0x0041,e2)

            print("Check 6")
            
            qp.setFont(QtGui.QFont('Arial', 7.5,weight=QtGui.QFont.Normal))

            qp.drawText(x5+27,y5+260,x5+248,y5+20,0x0084,"Description")
            qp.drawText(x5+275,y5+250,x5+44,y5+20,0x0084,"HSN")
            qp.drawText(x5+275,y5+270,x5+44,y5+20,0x0084,"/SAC")
            qp.drawText(x5+319,y5+260,x5+44,y5+20,0x0084,"Qty")
            qp.drawText(x5+363,y5+260,x5+44,y5+20,0x0084,"Rate")
            qp.drawText(x5+407,y5+250,x5+53,y5+20,0x0084,"Taxable")
            qp.drawText(x5+407,y5+270,x5+53,y5+20,0x0084,"Value")
            qp.drawText(x5+460,y5+250,x5+72,y5+20,0x0084,"CGST")
            qp.drawText(x5+532,y5+250,x5+72,y5+20,0x0084,"SGST")
            qp.drawText(x5+604,y5+250,x5+72,y5+20,0x0084,"IGST")
            qp.setFont(QtGui.QFont('Arial', 7.5,weight=QtGui.QFont.Normal))
            
            qp.drawText(x5+675,y5+260,x5+55,y5+20,0x0084,"Net Amount")

            qp.drawText(x5+460,y5+270,x5+32,y5+20,0x0084,"Rate")
            qp.drawText(x5+492,y5+270,x5+40,y5+20,0x0084,"Amt")
            
            qp.drawText(x5+532,y5+270,x5+32,y5+20,0x0084,"Rate")
            qp.drawText(x5+564,y5+270,x5+40,y5+20,0x0084,"Amt")

            
            qp.drawText(x5+604,y5+270,x5+32,y5+20,0x0084,"Rate")
            qp.drawText(x5+636,y5+270,x5+40,y5+20,0x0084,"Amt")

            qp.drawText(90,720,195,20,0x0082,"TOTAL")

            print("Check 7")
            
            qp.setFont(QtGui.QFont('Arial', 7.5,weight=QtGui.QFont.Normal))

            text="1. Our resposibility ceases after the goods are handed over to carriers"
            qp.drawText(x6+15,y6+550,x6+300,y6+20,0x0081,text)

            text="2. Any dispute as to pilterage or shortage must be settled with the carriers after"
            qp.drawText(x6+15,y6+565,x6+350,y6+20,0x0081,text)

            text="duly weighing the consignment before taking delivery, interest 18% per annum"
            qp.drawText(x6+15,y6+580,x6+350,y6+20,0x0081,text)

            text="will be charged on overdue accounts"
            qp.drawText(x6+15,y6+595,x6+300,y6+20,0x0081,text)

            text="3. Payment by cheque or Draft only"
            qp.drawText(x6+15,y6+610,300,y6+20,0x0081,text)

            text="4. Subject to Tirunelveli Jurisdiction"
            qp.drawText(x6+15,y6+625,x6+300,y6+20,0x0081,text)

            qp.setFont(QtGui.QFont('Arial', 7.8,weight=QtGui.QFont.Normal))

            text="Gross Amount:"
            qp.drawText(x7+300,y7+550,x7+233,y7+20,0x0082,text)

            text="Taxable Amount:"
            qp.drawText(x7+300,y7+567,x7+233,y7+20,0x0082,text)

            text="CGST:"
            qp.drawText(x7+300,y7+584,x7+233,y7+20,0x0082,text)

            text="SGST:"
            qp.drawText(x7+300,y7+601,x7+233,y7+20,0x0082,text)

            text="IGST:"
            qp.drawText(x7+300,y7+618,x7+233,y7+20,0x0082,text)

            text="Total Tax:"
            qp.drawText(x7+300,y7+635,x7+233,y7+20,0x0082,text)

            qp.setFont(QtGui.QFont('Arial', 7.9,weight=QtGui.QFont.Normal))
            
            qp.drawText(x7+323,y7+550,x7+338,y7+20,0x0082,f1)

            qp.drawText(x7+323,y7+567,x7+338,y7+20,0x0082,f1)

            qp.drawText(x7+323,y7+584,x7+338,y7+20,0x0082,f4)

            qp.drawText(x7+323,y7+601,x7+338,y7+20,0x0082,f5)

            qp.drawText(x7+323,y7+618,x7+338,y7+20,0x0082,f6)

            qp.drawText(x7+323,y7+635,x7+338,y7+20,0x0082,f2)

            qp.drawText(x7+323,y7+655,x7+338,y7+20,0x0082,f3)

            qp.setFont(QtGui.QFont('Arial', 8,weight=QtGui.QFont.Normal))

            text="Invoice Amount:"
            qp.drawText(x7+300,y7+655,x7+233,y7+20,0x0082,text)


            print("Check 8")
            
            text="1"
            y5=y5-15
            qp.setFont(QtGui.QFont('Arial', 7,weight=QtGui.QFont.Normal))
            tot=0
            for i in range(1,self.rowCount):

                y5=y5+15
                d1=str(i)
                d2=self.tableWidget.item(i-1,1).text()
                d4=self.tableWidget.item(i-1,2).text()
                d5=self.tableWidget.item(i-1,4).text()
                d6=self.tableWidget.item(i-1,5).text()
                d7=self.tableWidget.item(i-1,6).text()
                d8=self.tableWidget.item(i-1,7).text()
                d9=self.tableWidget.item(i-1,8).text()

                d5=float(d5)
                tot=tot+d5
                d6=float(d6)
                d7=float(d7)
                d8=float(d8)
                d9=float(d9)
                
                d10=(d8*100)/d7
                if c7==state:
                    d11="%.2f"%(d10/2)
                    d12="%.2f"%(d8/2)
                    d13=""
                    d14=""
                else:
                    d11=""
                    d12=""
                    d13="%.2f"%(d10)
                    d14="%.2f"%(d8)
                    
                d5="%.2f"%d5
                d6="%.2f"%d6
                d7="%.2f"%d7
                d9="%.2f"%d9
                
                qp.drawText(x5+0,y5+295,x5+19,y5+20,0x0082,d1)

                qp.drawText(x5+33,y5+295,x5+248,y5+20,0x0081,d2)

                qp.drawText(x5+278,y5+295,x5+34,y5+20,0x0084,d4)

                qp.drawText(x5+321,y5+295,x5+33,y5+20,0x0082,d5)

                qp.drawText(x5+366,y5+295,x5+33,y5+20,0x0082,d6)

                qp.drawText(x5+418,y5+295,x5+34,y5+20,0x0082,d7)

                qp.drawText(x5+464,y5+295,x5+20,y5+20,0x0084,d11)

                qp.drawText(x5+489,y5+295,x5+34,y5+20,0x0082,d12)

                qp.drawText(x5+535,y5+295,x5+20,y5+20,0x0084,d11)

                qp.drawText(x5+561,y5+295,x5+34,y5+20,0x0082,d12)

                qp.drawText(x5+606,y5+295,x5+20,y5+20,0x0084,d13)

                qp.drawText(x5+633,y5+295,x5+34,y5+20,0x0082,d14)

                qp.drawText(x5+688,y5+295,x5+34,y5+20,0x0082,d9)

            qp.drawText(330,720,43,20,0x0082,str(tot))

            



            #qp.drawText(330,825,43,20,0x0082,"for "+a9)
            qp.setFont(QtGui.QFont('Arial', 8,weight=QtGui.QFont.Normal))
            text="for "+a9
            qp.drawText(363,825,378,145,0x0082,text)

            qp.drawText(363,825,378,260,0x0082,"Signature")

            num=int(float(f3))


            num1=inf.number_to_words((num%100))
            num2=inf.number_to_words((int(num/100)%10))
            num3=inf.number_to_words((int(num/1000)%100))
            num4=inf.number_to_words((int(num/100000)%100))

            text="Rupees "

            if 'zero' not in num4:
                text=text+ num4 + " Lakh "
                print(" Lakhs ")
            if 'zero' not in num3:
                text=text+ num3 + " Thousand "
                print("Thousand")
            if 'zero' not in num2:
                text=text+ num2 + " Hundred "
                print("Hundred")
            if 'zero' not in num1:
                text=text + num1 +" "
                
            text=text + "only"



            #text=inf.number_to_words(int(float(f3))) + ' only'
            qp.drawText(25,805,310,150,0x0081,text)

            
            qp.end()



            

            

        
            
        
        

    
            
                                            
            
        
            
        
                    
        


    """
    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.FocusOut and source is self.my_text_edit):
            print("eventFilter: focus out")    
    """ 

    
        
        
        
        
         
    
    def setupUi(self, OtherWindow):
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.resize(1350, 729)
        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1386, 700))
        self.stackedWidget.setMouseTracking(False)
        self.stackedWidget.setAutoFillBackground(True)
        self.stackedWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Kenya))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(90, 153, 27, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.page)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(246, 153, 340, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(90, 203, 30, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_2.setGeometry(QtCore.QRect(246, 203, 340, 20))
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_9 = QtWidgets.QLabel(self.page)
        self.label_9.setGeometry(QtCore.QRect(90, 253, 45, 16))
        self.label_9.setObjectName("label_9")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_8.setGeometry(QtCore.QRect(246, 253, 340, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(90, 303, 48, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_3.setGeometry(QtCore.QRect(246, 303, 340, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(90, 353, 48, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_4.setGeometry(QtCore.QRect(246, 353, 340, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(90, 403, 48, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_5.setGeometry(QtCore.QRect(246, 403, 340, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(90, 453, 19, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_6.setGeometry(QtCore.QRect(246, 453, 340, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setGeometry(QtCore.QRect(90, 503, 37, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_7.setGeometry(QtCore.QRect(246, 503, 340, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_8 = QtWidgets.QLabel(self.page)
        self.label_8.setGeometry(QtCore.QRect(90, 553, 26, 16))
        self.label_8.setObjectName("label_8")
        self.comboBox = QtWidgets.QComboBox(self.page)
        self.comboBox.setGeometry(QtCore.QRect(246, 553, 340, 20))
        self.comboBox.setObjectName("comboBox")
        self.label_49 = QtWidgets.QLabel(self.page)
        self.label_49.setGeometry(QtCore.QRect(90, 100, 96, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.pushButton_12 = QtWidgets.QPushButton(self.page)
        self.pushButton_12.setGeometry(QtCore.QRect(1260, 20, 45, 45))
        self.pushButton_12.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("E:/BILL_SOFTWARE/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_12.setIcon(icon)
        self.pushButton_12.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_4 = QtWidgets.QPushButton(self.page)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 610, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.page)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 610, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setMinimumSize(QtCore.QSize(1350, 707))
        self.page_2.setObjectName("page_2")
        self.groupBox = QtWidgets.QGroupBox(self.page_2)
        self.groupBox.setGeometry(QtCore.QRect(7, 80, 1338, 221))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(270, 30, 461, 181))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_3.setContentsMargins(40, 40, 10, 0)
        self.formLayout_3.setHorizontalSpacing(50)
        self.formLayout_3.setVerticalSpacing(10)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_21 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_21.setObjectName("label_21")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.dateEdit = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.label_22 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_22.setObjectName("label_22")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.label_23 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_23.setObjectName("label_23")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.comboBox_3 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_3)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_17)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 70, 160, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.label_19 = QtWidgets.QLabel(self.page_2)
        self.label_19.setGeometry(QtCore.QRect(110, 20, 121, 31))
        self.label_19.setObjectName("label_19")
        self.spinBox = QtWidgets.QSpinBox(self.page_2)
        self.spinBox.setGeometry(QtCore.QRect(220, 30, 151, 21))
        self.spinBox.setMinimum(1)
        self.spinBox.setObjectName("spinBox")
        self.pushButton = QtWidgets.QPushButton(self.page_2)
        self.pushButton.setGeometry(QtCore.QRect(390, 30, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget = QtWidgets.QTabWidget(self.page_2)
        self.tabWidget.setGeometry(QtCore.QRect(3, 330, 1311, 351))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 1290, 291))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.label_32 = QtWidgets.QLabel(self.tab)
        self.label_32.setGeometry(QtCore.QRect(10, 301, 55, 15))
        self.label_32.setAutoFillBackground(True)
        self.label_32.setObjectName("label_32")
        self.label_32.setAlignment(QtCore.Qt.AlignRight)
        self.label_33 = QtWidgets.QLabel(self.tab)
        self.label_33.setGeometry(QtCore.QRect(56, 301, 400, 15))
        self.label_33.setAutoFillBackground(True)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.tab)
        self.label_34.setGeometry(QtCore.QRect(457, 301, 99, 15))
        self.label_34.setAutoFillBackground(True)
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.tab)
        self.label_35.setGeometry(QtCore.QRect(557, 301, 99, 15))
        self.label_35.setAutoFillBackground(True)
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.tab)
        self.label_36.setGeometry(QtCore.QRect(657, 301, 99, 15))
        self.label_36.setAutoFillBackground(True)
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.tab)
        self.label_37.setGeometry(QtCore.QRect(757, 301, 99, 15))
        self.label_37.setAutoFillBackground(True)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.tab)
        self.label_38.setGeometry(QtCore.QRect(857, 301, 99, 15))
        self.label_38.setAlignment(QtCore.Qt.AlignRight)
        self.label_38.setAutoFillBackground(True)
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.tab)
        self.label_39.setGeometry(QtCore.QRect(957, 301, 99, 15))
        self.label_39.setAlignment(QtCore.Qt.AlignRight)
        self.label_39.setAutoFillBackground(True)
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.tab)
        self.label_40.setGeometry(QtCore.QRect(1057, 301, 99, 15))
        self.label_40.setAlignment(QtCore.Qt.AlignRight)
        self.label_40.setAutoFillBackground(True)
        self.label_40.setObjectName("label_40")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(80, 40, 361, 151))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_4.setContentsMargins(15, 20, 100, 0)
        self.formLayout_4.setHorizontalSpacing(30)
        self.formLayout_4.setVerticalSpacing(8)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_24 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_24.setObjectName("label_24")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_18)
        self.label_25 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_25.setObjectName("label_25")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_19)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(50, 40, 301, 251))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_5 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_5.setContentsMargins(10, 10, 20, 0)
        self.formLayout_5.setHorizontalSpacing(20)
        self.formLayout_5.setVerticalSpacing(10)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_26 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_26.setObjectName("label_26")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_20)
        self.label_27 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_27.setObjectName("label_27")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_22)
        self.label_28 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_28.setObjectName("label_28")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_28)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_21)
        self.label_29 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_29.setObjectName("label_29")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_29)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_23)
        self.label_30 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_30.setObjectName("label_30")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_30)
        self.lineEdit_24 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_24)
        self.label_31 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_31.setObjectName("label_31")
        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_31)
        self.comboBox_4 = QtWidgets.QComboBox(self.formLayoutWidget_3)
        self.comboBox_4.setObjectName("comboBox_4")
        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboBox_4)
        self.label_53 = QtWidgets.QLabel(self.tab_3)
        self.label_53.setGeometry(QtCore.QRect(30, 10, 100, 22))
        self.label_53.setObjectName("label_53")
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.tab_3)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(450, 40, 301, 191))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_6 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_6.setContentsMargins(10, 10, 20, 0)
        self.formLayout_6.setHorizontalSpacing(20)
        self.formLayout_6.setVerticalSpacing(10)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_54 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_54.setObjectName("label_54")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_54)
        self.lineEdit_27 = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_27)
        self.label_55 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_55.setObjectName("label_55")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_55)
        self.lineEdit_30 = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_30)
        self.label_56 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_56.setObjectName("label_56")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_56)
        self.lineEdit_31 = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_31)
        self.label_57 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_57.setObjectName("label_57")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_57)
        self.lineEdit_32 = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_32)
        self.label_58 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_58.setObjectName("label_58")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_58)
        self.lineEdit_33 = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_33)
        self.label_59 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_59.setObjectName("label_59")
        self.formLayout_6.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_59)
        self.comboBox_10 = QtWidgets.QComboBox(self.formLayoutWidget_4)
        self.comboBox_10.setObjectName("comboBox_10")
        self.formLayout_6.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboBox_10)
        self.label_60 = QtWidgets.QLabel(self.tab_3)
        self.label_60.setGeometry(QtCore.QRect(440, 10, 100, 22))
        self.label_60.setObjectName("label_60")
        self.checkBox = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox.setGeometry(QtCore.QRect(570, 240, 203, 22))
        self.checkBox.setObjectName("checkBox")
        self.tabWidget.addTab(self.tab_3, "")
        self.pushButton_13 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_13.setGeometry(QtCore.QRect(1140, 20, 45, 45))
        self.pushButton_13.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("E:/BILL_SOFTWARE/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_13.setIcon(icon1)
        self.pushButton_13.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_15 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_15.setGeometry(QtCore.QRect(1200, 20, 45, 45))
        self.pushButton_15.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("E:/BILL_SOFTWARE/print.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_15.setIcon(icon2)
        self.pushButton_15.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_16.setGeometry(QtCore.QRect(1080, 20, 45, 45))
        self.pushButton_16.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("E:/BILL_SOFTWARE/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_16.setIcon(icon3)
        self.pushButton_16.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_17.setGeometry(QtCore.QRect(1260, 20, 45, 45))
        self.pushButton_17.setText("")
        self.pushButton_17.setIcon(icon)
        self.pushButton_17.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_18.setGeometry(QtCore.QRect(1020, 20, 45, 45))
        self.pushButton_18.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("E:/BILL_SOFTWARE/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_18.setIcon(icon4)
        self.pushButton_18.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_18.setObjectName("pushButton_18")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_2.setGeometry(QtCore.QRect(150, 80, 351, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_42 = QtWidgets.QLabel(self.groupBox_2)
        self.label_42.setGeometry(QtCore.QRect(20, 70, 111, 20))
        self.label_42.setObjectName("label_42")
        self.label_41 = QtWidgets.QLabel(self.groupBox_2)
        self.label_41.setGeometry(QtCore.QRect(20, 30, 111, 20))
        self.label_41.setObjectName("label_41")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_26.setGeometry(QtCore.QRect(110, 70, 213, 20))
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_25.setGeometry(QtCore.QRect(110, 30, 213, 20))
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 170, 101, 21))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_43 = QtWidgets.QLabel(self.groupBox_2)
        self.label_43.setGeometry(QtCore.QRect(20, 110, 111, 20))
        self.label_43.setObjectName("label_43")
        self.comboBox_8 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_8.setGeometry(QtCore.QRect(110, 110, 213, 20))
        self.comboBox_8.setObjectName("comboBox_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(1260, 20, 45, 45))
        self.pushButton_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_3.setAutoFillBackground(True)
        self.pushButton_3.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("E:/BILL_SOFTWARE/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon5)
        self.pushButton_3.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.page_4)
        self.groupBox_3.setGeometry(QtCore.QRect(130, 70, 451, 251))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_44 = QtWidgets.QLabel(self.groupBox_3)
        self.label_44.setGeometry(QtCore.QRect(30, 50, 47, 22))
        self.label_44.setObjectName("label_44")
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_5.setGeometry(QtCore.QRect(170, 50, 221, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.label_45 = QtWidgets.QLabel(self.groupBox_3)
        self.label_45.setGeometry(QtCore.QRect(30, 100, 47, 22))
        self.label_45.setObjectName("label_45")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_28.setEnabled(True)
        self.lineEdit_28.setGeometry(QtCore.QRect(170, 100, 221, 22))
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.comboBox_7 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_7.setGeometry(QtCore.QRect(170, 150, 221, 22))
        self.comboBox_7.setObjectName("comboBox_7")
        self.label_48 = QtWidgets.QLabel(self.groupBox_3)
        self.label_48.setGeometry(QtCore.QRect(30, 150, 47, 22))
        self.label_48.setObjectName("label_48")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_6.setGeometry(QtCore.QRect(270, 200, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_19 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_19.setGeometry(QtCore.QRect(1260, 20, 45, 45))
        self.pushButton_19.setText("")
        self.pushButton_19.setIcon(icon)
        self.pushButton_19.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_19.setObjectName("pushButton_19")
        self.stackedWidget.addWidget(self.page_4)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.label_50 = QtWidgets.QLabel(self.page_9)
        self.label_50.setGeometry(QtCore.QRect(120, 30, 50, 20))
        self.label_50.setObjectName("label_50")
        self.spinBox_2 = QtWidgets.QSpinBox(self.page_9)
        self.spinBox_2.setGeometry(QtCore.QRect(220, 30, 150, 22))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(500)
        self.spinBox_2.setObjectName("spinBox_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.page_9)
        self.pushButton_7.setGeometry(QtCore.QRect(390, 30, 75, 22))
        self.pushButton_7.setObjectName("pushButton_7")
        self.groupBox_4 = QtWidgets.QGroupBox(self.page_9)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 100, 1300, 191))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_51 = QtWidgets.QLabel(self.groupBox_4)
        self.label_51.setGeometry(QtCore.QRect(270, 30, 50, 22))
        self.label_51.setObjectName("label_51")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.groupBox_4)
        self.dateEdit_2.setGeometry(QtCore.QRect(370, 30, 250, 22))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_52 = QtWidgets.QLabel(self.groupBox_4)
        self.label_52.setGeometry(QtCore.QRect(270, 80, 50, 22))
        self.label_52.setObjectName("label_52")
        self.comboBox_9 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_9.setGeometry(QtCore.QRect(370, 80, 250, 22))
        self.comboBox_9.setObjectName("comboBox_9")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.page_9)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 320, 1300, 350))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(9)
        self.tableWidget_2.setRowCount(1)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)

        self.label_11 = QtWidgets.QLabel(self.page_9)
        self.label_11.setGeometry(QtCore.QRect(857, 671, 99, 15))
        self.label_11.setAlignment(QtCore.Qt.AlignRight)
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(self.page_9)
        self.label_12.setGeometry(QtCore.QRect(957, 671, 99, 15))
        self.label_12.setAlignment(QtCore.Qt.AlignRight)
        self.label_12.setObjectName("label_12")

        self.label_13 = QtWidgets.QLabel(self.page_9)
        self.label_13.setGeometry(QtCore.QRect(1057, 671, 99, 15))
        self.label_13.setAlignment(QtCore.Qt.AlignRight)
        self.label_13.setObjectName("label_13")
     

        




        
        self.pushButton_20 = QtWidgets.QPushButton(self.page_9)
        self.pushButton_20.setGeometry(QtCore.QRect(1260, 20, 45, 45))
        self.pushButton_20.setText("")
        self.pushButton_20.setIcon(icon)
        self.pushButton_20.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.page_9)
        self.pushButton_21.setGeometry(QtCore.QRect(1200, 20, 45, 45))
        self.pushButton_21.setText("")
        self.pushButton_21.setIcon(icon1)
        self.pushButton_21.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.page_9)
        self.pushButton_22.setGeometry(QtCore.QRect(1140, 20, 45, 45))
        self.pushButton_22.setText("")
        self.pushButton_22.setIcon(icon3)
        self.pushButton_22.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.page_9)
        self.pushButton_23.setGeometry(QtCore.QRect(1080, 20, 45, 45))
        self.pushButton_23.setText("")
        self.pushButton_23.setIcon(icon4)
        self.pushButton_23.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_23.setObjectName("pushButton_23")
        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.groupBox_5 = QtWidgets.QGroupBox(self.page_10)
        self.groupBox_5.setGeometry(QtCore.QRect(80, 80, 661, 221))
        self.groupBox_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_61 = QtWidgets.QLabel(self.groupBox_5)
        self.label_61.setGeometry(QtCore.QRect(80, 50, 60, 22))
        self.label_61.setObjectName("label_61")
        self.comboBox_11 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_11.setGeometry(QtCore.QRect(200, 50, 250, 22))
        self.comboBox_11.setObjectName("comboBox_11")
        self.label_62 = QtWidgets.QLabel(self.groupBox_5 )
        self.label_62.setGeometry(QtCore.QRect(80, 90, 60, 22))
        self.label_62.setObjectName("label_62")
        
        self.comboBox_16 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_16.setGeometry(QtCore.QRect(200, 90, 250, 22))
        self.comboBox_16.setObjectName("comboBox_16")
        self.label_164 = QtWidgets.QLabel(self.groupBox_5 )
        self.label_164.setGeometry(QtCore.QRect(80, 130, 60, 22))
        self.label_164.setObjectName("label_164")
        self.lineEdit_34 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_34.setGeometry(QtCore.QRect(200, 130, 250, 22))
        self.lineEdit_34.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_34.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_8.setGeometry(QtCore.QRect(350, 170, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_24 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_24.setGeometry(QtCore.QRect(1260, 20, 45, 45))
        self.pushButton_24.setText("")
        self.pushButton_24.setIcon(icon)
        self.pushButton_24.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_24.setObjectName("pushButton_24")
        self.stackedWidget.addWidget(self.page_10)
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setObjectName("page_11")
        self.groupBox_6 = QtWidgets.QGroupBox(self.page_11)
        self.groupBox_6.setGeometry(QtCore.QRect(80, 70, 451, 201))
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_63 = QtWidgets.QLabel(self.groupBox_6)
        self.label_63.setGeometry(QtCore.QRect(60, 50, 50, 22))
        self.label_63.setObjectName("label_63")
        self.comboBox_12 = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox_12.setGeometry(QtCore.QRect(170, 50, 200, 22))
        self.comboBox_12.setObjectName("comboBox_12")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_9.setGeometry(QtCore.QRect(250, 130, 101, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_25 = QtWidgets.QPushButton(self.page_11)
        self.pushButton_25.setGeometry(QtCore.QRect(1260, 20, 45, 45))
        self.pushButton_25.setText("")
        self.pushButton_25.setIcon(icon)
        self.pushButton_25.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_25.setObjectName("pushButton_25")
        self.stackedWidget.addWidget(self.page_11)
        self.page_12 = QtWidgets.QWidget()
        self.page_12.setObjectName("page_12")
        self.groupBox_7 = QtWidgets.QGroupBox(self.page_12)
        self.groupBox_7.setGeometry(QtCore.QRect(70, 50, 500, 601))
        self.groupBox_7.setObjectName("groupBox_7")

        




        
        


        self.tableWidget_3 = QtWidgets.QTableWidget(self.groupBox_7)
        self.tableWidget_3.setEnabled(True)
        self.tableWidget_3.setGeometry(QtCore.QRect(30, 40, 450, 541))
        self.tableWidget_3.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_3.setObjectName("tableWidget")
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setRowCount(0)
        
        
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
       
        
        self.pushButton_26 = QtWidgets.QPushButton(self.page_12)
        self.pushButton_26.setGeometry(QtCore.QRect(1260, 20, 45, 45))
        self.pushButton_26.setText("")
        self.pushButton_26.setIcon(icon)
        self.pushButton_26.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_26.setObjectName("pushButton_26")
        self.stackedWidget.addWidget(self.page_12)
        self.page_13 = QtWidgets.QWidget()
        self.page_13.setObjectName("page_13")
        self.groupBox_8 = QtWidgets.QGroupBox(self.page_13)
        self.groupBox_8.setGeometry(QtCore.QRect(70, 100, 711, 550))
        self.groupBox_8.setObjectName("groupBox_8")
        self.layoutWidget_2 = QtWidgets.QWidget(self.groupBox_8)
        self.layoutWidget_2.setGeometry(QtCore.QRect(74, 520, 86, 25))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_7.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_10 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_7.addWidget(self.pushButton_10)
        self.lineEdit_35 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_35.setGeometry(QtCore.QRect(230, 320, 440, 20))
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.label_64 = QtWidgets.QLabel(self.groupBox_8)
        self.label_64.setGeometry(QtCore.QRect(74, 370, 19, 20))
        self.label_64.setObjectName("label_64")
        self.lineEdit_36 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_36.setGeometry(QtCore.QRect(230, 370, 440, 20))
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.label_65 = QtWidgets.QLabel(self.groupBox_8)
        self.label_65.setGeometry(QtCore.QRect(74, 220, 48, 20))
        self.label_65.setObjectName("label_65")
        self.label_66 = QtWidgets.QLabel(self.groupBox_8)
        self.label_66.setGeometry(QtCore.QRect(74, 470, 26, 20))
        self.label_66.setObjectName("label_66")
        self.lineEdit_38 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_38.setGeometry(QtCore.QRect(230, 220, 440, 20))
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.lineEdit_39 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_39.setEnabled(False)
        self.lineEdit_39.setGeometry(QtCore.QRect(230, 120, 440, 20))
        self.lineEdit_39.setFrame(True)
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.label_67 = QtWidgets.QLabel(self.groupBox_8)
        self.label_67.setGeometry(QtCore.QRect(74, 420, 37, 20))
        self.label_67.setObjectName("label_67")
        self.lineEdit_40 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_40.setGeometry(QtCore.QRect(230, 170, 440, 20))
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.layoutWidget_3 = QtWidgets.QWidget(self.groupBox_8)
        self.layoutWidget_3.setGeometry(QtCore.QRect(230, 520, 440, 25))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_8.setContentsMargins(250, 0, 20, 0)
        self.horizontalLayout_8.setSpacing(20)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_11 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_8.addWidget(self.pushButton_11)
        self.lineEdit_41 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_41.setGeometry(QtCore.QRect(230, 270, 440, 20))
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.label_68 = QtWidgets.QLabel(self.groupBox_8)
        self.label_68.setGeometry(QtCore.QRect(74, 120, 30, 20))
        self.label_68.setObjectName("label_68")
        self.label_69 = QtWidgets.QLabel(self.groupBox_8)
        self.label_69.setGeometry(QtCore.QRect(74, 170, 45, 20))
        self.label_69.setObjectName("label_69")
        self.label_70 = QtWidgets.QLabel(self.groupBox_8)
        self.label_70.setGeometry(QtCore.QRect(74, 270, 48, 20))
        self.label_70.setObjectName("label_70")
        self.label_71 = QtWidgets.QLabel(self.groupBox_8)
        self.label_71.setGeometry(QtCore.QRect(74, 320, 48, 20))
        self.label_71.setObjectName("label_71")
        self.comboBox_13 = QtWidgets.QComboBox(self.groupBox_8)
        self.comboBox_13.setGeometry(QtCore.QRect(230, 470, 440, 20))
        self.comboBox_13.setObjectName("comboBox_13")
        self.label_73 = QtWidgets.QLabel(self.groupBox_8)
        self.label_73.setGeometry(QtCore.QRect(74, 70, 27, 20))
        self.label_73.setObjectName("label_73")
        self.lineEdit_42 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_42.setGeometry(QtCore.QRect(230, 420, 440, 20))
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.comboBox_14 = QtWidgets.QComboBox(self.groupBox_8)
        self.comboBox_14.setGeometry(QtCore.QRect(230, 70, 440, 20))
        self.comboBox_14.setObjectName("comboBox_14")
        self.pushButton_27 = QtWidgets.QPushButton(self.page_13)
        self.pushButton_27.setGeometry(QtCore.QRect(1260, 20, 45, 45))
        self.pushButton_27.setText("")
        self.pushButton_27.setIcon(icon)
        self.pushButton_27.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_27.setObjectName("pushButton_27")
        self.stackedWidget.addWidget(self.page_13)
        self.page_14 = QtWidgets.QWidget()
        self.page_14.setObjectName("page_14")
        self.groupBox_9 = QtWidgets.QGroupBox(self.page_14)
        self.groupBox_9.setGeometry(QtCore.QRect(30, 20, 751, 591))
        self.groupBox_9.setObjectName("groupBox_9")
        self.lineEdit_37 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_37.setGeometry(QtCore.QRect(220, 330, 440, 20))
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.label_72 = QtWidgets.QLabel(self.groupBox_9)
        self.label_72.setGeometry(QtCore.QRect(64, 380, 19, 20))
        self.label_72.setObjectName("label_72")
        self.lineEdit_43 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_43.setGeometry(QtCore.QRect(220, 380, 440, 20))
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.label_74 = QtWidgets.QLabel(self.groupBox_9)
        self.label_74.setGeometry(QtCore.QRect(64, 230, 48, 20))
        self.label_74.setObjectName("label_74")
        self.label_75 = QtWidgets.QLabel(self.groupBox_9)
        self.label_75.setGeometry(QtCore.QRect(64, 480, 26, 20))
        self.label_75.setObjectName("label_75")
        self.lineEdit_44 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_44.setEnabled(True)
        self.lineEdit_44.setGeometry(QtCore.QRect(220, 80, 440, 20))
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.lineEdit_45 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_45.setGeometry(QtCore.QRect(220, 230, 440, 20))
        self.lineEdit_45.setObjectName("lineEdit_45")
        self.lineEdit_46 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_46.setGeometry(QtCore.QRect(220, 130, 440, 20))
        self.lineEdit_46.setFrame(True)
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.label_76 = QtWidgets.QLabel(self.groupBox_9)
        self.label_76.setGeometry(QtCore.QRect(64, 430, 37, 20))
        self.label_76.setObjectName("label_76")
        self.lineEdit_47 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_47.setGeometry(QtCore.QRect(220, 180, 440, 20))
        self.lineEdit_47.setObjectName("lineEdit_47")
        self.layoutWidget_4 = QtWidgets.QWidget(self.groupBox_9)
        self.layoutWidget_4.setGeometry(QtCore.QRect(220, 530, 440, 25))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_11.setContentsMargins(250, 0, 20, 0)
        self.horizontalLayout_11.setSpacing(20)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButton_14 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_11.addWidget(self.pushButton_14)
        self.lineEdit_48 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_48.setGeometry(QtCore.QRect(220, 280, 440, 20))
        self.lineEdit_48.setObjectName("lineEdit_48")
        self.label_77 = QtWidgets.QLabel(self.groupBox_9)
        self.label_77.setGeometry(QtCore.QRect(64, 130, 30, 20))
        self.label_77.setObjectName("label_77")
        self.label_78 = QtWidgets.QLabel(self.groupBox_9)
        self.label_78.setGeometry(QtCore.QRect(64, 180, 45, 20))
        self.label_78.setObjectName("label_78")
        self.label_79 = QtWidgets.QLabel(self.groupBox_9)
        self.label_79.setGeometry(QtCore.QRect(64, 280, 48, 20))
        self.label_79.setObjectName("label_79")
        self.label_80 = QtWidgets.QLabel(self.groupBox_9)
        self.label_80.setGeometry(QtCore.QRect(64, 330, 48, 20))
        self.label_80.setObjectName("label_80")
        self.comboBox_15 = QtWidgets.QComboBox(self.groupBox_9)
        self.comboBox_15.setGeometry(QtCore.QRect(220, 480, 440, 20))
        self.comboBox_15.setObjectName("comboBox_15")
        self.label_81 = QtWidgets.QLabel(self.groupBox_9)
        self.label_81.setGeometry(QtCore.QRect(64, 80, 27, 20))
        self.label_81.setObjectName("label_81")
        self.lineEdit_49 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_49.setGeometry(QtCore.QRect(220, 430, 440, 20))
        self.lineEdit_49.setObjectName("lineEdit_49")
        self.pushButton_28 = QtWidgets.QPushButton(self.page_14)
        self.pushButton_28.setGeometry(QtCore.QRect(1260, 20, 45, 45))
        self.pushButton_28.setText("")
        self.pushButton_28.setIcon(icon)
        self.pushButton_28.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_28.setObjectName("pushButton_28")
        self.stackedWidget.addWidget(self.page_14)
        self.page_15 = QtWidgets.QWidget()
        self.page_15.setObjectName("page_15")
        self.groupBox_10 = QtWidgets.QGroupBox(self.page_15)
        self.groupBox_10.setGeometry(QtCore.QRect(20, 20, 310, 150))
        self.groupBox_10.setTitle("")
        self.groupBox_10.setObjectName("groupBox_10")
        self.label_82 = QtWidgets.QLabel(self.groupBox_10)
        self.label_82.setGeometry(QtCore.QRect(0, 0, 310, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_82.setFont(font)
        self.label_82.setAlignment(QtCore.Qt.AlignCenter)
        self.label_82.setObjectName("label_82")
        self.label_105 = QtWidgets.QLabel(self.groupBox_10)
        self.label_105.setGeometry(QtCore.QRect(0, 20, 310, 130))
        self.label_105.setAlignment(QtCore.Qt.AlignCenter)
        self.label_105.setObjectName("label_105")
        self.groupBox_11 = QtWidgets.QGroupBox(self.page_15)
        self.groupBox_11.setGeometry(QtCore.QRect(350, 20, 310, 150))
        self.groupBox_11.setTitle("")
        self.groupBox_11.setObjectName("groupBox_11")
        self.label_84 = QtWidgets.QLabel(self.groupBox_11)
        self.label_84.setGeometry(QtCore.QRect(0, 0, 310, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_84.setFont(font)
        self.label_84.setAlignment(QtCore.Qt.AlignCenter)
        self.label_84.setObjectName("label_84")
        self.label_108 = QtWidgets.QLabel(self.groupBox_11)
        self.label_108.setGeometry(QtCore.QRect(0, 20, 310, 130))
        self.label_108.setAlignment(QtCore.Qt.AlignCenter)
        self.label_108.setObjectName("label_108")
        self.groupBox_12 = QtWidgets.QGroupBox(self.page_15)
        self.groupBox_12.setGeometry(QtCore.QRect(20, 190, 310, 150))
        self.groupBox_12.setTitle("")
        self.groupBox_12.setObjectName("groupBox_12")
        self.label_83 = QtWidgets.QLabel(self.groupBox_12)
        self.label_83.setGeometry(QtCore.QRect(0, 0, 310, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_83.setFont(font)
        self.label_83.setAlignment(QtCore.Qt.AlignCenter)
        self.label_83.setObjectName("label_83")
        self.label_106 = QtWidgets.QLabel(self.groupBox_12)
        self.label_106.setGeometry(QtCore.QRect(0, 20, 310, 130))
        self.label_106.setAlignment(QtCore.Qt.AlignCenter)
        self.label_106.setObjectName("label_106")
        self.groupBox_13 = QtWidgets.QGroupBox(self.page_15)
        self.groupBox_13.setGeometry(QtCore.QRect(350, 190, 310, 150))
        self.groupBox_13.setTitle("")
        self.groupBox_13.setObjectName("groupBox_13")
        self.label_85 = QtWidgets.QLabel(self.groupBox_13)
        self.label_85.setGeometry(QtCore.QRect(0, 0, 310, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_85.setFont(font)
        self.label_85.setAutoFillBackground(False)
        self.label_85.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_85.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_85.setLineWidth(0)
        self.label_85.setAlignment(QtCore.Qt.AlignCenter)
        self.label_85.setObjectName("label_85")
        self.label_107 = QtWidgets.QLabel(self.groupBox_13)
        self.label_107.setGeometry(QtCore.QRect(0, 20, 310, 130))
        self.label_107.setAlignment(QtCore.Qt.AlignCenter)
        self.label_107.setObjectName("label_107")
        self.groupBox_14 = QtWidgets.QGroupBox(self.page_15)
        self.groupBox_14.setGeometry(QtCore.QRect(680, 20, 310, 150))
        self.groupBox_14.setTitle("")
        self.groupBox_14.setObjectName("groupBox_14")
        self.label_87 = QtWidgets.QLabel(self.groupBox_14)
        self.label_87.setGeometry(QtCore.QRect(0, 0, 310, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_87.setFont(font)
        self.label_87.setAlignment(QtCore.Qt.AlignCenter)
        self.label_87.setObjectName("label_87")
        self.label_109 = QtWidgets.QLabel(self.groupBox_14)
        self.label_109.setGeometry(QtCore.QRect(0, 20, 310, 130))
        self.label_109.setAlignment(QtCore.Qt.AlignCenter)
        self.label_109.setObjectName("label_109")
        self.groupBox_15 = QtWidgets.QGroupBox(self.page_15)
        self.groupBox_15.setGeometry(QtCore.QRect(680, 190, 310, 150))
        self.groupBox_15.setTitle("")
        self.groupBox_15.setObjectName("groupBox_15")
        self.label_86 = QtWidgets.QLabel(self.groupBox_15)
        self.label_86.setGeometry(QtCore.QRect(0, 0, 310, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_86.setFont(font)
        self.label_86.setAlignment(QtCore.Qt.AlignCenter)
        self.label_86.setObjectName("label_86")
        self.label_110 = QtWidgets.QLabel(self.groupBox_15)
        self.label_110.setGeometry(QtCore.QRect(0, 20, 310, 130))
        self.label_110.setAlignment(QtCore.Qt.AlignCenter)
        self.label_110.setObjectName("label_110")
        self.groupBox_16 = QtWidgets.QGroupBox(self.page_15)
        self.groupBox_16.setGeometry(QtCore.QRect(1010, 20, 310, 150))
        self.groupBox_16.setTitle("")
        self.groupBox_16.setObjectName("groupBox_16")
        self.label_88 = QtWidgets.QLabel(self.groupBox_16)
        self.label_88.setGeometry(QtCore.QRect(0, 0, 310, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_88.setFont(font)
        self.label_88.setAlignment(QtCore.Qt.AlignCenter)
        self.label_88.setObjectName("label_88")
        self.label_112 = QtWidgets.QLabel(self.groupBox_16)
        self.label_112.setGeometry(QtCore.QRect(0, 20, 310, 130))
        self.label_112.setAlignment(QtCore.Qt.AlignCenter)
        self.label_112.setObjectName("label_112")
        self.groupBox_17 = QtWidgets.QGroupBox(self.page_15)
        self.groupBox_17.setGeometry(QtCore.QRect(1010, 190, 310, 150))
        self.groupBox_17.setTitle("")
        self.groupBox_17.setObjectName("groupBox_17")
        self.label_89 = QtWidgets.QLabel(self.groupBox_17)
        self.label_89.setGeometry(QtCore.QRect(0, 0, 310, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_89.setFont(font)
        self.label_89.setAlignment(QtCore.Qt.AlignCenter)
        self.label_89.setObjectName("label_89")
        self.label_111 = QtWidgets.QLabel(self.groupBox_17)
        self.label_111.setGeometry(QtCore.QRect(0, 20, 310, 130))
        self.label_111.setAlignment(QtCore.Qt.AlignCenter)
        self.label_111.setObjectName("label_111")
        self.tableView_2 = QtWidgets.QTableView(self.page_15)
        self.tableView_2.setGeometry(QtCore.QRect(20, 400, 640, 281))
        self.tableView_2.setObjectName("tableView_2")
        self.tableView_3 = QtWidgets.QTableView(self.page_15)
        self.tableView_3.setGeometry(QtCore.QRect(680, 400, 640, 281))
        self.tableView_3.setObjectName("tableView_3")
        self.label_103 = QtWidgets.QLabel(self.page_15)
        self.label_103.setGeometry(QtCore.QRect(20, 380, 640, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_103.setFont(font)
        self.label_103.setAlignment(QtCore.Qt.AlignCenter)
        self.label_103.setObjectName("label_103")
        self.label_104 = QtWidgets.QLabel(self.page_15)
        self.label_104.setGeometry(QtCore.QRect(680, 380, 640, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_104.setFont(font)
        self.label_104.setAlignment(QtCore.Qt.AlignCenter)
        self.label_104.setObjectName("label_104")
        self.stackedWidget.addWidget(self.page_15)
        self.page_16 = QtWidgets.QWidget()
        self.page_16.setObjectName("page_16")
        self.stackedWidget.addWidget(self.page_16)
        OtherWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OtherWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1350, 21))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menuMasters = QtWidgets.QMenu(self.menubar)
        self.menuMasters.setObjectName("menuMasters")
        self.menuModify = QtWidgets.QMenu(self.menuMasters)
        self.menuModify.setObjectName("menuModify")
        self.menuEntry = QtWidgets.QMenu(self.menubar)
        self.menuEntry.setObjectName("menuEntry")
        self.menuInventory = QtWidgets.QMenu(self.menubar)
        self.menuInventory.setObjectName("menuInventory")
        self.menuReceivables = QtWidgets.QMenu(self.menuInventory)
        self.menuReceivables.setObjectName("menuReceivables")
        self.menuPayables = QtWidgets.QMenu(self.menuInventory)
        self.menuPayables.setObjectName("menuPayables")
        self.menuProducts = QtWidgets.QMenu(self.menubar)
        self.menuProducts.setObjectName("menuProducts")
        self.menuModify_2 = QtWidgets.QMenu(self.menuProducts)
        self.menuModify_2.setObjectName("menuModify_2")
        OtherWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OtherWindow)
        self.statusbar.setObjectName("statusbar")
        OtherWindow.setStatusBar(self.statusbar)
        self.actionClose_company = QtWidgets.QAction(OtherWindow)
        self.actionClose_company.setObjectName("actionClose_company")
        self.actionExit = QtWidgets.QAction(OtherWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAdd_purchase = QtWidgets.QAction(OtherWindow)
        self.actionAdd_purchase.setObjectName("actionAdd_purchase")
        self.actionAdd_Sales = QtWidgets.QAction(OtherWindow)
        self.actionAdd_Sales.setObjectName("actionAdd_Sales")
        self.actionPurchases = QtWidgets.QAction(OtherWindow)
        self.actionPurchases.setObjectName("actionPurchases")
        self.actionSales = QtWidgets.QAction(OtherWindow)
        self.actionSales.setObjectName("actionSales")
        self.actionProfit_and_loss = QtWidgets.QAction(OtherWindow)
        self.actionProfit_and_loss.setObjectName("actionProfit_and_loss")
        self.actionAdd_supplier = QtWidgets.QAction(OtherWindow)
        self.actionAdd_supplier.setObjectName("actionAdd_supplier")
        self.actionAdd_customer = QtWidgets.QAction(OtherWindow)
        self.actionAdd_customer.setObjectName("actionAdd_customer")
        self.actionCustomer = QtWidgets.QAction(OtherWindow)
        self.actionCustomer.setObjectName("actionCustomer")
        self.actionSupplier = QtWidgets.QAction(OtherWindow)
        self.actionSupplier.setObjectName("actionSupplier")
        self.actionModify = QtWidgets.QAction(OtherWindow)
        self.actionModify.setObjectName("actionModify")
        self.actionSupplier_2 = QtWidgets.QAction(OtherWindow)
        self.actionSupplier_2.setObjectName("actionSupplier_2")
        self.actionCustomer_2 = QtWidgets.QAction(OtherWindow)
        self.actionCustomer_2.setObjectName("actionCustomer_2")
        self.actionCustomer_3 = QtWidgets.QAction(OtherWindow)
        self.actionCustomer_3.setObjectName("actionCustomer_3")
        self.actionSupplier_3 = QtWidgets.QAction(OtherWindow)
        self.actionSupplier_3.setObjectName("actionSupplier_3")
        self.actionDebit = QtWidgets.QAction(OtherWindow)
        self.actionDebit.setObjectName("actionDebit")
        self.actionCredit = QtWidgets.QAction(OtherWindow)
        self.actionCredit.setObjectName("actionCredit")
        self.actionSummary = QtWidgets.QAction(OtherWindow)
        self.actionSummary.setObjectName("actionSummary")
        self.actionSummary_2 = QtWidgets.QAction(OtherWindow)
        self.actionSummary_2.setObjectName("actionSummary_2")
        self.actionParty = QtWidgets.QAction(OtherWindow)
        self.actionParty.setObjectName("actionParty")
        self.actionParty_2 = QtWidgets.QAction(OtherWindow)
        self.actionParty_2.setObjectName("actionParty_2")
        self.actionAll = QtWidgets.QAction(OtherWindow)
        self.actionAll.setObjectName("actionAll")
        self.actionAll_2 = QtWidgets.QAction(OtherWindow)
        self.actionAll_2.setObjectName("actionAll_2")
        
        self.menu_File.addAction(self.actionClose_company)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionExit)
        self.menuModify.addAction(self.actionSupplier_2)
        self.menuModify.addAction(self.actionCustomer_2)
        self.menuMasters.addAction(self.actionAdd_supplier)
        self.menuMasters.addAction(self.actionAdd_customer)
        
        self.menuMasters.addAction(self.menuModify.menuAction())
        self.menuEntry.addAction(self.actionPurchases)
        self.menuEntry.addAction(self.actionSales)
        self.menuReceivables.addAction(self.actionParty)
        self.menuReceivables.addAction(self.actionAll_2)
        self.menuPayables.addAction(self.actionParty_2)
        self.menuPayables.addAction(self.actionAll)
        self.menuInventory.addAction(self.actionDebit)
        self.menuInventory.addAction(self.actionCredit)
        self.menuInventory.addAction(self.menuReceivables.menuAction())
        self.menuInventory.addAction(self.menuPayables.menuAction())
        self.menuInventory.addAction(self.actionSummary_2)
        self.menuModify_2.addAction(self.actionCustomer_3)
        self.menuModify_2.addAction(self.actionSupplier_3)
        self.menuProducts.addAction(self.actionCustomer)
        self.menuProducts.addAction(self.actionSupplier)
        self.menuProducts.addAction(self.menuModify_2.menuAction())
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuMasters.menuAction())
        self.menubar.addAction(self.menuEntry.menuAction())
        self.menubar.addAction(self.menuInventory.menuAction())
        self.menubar.addAction(self.menuProducts.menuAction())

        self.retranslateUi(OtherWindow)
        self.stackedWidget.setCurrentIndex(11)
        self.tabWidget.setCurrentIndex(0)

        
        self.actionClose_company.triggered.connect(self.master)

        self.actionExit.triggered.connect(self.master2)


        self.actionAdd_customer.triggered.connect(self.do_this)
        """Clicking Add_customer < masters < menu bar"""   
        self.actionSales.triggered.connect(self.do_this1)
        """Clicking Sales < Entry < menu bar"""   
        self.actionSupplier.triggered.connect(self.do_this2)
        """Clicking Supplier < Products < menu bar"""   
        self.actionCustomer.triggered.connect(self.do_this3)
        """Clicking Customer < Products < menu bar""" 
        self.actionPurchases.triggered.connect(self.do_this4)
        """Clicking Purchases < Entry < menu bar"""   
        self.actionAdd_supplier.triggered.connect(self.do_this5)
        """Clicking Add_supplier < masters < menu bar""" 
        self.actionSupplier_3.triggered.connect(self.do_this6)
        """Clicking Supplier < Modify < Products < menu bar"""
        self.actionCustomer_3.triggered.connect(self.do_this7)
        """Clicking Customer < Modify < Products < menu bar"""
        self.actionDebit.triggered.connect(self.do_this8)
        """Clicking Debit < Inventory < menu bar"""   
        self.actionCredit.triggered.connect(self.do_this9)
        """Clicking Crebit < Inventory < menu bar"""   
        self.actionParty.triggered.connect(self.do_this10)
        """Clicking Party < Receivables < Inventory < menu bar"""   
        self.actionParty_2.triggered.connect(self.do_this11)
        """Clicking Party < Payables < Inventory < menu bar"""   
        self.actionAll_2.triggered.connect(self.do_this12)
        """Clicking All < Receivables < Inventory < menu bar"""   
        self.actionAll.triggered.connect(self.do_this13)
        """Clicking All < Payables < Inventory < menu bar"""   
        self.actionSupplier_2.triggered.connect(self.do_this14)
        """Clicking Supplier < Modify < masters < menu bar"""   
        self.actionCustomer_2.triggered.connect(self.do_this15)
        """Clicking Customer < Modify < masters < menu bar"""   
        
        self.actionSummary_2.triggered.connect(self.do_this17)
        """Clicking Summary < Inventory < menu bar"""   
        
        
        self.pushButton_5.clicked.connect(self.do_this18)
        """ADD PUSHBUTTON in product entry"""   
            
        self.pushButton_3.clicked.connect(self.do_this19)
        """CLOSE PUSHBUTTON in product entry"""   
        self.pushButton_19.clicked.connect(self.do_this19)
        """CLOSE PUSHBUTTON in product modify"""   
        self.comboBox_5.activated.connect(self.do_this20)
        """NAME COMBOBOX in product modify"""   
        self.pushButton_6.clicked.connect(self.do_this21)
        """SAVE CHANGES PUSHBUTTON in product modify"""
        self.pushButton_2.clicked.connect(self.do_this22)

        
        self.pushButton_4.clicked.connect(self.do_this23)

        self.comboBox_14.activated.connect(self.do_this24)
        """NAME COMBOBOX in master modify"""

        self.pushButton_10.clicked.connect(self.do_this26)
        """RESET PUSHBUTTON in master modify"""

        self.pushButton_11.clicked.connect(self.do_this27)
        """OK PUSHBUTTON in master modify"""

        self.pushButton_8.clicked.connect(self.do_this28)

        self.tableWidget.cellClicked.connect(self.do_this29)

        self.comboBox_3.activated.connect(self.do_this33)

        self.checkBox.stateChanged.connect(self.do_this34)

        self.tableWidget.cellChanged.connect(self.do_this35)

        self.tableWidget.cellDoubleClicked.connect(self.do_this36)

        self.pushButton_18.clicked.connect(self.do_this42)
        """Undo button in sales"""
        
        self.pushButton.clicked.connect(self.do_this41)
        """Edit button in sales"""
        
        self.pushButton_16.clicked.connect(self.do_this39)
        """Save button in sales"""

        self.pushButton_13.clicked.connect(self.do_this43)
        """Delete button in sales"""

        self.pushButton_17.clicked.connect(self.do_this44)
        """Close button in sales"""

        self.comboBox_11.activated.connect(self.do_this45)

        self.tableWidget_2.cellClicked.connect(self.do_this46)

        self.tableWidget_2.cellChanged.connect(self.do_this49)

        self.pushButton_7.clicked.connect(self.do_this51)
        """Edit button in purchase"""

        self.pushButton_23.clicked.connect(self.do_this53)
        """Undo button in purchase"""

        self.pushButton_22.clicked.connect(self.do_this54)
        """Save button in purchase"""

        self.pushButton_20.clicked.connect(self.do_this55)
        """close button in purchase"""

        self.pushButton_21.clicked.connect(self.do_this56)
        """Delete button in purchase"""

        self.pushButton_9.clicked.connect(self.do_this57)


        self.pushButton_26.clicked.connect(self.do_this58)

        self.pushButton_15.clicked.connect(self.do_this59)
        
        

        


        


        

        self.pushButton_12.clicked.connect(self.do_this19)
        self.pushButton_27.clicked.connect(self.do_this19)
        self.pushButton_24.clicked.connect(self.do_this19)
        self.pushButton_25.clicked.connect(self.do_this19)
        
            
        
        
        
                
        self.comboBox_7.addItems(['5','10','18','28'])
        """GST COMBOBOX in product modify"""   
        self.comboBox_8.addItems(['5','10','18','28'])
        """GST COMBOBOX in product entry"""

        

        
        
        
        
        
        self.comboBox.addItems(self.states)
        self.comboBox_4.addItems(self.states)
        self.comboBox_10.addItems(self.states)
        self.comboBox_13.addItems(self.states)
        

        self.tableWidget_3.setColumnWidth(0,300)
        self.tableWidget_3.setColumnWidth(1,125)

        self.tableWidget_2.setColumnWidth(0,30)
        self.tableWidget_2.setColumnWidth(1,400)
        self.tableWidget_2.setColumnWidth(2,100)
        self.tableWidget_2.setColumnWidth(3,100)
        self.tableWidget_2.setColumnWidth(4,100)
        self.tableWidget_2.setColumnWidth(5,100)
        self.tableWidget_2.setColumnWidth(6,100)
        self.tableWidget_2.setColumnWidth(7,100)
        self.tableWidget_2.setColumnWidth(8,100)

        self.tableWidget.setColumnWidth(0,30)
        self.tableWidget.setColumnWidth(1,400)
        self.tableWidget.setColumnWidth(2,100)
        self.tableWidget.setColumnWidth(3,100)
        self.tableWidget.setColumnWidth(4,100)
        self.tableWidget.setColumnWidth(5,100)
        self.tableWidget.setColumnWidth(6,100)
        self.tableWidget.setColumnWidth(7,100)
        self.tableWidget.setColumnWidth(8,100)
        



        
        
        
        
        

        
        


        
        self.pushButton_4.clicked.connect(self.lineEdit_2.clear)
        self.pushButton_4.clicked.connect(self.lineEdit.clear)
        self.pushButton_4.clicked.connect(self.lineEdit_4.clear)
        self.pushButton_4.clicked.connect(self.lineEdit_3.clear)
        self.pushButton_4.clicked.connect(self.lineEdit_5.clear)
        self.pushButton_4.clicked.connect(self.lineEdit_6.clear)
        self.pushButton_4.clicked.connect(self.lineEdit_7.clear)
        self.pushButton_4.clicked.connect(self.lineEdit_8.clear)      

        
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)

    def retranslateUi(self, OtherWindow):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "Other Window"))
        self.label.setText(_translate("OtherWindow", "Name"))
        self.label_2.setText(_translate("OtherWindow", "GSTIN"))
        self.label_9.setText(_translate("OtherWindow", "Phone no"))
        self.label_3.setText(_translate("OtherWindow", "Address 1"))
        self.label_4.setText(_translate("OtherWindow", "Address 2"))
        self.label_5.setText(_translate("OtherWindow", "Address 3"))
        self.label_6.setText(_translate("OtherWindow", "City"))
        self.label_7.setText(_translate("OtherWindow", "Pincode"))
        self.label_8.setText(_translate("OtherWindow", "State"))
        self.label_49.setText(_translate("OtherWindow", "Customer details"))
        self.pushButton_4.setText(_translate("OtherWindow", "RESET"))
        self.pushButton_2.setText(_translate("OtherWindow", "OK"))
        self.label_20.setText(_translate("OtherWindow", "Invoice type"))
        self.label_21.setText(_translate("OtherWindow", "Date"))
        self.label_22.setText(_translate("OtherWindow", "Party"))
        self.label_23.setText(_translate("OtherWindow", "Party GSTIN"))
        self.radioButton.setText(_translate("OtherWindow", "Within state"))
        self.radioButton_2.setText(_translate("OtherWindow", "Inter-state"))
        self.label_19.setText(_translate("OtherWindow", "Voucher No"))
        self.pushButton.setText(_translate("OtherWindow", "Edit"))



        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("OtherWindow", "                                Product/Services                          "))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("OtherWindow", "HSN/SAC"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("OtherWindow", "Unit"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("OtherWindow", "Qty"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("OtherWindow", "Rate"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("OtherWindow", "Gross Amount"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("OtherWindow", "Tax"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("OtherWindow", "Net Amount"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("OtherWindow", "1"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_32.setText(_translate("OtherWindow", ""))
        self.label_33.setText(_translate("OtherWindow", ""))
        self.label_34.setText(_translate("OtherWindow", ""))
        self.label_35.setText(_translate("OtherWindow", ""))
        self.label_36.setText(_translate("OtherWindow", ""))
        self.label_37.setText(_translate("OtherWindow", ""))
        self.label_38.setText(_translate("OtherWindow", ""))
        self.label_39.setText(_translate("OtherWindow", ""))
        self.label_40.setText(_translate("OtherWindow", ""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("OtherWindow", "Items"))
        self.label_24.setText(_translate("OtherWindow", "VEHICLE NO"))
        self.label_25.setText(_translate("OtherWindow", "DOC THROUGH"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("OtherWindow", "Other info"))
        self.label_26.setText(_translate("OtherWindow", "Address 1"))
        self.label_27.setText(_translate("OtherWindow", "Address 2"))
        self.label_28.setText(_translate("OtherWindow", "Address 3"))
        self.label_29.setText(_translate("OtherWindow", "City"))
        self.label_30.setText(_translate("OtherWindow", "Pin code"))
        self.label_31.setText(_translate("OtherWindow", "State"))
        self.label_53.setText(_translate("OtherWindow", "Billing Address"))
        self.label_54.setText(_translate("OtherWindow", "Address 1"))
        self.label_55.setText(_translate("OtherWindow", "Address 2"))
        self.label_56.setText(_translate("OtherWindow", "Address 3"))
        self.label_57.setText(_translate("OtherWindow", "City"))
        self.label_58.setText(_translate("OtherWindow", "Pin code"))
        self.label_59.setText(_translate("OtherWindow", "State"))
        self.label_60.setText(_translate("OtherWindow", "Shipping Address"))
        self.checkBox.setText(_translate("OtherWindow", "Same as Billing address"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("OtherWindow", "Address"))
        self.groupBox_2.setTitle(_translate("OtherWindow", "GroupBox"))
        self.label_42.setText(_translate("OtherWindow", "HSN/SAC"))
        self.label_41.setText(_translate("OtherWindow", "Name"))
        self.pushButton_5.setText(_translate("OtherWindow", "ADD"))
        self.label_43.setText(_translate("OtherWindow", "GST"))
        self.groupBox_3.setTitle(_translate("OtherWindow", "GroupBox"))
        self.label_44.setText(_translate("OtherWindow", "Name"))
        self.label_45.setText(_translate("OtherWindow", "HSN/SAC"))
        self.label_48.setText(_translate("OtherWindow", "GST"))
        self.pushButton_6.setText(_translate("OtherWindow", "Save changes"))
        self.label_50.setText(_translate("OtherWindow", "Order no"))
        self.pushButton_7.setText(_translate("OtherWindow", "Edit"))
        self.groupBox_4.setTitle(_translate("OtherWindow", "Order details"))
        self.label_51.setText(_translate("OtherWindow", "Date"))
        self.label_52.setText(_translate("OtherWindow", "Party"))
        
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("OtherWindow", "SNo"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("OtherWindow", "Product name"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("OtherWindow", "HSN/SAC"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("OtherWindow", "Unit"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("OtherWindow", "Qty"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("OtherWindow", "Rate"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("OtherWindow", "Gross amount"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("OtherWindow", "Tax"))
        item = self.tableWidget_2.horizontalHeaderItem(8)
        item.setText(_translate("OtherWindow", "Net Amount"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("OtherWindow", "1"))
        self.label_11.setText(_translate("OtherWindow", ""))
        self.label_12.setText(_translate("OtherWindow", ""))
        self.label_13.setText(_translate("OtherWindow", ""))
        
        self.groupBox_5.setTitle(_translate("OtherWindow", "GroupBox"))
        self.label_61.setText(_translate("OtherWindow", "Party"))
        self.label_62.setText(_translate("OtherWindow", "Voucher no"))
        self.label_164.setText(_translate("OtherWindow", "Amount"))
        self.pushButton_8.setText(_translate("OtherWindow", "ADD"))
        self.groupBox_6.setTitle(_translate("OtherWindow", "GroupBox"))
        self.label_63.setText(_translate("OtherWindow", "Party"))
        self.pushButton_9.setText(_translate("OtherWindow", "Show"))
        self.groupBox_7.setTitle(_translate("OtherWindow", "GroupBox"))




        
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("OtherWindow", "Party"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("OtherWindow", "Amount"))



        
        

        


        
       
        

        
        self.groupBox_8.setTitle(_translate("OtherWindow", "GroupBox"))
        self.pushButton_10.setText(_translate("OtherWindow", "RESET"))
        self.label_64.setText(_translate("OtherWindow", "City"))
        self.label_65.setText(_translate("OtherWindow", "Address 1"))
        self.label_66.setText(_translate("OtherWindow", "State"))
        self.label_67.setText(_translate("OtherWindow", "Pincode"))
        self.pushButton_11.setText(_translate("OtherWindow", "OK"))
        self.label_68.setText(_translate("OtherWindow", "GSTIN"))
        self.label_69.setText(_translate("OtherWindow", "Phone no"))
        self.label_70.setText(_translate("OtherWindow", "Address 2"))
        self.label_71.setText(_translate("OtherWindow", "Address 3"))
        self.label_73.setText(_translate("OtherWindow", "Name"))
        self.groupBox_9.setTitle(_translate("OtherWindow", "Company details"))
        self.label_72.setText(_translate("OtherWindow", "City"))
        self.label_74.setText(_translate("OtherWindow", "Address 1"))
        self.label_75.setText(_translate("OtherWindow", "State"))
        self.label_76.setText(_translate("OtherWindow", "Pincode"))
        self.pushButton_14.setText(_translate("OtherWindow", "Update"))
        self.label_77.setText(_translate("OtherWindow", "GSTIN"))
        self.label_78.setText(_translate("OtherWindow", "Phone no"))
        self.label_79.setText(_translate("OtherWindow", "Address 2"))
        self.label_80.setText(_translate("OtherWindow", "Address 3"))
        self.label_81.setText(_translate("OtherWindow", "Name"))
        self.label_82.setText(_translate("OtherWindow", "Sales This Year"))
        self.label_105.setText(_translate("OtherWindow", "0"))
        self.label_84.setText(_translate("OtherWindow", "Purchases This Year"))
        self.label_108.setText(_translate("OtherWindow", "0"))
        self.label_83.setText(_translate("OtherWindow", "Sales This Month"))
        self.label_106.setText(_translate("OtherWindow", "0"))
        self.label_85.setText(_translate("OtherWindow", "Purchases This Month"))
        self.label_107.setText(_translate("OtherWindow", "0"))
        self.label_87.setText(_translate("OtherWindow", "Receivables"))
        self.label_109.setText(_translate("OtherWindow", "0"))
        self.label_86.setText(_translate("OtherWindow", "Payables"))
        self.label_110.setText(_translate("OtherWindow", "0"))
        self.label_88.setText(_translate("OtherWindow", "Profit"))
        self.label_112.setText(_translate("OtherWindow", "0"))
        self.label_89.setText(_translate("OtherWindow", "Stock in hand"))
        self.label_111.setText(_translate("OtherWindow", "0"))
        self.label_103.setText(_translate("OtherWindow", "Top 10 Receivables"))
        self.label_104.setText(_translate("OtherWindow", "Top 10 Payables"))
        self.menu_File.setTitle(_translate("OtherWindow", "&File"))
        self.menuMasters.setTitle(_translate("OtherWindow", "Masters"))
        self.menuModify.setTitle(_translate("OtherWindow", "Modify"))
        self.menuEntry.setTitle(_translate("OtherWindow", "Entry"))
        self.menuInventory.setTitle(_translate("OtherWindow", "Inventory"))
        self.menuReceivables.setTitle(_translate("OtherWindow", "Receivables"))
        self.menuPayables.setTitle(_translate("OtherWindow", "Payables"))
        self.menuProducts.setTitle(_translate("OtherWindow", "Products"))
        self.menuModify_2.setTitle(_translate("OtherWindow", "Modify"))
        self.actionClose_company.setText(_translate("OtherWindow", "Close company"))
        self.actionExit.setText(_translate("OtherWindow", "Exit"))
        self.actionAdd_purchase.setText(_translate("OtherWindow", "Add supplier"))
        self.actionAdd_Sales.setText(_translate("OtherWindow", "Add purchase"))
        self.actionPurchases.setText(_translate("OtherWindow", "Purchases"))
        self.actionSales.setText(_translate("OtherWindow", "Sales"))
        self.actionProfit_and_loss.setText(_translate("OtherWindow", "Profit and loss"))
        self.actionAdd_supplier.setText(_translate("OtherWindow", "Add supplier"))
        self.actionAdd_customer.setText(_translate("OtherWindow", "Add customer"))
        self.actionCustomer.setText(_translate("OtherWindow", "Customer"))
        self.actionSupplier.setText(_translate("OtherWindow", "Supplier"))
        self.actionModify.setText(_translate("OtherWindow", "Modify"))
        self.actionSupplier_2.setText(_translate("OtherWindow", "Supplier"))
        self.actionCustomer_2.setText(_translate("OtherWindow", "Customer"))
        self.actionCustomer_3.setText(_translate("OtherWindow", "Customer"))
        self.actionSupplier_3.setText(_translate("OtherWindow", "Supplier"))
        self.actionDebit.setText(_translate("OtherWindow", "Debit"))
        self.actionCredit.setText(_translate("OtherWindow", "Credit"))
        self.actionSummary.setText(_translate("OtherWindow", "Summary"))
        self.actionSummary_2.setText(_translate("OtherWindow", "Summary"))
        self.actionParty.setText(_translate("OtherWindow", "Party"))
        self.actionParty_2.setText(_translate("OtherWindow", "Party"))
        self.actionAll.setText(_translate("OtherWindow", "All"))
        self.actionAll_2.setText(_translate("OtherWindow", "All"))
        


        











class Ui_Dialog(object):


    def switchToB(self):
        print("hi")
        global x
        global user
        global password
        global valid
        a=self.lineEdit.displayText()
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        b=self.lineEdit_2.displayText()
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        if user==a and password==b:
            print("Welldone")
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            INITIALIZE.massForm.hide()
            INITIALIZE.compForm1.hide()
            INITIALIZE.compForm.show()
            
        else:
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Mismatch in User name and password")       
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()

    
                

    
    

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(353, 164)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 30, 150, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 30, 60, 13))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 70, 150, 20))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 70, 60, 13))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(200, 120, 75, 23))
        self.pushButton.setObjectName("pushButton")


        """Goes to the other script do"""
        self.pushButton.clicked.connect(self.switchToB)
        



        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.label.setText(_translate("Dialog", "User name"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        






class Ui_Dialog1(object):
    
    
    
    def accept(self):
        
        global dc
        global dnc
        global OtherWindow1
        
        dc=self.comboBox.currentText()
        
        dnc=self.spinBox.value()

        
        OtherWindow1.do_this60()
        
        
        


        
    def setupUi(self, Dialog):
        
        Dialog.setObjectName("Dialog")
        Dialog.resize(346, 167)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 120, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 30, 81, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 81, 21))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(150, 30, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Original")
        self.comboBox.addItem("Duplicate")
        self.comboBox.addItem("Triplicate")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(150, 80, 131, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(100)
        self.spinBox.setObjectName("spinBox")

        self.buttonBox.accepted.connect(self.accept)
        

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Copy"))
        self.label_2.setText(_translate("Dialog", "No. of copies"))












class Ui_MainWindow(object):
    
                    

    a=-1 
    b=[]
    e=[]
    states=[]
    

    
    states.append('Andaman & Nicobar Islands')
    states.append('Andhra Pradesh')
    states.append('Andrapradesh(New)')
    states.append('Arunachal Pradesh')
    states.append('Assam')
    states.append('Bihar')
    states.append('Chandigarh')
    states.append('Chhattisgarh')
    states.append('Dadra & Nagar Haveli')
    states.append('Daman & Diu')
    states.append('Delhi')
    states.append('Goa')
    states.append('Gujarat')
    states.append('Haryana')
    states.append('Himachal Pradesh')
    states.append('Jammu & Kashmir')
    states.append('Jharkhand')
    states.append('Karnataka')
    states.append('Kerala')
    states.append('Lakshadweep')
    states.append('Madhya Pradesh')
    states.append('Maharashtra')
    states.append('Manipur')
    states.append('Meghalaya')
    states.append('Mizoram')
    states.append('Nagaland')
    states.append('Orissa')
    states.append('Puducherry')
    states.append('Punjab')
    states.append('Rajasthan')
    states.append('Sikkim')
    states.append('Tamil Nadu')
    states.append('Telengana')
    states.append('Tripura')
    states.append('Uttarakhand')
    states.append('Uttar Pradesh')
    states.append('West Bengal')

    


    
           
    
    def processtrigger(self,q):
      global x
      global user
      global password
      global comp_no
      global state
      print(q.text()+" is triggered")
      self.a=q.text()
      cus.execute("SELECT sno,user_name,password,state FROM COMPANY WHERE name=('%s')"%(self.a))
      d=cus.fetchall()
      for i in d:
          comp_no=i[0]
          user=i[1]
          password=i[2]
          state=i[3]
      
      print(self.a)
      x=self.a
      INITIALIZE.compForm1.show()
      print("yes")
      


      
        

    def do_this(self):
        self.menubar.setEnabled(False)
        
        self.stackedWidget.setCurrentIndex(0)
        print("hi")
        
        self.do_this3()

    def do_this1(self):
        self.menubar.setEnabled(True)
        self.stackedWidget.setCurrentIndex(1)

    def do_this2(self):
        
        a=self.lineEdit_50.displayText()
        b=self.lineEdit_44.displayText()
        self.lineEdit_52.setEchoMode(QtWidgets.QLineEdit.Normal)
        c=self.lineEdit_52.displayText()
        self.lineEdit_52.setEchoMode(QtWidgets.QLineEdit.Password)
        print(c)
        self.lineEdit_51.setEchoMode(QtWidgets.QLineEdit.Normal)
        d=self.lineEdit_51.displayText()
        print(d)
        self.lineEdit_51.setEchoMode(QtWidgets.QLineEdit.Password)
        e=self.lineEdit_46.displayText()
        f=self.lineEdit_47.displayText()
        g=self.lineEdit_45.displayText()
        h=self.lineEdit_48.displayText()
        i=self.lineEdit_37.displayText()
        j=self.lineEdit_43.displayText()
        k=self.lineEdit_49.displayText()
        l=self.comboBox_15.currentText()
        

        if a=='':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Enter Name of the company")
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif b=='':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Enter a User name")
            msg.setWindowTitle("Message")   
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif c=='':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Enter Password")
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif d=='':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Enter Confirmation password")
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif c!=d:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Mismatch of password")
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            self.lineEdit_52.clear()
            self.lineEdit_51.clear()
        elif e=='':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Enter Company GSTIN")
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif f=='':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Enter Phone number")
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif g=='':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Enter Address1")
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif j=='':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Enter City")
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif k=='':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Enter Pincode")
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif l=='':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Enter State")
            msg.setWindowTitle("Message")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        else:
            print("good")
            if h=='':
                cus.execute("INSERT INTO COMPANY (name,user_name,password,GSTIN,phno,add1,city,pincode,state) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(a,b,c,e,f,g,j,k,l))
            elif i=='':
                cus.execute("INSERT INTO COMPANY (name,user_name,password,GSTIN,phno,add1,add2,city,pincode,state) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(a,b,c,e,f,g,h,j,k,l))
            else:
                cus.execute("INSERT INTO COMPANY (name,user_name,password,GSTIN,phno,add1,add2,add3,city,pincode,state) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(a,b,c,e,f,g,h,i,j,k,l))
  
                
                   
            mydb.commit()

            print(a)

            self.menuRecent_Companies.addAction(a)


            
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Company added successfully!")
            msg.setWindowTitle("Message")        
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            self.do_this3()

    def do_this3(self):
        
        self.lineEdit_50.clear()
        self.lineEdit_44.clear()
        self.lineEdit_52.clear()
        self.lineEdit_51.clear()
        self.lineEdit_46.clear()
        self.lineEdit_47.clear()
        self.lineEdit_45.clear()
        self.lineEdit_48.clear()
        self.lineEdit_37.clear()
        
        self.lineEdit_43.clear()
        self.lineEdit_49.clear()
        self.comboBox_15.setCurrentIndex(-1)

   



    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1350, 756)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1386, 750))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.groupBox_9 = QtWidgets.QGroupBox(self.page)
        self.groupBox_9.setGeometry(QtCore.QRect(40, 20, 751, 671))
        self.groupBox_9.setObjectName("groupBox_9")
        self.lineEdit_37 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_37.setGeometry(QtCore.QRect(220, 430, 440, 20))
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.label_72 = QtWidgets.QLabel(self.groupBox_9)
        self.label_72.setGeometry(QtCore.QRect(64, 480, 19, 20))
        self.label_72.setObjectName("label_72")
        self.lineEdit_43 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_43.setGeometry(QtCore.QRect(220, 480, 440, 20))
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.label_74 = QtWidgets.QLabel(self.groupBox_9)
        self.label_74.setGeometry(QtCore.QRect(64, 330, 48, 20))
        self.label_74.setObjectName("label_74")
        self.label_75 = QtWidgets.QLabel(self.groupBox_9)
        self.label_75.setGeometry(QtCore.QRect(64, 580, 26, 20))
        self.label_75.setObjectName("label_75")
        self.lineEdit_44 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_44.setEnabled(True)
        self.lineEdit_44.setGeometry(QtCore.QRect(220, 80, 440, 20))
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.lineEdit_45 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_45.setGeometry(QtCore.QRect(220, 330, 440, 20))
        self.lineEdit_45.setObjectName("lineEdit_45")
        self.lineEdit_46 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_46.setGeometry(QtCore.QRect(220, 230, 440, 20))
        self.lineEdit_46.setFrame(True)
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.label_76 = QtWidgets.QLabel(self.groupBox_9)
        self.label_76.setGeometry(QtCore.QRect(64, 530, 37, 20))
        self.label_76.setObjectName("label_76")
        self.lineEdit_47 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_47.setGeometry(QtCore.QRect(220, 280, 440, 20))
        self.lineEdit_47.setObjectName("lineEdit_47")
        self.layoutWidget_4 = QtWidgets.QWidget(self.groupBox_9)
        self.layoutWidget_4.setGeometry(QtCore.QRect(220, 640, 440, 25))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_11.setContentsMargins(250, 0, 20, 0)
        self.horizontalLayout_11.setSpacing(20)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButton_14 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_11.addWidget(self.pushButton_14)
        self.lineEdit_48 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_48.setGeometry(QtCore.QRect(220, 380, 440, 20))
        self.lineEdit_48.setObjectName("lineEdit_48")
        self.label_77 = QtWidgets.QLabel(self.groupBox_9)
        self.label_77.setGeometry(QtCore.QRect(64, 230, 30, 20))
        self.label_77.setObjectName("label_77")
        self.label_78 = QtWidgets.QLabel(self.groupBox_9)
        self.label_78.setGeometry(QtCore.QRect(64, 280, 45, 20))
        self.label_78.setObjectName("label_78")
        self.label_79 = QtWidgets.QLabel(self.groupBox_9)
        self.label_79.setGeometry(QtCore.QRect(64, 380, 48, 20))
        self.label_79.setObjectName("label_79")
        self.label_80 = QtWidgets.QLabel(self.groupBox_9)
        self.label_80.setGeometry(QtCore.QRect(64, 430, 48, 20))
        self.label_80.setObjectName("label_80")
        self.comboBox_15 = QtWidgets.QComboBox(self.groupBox_9)
        self.comboBox_15.setGeometry(QtCore.QRect(220, 580, 440, 20))
        self.comboBox_15.setObjectName("comboBox_15")
        self.label_81 = QtWidgets.QLabel(self.groupBox_9)
        self.label_81.setGeometry(QtCore.QRect(64, 80, 61, 20))
        self.label_81.setObjectName("label_81")
        self.lineEdit_49 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_49.setGeometry(QtCore.QRect(220, 530, 440, 20))
        self.lineEdit_49.setObjectName("lineEdit_49")
        self.lineEdit_50 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_50.setEnabled(True)
        self.lineEdit_50.setGeometry(QtCore.QRect(220, 30, 440, 20))
        self.lineEdit_50.setObjectName("lineEdit_50")
        self.label_82 = QtWidgets.QLabel(self.groupBox_9)
        self.label_82.setGeometry(QtCore.QRect(64, 30, 81, 20))
        self.label_82.setObjectName("label_82")
        self.lineEdit_51 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_51.setEnabled(True)
        self.lineEdit_51.setGeometry(QtCore.QRect(220, 180, 440, 20))
        self.lineEdit_51.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_51.setObjectName("lineEdit_51")
        self.label_83 = QtWidgets.QLabel(self.groupBox_9)
        self.label_83.setGeometry(QtCore.QRect(64, 180, 91, 20))
        self.label_83.setObjectName("label_83")
        self.lineEdit_52 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_52.setEnabled(True)
        self.lineEdit_52.setGeometry(QtCore.QRect(220, 130, 440, 20))
        self.lineEdit_52.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_52.setObjectName("lineEdit_52")
        self.label_84 = QtWidgets.QLabel(self.groupBox_9)
        self.label_84.setGeometry(QtCore.QRect(64, 130, 61, 20))
        self.label_84.setObjectName("label_84")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(1260, 20, 45, 45))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("E:/BILL_SOFTWARE/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1350, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        
        self.menuRecent_Companies = QtWidgets.QMenu(self.menuFile)
        self.menuRecent_Companies.setObjectName("menuRecent_Companies")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_New_Company = QtWidgets.QAction(MainWindow)
        self.action_New_Company.setCheckable(False)
        self.action_New_Company.setObjectName("action_New_Company")
        self.actionRecent_Companies = QtWidgets.QAction(MainWindow)
        self.actionRecent_Companies.setObjectName("actionRecent_Companies")
        self.actionE_xit = QtWidgets.QAction(MainWindow)
        self.actionE_xit.setObjectName("actionE_xit")
        
        self.menuFile.addAction(self.action_New_Company)
        self.menuFile.addAction(self.menuRecent_Companies.menuAction())
        self.menuFile.addAction(self.actionE_xit)
        self.menubar.addAction(self.menuFile.menuAction())



        self.menuRecent_Companies.triggered.connect(self.processtrigger)
        

        self.stackedWidget.setCurrentIndex(1)
        self.action_New_Company.triggered.connect(self.do_this)
        
        self.pushButton.clicked.connect(self.do_this1)
        self.pushButton_14.clicked.connect(self.do_this2)
        
        self.comboBox_15.addItems(self.states)

        self.retranslateUi(MainWindow)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_50, self.lineEdit_44)
        MainWindow.setTabOrder(self.lineEdit_44, self.lineEdit_52)
        MainWindow.setTabOrder(self.lineEdit_52, self.lineEdit_51)
        MainWindow.setTabOrder(self.lineEdit_51, self.lineEdit_46)
        MainWindow.setTabOrder(self.lineEdit_46, self.lineEdit_47)
        MainWindow.setTabOrder(self.lineEdit_47, self.lineEdit_45)
        MainWindow.setTabOrder(self.lineEdit_45, self.lineEdit_48)
        MainWindow.setTabOrder(self.lineEdit_48, self.lineEdit_37)
        MainWindow.setTabOrder(self.lineEdit_37, self.lineEdit_43)
        MainWindow.setTabOrder(self.lineEdit_43, self.lineEdit_49)
        MainWindow.setTabOrder(self.lineEdit_49, self.comboBox_15)
        MainWindow.setTabOrder(self.comboBox_15, self.pushButton_14)
        MainWindow.setTabOrder(self.pushButton_14, self.pushButton)

    def retranslateUi(self, MainWindow):
        print("how are you")
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Company details"))
        self.label_72.setText(_translate("MainWindow", "City"))
        self.label_74.setText(_translate("MainWindow", "Address 1"))
        self.label_75.setText(_translate("MainWindow", "State"))
        self.label_76.setText(_translate("MainWindow", "Pincode"))
        self.pushButton_14.setText(_translate("MainWindow", "OK"))
        self.label_77.setText(_translate("MainWindow", "GSTIN"))
        self.label_78.setText(_translate("MainWindow", "Phone no"))
        self.label_79.setText(_translate("MainWindow", "Address 2"))
        self.label_80.setText(_translate("MainWindow", "Address 3"))
        self.label_81.setText(_translate("MainWindow", "User name"))
        self.label_82.setText(_translate("MainWindow", "Company Name"))
        self.label_83.setText(_translate("MainWindow", "Confirm Password"))
        self.label_84.setText(_translate("MainWindow", "Password"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.action_New_Company.setText(_translate("MainWindow", "&New Company"))
        self.menuRecent_Companies.setTitle(_translate("MainWindow", "Recent  &Companies"))
        
        cus.execute("SELECT name FROM COMPANY")
        a=cus.fetchall()        
        for i in a:
            self.menuRecent_Companies.addAction(i[0])
            
            
        self.actionE_xit.setText(_translate("MainWindow", "E&xit"))




class INITIALIZE:
    def __init__(self):
        global OtherWindow1
        app=QtWidgets.QApplication(sys.argv)
        INITIALIZE.massForm = QtWidgets.QMainWindow()
        MainWindow=Ui_MainWindow()        
        MainWindow.setupUi(INITIALIZE.massForm)
        INITIALIZE.massForm.show()
        
        
        INITIALIZE.compForm = QtWidgets.QMainWindow()
        OtherWindow1=Ui_OtherWindow()
        OtherWindow1.setupUi(INITIALIZE.compForm)
        
        INITIALIZE.compForm1 = QtWidgets.QDialog()
        Dialog=Ui_Dialog()
        Dialog.setupUi(INITIALIZE.compForm1)

        INITIALIZE.compForm2 = QtWidgets.QDialog()
        Dialog1 = Ui_Dialog1()
        Dialog1.setupUi(INITIALIZE.compForm2)
        
        app.exec()

def main():
    program=INITIALIZE()

if __name__=='__main__':
    main()
