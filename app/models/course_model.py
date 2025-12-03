# app/models/course_model.py
from app.connection import get_connection

class Course:
    """Course model for database operations"""

    @staticmethod
    def get_all():
        """Get all courses"""
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM course")
        courses = cursor.fetchall()
        conn.close()
        return courses
    
    def get_by_program_id(program_id):
        """Get Courrse By ID Program"""
        None