import os
import time
import multiprocessing
import threading
# Create a directory to store the files

os.makedirs("files")
os.makedirs("tempfiles")

# Generate 1000 files, each with a size of 1MB
file_size = 1024 * 1024   # 1MB
start_time = time.time()
elapsed_time = 0
transfer_elapsed_time = 0
process = multiprocessing.Process(target=print, args=("Creating 1000 files of 1MB each...",))
def create_files():
    for i in range(1024*6):
        file_name = f"files/file{i}.txt"
        with open(file_name, "wb") as file:
            file.write(b"0" * file_size)
        file.close()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Created {1024*6} files of 1MB each in {elapsed_time} seconds.")
    print("Creation rate: ", 1024*6/elapsed_time, "mb per second")
    transfer_files()

def transfer_files():
    transfer_start_time = time.time()
    for i in range(1024*6):
        file_name = f"files/file{i}.txt"
        new_file_name = f"tempfiles/file{i}.txt"
        with open(file_name, "rb") as file:        
            with open(new_file_name, "wb") as new_file:
                new_file.write(file.read())
                new_file.close()
            file.close()
        os.remove(file_name)
    transfer_end_time = time.time()
    transfer_elapsed_time = transfer_end_time - transfer_start_time
    print(f"Transferred {1024*6} files of 1MB each in {transfer_elapsed_time} seconds.")
    print("Cleaning up...")
    print("Transfer rate: ", 1024*6/transfer_elapsed_time, "MB per second")
    cleanup()
def cleanup():
    for i in range(1024*6):
        # file_name = f"files/file{i}.txt"
        new_file_name = f"tempfiles/file{i}.txt"
        os.remove(new_file_name)
    os.rmdir("files")
    os.rmdir("tempfiles")


thread1 = threading.Thread(target=create_files)
thread1.start()
print("Done.")


