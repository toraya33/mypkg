import rclpy                     #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from person_msgs.srv import Query

rclpy.init()                     #rclpyの初期化（最初に1回）
node = Node("talker")            #ノード作成（nodeという「オブジェクト」を作成）

def cb(request, response):
    if request.name == "泥谷虎之介":
        response.age = 41
    else:
        response.age = 255
    return response


def main():
    srv = node.create_service(Query, "query", cb)
    rclpy.spin(node)
