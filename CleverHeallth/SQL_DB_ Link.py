import sqlite3

from flask import Flask, render_template, request

conn = sqlite3.connect('SQL_DB.db')
