from immich import Immich

from pathlib import Path

from logs import logging
logger = logging.getLogger(__name__)

class ImmichAlbumDownloader(Immich):
    def __init__(self, api_key: str, server: str, album_name: str, output_dir: str):
        super().__init__(api_key, server)
        self.album_name = album_name
        self.output_dir = output_dir

    def download_album(self):
        albums = self.get_albums()

        # find albume by name
        album = None
        for testalbum in albums:
            if testalbum['albumName'] == self.album_name:
                album = testalbum

        if album is None:
            logger.error(f"Album '{self.album_name}' not found.")
            raise(f"Error: Album '{self.album_name}' not found.")

        logger.info(f"Found album '{album['albumName']}' with ID: {album['id']}")
        assets_data = self.get_album_assets(album['id'])

        assets = []
        if 'assets' in assets_data:
            # Immich v2 compatibility
            logger.info("Using Immich v2 API for album assets")
            assets = assets_data['assets']
        else:
            # Immich v3 API uses search endpoint
            logger.info("Using Immich v3 API for album assets")
            search_data = self.search_metadata(album['id'])
            if 'assets' in search_data and 'items' in search_data['assets']:
                assets = search_data['assets']['items']
            else:
                logger.error("Could not find assets in the search metadata response")

        for a in assets:
            asset_data = self.get_asset_original(a['id'])
            logger.info(f"Downloaded {len(asset_data)} bytes for asset {a['originalFileName']}")
            
            # Save to output directory
            output_path = Path(self.output_dir) / a['originalFileName']
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'wb') as f:
                f.write(asset_data)
            logger.info(f"Saved asset to {output_path}")