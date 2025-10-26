import os
from dotenv import load_dotenv
import requests
import pandas as pd

# Load environment variables
load_dotenv()

# Define function to handle json normalisation of itad outputs
def normalise_itad(data: dict) -> pd.DataFrame:
    """ Convert itad json response pd dataframe and normalise column names"""
    df = pd.json_normalize(data)
    df.columns = df.columns.str.replace('.', '_')
    return df

# Define Class to handle itad API calls
class itadapi:
    """ Simplified class to handle itad API calls"""
    
    # Static variables for API credentials (can be modified to self class if needing multiple instances)
    client_id = os.getenv('itad_client_id')
    client_secret = os.getenv('itad_client_secret')
    api_key = os.getenv('itad_api_key')

    if not client_id or not client_secret or not api_key:
        raise ValueError("Missing API Credentials")

    base_url = "https://api.isthereanydeal.com"

    @staticmethod
    def lookup_game(title: str):
        """ Lookup game information by title"""
        if not itadapi.api_key:
            raise ValueError("API Key is missing")
        
        # Load parameters
        params = {
            'title': title,
            'key': itadapi.api_key
        }

        # Set URL
        url = f"{itadapi.base_url}/games/lookup/v1"

        # Make GET request
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            json_data = response.json()

            game_found = json_data.get('found')
            if not game_found:
                raise ValueError(f"Game '{title}' not found in IsThereAnyDeal database.")
            
            return normalise_itad(json_data)
        
        except ValueError as e:
            print(f"{e}")
            return None
        except Exception as e:
            print(f" Error looking up game: {e}")
            return None
        
    def get_historical_prices(title: str, country: str = 'AU'):
        """ Get historical price data for a game by title"""
        if not itadapi.api_key:
            raise ValueError("API Key is missing")
        
        # Get game ID
        game_info = itadapi.lookup_game(title)
        if game_info is None:
            return None

        game_id = game_info.game_id

        # Load parameters
        params = {
            'id': game_id,
            'country': country,
            'key': itadapi.api_key
        }

        # Set URL
        url = f"{itadapi.base_url}/games/history/v2"

        # Make GET request
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            json_data = response.json()

            return normalise_itad(json_data)
        
        except Exception as e:
            print(f" Error retrieving historical prices: {e}")
            return None


