import os

def write_file(working_directory, file_path, content):
    try:
        wk_dir_abs_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(wk_dir_abs_path, file_path))
        # print(f"Working directory: {wk_dir_abs_path}")
        # print(f"Target file: {target_file}")
        valid_file = os.path.commonpath([wk_dir_abs_path, target_file]) == wk_dir_abs_path
        # print(f'Common path = {os.path.commonpath([wk_dir_abs_path, target_file])}')
        if not valid_file:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isdir(file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        with open(target_file, 'w') as f:
            f.write(content)
        return f'Sucessfully wrote to "{target_file}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {str(e)}"