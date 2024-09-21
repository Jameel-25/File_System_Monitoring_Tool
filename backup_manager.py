import shutil
from pathlib import Path

def create_backup(src_dir, backup_dir):
    Path(backup_dir).mkdir(exist_ok=True)
    shutil.make_archive(backup_dir + "/backup_file", 'zip', src_dir)
    print(f"Backup of {src_dir} created in {backup_dir}.")
