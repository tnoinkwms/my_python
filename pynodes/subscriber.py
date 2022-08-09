import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Subscriber(Node):
    def __init__(self):
        super().__init__('subscriber')
        #create_subsctiptionでsubscriberとして設定できる．
        #1-Stringはトピック通信に使うメッセージの型
        #2-'chatter'はトピックの名前
        #3-self.chatter_callbackはコールバック関数
        #4-10はキューのサイズ
        self.sub = self.create_subscription(String,'chatter',self.chatter_callback,10)
    #コールバック関数，受け取ったメッセージの
    def chatter_callback(self,msg):
        self.get_logger().info(f'I heard: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    try:
        #ここでノードの作成
        subscriber = Subscriber()
        #コールバック関数を実行
        rclpy.spin(subscriber)
    finally:
        #最後にノードを壊して，rclpyモジュールを終了
        subscriber.destroy_node()
        rclpy.shutdown()
    
if __name__ == '__main__':
    main()