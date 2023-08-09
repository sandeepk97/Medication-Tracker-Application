from flask import Blueprint, jsonify
from medication.service import get_medication_list, add_medication, update_medication_by_id, delete_medication_by_id, update_medication_completion, get_medication_completion, add_notes, view_notes, update_notes, delete_notes

medication_bp = Blueprint('medication', __name__)



@medication_bp.route('/list', methods=['GET'])
def get_all_medications():
    medication = get_medication_list()
    return jsonify(medication)


@medication_bp.route('/add', methods=['POST'])
def get_medication_id():
    medication = add_medication()
    return jsonify(medication)

@medication_bp.route('/update/:id', methods=['POST'])
def update_medication(medication_id):
    medication = update_medication_by_id(medication_id)
    return jsonify(medication)

@medication_bp.route('/delete/:id', methods=['POST'])
def delete_medication(medication_id):
    medication = delete_medication_by_id(medication_id)
    return jsonify(medication)

@medication_bp.route('/completion/:id', methods=['POST'])
def update_medication_completion_def(medication_id):
    medication = update_medication_completion(medication_id)
    return jsonify(medication)

@medication_bp.route('/completion/:id', methods=['GET'])
def get_completion(medication_id):
    medication = get_medication_completion(medication_id)
    return jsonify(medication)

@medication_bp.route('/notes/add/:id', methods=['POST'])
def add_notes_def(medication_id):
    notes = add_notes(medication_id)
    return jsonify(notes)

@medication_bp.route('/notes/:id', methods=['GET'])
def view_notes_def(notes_id):
    notes = view_notes(notes_id)
    return jsonify(notes)

@medication_bp.route('/notes/update/:id', methods=['POST'])
def update_notes_def(notes_id):
    notes = update_notes(notes_id)
    return jsonify(notes)

@medication_bp.route('/notes/delete/:id', methods=['POST'])
def delete_notes_def(notes_id):
    notes = delete_notes(notes_id)
    return jsonify(notes)



