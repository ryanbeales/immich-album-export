import httpx

from logs import logging
logger = logging.getLogger(__name__)

class Immich():
    def __init__(self, api_key: str, server: str):
        self.headers = {
            "x-api-key": api_key
        }
        self.server = server
        self.httpx_client = httpx.Client(base_url=self.server, headers=self.headers)

    def _make_request(self, method: str, endpoint: str):
        logger.debug(f"Request: {method}. {endpoint}")
        response = self.httpx_client.request(method, endpoint)
        logger.debug("Response status: {response.status_code}")
        if response.status_code > 299:
            raise Exception('Expected status 2xx, got', response.status_code)
        
        return response

    def get_albums(self):
        albums = self._make_request("GET", "/api/albums").json()
        logger.debug("Albums: { albums}")
        return albums

    def get_album_assets(self, album_id: str):
        assets = self._make_request("GET", f"/api/albums/{album_id}").json()
        logger.debug(f"Album assets: {assets}")
        return assets

    def get_asset_original(self, asset_id: str):
        original = self._make_request("GET", f"/api/assets/{asset_id}/original")
        return original.content 