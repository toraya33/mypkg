import rclpy
from rclpy.node import Node
from person_msgs.msg import Person

rclpy.init()
node = Node("listener")


def cb(msg):                                           #メッセージが届くたびに呼ばれる
    node.get_logger().info("Listen: %s" % msg)


def main():
    sub = node.create_subscription(Person, "person", cb, 10)  #型、トピック名、コールバック、キュー長
    rclpy.spin(node)
