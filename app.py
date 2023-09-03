from flask import Flask, render_template, request, jsonify,send_file,redirect,Response
import sqlite3
from datetime import date
from datetime import datetime
import pandas as pd
import time
import telepot
from flask_mail import Mail, Message
import json
import qrcode
from PIL import Image
import os
import cv2
from pyzbar.pyzbar import decode
import pyautogui


# Import rat detection module
from rat_detection import detect_rats
# app = Flask(app_name) # pick the name

# import smtplib
# import string


    




bot = telepot.Bot("5943603253:AAGItzemm6TQ7zC-QNURi3Tk_dEouTRqLbU")

con = sqlite3.connect('DataBase.db')
cr = con.cursor()
cr.execute('create table if not exists products1(Id TEXT, Name TEXT, Type TEXT, Date TEXT,Quantity INTEGER,Qrstatus INTEGER)')

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
if not os.path.exists(app.config['UPLOAD_FOLDER']):
   os.makedirs(app.config['UPLOAD_FOLDER'])

# app.config['MAIL_SERVER']='smtp.mail.me.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sharonkumarallaparthi@gmail.com'
app.config['MAIL_PASSWORD'] = 'acwhzwzirvvajvkm'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def index():
   return render_template("index.html")
   os.system('cmd /k "python rat_detection/detect.py"')
   
@app.route('/get_data')
def get_data():
   from serial_test import read_data
   data = read_data()
   print("recieved data {}".format(data))
   if float(data[2]) > 100.0:
      print('gas detected')
      bot.sendMessage('1200270414', str('gas detected'))
   if float(data[3]) < 5.0 :
      print('low weight')
      bot.sendMessage('1200270414', str('low weight'))
   return jsonify(data)

@app.route('/get_data1')
def get_data1():
   con = sqlite3.connect('DataBase.db')
   cr = con.cursor()

   cr.execute('select * from products1')
   result = cr.fetchall()

   today = date.today()
   today = pd.to_datetime(today)
   List = []
   for row in result:
      end = pd.to_datetime(row[3])
      if today > end:
         List.append(row)
   
   if not (List is None):
      Data = []
      for row in List:
         Data.append("product validity expired, Details: product id {}, product name {}, product type {}, expiry date {}, quantity {}, QR Status {}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
      return jsonify(Data)
   return jsonify('ok')

class A:
   i=0
   def __init(self):
      A.i+=1

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
   
   if request.method == 'POST':
      Id = request.form['id']
      Name = request.form['name']
      Type = request.form['type']
      Date = request.form['edate']
      Quantity=request.form['quantity']
      Qrstatus=request.form['qrstatus']
      if len(Name.split('-'))!=2:
         pyautogui.alert("Enter the Field Properly for Product-Company Name")
         return render_template('addproduct.html')
      data = [Id, Name, Type, Date,Quantity,Qrstatus]
      print(data,data)

      con = sqlite3.connect('DataBase.db')
      cr = con.cursor()
      cr.execute('insert into products1 values(?, ?, ?, ?,?,?)', data)
      cursor = con.execute('SELECT * FROM products1 WHERE ID = ?', (data[0],))
      row_data = cursor.fetchone()
      print(row_data)
      row_data_str = json.dumps(row_data)
      # if(Qrstatus==1):
      qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
      qr.add_data(row_data_str)
      qr.make(fit=True)
      qr_image = qr.make_image(fill_color="black", back_color="white")
      # a=A()
      qr_image.save('qr_code'+data[0]+'.png')
      img_path = os.path.join("C:/Users/sharon/Desktop/combine/warehouse/", 'qr_code'+data[0]+'.png')
      qr_image.save(img_path)
      print(img_path,"okijuhg")
      con.commit()
      return render_template('addproduct.html',qrstatus=Qrstatus)
   return render_template('addproduct.html')
#FOR forms must keep methods attribute else the route will not execute !IMP
@app.route('/existing_product',methods=['POST','GET'])
def existing_product():
   if request.method == 'POST':
      Name = request.form['name']
      Type = request.form['type']
      Quantity=request.form['quantity']
      if len(Name.split('-'))!=2:
         pyautogui.alert("Enter the Field Properly for Product-Company Name")
         return render_template('addproduct.html')
      con = sqlite3.connect('DataBase.db')
      cr = con.cursor()
      a=con.execute('SELECT Quantity FROM products1 WHERE NAME=? AND TYPE=?', (Name,Type))
      qrid=json.dumps(con.execute('SELECT ID FROM products1 WHERE NAME=? AND TYPE=?', (Name,Type)).fetchone())[2:-2]
      print(a,a)
      b=json.dumps(a.fetchone())
      print(b)
      b=b[1:-1]
      Quantity=int(Quantity)+int(b)
      cursor = con.execute('UPDATE products1 SET Quantity =? WHERE NAME=? AND TYPE=?', (Quantity,Name,Type))
      con.commit()
      return redirect('/decode/'+str(qrid)) 
   return render_template('addproduct.html')   
@app.route('/cardscan')
def cardscan():
   from serial_test import read_data1
   data = read_data1()
   print('recieved data '+data)
   
   con = sqlite3.connect('DataBase.db')
   cr = con.cursor()

   cr.execute("select * from products1 where Id = '"+data+"'")
   result = cr.fetchone()
   print(result)
   return render_template('viewdata.html', result=result)


@app.route('/delete/<qr_id>')
def deleteproduct(qr_id):
   con = sqlite3.connect('DataBase.db')
   cr = con.cursor()
   
   cursor = con.execute('Delete FROM products1 WHERE ID = ?', (str(qr_id),))
   con.commit()
   return redirect('/viewdata',code=302)

@app.route('/viewdata')
def viewdata():
      con = sqlite3.connect('DataBase.db')
      cr = con.cursor()

      cr.execute("select * from products1")
      result = cr.fetchall()
      print(result)
      return render_template('viewdata.html', products=result)

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/productone/<qr_id>')
def productone(qr_id):
   return render_template('productone.html',qr_id=qr_id)
@app.route('/producttwo')
def product1():
   return render_template('producttwo.html')
@app.route('/contact')
def contact():
   return render_template('contact.html')
@app.route('/mail',methods=['GET','POST'])
def mails():
   # #return render_template('index.html')
   if request.method=="POST":
      msg= request.form['message']
      subject=request.form['subject']
      firstname=request.form['first_name']
      lastname=request.form['last_name']
      phone=request.form['Phone']
      m=request.form['email']

      messages=Message(subject,sender='dnoorali2015@gmail.com',recipients=['1rn19cs037.noor@gmail.com'])
      messages.body=msg
      mail.send(messages)
      success="Message Sent"
      return render_template('index.html',success=success)   


@app.route('/qr/<qr_id>')
def qr(qr_id):
   return render_template('qrcode.html',qr_id=qr_id)

@app.route('/qr/img/<qr_id>')
def qr_img(qr_id):
   
   print(qr_id)
   # img_path = os.path.join(app.config['UPLOAD_FOLDER'], f'qr_code{qr_id}.png')
   # print(img_path,img_path)
   
   
   
   return send_file(os.path.join("C:/Users/sharon/Desktop/combine/warehouse/qr_code"+str(qr_id)+".png"), mimetype='image/png')
   # if os.path.exists(img_path):
   #    return send_file(img_path, mimetype='image/png')
   # else:
   #    return 'QR code not found', 404


@ app.route('/decode/<qr_id>')
def decode(qr_id):
   print(qr_id)
   s='qr_code'+str(qr_id)+'.png'
   print(s,s,qr_id)

   con = sqlite3.connect('DataBase.db')
   cr = con.cursor()
   
   cursor = con.execute('SELECT * FROM products1 WHERE ID = ?', (str(qr_id),))
   row_data = cursor.fetchone()
   print(row_data)
   
   con.commit()
   return render_template('qrpage.html',row_data=row_data)


@app.route('/video_feed')
def video_feed():
   return Response(detect_rats("http://192.168.177.133:8080/video"))


def get_type(value):
    return type(value).__name__

# Register the filter with the Jinja environment
app.jinja_env.filters['get_type'] = get_type

if __name__ == "__main__":
   # app.run(debug=True, use_reloader=False)
   app.run(debug=True)
