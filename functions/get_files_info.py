import os

def get_files_info(working_directory, directory="."):
    try:
        wk_dir_abs_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(wk_dir_abs_path, directory))
        # print(f"Working directory: {wk_dir_abs_path}")
        # print(f"Target directory: {target_dir}")
        valid_dir = os.path.commonpath([wk_dir_abs_path, target_dir]) == wk_dir_abs_path
        # print(f'Common path = {os.path.commonpath([wk_dir_abs_path, target_dir])}')
        if not valid_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        item_list = ""
        ## list out items in desired directory
        items = os.listdir(target_dir)

        for item in items:
            item_size = os.path.getsize(os.path.join(target_dir, item))
            is_dir = os.path.isdir(os.path.join(target_dir, item))
            item_list += f'- {item}: file_size={item_size}, is_dir={is_dir}\n'

        return item_list

        # for each item: record name, file size, and whether it's a directory itself
        # build string representing contents -> f'{item_name}: file_size={item_size}, is_dir={is_dir}'
    except Exception as e:
        return f"Error: {str(e)}"



    