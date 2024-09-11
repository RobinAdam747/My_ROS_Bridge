import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy

class JoyMessageForwarder(Node):
    def __init__(self):
        super().__init__('joy_message_forwarder')
        self.subscription = self.create_subscription(
            Joy,  # The message type is Joy
            '/joy',  # Replace with your source topic
            self.listener_callback,
            10)
        self.publisher = self.create_publisher(
            Joy,  # The message type is Joy
            '/a200_1057/joy_teleop/joy',  # Replace with your destination topic
            10)

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
