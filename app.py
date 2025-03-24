from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import socket
import sqlite3
from datetime import datetime

app = Flask(__name__)

DATABASE = '/src/db/images.db' # Name of our database file

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row # Return rows as dictionaries
    return conn

def init_db():
    conn = get_db_connection()
    with app.open_resource('schema.sql') as f:
        conn.executescript(f.read().decode('utf8'))
    conn.commit()
    conn.close()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')

@app.route('/', methods=['GET'])
def index():
    conn = get_db_connection()
    images = conn.execute('SELECT * FROM images').fetchall()
    conn.close()
    return render_template('index.html', images=images)

@app.route('/api/add', methods=['POST'])
def add():
    if request.method == 'POST':
        data = request.get_json()  # Get JSON data from the request body
        if data:
        	conn = get_db_connection()
        	try:
        		conn.execute('INSERT INTO images (name, version, status) VALUES (?, ?, ?)', (data["name"], data["version"], data["status"]))
        		conn.commit()
        		conn.close()
        		return jsonify({"message": "Created Successfully {}-{}".format(data["name"], data["version"])}), 201
        	except Exception as e:
        		conn.close()
        		return jsonify({"message": str(e)}), 400
        else:
            return jsonify({"error": "No JSON data provided"}), 400  # 400 Bad Request

@app.route('/api/update', methods=['POST'])
def update():
    if request.method == 'POST':
        data = request.get_json()  # Get JSON data from the request body
        if data:
        	conn = get_db_connection()
        	try:
        		conn.execute('UPDATE images SET status = ?, updated_date = ? WHERE name = ? AND version = ?', (data["status"], datetime.now(), data["name"], data["version"]))
        		conn.commit()
        		conn.close()
        		return jsonify({"message": "Updated Successfully {}-{}".format(data["name"], data["version"])}), 200
        	except Exception as e:
        		conn.close()
        		return jsonify({"message": str(e)}), 400
        else:
            return jsonify({"error": "No JSON data provided"}), 400  # 400 Bad Request

@app.route('/api/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        data = request.get_json()  # Get JSON data from the request body
        if data:
        	conn = get_db_connection()
        	try:
        		conn.execute('DELETE FROM images WHERE name = ? AND version = ?', (data["name"], data["version"]))
        		conn.commit()
        		conn.close()
        		return jsonify({"message": "Deleted Successfully {}-{}".format(data["name"], data["version"])}), 200
        	except Exception as e:
        		conn.close()
        		return jsonify({"message": str(e)}), 400
        else:
            return jsonify({"error": "No JSON data provided"}), 400  # 400 Bad Request

@app.route('/api/get_all_pending_images', methods=['GET'])
def get_all_pending_images():
    conn = get_db_connection()
    images = conn.execute('SELECT * FROM images WHERE status = "PENDING"').fetchall()
    conn.close()
    image_list = [dict(image) for image in images]
    return jsonify({"message": "List of PENDING status images", "data": image_list}), 200