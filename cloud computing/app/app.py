import mysql.connector
from flask import Flask, render_template

app = Flask(__name__, template_folder='tamplates')
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page2.html')
def display_data():
    # Connect to MySQL
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="5073376",
        database="student_database"
    )

    # Execute SQL query
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM students")

    # Fetch data
    data = cursor.fetchall()

    # Close connection
    mydb.close()

    # Render HTML template with data
    return render_template('page2.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
