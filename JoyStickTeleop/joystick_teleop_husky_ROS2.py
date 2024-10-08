import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
import time

class JoyMessageForwarder(Node):
    def __init__(self):
        super().__init__('joy_message_forwarder')

        # Check if the source topic exists
        self.wait_for_topic('/joy')

        # Check if the destination topic exists
        self.wait_for_topic('/a200_1057/joy_teleop/joy')

        # Add a delay before starting the subscriber and publisher
        delay_seconds = 5  # Set the delay time in seconds
        self.get_logger().info(f'Delaying for {delay_seconds} seconds before starting...')
        time.sleep(delay_seconds)

        # Create the subscription after ensuring the source topic exists
        self.subscription = self.create_subscription(
            Joy,  # The message type is Joy
            '/joy',  # Replace with your source topic
            self.listener_callback,
            10)

        # Create the publisher after ensuring the destination topic exists
        self.publisher = self.create_publisher(
            Joy,  # The message type is Joy
            '/a200_1057/joy_teleop/joy',  # Replace with your destination topic
            10)

    def wait_for_topic(self, topic_name):
        self.get_logger().info(f'Waiting for topic {topic_name} to be available...')
        while not self.topic_exists(topic_name):
            rclpy.spin_once(self, timeout_sec=1.0)
        self.get_logger().info(f'Topic {topic_name} is now available.')

    def topic_exists(self, topic_name):
        topic_list = self.get_topic_names_and_types()
        for topic in topic_list:
            if topic_name == topic[0]:  # Check if topic_name exactly matches the topic name
                return True
        return False

    def listener_callback(self, msg):
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    joy_message_forwarder = JoyMessageForwarder()
    rclpy.spin(joy_message_forwarder)
    joy_message_forwarder.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
