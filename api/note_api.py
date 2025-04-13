from flask import Blueprint, request, jsonify
from models.note_model import Note
from config import collection

note_api = Blueprint('note_api', __name__)

@note_api.route('/api/notes', methods=['GET'])
def get_notes():
    notes = Note.get_all(collection)
    return jsonify([{
        "id": note.id,
        "title": note.title,
        "desc": note.desc,
        "status": note.status
    } for note in notes])

@note_api.route('/api/notes', methods=['POST'])
def create_note():
    data = request.get_json()
    note = Note(data['title'], data['desc'])
    note.save(collection)
    return jsonify({
        "id": str(note.id),
        "title": note.title,
        "desc": note.desc,
        "status": note.status
    }), 201

@note_api.route('/api/notes/<note_id>', methods=['PUT'])
def update_note(note_id):
    data = request.get_json()
    Note.update(collection, note_id, data['title'], data['desc'])
    return jsonify({"message": "Note updated successfully"})

@note_api.route('/api/notes/<note_id>', methods=['DELETE'])
def delete_note(note_id):
    Note.delete(collection, note_id)
    return jsonify({"message": "Note deleted successfully"})
