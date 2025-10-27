from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os
from init_db import init_db

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Required for flash messages

# Initialize the database when the app starts
init_db()

def get_db():
    # Ensure data directory exists
    if not os.path.exists('data'):
        os.makedirs('data')
    return sqlite3.connect('data/todos.db')

@app.route('/')
def index():
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT * FROM tasks ORDER BY created_at DESC')
    tasks = c.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    description = request.form['description']
    
    if not title:
        flash('Title is required!', 'error')
        return redirect(url_for('index'))
    
    conn = get_db()
    c = conn.cursor()
    c.execute('INSERT INTO tasks (title, description) VALUES (?, ?)',
              (title, description))
    conn.commit()
    conn.close()
    
    flash('Task added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/complete/<int:id>')
def complete(id):
    conn = get_db()
    c = conn.cursor()
    c.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    
    flash('Task marked as complete!', 'success')
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db()
    c = conn.cursor()
    c.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    
    flash('Task deleted!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
