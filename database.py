# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 11:47:48 2022

@author: hp
"""

import sqlite3
conn=sqlite3.connect(r"C:\Users\hp\Python Project\pythonsqlite.db",check_same_thread=False)
c=conn.cursor()
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS person(person_id INTEGER  PRIMARY KEY,person_name TEXT,person_no INTEGER,person_dept TEXT,person_record_date DATE)')
def add_data(person_id,person_name,person_no,person_dept,person_record_date):
    c.execute('INSERT INTO person(person_id,person_name,person_no,person_dept,person_record_date) VALUES (?,?,?,?,?)',(person_id,person_name,person_no,person_dept,person_record_date))
    conn.commit()
def view_all_person():
    c.execute('select *from person')
    data=c.fetchall()
    return data
def view_update():
    c.execute('select distinct person_dept from person')
    data = c.fetchall()
    return data
def get_department(person_dept):
    c.execute('select * from person where person_dept="{}"'.format(person_dept))
    data = c.fetchall()
    return data
def update(new_person_dept,new_person_record_date,person_id):
    c.execute('update person set person_dept=?,person_record_date=? where person_id=?',(new_person_dept,new_person_record_date,person_id))
    conn.commit()
    data=c.fetchall()
    return data
def delete(person_dept):
    c.execute('delete from person where person_dept="{}"'.format(person_dept))
    conn.commit()