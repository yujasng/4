import os
import sys
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

sys.path.append(os.getcwd())


class My_subscriber(Node):
    def __init__(self):
        super().__init__('chatter_subscriber')

        self.subscription = self.create_subscription(Twist, '/turtle1/cmd_vel', self.listener_callback, 10)#TODO-1: complete subscription
        
        self.subscription  
        self.total_score = 0

    def listener_callback(self, msg):
        print(msg.linear.x)
            

def main(args=None):
    rclpy.init(args=args)#TODO-2: init rclpy
    subscriber1 = My_subscriber()#TODO-3: create a subscriber instance
    rclpy.spin(subscriber1)#TODO-4: spin
    subscriber1.destroy_node()
    rclpy.shutdown()
    print("finished")


if __name__ == '__main__':
    main()



