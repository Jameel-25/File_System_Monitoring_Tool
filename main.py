from file_manager import create_directory, create_file, delete_file
from system_monitor import monitor_system
from command_runner import run_command
from backup_manager import create_backup
import threading

if __name__ == "__main__":
    # Create a test directory and file
    create_directory("test_dir")
    create_file("test_dir/test_file.txt", "Hello, this is a test file.")
    
    # Start system monitoring in a separate thread
    monitor_thread = threading.Thread(target=monitor_system)
    monitor_thread.start()

    # Run a system command (e.g., list files in the test_dir)
    run_command("ls -l test_dir")

    # Create a backup of the test_dir
    create_backup("test_dir", "backup")

    # Delete the file after backup
    delete_file("test_dir/test_file.txt")
