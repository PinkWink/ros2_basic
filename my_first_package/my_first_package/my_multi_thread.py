import rclpy as rp
from rclpy.executors import MultiThreadedExecutor
from rclpy.node import Node

from my_first_package.my_publisher import TurtlesimPublisher
from my_first_package.my_subscriber import TurtlesimSubscriber


def main(args=None):
    rp.init()

    sub = TurtlesimSubscriber()
    pub = TurtlesimPublisher()

    executor = MultiThreadedExecutor()

    executor.add_node(sub)
    executor.add_node(pub)

    try:
        executor.spin()

    finally:
        executor.shutdown()
        sub.destroy_node()
        pub.destroy_node()
        rp.shutdown()


if __name__ == '__main__':
    main() 