# -*- coding: utf-8 -*-
"""
Created on Sun Jan 1 15:38:30 2017

author: lak
"""

import sqlite3 

db = sqlite3.connect('library_data.db')
c = db.cursor()

c.executescript('''
PRAGMA Foreign_Keys=True;

CREATE TABLE IF NOT EXISTS  authors (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE NOT NULL
    );

CREATE TABLE IF NOT EXISTS publishers (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    publisher TEXT UNIQUE NOT NULL
    );
    
CREATE TABLE IF NOT EXISTS languages (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    language TEXT UNIQUE NOT NULL
    );

CREATE TABLE IF NOT EXISTS resource_medium (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    medium TEXT UNIQUE
    );

CREATE TABLE IF NOT EXISTS keywords (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    keyword TEXT UNIQUE
    );
    

CREATE TABLE IF NOT EXISTS resource (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE NOT NULL,
    year INTEGER,
    pages INTEGER,
    languageID INTEGER REFERENCES languages(ID),
    mediaID INTEGER REFERENCES resource_medium(ID),
    publisherID INTEGER REFERENCES publishers(ID),
    abstract TEXT
    );

CREATE TABLE IF NOT EXISTS RESOURCE_AUTHOR(  
    resourceID INTEGER,
    authorID INTEGER,
    PRIMARY KEY (resourceID, authorID)
    );    

CREATE TABLE IF NOT EXISTS RESOURCE_KEYWORDS(
    resourceID INTEGER,
    keywordID INTEGER,
    PRIMARY KEY(resourceID, keywordID)
    );


CREATE TABLE IF NOT EXISTS project_category(
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    category TEXT UNIQUE
    );


CREATE TABLE IF NOT EXISTS projects (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    project_name TEXT NOT NULL,
    project_category INTEGER REFERENCES project_category(ID),
    description TEXT,
    date_start DATE, 
    date_end DATE 
    );
    

CREATE TABLE IF NOT EXISTS PROJECT_REFERENCES(
    projectID INTEGER,
    resourceID INTEGER,
    PRIMARY KEY (projectID, resourceID)
    );

    ''')

db.commit()
db.close()

