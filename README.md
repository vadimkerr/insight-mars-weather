# Setup

Install required python modules:

`python3 -m pip install -r requirements.txt`

Give execution permission to the script:

`chmod +x ./core/mars_weather.py`


Set API_KEY env variable (you can obtain one here: https://api.nasa.gov/):

`export API_KEY=<your_api_key>`


# Run

You can run the script either as:

`./core/mars_weather.py`

or:

`python3 -m core`


Also, you can run the script in docker container:

Build: `docker build -t mars-weather .`

Run: `docker run -e API_KEY=<your_api_key> mars-weather`


# Test

Py.test is used as a testing suite

Run tests:

`python3 -m pytest tests/`
