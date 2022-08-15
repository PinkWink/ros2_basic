import rclpy as rp
from rclpy.node import Node

from turtlesim.msg import Pose


class TurtlesimSubscriber(Node):

    def __init__(self):
        super().__init__('turtlesim_subscriber')
        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.callback,
            10)
        self.subscription  # prevent unused variable warning

    def callback(self, msg):
        print("X : ", msg.x, ", Y : ", msg.y)


def main(args=None):
    rp.init(args=args)

    turtlesim_subscriber = TurtlesimSubscriber()
    rp.spin(turtlesim_subscriber)

    turtlesim_subscriber.destroy_node()
    rp.shutdown()


if __name__ == '__main__':
    main()
    