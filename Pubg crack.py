import requests
import hashlib
import time
import hmac
from datetime import datetime
import pyfiglet
"""

PUBG crack version 3.3.0 programmed by Vermouth


"""
class PUBGAPI:
    BASE_URL = 'https://api.pubg.com'
    
    HEADERS = {
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/json',
        'User-Agent': 'My PUBG API Client/1.0',
        'X-Request-ID': 'unique-request-id',
        'X-Timestamp': str(int(time.time() * 1000)),
        'X-Signature': '',"SigAndroidFuke"
        'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
        'X-Api-Key': 'YOUR_API_KEY',
        'X-Client-Id': 'your-client-id',
        'X-Client-Secret': 'your-client-secret',
        'X-Auth-Token': 'your-auth-token',
        'X-Content-Type-Options': 'nosniff',
        'X-Frame-Options': 'DENY',
        'X-XSS-Protection': '1; mode=block',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'DNT': '1',
        'X-Forwarded-For': 'your-ip-address',
        'X-Request-Id': 'unique-request-id',  # Added twice for example
        'X-Api-Version': '1.0',
        'X-Permitted-Cross-Domain-Policies': 'none',
        'X-Frame-Options': 'SAMEORIGIN',
        'X-Content-Type-Options': 'nosniff'
    }

    def __init__(self, api_key=None, secret_key=None):
        self.session = requests.Session()
        self.session.headers.update(self.HEADERS)
        self.api_key = api_key
        self.secret_key = secret_key

    def generate_signature(self, data):
        """Generate HMAC-SHA256 signature for the request"""
        if not self.secret_key:
            return ''
        signature = hmac.new(self.secret_key.encode(), data.encode(), hashlib.sha256).hexdigest()
        return signature

    def get(self, endpoint, params=None):
        url = f'{self.BASE_URL}/{endpoint}'
        self.session.headers['X-Signature'] = self.generate_signature(url)
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, data=None):
        url = f'{self.BASE_URL}/{endpoint}'
        self.session.headers['X-Signature'] = self.generate_signature(url)
        response = self.session.post(url, json=data)
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint):
        url = f'{self.BASE_URL}/{endpoint}'
        self.session.headers['X-Signature'] = self.generate_signature(url)
        response = self.session.delete(url)
        response.raise_for_status()
        return response.json()

    # API Endpoints
    def get_player(self, player_name):
        """Get player data"""
        endpoint = 'players'
        params = {'filter[playerNames]': player_name}
        return self.get(endpoint, params)

    def get_match(self, match_id):
        """Get match data"""
        endpoint = f'matches/{match_id}'
        return self.get(endpoint)

    def get_teams(self, match_id):
        """Get teams data in a match"""
        endpoint = f'matches/{match_id}/teams'
        return self.get(endpoint)

    def get_leaderboards(self, region):
        """Get leaderboards"""
        endpoint = f'leaderboards/{region}'
        return self.get(endpoint)

    def get_tournaments(self):
        """Get list of tournaments"""
        endpoint = 'tournaments'
        return self.get(endpoint)

    def get_player_stats(self, player_id):
        """Get player stats"""
        endpoint = f'players/{player_id}/stats'
        return self.get(endpoint)

    def get_season_stats(self, season_id):
        """Get season stats"""
        endpoint = f'seasons/{season_id}/stats'
        return self.get(endpoint)

    def get_match_details(self, match_id):
        """Get match details"""
        endpoint = f'matches/{match_id}/details'
        return self.get(endpoint)

    def get_team_members(self, team_id):
        """Get team members"""
        endpoint = f'teams/{team_id}/members'
        return self.get(endpoint)

    def get_item_list(self):
        """Get list of items"""
        endpoint = 'items'
        return self.get(endpoint)

    def get_map_info(self):
        """Get map information"""
        endpoint = 'maps'
        return self.get(endpoint)

    def get_game_modes(self):
        """Get game modes"""
        endpoint = 'modes'
        return self.get(endpoint)

    def get_current_events(self):
        """Get current events"""
        endpoint = 'events/current'
        return self.get(endpoint)

    def get_event_details(self, event_id):
        """Get event details"""
        endpoint = f'events/{event_id}'
        return self.get(endpoint)

    def create_match(self, data):
        """Create a new match"""
        endpoint = 'matches'
        return self.post(endpoint, data)

    def update_player(self, player_id, data):
        """Update player data"""
        endpoint = f'players/{player_id}'
        return self.post(endpoint, data)

    def delete_player(self, player_id):
        """Delete player"""
        endpoint = f'players/{player_id}'
        return self.delete(endpoint)

    def get_game_statistics(self):
        """Get general game statistics"""
        endpoint = 'statistics'
        return self.get(endpoint)

    def get_replays(self):
        """Get list of replays"""
        endpoint = 'replays'
        return self.get(endpoint)

    def get_player_achievements(self, player_id):
        """Get player achievements"""
        endpoint = f'players/{player_id}/achievements'
        return self.get(endpoint)

    def get_weapons(self):
        """Get list of weapons"""
        endpoint = 'weapons'
        return self.get(endpoint)

    def get_player_rank(self, player_id):
        """Get player rank"""
        endpoint = f'players/{player_id}/rank'
        return self.get(endpoint)

    def get_custom_games(self):
        """Get list of custom games"""
        endpoint = 'custom_games'
        return self.get(endpoint)

    def get_custom_game_details(self, game_id):
        """Get custom game details"""
        endpoint = f'custom_games/{game_id}'
        return self.get(endpoint)

    def get_game_events(self):
        """Get game events"""
        endpoint = 'game_events'
        return self.get(endpoint)

    def get_game_event_details(self, event_id):
        """Get game event details"""
        endpoint = f'game_events/{event_id}'
        return self.get(endpoint)

    def get_player_inventory(self, player_id):
        """Get player inventory"""
        endpoint = f'players/{player_id}/inventory'
        return self.get(endpoint)

    def get_player_match_history(self, player_id):
        """Get player match history"""
        endpoint = f'players/{player_id}/match_history'
        return self.get(endpoint)

    def get_player_rank_history(self, player_id):
        """Get player rank history"""
        endpoint = f'players/{player_id}/rank_history'
        return self.get(endpoint)

if __name__ == '__main__':
    # Print script information
    script_version = '1.0.0'
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"\x1b[38;5;190m     \t           Script Version: {script_version}")
    print(f"\x1b[38;5;174m             Date and Time: {current_datetime}")
    print("\x1b[38;5;150m               Script programmed by Vermouth")
    text = "  Vermouth"
    fig = pyfiglet.Figlet(font='slant')
    formatted_text = fig.renderText(text)
    print("\x1b[38;5;99m" + formatted_text + "\x1b[0m")
    print("\x1b[38;5;228m")
    
    api = PUBGAPI(api_key="K8XXCJECOec14579def52039ed4a95845a7ab", secret_key="XKXCJWNWPPUB")
    
    player_name = "XJXDJEQPQNDCUS62"
    player_data = api.get_player(player_name)
    print(player_data)
    
    match_id = "ID"
    match_data = api.get_match(match_id)
    print(match_data)
