import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Publisher(Node):
    def __init__(self):
        super().__init__('publisher')
        self.i = 0
        self.pub = self.create_publisher(String, 'chatter', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
    def timer_callback(self):
        msg = String()
        msg.data = f'Hello Wold {self.i}'
        self.i += 1
        self.get_logger().info(f'Publishing:"{msg.data}')
        self.pub.publish(msg)
    
def main(args = None):
    rclpy.init(args=args)
    try:
        publisher = Publisher()
        rclpy.spin(publisher)
    finally:
        publisher.destory_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

