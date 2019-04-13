from flask import Flask, render_template, redirect, request
import pandas as pd
import mysql.connector

app = Flask(__name__)

# loads query from sql database to pandas df
def load_sql_table(query):
    try:
        df = pd.read_sql(query, con=connector)
        return df
    except:
        return None

@app.route('/')
def start_redirect():
    return redirect("http://127.0.0.1:5000/dashboard.html", code=302)

@app.route('/dashboard.html', methods=['GET', 'POST'])
def start_dashboard():
    # Ask for all tables in your SQL Database
    # Request might look different for non MySQL
    # E.g. for SQL Server: sql_statement = "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'"
    # TODO: Modify for your needs
    sql_statement = "SHOW TABLES"
    tables = load_sql_table(sql_statement)

    if request.method == 'POST':
        whichTable = request.form['whichTable']
        # Load the requested table from Database
        # TODO: Set your database query for the chosen table (e.g. modify db schema)
        SQL_table = "SELECT * FROM " + whichTable
        table = load_sql_table(SQL_table)
        result = table.reset_index().to_json(orient='records')
        return render_template('dashboard.html', tables=tables, table=result, selectedTable=whichTable)

    else:
        result = []
        return render_template('dashboard.html', tables=tables, table=result, selectedTable='None')


if __name__ == '__main__':
    # connect to your database
    try:
        # TODO: Use Library of your needs
        # E.g. for SQL Server it might be pyodbc
        # use 127.0.0.1 if localhost
        connector = mysql.connector.connect(user='root', password='shoaib', host='127.0.0.1', database='classicmodels')
    except:
        print("No access to the required database")
    app.run()
