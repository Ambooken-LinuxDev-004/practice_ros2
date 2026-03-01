/* (SAME AS PYTEST)

Test suite for Ros 2 minimal publisher node.

Script contain unit tests for verifying the functionality of minimal Ros 2 publisher.

Tests node creation, message counter increment & message content formatting.

Subscription topics: None
Publishing topics: /py_example_topic(std_msgs/String): Example message with increment counter.

Author: Joe Ambooken
Date: March 1, 2026 

*/

#include <gtest/gtest.h>
#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp>

class MinimalCppPublisher;

#define TESTING_EXCLUDE_MAIN
#include "../../src/cpp_minimal_publisher.cpp"

class TestMinimalPublisher : public ::testing::Test
{
  protected:
  void SetUp() override
  {
    rclcpp::init(0, nullptr);

    node = std::make_shared<MinimalCppPublisher>();

  }

  void TearDown() override
  {
    node.reset();
    rclcpp::shutdown();

  }

  std::shared_ptr<MinimalCppPublisher> node;

};

TEST_F(TestMinimalPublisher, TestNodeCreation)
{
  EXPECT_EQ(std::string(node->get_name()), std::string("minimal_cpp_publisher"));

  auto pub_endpoints = node->get_publishers_info_by_topic("/cpp_example_topic");
  EXPECT_EQ(pub_endpoints.size(), 1u);
}

TEST_F(TestMinimalPublisher, TestMessageContent)
{
  std::shared_ptr<std_msgs::msg::String> received_msg;

  auto subscription = node->create_subscription<std_msgs::msg::String>(
    "/cpp_example_topic", 10,
    [&received_msg](const std_msgs::msg::String::SharedPtr msg) {
      received_msg = std::make_shared<std_msgs::msg::String>(*msg);
    });

  node->timerCallback();

  rclcpp::spin_some(node);

  EXPECT_EQ(received_msg->data.substr(0, 12), "Hello World!");
}

int main(int argc, char** argv)
{
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}



