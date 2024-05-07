-- Create a new database called 'student_database'
CREATE DATABASE IF NOT EXISTS student_database;

-- Switch to 'student_database'
USE student_database;

-- Create a table to store student information
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    cgpa DECIMAL(3, 2) NOT NULL
);

-- Insert some sample data into the 'students' table
INSERT INTO students (name,Id, age, cgpa) VALUES
    ('Shahd',1, 20, 3.5),
    ('Malak',2, 20, 3.5),
    ('Habiba',3, 20, 3.5),
    ('Hamas',4, 20, 3.5);
