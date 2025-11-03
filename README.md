# immmich-export-album
A simple tool to export an album as files from an immich server.

My use case is an existing photo frame which collects photos from an nfs directory. This tool will sync immich albums in to this directory where they will be picked up by the photoframe. This will be run in kuberenetes as a cronjob, placing the files in to the photo directory nightly.

## Running
Get an api key for your immich instance at:
https://immich-server-name/user-settings

Give the permissions:
```
album.download
album.read
asset.download
```

Then it's easiest to run the docker container, otherwise use steps similar to the local setup below.
```
docker run --rm ghcr.io/ryanbeales/immich-export-album --immich-api-key={apikey} --immich_server=https://immich-server-name --immich_album_name="Album" --output_dir=output
```
The output directory will contain all the files in the album and keep them synced. It is a one way sync, files removed from the album will remain in the output directory and removing files form the output will have them replaced.

## Kubernetes

For an example of running in kuberetnes, please see the manifests [here](https://github.com/ryanbeales/personal-microk8s-config/tree/main/self-hosted-services/image-album-export)

## Local Setup
Install `uv` by following https://docs.astral.sh/uv/getting-started/installation/

Install python 3.13
```
uv python install 3.13
```

Install dependencies:
```
uv sync
```

Create a `.env` file (these can be specified in `.env`, as environment variables or as command line arguments):
```
OUTPUT_DIR=output
IMMICH_SERVER=https://immich-server-name
IMMICH_API_KEY=apikey
IMMICH_ALBUM_NAME=PhotoFrame
```

Create the directories:
```
mkdir output
```

Run the application:
```
uv run python main.py
```