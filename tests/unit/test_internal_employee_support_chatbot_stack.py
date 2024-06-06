import aws_cdk as core
import aws_cdk.assertions as assertions

from internal_employee_support_chatbot.internal_employee_support_chatbot_stack import InternalEmployeeSupportChatbotStack

# example tests. To run these tests, uncomment this file along with the example
# resource in internal_employee_support_chatbot/internal_employee_support_chatbot_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = InternalEmployeeSupportChatbotStack(app, "internal-employee-support-chatbot")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
