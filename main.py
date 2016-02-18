# coding=utf-8
"""
测试用main
"""
import wechatrecord
import argparse

tool_desc = 'WeChat Chat History Export Tool can export the chat history in wechat to HTML or Excel document.'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=tool_desc)
    parser.add_argument("--list-user", help="List your wechat user.", action="store_true")
    parser.add_argument("--list-friend", help="List your friends in wechat.", action="store_true")
    parser.add_argument("-u", help='The wechat user id. Please list your wechat user first by "--list-user".',
                        metavar="User")
    required_group = parser.add_argument_group('required arguments')
    required_group.add_argument("-d", metavar="Document", help="The wechat document path.", required=True)
    # parser.add_argument("echo", help="echo the string you use here")
    args = parser.parse_args()
    listfriend = args.list_friend
D
