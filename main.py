"""main file to process requests """
import os
import pathlib
import sys
import requests

# using pathlib for file path handling(useful in handling paths with windows, mac, linux etc)
PACKAGE_DIR = pathlib.Path(__file__).parent


class TrelloRequests:
    """
    performing python requests to create board, cards edit cards and delete them using trello api
    """
    # @staticmethod
    # def any_static_method_needed(filepath):
    #     """
    #     explanation
    #       """

    def __init__(self):
        """
         This is used incase if any variables need to be initialized
         """
        self.sample_list = []
        self.sample_int = 0

    def clear(self):
        """Resets the variables if needed for multiple iterations"""
        self.sample_list.clear()
        self.sample_int = 0

    def create_card_on_board(self):
        """create card on the given list"""
        # url = "https://api.trello.com/1/cards"
        # query = {
        #     'key': '62e208412de52ff355e3f55dec33940e',
        #     'token': '1aaac0fc3a463f39bf5352960a4aaa65c163821d23c0c816287093884aa42cd9',
        #     'list_id': 'abcdef',
        #     'name': 'sample_card'
        # }
        # response = requests.request("POST", url, params=query)

    def add_board(self):
        """adds board with given name"""

        url = "https://api.trello.com/1/boards/"
        query = {
            'key': '62e208412de52ff355e3f55dec33940e',
            'token': '1aaac0fc3a463f39bf5352960a4aaa65c163821d23c0c816287093884aa42cd9',
            'name': 'test_board3'
        }

        response = requests.request("POST", url, params=query)
        board_id = response.json()["shortUrl"].split("/")[-1].strip()
        board_name = response.json()["url"].split("/")[-1].strip()
        print("board id is " + board_id)
        print("board name is " + board_name)
        print("response text is " + response.text)


def main():
    """Main program entry point.
    """

    requests_trello = TrelloRequests()

    print("adding board:")
    requests_trello.add_board()


    # print("adding cards:")
    # requests_trello.add_card_to_board()

    # print("deleting cards:")
    # requests_trello.delete_card_from_board()

    return 0


if __name__ == '__main__':
    sys.exit(main())
