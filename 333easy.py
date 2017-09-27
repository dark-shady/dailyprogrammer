#https://www.reddit.com/r/dailyprogrammer/comments/72ivih/20170926_challenge_333_easy_packet_assembler/
import sys

messages = {}
for packet in sys.stdin:

    message_id, packet_num, packets_per_message, *packet_content = packet.split()
    packet_content = ' '.join(packet_content)
    packet_num = int(packet_num)

    if message_id not in messages:
        messages[message_id] = [[packet_num, packet_content]]
    else:
        messages[message_id].append([packet_num, packet_content])

    if len(messages[message_id]) == int(packets_per_message):
        messages[message_id].sort()
        for i in range(len(messages[message_id])):
            print("{:6} {:4} {:4} {}".format(message_id, i, packets_per_message, messages[message_id][i][1]))
