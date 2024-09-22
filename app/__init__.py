# Import the query execution function from the utils module
from .utils import execute_query

# Import the individual page modules for easy access
from .pages import dashboard, student_info, customer_info, add_records

# Make the pages accessible directly
__all__ = ['dashboard', 'student_info', 'customer_info', 'add_records', 'execute_query']
