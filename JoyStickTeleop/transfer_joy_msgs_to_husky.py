#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy

# Global variables
latest_joy_msg = None
button_held = False
message_timer = None

def joy_callback(msg):
    global latest_joy_msg, button_held

    CONTROL_BUTTON_INDEX = 4  # Index of the button that controls sending

    # Update the latest Joy message
    latest_joy_msg = msg

    if CONTROL_BUTTON_INDEX < len(msg.buttons):
        current_button_state = msg.buttons[CONTROL_BUTTON_INDEX] == 1
    else:
        rospy.logwarn("Control button index {} is out of range".format(CONTROL_BUTTON_INDEX))
        return


    if current_button_state and not button_held:
        # Control button was just pressed
        button_held = True
        rospy.loginfo("Control button {} pressed. Starting to send latest Joy message.".format(CONTROL_BUTTON_INDEX))
        start_sending_message()
    elif not current_button_state and button_held:
        # Control button was just released
        button_held = False
        rospy.loginfo("Control button {} released. Stopping message sending.".format(CONTROL_BUTTON_INDEX))
        stop_sending_message()

def start_sending_message():
    global message_timer
    # Set up a timer to send the message periodically
    message_timer = rospy.Timer(rospy.Duration(0.1), send_message)  # Send message every 1 second

def stop_sending_message():
    global message_timer
    # Stop the timer when the button is released
    if message_timer:
        message_timer.shutdown()
        message_timer = None

def send_message(event):
    # Publish the latest Joy message while the control button is held down
    if latest_joy_msg:
        pub.publish(latest_joy_msg)

def main():
    global pub

    rospy.init_node('joy_message_forwarder')

    # Publisher to send the latest Joy message
    pub = rospy.Publisher('/joy_teleop/joy', Joy, queue_size=10)

    # Subscriber to the joy topic
    rospy.Subscriber('joy', Joy, joy_callback)

    rospy.spin()

if __name__ == '__main__':
    main()

