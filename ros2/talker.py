import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import sys

class My_publisher(Node):

    def __init__(self):
        super().__init__('chatter_publisher')
        self.publisher_ = self.create_publisher(String, 'twitter', 10)#TODO-1
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        if self.count < 5:
            msg = String()
            msg.data = "hello world" #TODO-2
            self.publisher_.publish(msg)# TODO-3: publish the msg
            self.get_logger().info('chatter_publisher: "%s"' % msg.data)
            self.count += 1
        else:
            self.timer.cancel()
            sys.exit(1)
            
def main(args=None):
    rclpy.init(args=args)

    publisher1 = My_publisher()

    rclpy.spin(publisher1)

    publisher1.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
