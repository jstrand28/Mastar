import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster

class OdomTFBroadcaster(Node):
    def __init__(self):
        super().__init__('odom_tf_broadcaster')

        # TF broadcaster
        self.tf_broadcaster = TransformBroadcaster(self)

        # Create a timer to publish the TF at a fixed rate
        self.timer = self.create_timer(0.1, self.broadcast_odom_tf)

    def broadcast_odom_tf(self):
        # Get the current time
        current_time = self.get_clock().now().to_msg()

        # Create a TransformStamped message
        tf_stamped = TransformStamped()
        tf_stamped.header.stamp = current_time
        tf_stamped.header.frame_id = 'odom'
        tf_stamped.child_frame_id = 'base_link'

        # TODO: Set the transform (translation and rotation) based on your robot's sensors

        # Send the transform
        self.tf_broadcaster.sendTransform(tf_stamped)

def main(args=None):
    rclpy.init(args=args)

    odom_tf_broadcaster = OdomTFBroadcaster()

    rclpy.spin(odom_tf_broadcaster)

    odom_tf_broadcaster.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
