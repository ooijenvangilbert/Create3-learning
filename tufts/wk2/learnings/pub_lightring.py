'''
pub_lightring.py

'''

import rclpy
import sys
from rclpy.node import Node

from irobot_create_msgs.msg import LedColor
from irobot_create_msgs.msg import LightringLeds

namespace = '/MyRobot'

class LEDPublisher(Node):

    def __init__(self):
        super().__init__('led_publisher')

        self.lights_publisher = self.create_publisher(LightringLeds, '/cmd_lightring', 10)
        self.lightring = LightringLeds()
        self.lightring.override_system = True
        
        timer_period = 2
        self.timer = self.create_timer(timer_period, self.timer_callback)
    
    def timer_callback(self, r=0, g=0, b=255):
        self.lightring.leds = [LedColor(red = r, green = g, blue = b),LedColor(red = r, green = g, blue = b),LedColor(red = r, green = g, blue = b),LedColor(red = r, green = g, blue = b),LedColor(red = r, green = g, blue = b),LedColor(red = r, green = g, blue = b)]
        self.lights_publisher.publish(self.lightring)

    def reset(self):
        self.lightring.override_system = False
        white = [LedColor(red = 255, green = 255, blue = 255),LedColor(red = 255, green = 255, blue = 255),LedColor(red = 255, green = 255, blue = 255),LedColor(red = 255, green = 255, blue = 255),LedColor(red = 255, green = 255, blue = 255),LedColor(red = 255, green = 255, blue = 255)]
        self.lightring.leds = white
        self.lights_publisher.publish(self.lightring)

def main(args=None):
    rclpy.init(args=args)
    led_publisher = LEDPublisher()

    try:
        rclpy.spin(led_publisher)
    except KeyboardInterrupt:
        print('\nCaught keyboard interrupt')
    finally:
        print('done')
        led_publisher.reset()
        led_publisher.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
    

