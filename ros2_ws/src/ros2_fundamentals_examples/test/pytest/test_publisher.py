#!/usr/bin/env python3

"""
Test suite for Ros 2 minimal publisher node.

Script contain unit tests for verifying the functionality of minimal Ros 2 publisher.

Tests node creation, message counter increment & message content formatting.

Subscription topics: None
Publishing topics: /py_example_topic(std_msgs/String): Example message with increment counter.

Author: Joe Ambooken
Date: February 25, 2026
"""

import pytest
import rclpy
from std_msgs.msg import String
from ros2_fundamentals_examples.py_minimal_publisher import MinimalPyPublisher

def test_publisher_creation():
  """
  Test if publisher node is created correctly.
  Verifies Node name, publisher object exists & if topic name is correct.
  Raises Assertion Error if anything above fails.
  """

  # Initialize ROS 2 communication

  rclpy.init()

  try:
    # Create instance of publisher node.
    node = MinimalPyPublisher()
    
    # Verifying node name as expected
    assert node.get_name() == "minimal_py_publisher"

    # Verfying publisher exists and has correct topic name
    assert hasattr(node, 'publisher_1')
    assert node.publisher_1.topic_name == '/py_example_topic'

  finally:
    # Clean up ROS 2 communication
    rclpy.shutdown()


def test_message_counter():
  """
  Test if message counter increments correctly.
  Tests if counter(node.counter) increases by 1 after each timer callback execution.

  Raises assertion error if anything fails.
  """

  rclpy.init()

  try:
    node = MinimalPyPublisher()
    initial_count = node.counter
    node.timer_callback()
    assert node.counter == initial_count + 1
  
  finally:
    rclpy.shutdown()

def test_message_content():
  """
  Test if message content is formatted correctly.
  Verifies message string is formatted using an f-string with the current counter value.
  Raises assertion error if message format doesn't match expected output.
  """

  rclpy.init()

  try:
    node = MinimalPyPublisher()

    # Set counter to a known value for testing
    node.counter = 5
    msg = String()

    # Using f-string instead of % formatting
    msg.data = f'Hello World: {node.counter}'
    assert msg.data == 'Hello World: 5'

  finally:
    rclpy.shutdown()


if __name__ == "__main__":
  pytest.main(['-v'])







