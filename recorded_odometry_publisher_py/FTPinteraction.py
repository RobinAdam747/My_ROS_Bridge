from ftplib import FTP, error_perm, error_temp, error_proto, error_reply
import os
import logging

def connect_to_ftp(server, username, password):
    try:
        # Connect to the FTP server
        ftp = FTP(server)
        
        # Login to the server
        ftp.login(user=username, passwd=password)
        
        # Print success
        print("Login success!")

        return ftp
    except (error_perm, error_temp, error_proto, error_reply) as e:
        print(f"FTP error: {e}")
        return None

def file_exists_on_ftp(ftp, remote_file_path):
    try:
        # Get the directory and file name from the remote file path
        directory, file_name = remote_file_path.rsplit('/', 1)
        
        # List files in the directory
        files = ftp.nlst(directory)
        
        # Print progress
        print("Finding file at " + directory + "...")

        # Check if the file is in the list
        # return file_name in files
        return True
    except (error_perm, error_temp, error_proto, error_reply) as e:
        print(f"FTP error: {e}")

        print("Error finding the file: " + file_name)

        return False

def fetch_file_from_ftp(ftp, remote_file_path, local_file_path):
    try:
        # Ensure the local directory exists
        local_dir = os.path.dirname(local_file_path)
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)
            logging.info(f"Created directory: {local_dir}")

        # Open a local file to write the downloaded content
        with open(local_file_path, 'wb') as local_file:
            # Retrieve the file from the server and write it to the local file
            ftp.retrbinary(f'RETR {remote_file_path}', local_file.write)

        # Print progress
        print("Retreived file")

    except (error_perm, error_temp, error_proto, error_reply) as e:
        print(f"FTP error: {e}")

def delete_file_from_ftp(ftp, remote_file_path):
    try:
        # Delete the file from the server
        ftp.delete(remote_file_path)

        # Print progress
        print("Server file deleted")

    except (error_perm, error_temp, error_proto, error_reply) as e:
        print(f"FTP error: {e}")

def main(server, username, password, remote_file_path, local_file_path):
    while True:
        # Connect to the FTP server
        ftp = connect_to_ftp(server, username, password)

        if ftp is not None:
            # Check if the file exists
            if file_exists_on_ftp(ftp, remote_file_path):
                # Fetch the file from the server
                fetch_file_from_ftp(ftp, remote_file_path, local_file_path)
                
                # Delete the file from the server
                # delete_file_from_ftp(ftp, remote_file_path)
            
            # Close the connection
            ftp.quit()

# RooiBot details
server = '192.168.1.33'
username = 'noeticpioneer'
password = 'esl'
remote_file_path = '/home/noeticpioneer/My_ROS_Bridge/recorded_odometry_publisher_py/Bags/Odometry/RosAria-pose.csv'
local_file_path = '/home/colcon_ws/src/My_ROS_Bridge/recorded_odometry_publisher_py/Bags/Odometry/RosAria-pose.csv'

# Husky details
# server = '' # Add the Husky's IP address (of the Jetson or other OBC)
# username = 'administrator'
# password = 'clearpath'
# remote_file_path = '/home/administrator/My_ROS_Bridge/recorded_odometry_publisher_py/Bags/Odometry/RosAria-pose.csv'    # Check the path on the Husky
# local_file_path = '/home/esl/My_ROS_Bridge/recorded_odometry_publisher_py/Bags/Odometry/RosAria-pose.csv'   # Check the path on the NUC

main(server, username, password, remote_file_path, local_file_path)