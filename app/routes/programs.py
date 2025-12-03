# app/routes/programs.py
from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from app.services.program_service import ProgramService
from app.models.program_model import Program

programs_bp = Blueprint('programs', __name__, url_prefix='/programs', template_folder='../templates')


@programs_bp.route('/')
def list():
    """Display list of programs"""
    programs = ProgramService.get_all_programs()
    return render_template('programs/list.html', programs=programs)

@programs_bp.route('/search', methods=['GET', 'POST'])
def search():
    """Search programs"""
    if request.method == 'POST':
        program_id = request.form.get('program_id')
        name = request.form.get('name')

        programs = ProgramService.search_programs(
            program_id=program_id,
            name=name
        )
        return render_template('programs/list.html', programs=programs)
    
    return redirect(url_for('programs.list'))


@programs_bp.route('/create', methods=['GET', 'POST'])
def create():
    """Create a new program"""
    if request.method == 'GET':
        programs = Program.get_all()  # Get programs
        return render_template('programs/form.html', programs=programs)

    # Handle POST request
    data = {
        'program_name': request.form.get('program_name'),
        'program_code': request.form.get('program_code'),
        'program_id': request.form.get('program_id'),
        'credits': request.form.get('credits'),
        'description': request.form.get('description')
    }

    success, message = ProgramService.create_course(data)
    if success:
        flash(message, 'success')
        return redirect(url_for('programs.list'))
    else:
        flash(message if isinstance(message, str) else ', '.join(message), 'danger')
        return redirect(url_for('programs.create'))


@programs_bp.route('/delete/<int:program_id>', methods=['POST'])
def delete(program_id):
    """Delete program"""
    success, message = ProgramService.delete_program(program_id)
    if success:
        return jsonify({'success': True, 'message': message})
    return jsonify({'success': False, 'message': message}), 400
