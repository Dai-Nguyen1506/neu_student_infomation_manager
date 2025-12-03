# app/models/program_model.py
from app.connection import get_connection


class Program:
    """Program model for database operations"""

    @staticmethod
    def get_all():
        """Get all programs"""
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM program")
        programs = cursor.fetchall()
        conn.close()
        return programs

    @staticmethod
    def get_by_id(program_id):
        """Get program by ID"""
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM program WHERE program_id = %s", (program_id,))
        program = cursor.fetchone()
        conn.close()
        return program

    @staticmethod
    def search(program_id=None, name=None):
        """Search programs by various criteria"""
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM program WHERE 1=1"
        values = []

        if program_id:
            query += " AND program_id = %s"
            values.append(program_id)
        if name:
            query += " AND program_name LIKE %s"
            values.append("%" + name + "%")

        cursor.execute(query, tuple(values))
        programs = cursor.fetchall()
        conn.close()
        return programs

    @staticmethod
    def delete(program_id):
        """Delete a program"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM program WHERE program_id = %s", (program_id,))
        conn.commit()
        conn.close()

