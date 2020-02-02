# Chromecast API

[![HitCount](http://hits.dwyl.io/AlbertSuarez/chromecast-api.svg)](http://hits.dwyl.io/AlbertSuarez/chromecast-api)
![Python application](https://github.com/AlbertSuarez/chromecast-api/workflows/Python%20application/badge.svg)
[![GitHub stars](https://img.shields.io/github/stars/AlbertSuarez/chromecast-api.svg)](https://GitHub.com/AlbertSuarez/chromecast-api/stargazers/)
[![GitHub forks](https://img.shields.io/github/forks/AlbertSuarez/chromecast-api.svg)](https://GitHub.com/AlbertSuarez/chromecast-api/network/)
[![GitHub contributors](https://img.shields.io/github/contributors/AlbertSuarez/chromecast-api.svg)](https://GitHub.com/AlbertSuarez/chromecast-api/graphs/contributors/)
[![GitHub license](https://img.shields.io/github/license/AlbertSuarez/chromecast-api.svg)](https://github.com/AlbertSuarez/chromecast-api/blob/master/LICENSE)
[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://GitHub.com/AlbertSuarez/chromecast-api)

📺 Chromecast API within your local network

[API Endpoint](http://localhost:8321/) | [API Documentation](http://localhost:8321/docs) | [Swagger UI](http://localhost:8321/ui)

![Animation](docs/animation.gif)

## Requirements

1. Python 3.7+

## Recommendations

Usage of [virtualenv](https://realpython.com/blog/python/python-virtual-environments-a-primer/) is recommended for package library / runtime isolation.

## Usage

To run the API, please execute the following commands from the root directory:

1. Setup virtual environment

2. Install dependencies

    ```bash
    pip3 install -r requirements.lock
    ```

3. Run the server as a uWSGI server with the given bash script

    ```bash
    ./run.sh
    ```

    or as a Python module

    ```bash
    python3 -m src
    ```

## Authors

- [Albert Suàrez](https://github.com/AlbertSuarez)

## License

MIT © Chromecast API
