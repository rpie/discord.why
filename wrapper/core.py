'''
Created By HellSec
Date: OCT 31, 2021
'''

import requests, time

class Discord:
    def __init__(self, token):
        self.token = token
        self.headers = {'authorization': token}

    def check_status(self, response):
        '''
        Status response for Discord
        Given a response code for an error output
        Ex: 
            ERROR 403
            The Authorization token you passed did not have permission to the resource.
        '''
        if response.status_code == 403: return('The Authorization token you passed did not have permission to the resource.')
        if response.status_code == 400: return('The request was improperly formatted, or the server couldn\'t understand it.')
        if response.status_code == 429: return('You are being rate limited.')
        if response.status_code == 403: return('The Authorization header was missing or invalid.')
        if response.status_code == 200: return response

    def send_message(self, message=None, channel=None, mention=None, delete_after=0):
        '''
        Send message function
        Requires message content and channel ID
        delete_after is when to delete rounded to seconds 
        '''
        r = requests.post(
            url = f'https://discord.com/api/v9/channels/{channel}/messages',
            data = {'content': str(message)},
            headers = self.headers
        )
        if delete_after != 0 and r.status_code == 200:
            message, channel = r.json()['id'], r.json()['channel_id']
            time.sleep(int(delete_after))
            self.delete_message(message, channel)

        return self.check_status(r)

    def delete_message(self, message=None, channel=None):
        '''
        Delete a message based off message ID
        '''
        r = requests.delete(
            url = f'https://discord.com/api/v9/channels/{channel}/messages/{message}',
            headers = self.headers
        )
        return self.check_status(r)

    def get_user(self, user=None, connections=False, servers=False) -> dict:
        '''
        Get user details and respond with a dict object
        '''
        r = requests.get(
            url = f'https://discord.com/api/v9/users/{user}/profile?with_mutual_guilds={servers}',
            headers = self.headers
        )
        return self.check_status(r)