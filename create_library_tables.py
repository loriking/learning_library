# -*- coding: utf-8 -*-
"""
Created on Sun Jan 1 15:38:30 2017

author: lak
"""

import sqlite3 

def make_db():
    db = sqlite3.connect('learning_stack.db')
    c = db.cursor()

    c.executescript('''
    PRAGMA Foreign_Keys=True;
    
    CREATE TABLE IF NOT EXISTS languages (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        language TEXT UNIQUE NOT NULL
        );
        
    CREATE TABLE IF NOT EXISTS authors (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE NOT NULL
        );
    
    CREATE TABLE IF NOT EXISTS publishers (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        publisher TEXT UNIQUE NOT NULL
        );
    
    CREATE TABLE IF NOT EXISTS subjects (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        subject TEXT UNIQUE
        );
        
    CREATE TABLE IF NOT EXISTS levels (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        level TEXT NOT NULL
        );

    CREATE TABLE IF NOT EXISTS resource_medium (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        medium TEXT UNIQUE
        );
    
    CREATE TABLE IF NOT EXISTS game_engine(
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE  
        );
        
    CREATE TABLE IF NOT EXISTS platform (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE  
        );
        
    CREATE TABLE IF NOT EXISTS website_name (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE  
        );
        
    CREATE TABLE IF NOT EXISTS producers(
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT NOT NULL
        );
        
    CREATE TABLE IF NOT EXISTS provider(
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT NOT NULL
        );
    
    
    CREATE TABLE IF NOT EXISTS texts (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT NOT NULL UNIQUE,
        year INTEGER,
        pages INTEGER,
        subjectID INTEGER REFERENCES subjects(ID),
        notes TEXT,
        publisherID INTEGER REFERENCES publishers(ID),
        languageID INTEGER REFERENCES languages(ID),
        mediaID INTEGER REFERENCES resource_medium(ID),
        levelID INTEGER REFERENCES levels(ID)
        );
    
    CREATE TABLE IF NOT EXISTS websites (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT NOT NULL,
        creation_date INTEGER,
        subjectID INTEGER REFERENCES subjects(ID),
        website_nameID INTEGER REFERENCES website_name(ID),
        url TEXT,
        access_date INTEGER,
        notes TEXT,
        mediaID INTEGER REFERENCES resource_medium(ID)
        );
            
    CREATE TABLE IF NOT EXISTS audio (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT NOT NULL,
        duration_secs INTEGER NOT NULL,
        subjectID INTEGER REFERENCES subjects(ID),
        producerID INTEGER REFERENCES producers(ID),
        year INTEGER,
        program TEXT,
        url TEXT,
        mediaID INTEGER REFERENCES resource_medium(ID),
        languageID INTEGER REFERENCES languages(ID)
        );
             
    CREATE TABLE IF NOT EXISTS video (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT NOT NULL,
        duration_mins INTEGER NOT NULL,
        subjectID INTEGER REFERENCES subjects(ID),
        producerID INTEGER REFERENCES producers(ID),
        year INTEGER,
        url TEXT,
        comments TEXT,
        mediaID INTEGER REFERENCES resource_medium(ID),
        languageID INTEGER REFERENCES languages(ID)
        );   
    
    CREATE TABLE IF NOT EXISTS courses (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT NOT NULL,
        providerID INTEGER REFERENCES provider(ID),
        url TEXT,
        subjectID INTEGER REFERENCES subjects(ID),
        start_date TEXT NOT NULL,
        duration_weeks INTEGER,
        comments TEXT,
        mediaID INTEGER REFERENCES resource_medium(ID),
        levelID INTEGER REFERENCES levels(ID)
        );
        
    CREATE TABLE IF NOT EXISTS interactive_media(
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT NOT NULL,
        year INTEGER,
        subjectID INTEGER REFERENCES subjects(ID),
        platformID INTEGER REFERENCES platform(ID),
        engineID INTEGER REFERENCES game_engine(ID),
        version REAL,
        comments TEXT,
        mediaID INTEGER REFERENCES resource_medium(ID)        
        );
        
    CREATE TABLE IF NOT EXISTS images(
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT NOT NULL,
        date INTEGER,
        copywrite TEXT,
        dimensions TEXT,
        website_nameID INTEGER REFERENCES website_name(ID),
        url TEXT,
        comments TEXT,       
        mediaID INTEGER REFERENCES resource_medium(ID)
        );
        
    CREATE TABLE IF NOT EXISTS resource_author(  
        resourceID INTEGER,
        authorID INTEGER,
        mediaID INTEGER,
        PRIMARY KEY (resourceID, authorID, mediaID)
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
        date_start TEXT, 
        date_end TEXT 
        );
        
    CREATE TABLE IF NOT EXISTS project_references(
        projectID INTEGER,
        resourceID INTEGER,
        mediaID INTEGER,
        PRIMARY KEY (projectID, resourceID, mediaID) 
        );
    ''')


    db.commit()


    default_languages = ['English']
    default_levels = ['Absolute Beginner', 'Beginner', 'Advanced Beginner', 'Low Intermediate', 'Intermediate',
                      'Low Advanced', 'Advanced', 'Professional']
    default_project_type = ['Python App']
    default_publisher = ['Unpublished']
    default_media_types = ['Book', 'Short story', 'Other text',
                           'Music', 'Sound', 'Podcast',
                           'Feature Film', 'Documentary', 'Other video',
                           'Audio only', 'MOOC', 'Blended Class',
                           'Photo', 'Clip art','Sprite',
                           'Interactive Fiction', 'Video game', 'Other interactive',
                           'Website', 'Documentation', 'Q&A Site']

    for i in default_languages:
        c.execute('INSERT OR IGNORE INTO languages(language) VALUES(?)', (i,))
    for i in default_levels:
        c.execute('INSERT OR IGNORE INTO levels(level) VALUES(?)', (i,))
    for i in default_project_type:
        c.execute('INSERT OR IGNORE INTO project_category(category) VALUES(?)', (i,))
    for i in default_publisher:
        c.execute('INSERT OR IGNORE INTO publishers(publisher) VALUES(?)', (i,))
    for i in default_media_types:
        c.execute('INSERT OR IGNORE INTO resource_medium(medium) VALUES(?)', (i,))


    db.commit()
    db.close()



if __name__ == '__main__':
    make_db()