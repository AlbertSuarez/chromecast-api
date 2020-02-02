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

<br>
<p align="center">
  <img alt="Animation" src="docs/animation.gif" width="100%"/>
</p>
<br>

## Motivation

The idea of this project was to play a bit with the awesome [PyChromecast](https://github.com/balloob/pychromecast) Python library and move its functionalities to a the black box concept of an API.

Currently the implemented API, at port `8321`, is able to list all the available devices within the local network and cast a source given the device name and a URL with some media. Optionally, you can set `source_url=random` for being surprised with one of the gallery videos.

```
http://localhost:8321/play?source=CHROMECAST_NAME&source_url=random
```

Apart from its functionality, an API documentation (using [ReDoc](https://github.com/Redocly/redoc)) and the typical Swagger UI are available at the following URLs.

- API documentation: http://localhost:8321/docs
- Swagger UI: http://localhost:8321/ui

<br>
<p align="center">
  <img alt="API Documentation" src="docs/api_documentation.png" width="49%"/>
  <img alt="Swagger UI" src="docs/swagger_ui.png" width="49%"/>
</p>
<br>

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
