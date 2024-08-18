#!/bin/bash

# Define variables
CSV_FILE="~/esl/colcon_ws/src/My_ROS_Bridge/JoyStickTeleop/joy.csv"
TOPIC="/joy"
INTERVAL=1  # Interval in seconds for sending the CSV file

# FTP server details
FTP_SERVER="192.168.1.100"  # IP of the FTP server
FTP_USERNAME="administrator"     
FTP_PASSWORD="clearpath"     
FTP_DEST_DIR="~/administrator/My_ROS_Bridge/JoyStickTeleop/"  # destination directory on the FTP server

# Function to write header to CSV file
write_header() {
    echo "axes_0,axes_1,axes_2,axes_3,axes_4,axes_5,axes_6,axes_7,button_0,button_1,button_2,button_3,button_4,button_5,button_6,button_7,button_8,button_9,button_10" > $CSV_FILE
}

# Function to send CSV file to FTP server
# send_to_ftp() {
#     echo "Sending CSV file to FTP server..."
#     curl -T $CSV_FILE ftp://$FTP_USERNAME:$FTP_PASSWORD@$FTP_SERVER$FTP_DEST_DIR/
#     if [ $? -eq 0 ]; then
#         echo "CSV file sent successfully to FTP server."
#     else
#         echo "Failed to send CSV file to FTP server."
#     fi
# }

# Function to send the file to the FTP server
send_to_ftp() {
    ftp -inv $FTP_SERVER <<EOF
user $FTP_USERNAME $FTP_PASSWORD
send $FTP_DEST_DIR $CSV_FILE
bye
EOF
}

# Main loop
while true; do
    # Write header to CSV file
    # write_header

    # # Simulate writing data to CSV file (replace this with actual data writing logic)
    # echo "Simulating data writing to CSV file..."
    # echo "0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0,0,0,0,0,0,0,0,0,0,0" >> $CSV_FILE

    # Send the CSV file to the FTP server
    send_to_ftp

    # Wait for the specified interval before the next iteration
    sleep $INTERVAL
done