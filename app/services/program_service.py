# app/services/program_service.py
from app.models.program_model import Program
from app.utils.validators import validate_program_data


class ProgramService:
    """Business logic for program operations"""

    @staticmethod
    def get_all_programs():
        """Get all programs"""
        return Program.get_all()

    @staticmethod
    def get_program_by_id(program_id):
        """Get a specific program"""
        return Program.get_by_id(program_id)

    @staticmethod
    def search_programs(program_id=None, name=None):
        """Search courses with filters"""
        return Program.search(program_id, name)

    @staticmethod
    def create_course(data):
        """Create a new program with validation"""
        # Validate data
        errors = validate_program_data(data)
        if errors:
            return False, errors

        # Create course
        Program.create(
            course_name=data.get('course_name'),
            course_code=data.get('course_code'),
            program_id=data.get('program_id'),
            credits=data.get('credits'),
            description=data.get('description')
        )
        return True, "Course created successfully"

    @staticmethod
    def delete_program(program_id):
        """Delete a course"""
        program = Program.get_by_id(program_id)
        if not program:
            return False, "Program not found"

        Program.delete(program_id)
        return True, "Program deleted successfully"
