import os

from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        wk_dir_abs_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(wk_dir_abs_path, file_path))
        # print(f"Working directory: {wk_dir_abs_path}")
        # print(f"Target file: {target_file}")
        valid_file = os.path.commonpath([wk_dir_abs_path, target_file]) == wk_dir_abs_path
        # print(f'Common path = {os.path.commonpath([wk_dir_abs_path, target_file])}')
        if not valid_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(target_file, 'r') as f:
            content = f.read(MAX_CHARS) 
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return content


    except Exception as e:
        return f"Error: {str(e)}"