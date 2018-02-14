def reverse_string(in_message):
    message_list = in_message.split(' ')
    message_list = list(reversed(message_list))
    message_list = ' '.join(message_list)
    return message_list


message = input("Enter your message: ")
print(reverse_string(message))
