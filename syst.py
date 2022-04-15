'''##############################################  LIBRARIES  ##############################################'''


import PySide2
import PySide2.QtWidgets
from ui import Ui_MainWindow
import sys
from price import prices
import os 
import tempfile
import mysql.connector



'''##############################################  INITIALIZATION  ##############################################'''


app = PySide2.QtWidgets.QApplication(sys.argv)
MainWindow = PySide2.QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


'''##############################################  Variable  ##############################################'''


finall_price = []
drinks = []
bill = []
total_for_manager = []
lines = []
password = "01060219132"


'''##############################################  LOGIC  ##############################################'''




myconn = mysql.connector.connect(
    host = "localhost" ,
    user = "root" ,
    passwd = "" ,
    database = "prices"
)
mycurs = myconn.cursor()

def header():
    global temp
    temp = tempfile.mktemp('.txt')    
    open(temp,'a').write(f"Bill for{ui.lineEdit_2.text()}\n")
    open(temp,'a').write(f"drink\t\tprice\t\tQty.\t\tTotal")


def add_database(x):
    sql = "INSERT INTO get_prices (drink , price) VALUES(%s,%s)"
    data = ("Mint", x )
    mycurs.execute(sql, data)
    myconn.commit()


def ret_func(x,y):
    mycurs.execute(f"SELECT price FROM get_prices WHERE {y} like '%{x}%' ")
    result = eval(mycurs.fetchall()[0][0])
    return result



def get_price():
    global z
    z = ui.spinBox.value()
    
    if z != 0:
        if ui.comboBox_4.currentText()!="Nothing" :
            drinks.append(ui.comboBox_4.currentText())
            finall_price.append(ret_func(ui.comboBox_4.currentText())*z)
            ui.lcdNumber_2.display(ret_func(ui.comboBox_4.currentText())*z)
            string = f"\n{ui.comboBox_4.currentText(),'drink'}\t\t{ret_func(ui.comboBox_4.currentText(),'drink')}EGP\t\t{z}\t\t{(z*ret_func(ui.comboBox_4.currentText(),'drink'))}EGP \n"
            open(temp,'a').write(f"{string}")

        if ui.comboBox_3.currentText()!="Nothing" :
            drinks.append(ui.comboBox_3.currentText())
            finall_price.append(ret_func(ui.comboBox_3.currentText())*z)
            ui.lcdNumber_2.display(ret_func(ui.comboBox_3.currentText())*z)
            string = f"\n{ui.comboBox_3.currentText(),'drink'}\t\t{ret_func(ui.comboBox_3.currentText(),'drink')}EGP\t\t{z}\t\t{(z*ret_func(ui.comboBox_3.currentText(),'drink'))}EGP \n"
            open(temp,'a').write(f"{string}")
        
        if ui.comboBox_5.currentText()!="Nothing" :
            drinks.append(ui.comboBox_5.currentText())
            finall_price.append(ret_func(ui.comboBox_5.currentText())*z)
            ui.lcdNumber_2.display(ret_func(ui.comboBox_5.currentText())*z)
            string = f"\n{ui.comboBox_5.currentText(),'drink'}\t\t{ret_func(ui.comboBox_5.currentText(),'drink')}EGP\t\t{z}\t\t{(z*ret_func(ui.comboBox_5.currentText(),'drink'))}EGP \n"
            open(temp,'a').write(f"{string}")
    
    ui.comboBox_4.setCurrentText("Nothing")
    ui.comboBox_3.setCurrentText("Nothing")
    ui.comboBox_5.setCurrentText("Nothing")


def add_fun():      
    if z != 0:        
        y = 0
        try:
            for i in range(len(finall_price)):
                y += finall_price[i]
                print(y)
                bill.append(y)
            ui.lcdNumber_2.display(bill[-1])
        except:
            ui.lcdNumber_2.display("err")

        ui.spinBox.setValue(0) 


def del_line():
    with open(temp, 'r+') as fp:
        # read an store all lines into list
        lines = fp.readlines()
        # move file pointer to the beginning of a file
        fp.seek(0)
        # truncate the file
        fp.truncate()

        # start writing lines except the last line
        # lines[:-1] from line 0 to the second last line
        fp.writelines(lines[:-1])




def rst():
    try:
        drinks.clear()
        finall_price.clear()
        bill.clear()
        os.remove(temp)
        ui.lineEdit_2.setText("")
        ui.lcdNumber_2.display(0)
        ui.comboBox_4.setCurrentText("Nothing")
        ui.comboBox_3.setCurrentText("Nothing")
        ui.comboBox_5.setCurrentText("Nothing")
    except:
        ui.lcdNumber_2.display("err")    

 

def printfun():
    add_fun()
    total_for_manager.append(bill[-1])
    print(total_for_manager)
    
    try:
        open(temp,'a').write(f"\n total price \t\t {bill[-1]} EGP")
        if bill[-1] > 0:
            os.startfile(temp,"print")
            ui.lcdNumber.display(0)
            ui.comboBox.setCurrentText("Nothing")
            ui.comboBox_2.setCurrentText("Nothing")
    except:
        ui.lcdNumber.display("err")




def tot_money():
    tot = 0
    for i in range(len(total_for_manager)):
        tot += total_for_manager[i]
        print(tot)
    
    if ui.lineEdit_3.text() == password:
        ui.label_16.setText(f"Total = {tot} EGP")
    else:
        ui.label_16.setText("You are not authorized to know")
    

'''##############################################  Buttons Connection  ##############################################'''

ui.pushButton_6.clicked.connect(get_price)
ui.pushButton_5.clicked.connect(printfun)
ui.pushButton_4.clicked.connect(rst)
ui.pushButton_7.clicked.connect(tot_money)
ui.pushButton_8.clicked.connect(header)
ui.pushButton_9.clicked.connect(del_line)

'''##############################################  SYS EXIT  ##############################################'''

sys.exit(app.exec_())