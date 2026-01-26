#! /usr/bin/env python3 - '#!' is Shebang used to say to OS that to use the following intrepreter. 

"""       Description 

This node periodically publishes message "Hello Joe"


------

Publishing Topic:

This channel contains 'hello joe' message

/py_example_topic - std_msgs/String


Subscribing Topic:

None

Author: Joe
Date: January 10, 2026

"""

import rclpy #importing ros2 client library for python
from rclpy.node import Node #importing Node class used for creating nodes.
 
from std_msgs.msg import String #importing string message type for ros2

class MinimalPyPublisher(Node):
  """_Creating node """

  def __init__(self):
    #create custom node class for publishing messages

    super().__init__('minimal_py_publisher') #Initializing name of node

    #create a publisher on the topic with queue size of 10 messages 

    self.publisher_1 = self.create_publisher(String, '/py_example_topic', 10)

    #create a timer for perio of 0.5 seconds to trigger publishing of message
    timer_period = 0.5
    self.timer = self.create_timer(timer_period, self.timer_callback)

    #initialize a counter variable for message content
    self.counter = 0
  
  def timer_callback(self):
    #callback function executed periodically by timer

    #create new string message object

    msg = String()

    #set message with counter

    msg.data = 'Hello, Joe: %d' % self.counter

    #publish the message you created above to a topic

    self.publisher_1.publish(msg)

    #log a message indicating the message has been published
    self.get_logger().info('Publishing: "%s"' % msg._data)

    self.counter = self.counter + 1


def main(args=None):
  """main function to start ros2 node
  """

  rclpy.init(args=args)

  #create an instance for minimal publisher node

  minimal_py_publisher = MinimalPyPublisher()

  rclpy.spin(minimal_py_publisher)

  #destroy node explicitily

  minimal_py_publisher.destroy_node()

  #shutdown ros 2 communication
  rclpy.shutdown()


if __name__ == '__main__':
  #execute the main function if script is run directly
  main()








