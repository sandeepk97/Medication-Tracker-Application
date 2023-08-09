from database import get_db_connection
from flask import jsonify
import mysql.connector

def validate_medication_data(data):
    pass


def get_medication_list_from_db():
    try:
        db = get_db_connection()  

        query = """
        SELECT id, name, schedule, time, number_of_doses, start_date, end_date
        FROM medication
        """
        cursor = db.cursor(dictionary=True)
        cursor.execute(query)
        medication_list = cursor.fetchall()

        cursor.close()
        db.close()

        return medication_list

    except mysql.connector.Error as err:
        return []

    except Exception as e:
        return []

def get_medication_list():
    medication_list = get_medication_list_from_db()

    formatted_medication_list = []
    for medication in medication_list:
        formatted_medication = {
            "id": medication['id'],
            "name": medication['name'],
            "schedule": medication['schedule'],
            "time": medication['time'],
            "numberOfDoses": medication['number_of_doses'],
            "startDate": medication['start_date'].strftime('%Y-%m-%d'),
            "endDate": medication['end_date'].strftime('%Y-%m-%d')
        }
        formatted_medication_list.append(formatted_medication)

    return (formatted_medication_list)

def add_medication(medication_data):
    try:
        db = get_db_connection() 
        validation_result = validate_medication_data(medication_data)

        query = """
        INSERT INTO medication (name, schedule, time, number_of_doses, start_date, end_date)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (
            medication_data['name'],
            medication_data['schedule'],
            medication_data['time'],
            medication_data['numberOfDoses'],
            medication_data['startDate'],
            medication_data['endDate']
        )

        cursor = db.cursor()
        cursor.execute(query, values)
        db.commit()

        cursor.close()
        db.close()

        return jsonify({'message': 'Medication added successfully.', 'status': 'success'}), 201
    except mysql.connector.Error as err:
        return jsonify({'message': 'Database error: ' + str(err), 'status': 'error'}), 500

    except Exception as e:
        return jsonify({'message': 'An error occurred: ' + str(e), 'status': 'error'}), 500

    return jsonify({'message': 'Unknown error occurred.', 'status': 'error'}), 500

def update_medication_by_id(medication_id):
    
    medication = {"name": "test"}
    
    return medication

def delete_medication_by_id(medication_id):
    
    medication = {"name": "test"}
    
    return medication

def update_medication_completion(medication_id):
    
    medication = {"name": "test"}
    
    return medication

def get_medication_completion(medication_id):
    
    medication = {"name": "test"}
    
    return medication

def add_notes(notes_id):
    
    notes = {"name": "test"}
    
    return notes
def view_notes(notes_id):
    
    notes = {"name": "test"}
    
    return notes
def update_notes(notes_id):
    
    notes = {"name": "test"}
    
    return notes
def delete_notes(notes_id):
    
    notes = {"name": "test"}
    
    return notes

