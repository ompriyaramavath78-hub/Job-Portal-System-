"""
Utility functions for file upload handling, validation, and security.
"""

import os
from datetime import datetime
from werkzeug.utils import secure_filename
from flask import current_app


def is_allowed_file(filename, file_type='resume'):
    """
    Validate if a file extension is allowed.
    
    Args:
        filename: The uploaded filename
        file_type: Type of file - 'profile' or 'resume'
    
    Returns:
        True if file is allowed, False otherwise
    """
    if '.' not in filename:
        return False
    
    extension = filename.rsplit('.', 1)[1].lower()
    
    if file_type == 'profile':
        allowed = current_app.config.get('ALLOWED_PROFILE_EXTENSIONS', {'jpg', 'jpeg', 'png', 'webp'})
    elif file_type == 'resume':
        allowed = current_app.config.get('ALLOWED_RESUME_EXTENSIONS', {'pdf', 'doc', 'docx'})
    else:
        return False
    
    return extension in allowed


def get_upload_path(user_id, file_type='resume'):
    """
    Get the upload directory path for a specific file type.
    
    Args:
        user_id: User ID
        file_type: Type of file - 'profile' or 'resume'
    
    Returns:
        Absolute path to upload directory
    """
    base_folder = current_app.config.get('UPLOAD_FOLDER', 
                                         os.path.join(current_app.root_path, 'static', 'uploads'))
    
    if file_type == 'profile':
        folder = os.path.join(base_folder, 'profile')
    elif file_type == 'resume':
        folder = os.path.join(base_folder, 'resumes')
    else:
        folder = base_folder
    
    # Create directory if it doesn't exist
    os.makedirs(folder, exist_ok=True)
    
    return folder


def save_upload_file(file, user_id, file_type='resume'):
    """
    Save uploaded file securely with unique naming.
    
    Args:
        file: The file object from request.files
        user_id: User ID
        file_type: Type of file - 'profile' or 'resume'
    
    Returns:
        Tuple of (filename, filepath_relative, full_path) or (None, None, None) on error
    """
    if not file or not file.filename:
        return None, None, None
    
    if not is_allowed_file(file.filename, file_type):
        return None, None, None
    
    # Get secure filename
    original_filename = secure_filename(file.filename)
    
    # Create unique filename with timestamp and user_id
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    file_extension = original_filename.rsplit('.', 1)[1].lower()
    unique_filename = f"{user_id}_{timestamp}.{file_extension}"
    
    # Get upload folder
    folder = get_upload_path(user_id, file_type)
    
    # Create full path
    full_path = os.path.join(folder, unique_filename)
    
    # Save file
    try:
        file.save(full_path)
        
        # Return relative path for database storage
        if file_type == 'profile':
            relative_path = f'uploads/profile/{unique_filename}'
        elif file_type == 'resume':
            relative_path = f'uploads/resumes/{unique_filename}'
        else:
            relative_path = f'uploads/{unique_filename}'
        
        return original_filename, relative_path, full_path
    except Exception as e:
        print(f"Error saving file: {e}")
        return None, None, None


def delete_upload_file(file_path):
    """
    Safely delete an uploaded file.
    
    Args:
        file_path: Relative file path (from database)
    
    Returns:
        True if deletion successful, False otherwise
    """
    try:
        full_path = os.path.join(current_app.root_path, 'static', file_path)
        if os.path.exists(full_path):
            os.remove(full_path)
            return True
    except Exception as e:
        print(f"Error deleting file: {e}")
    
    return False


def get_file_size(file_path):
    """
    Get file size in bytes.
    
    Args:
        file_path: Absolute path to file
    
    Returns:
        File size in bytes, or 0 if file doesn't exist
    """
    try:
        if os.path.exists(file_path):
            return os.path.getsize(file_path)
    except Exception as e:
        print(f"Error getting file size: {e}")
    
    return 0


def format_file_size(size_bytes):
    """
    Format file size in human-readable format.
    
    Args:
        size_bytes: Size in bytes
    
    Returns:
        Formatted string (e.g., "1.5 MB")
    """
    if size_bytes == 0:
        return "0 B"
    
    kb = size_bytes / 1024
    if kb < 1024:
        return f"{kb:.0f} KB"
    
    mb = kb / 1024
    if mb < 1024:
        return f"{mb:.1f} MB"
    
    gb = mb / 1024
    return f"{gb:.1f} GB"
