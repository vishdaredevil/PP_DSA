import os

def create_keep_files(root_dir):
    for current_path, dirs, files in os.walk(root_dir):
        # Ignore hidden folders
        if "/." in current_path or "\\." in current_path:
            continue

        # If directory has no files and no .keep already, add one
        if not files and '.keep' not in files:
            keep_file_path = os.path.join(current_path, '.keep')
            with open(keep_file_path, 'w') as f:
                f.write('')  # empty file
            print(f"Added: {keep_file_path}")

if __name__ == "__main__":
    # Change this path to where your repo root is
    project_root = "Module1"
    create_keep_files(project_root)
