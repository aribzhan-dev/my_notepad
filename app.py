from flask import Flask, render_template, request, redirect
from config import collection
from models.note_model import Note
from api.note_api import note_api

app = Flask(__name__)
app.register_blueprint(note_api)

@app.route('/')
def index():
    notes = Note.get_all(collection)
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add_note():
    title = request.form['title']
    desc = request.form['desc']
    note = Note(title, desc)
    note.save(collection)
    return redirect('/')

@app.route('/delete/<note_id>')
def delete_note(note_id):
    Note.delete(collection, note_id)
    return redirect('/')

@app.route('/update/<note_id>', methods=['POST'])
def update_note(note_id):
    title = request.form['title']
    desc = request.form['desc']
    Note.update(collection, note_id, title, desc)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
