from flask import (Flask, render_template, redirect, request, flash, session, jsonify, g)
from model import (Program, Section, Activity, Answer, db, connect_to_db)
from jinja2 import StrictUndefined
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

@app.route('/')
def index():
    return ''

@app.route('/programs', methods=['GET'])
def get_all_programs():
    programs = Program.query.all()
    output = []

    for program in programs:
        program_data = {}

        program_data['id'] = program.id
        program_data['name'] = program.name
        program_data['description'] = program.description

        output.append(program_data)
    
    return jsonify({'programs' : output})

@app.route('/programs/<int:id>')
def get_program(id):
    program = Program.query.filter_by(id=id).first()

    if not program:
        return jsonify({'message' : 'No program found.'})

    program_data = {}
    program_data['id'] = program.id
    program_data['name'] = program.name
    program_data['description'] = program.description

    return jsonify({'program' : program_data})

@app.route('/programs/<int:program_id>/sections/', methods=['GET'])
def get_all_sections(program_id):
    sections = Section.query.filter_by(program_id=program_id).all()
    output = []

    if not sections:
        return jsonify({'message': 'No sections found!'})

    for section in sections:
        section_data = {}

        section_data['id'] = section.id
        section_data['name'] = section.name
        section_data['description'] = section.description
        section_data['order_index'] = section.order_index
        section_data['is_last'] = section.is_last

        output.append(section_data)
    
    return jsonify({'sections' : output})

@app.route('/sections/<int:id>/', methods=['GET'])
def get_section(id):
    section = Section.query.filter_by(id=id).first()

    if not section:
        return jsonify({'message' : 'No section found.'})
    
    section_data = {}
    section_data['id'] = section.id
    section_data['name'] = section.name
    section_data['description'] = section.description
    section_data['order_index'] = section.order_index
    section_data['is_last'] = section.is_last

    return jsonify({'section' : section_data})

@app.route('/sections/<int:section_id>/activities/', methods=['GET'])
def get_activity(section_id):
    activity = Activity.query.filter_by(section_id=section_id).first()

    if not activity:
        return jsonify({'message' : 'No activities found.'})
    
    activity_data = {}
    activity_data['id'] = activity.id
    activity_data['section_id'] = activity.section_id
    activity_data['html_content'] = activity.html_content
    activity_data['question'] = activity.question

    if activity_data['question']:
        answer = Answer.query.filter_by(activity_id=activity.id).first()
        activity_data['answer_text'] = answer.answer_text

    return jsonify({'activity' : activity_data})


if __name__ == "__main__":
    connect_to_db(app)

    app.run(port=5000, host = '0.0.0.0', threaded = True)