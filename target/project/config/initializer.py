#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('Database.db')

with con:
    
    cur = con.cursor()
    
    #Create data for the user table
    cur.execute("CREATE TABLE users(UserId INT, UserName TEXT, Password TEXT)")
    cur.execute("INSERT INTO users VALUES(1,'Admin','0cef1fb10f60529028a71f58e54ed07b')")
    cur.execute("INSERT INTO users VALUES(2,'User','022b5ac7ea72a5ee3bfc6b3eb461f2fc')")
    cur.execute("INSERT INTO users VALUES(3,'Guest','94ca112be7fc3f3934c45c6809875168')")
    cur.execute("INSERT INTO users VALUES(4,'Plebian','0cbdc7572ff7d07cc6807a5b102a3b93')")
    
    #Create some data for pageinformation
    cur.execute("CREATE TABLE pages(pageId INT, title TEXT, content TEXT)")
    cur.execute("INSERT INTO pages VALUES(1,'The Dashboard','So, here we are. After a lot of hard work and hassle here we have the dashboard finally up and running. Please take note of this message since it will be updated a lot!')")
    cur.execute("INSERT INTO pages VALUES(2,'Seccond page','why is there a seccond page, we are going to update the first one right?')")

    #Create some data for messaging
    cur.execute("CREATE TABLE messages(messageId INT, name TEXT, message TEXT, link TEXT, [timestamp] timestamp )")
    cur.execute("INSERT INTO messages VALUES(1,'Jack Sparrow','Bring me them treasure', 'https://www.google.nl/search?q=pirate+treasure&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjHncGMn6DaAhVBJsAKHeJUCpsQ_AUICigB&biw=1303&bih=879#imgrc=vHC7-cQ7t5N1IM:', '2012-12-25 16:59:59')")
    cur.execute("INSERT INTO messages VALUES(2,'C. Ash', 'Can we please stay on topic and serious?', '', '2012-12-25 18:21:17')")
    
    con.commit()
    #con.close()
