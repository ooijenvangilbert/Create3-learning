'''
sub_ir.py
Subscriber example
'''

import rclpy        # ros client library py
import sys

from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from irobot_create_msgs.msg import IrIntensityVector

namespace = '[Namespace]'

class IRSubscriber(Node):

    def __init__(self):
        super().__init__('IR_Subscriber')
        print('Creating subscription to the IrItensityVector type over the /ir_intensity topic')
        self.subscription = self.create_subscription(IrIntensityVector, '/ir_intensity', self.listener_callback, qos_profile_sensor_data)

    def printIR(self, msg):
        print('Printing IR sensor readings :')
        for reading in msg.readings:
            val = reading.value
            print('IR sensor : ' + str(val))

    def listener_callback(self, msg:IrIntensityVector):
        print('now listening to IR sernsor readings')
        self.printIR(msg)

def main(args=None):
    rclpy.init(args=args)
    IR_subscriber = IRSubscriber()
    print('callbacks are called')

    try:
        rclpy.spin(IR_subscriber)
    except KeyboardInterrupt:
        print('\nCaught keyboard interrupt')
    finally:
        print('done')
        IR_subscriber.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
    