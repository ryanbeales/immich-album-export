from settings import get_settings
from immichalbumdownloader import ImmichAlbumDownloader

from logs import logging
logger = logging.getLogger(__name__)

def main():
    settings = get_settings()

    immich_downloader = ImmichAlbumDownloader(
        settings.immich_api_key,
        settings.immich_server,
        settings.immich_album_name,
        settings.output_dir
    )    

    immich_downloader.download_album()


if __name__ == "__main__":
    main()