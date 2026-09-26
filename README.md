# Weather API

A simple REST API built with FastAPI that fetches real-time weather data from OpenWeatherMap and returns it in a clean, custom JSON format.

Built as a learning project to practice: FastAPI, Pydantic, async HTTP requests, environment variables, and exception handling.

## Features

- `GET /` — health check, confirms the API is running and the API key loaded
- `GET /weather/{city}` — fetches current weather for a given city

## Tech Stack

- **FastAPI** — web framework
- **Pydantic** — data validation and response modeling
- **httpx** — async HTTP client for calling the external weather API
- **python-dotenv** — environment variable management
- **OpenWeatherMap API** — external weather data source

## How it works

1. A request comes in to `/weather/{city}`
2. The API calls OpenWeatherMap asynchronously using `httpx`
3. If the external API call fails (bad city, bad key, etc.), the API raises an `HTTPException` with the appropriate status code
4. On success, the raw response is mapped onto a Pydantic model (`WeatherResponse`) that defines exactly what fields the client gets back
5. FastAPI validates and serializes that model into JSON, and documents it automatically in `/docs`

## Setup

1. Clone the repo:
```bash
   git clone https://github.com/YOUR_USERNAME/weather-api.git
   cd weather-api
```

2. Create a virtual environment and install dependencies:
```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
```

3. Create a `.env` file in the project root:
```
   WEATHER_API_KEY=your_openweathermap_api_key_here
```
   Get a free key at [openweathermap.org](https://openweathermap.org/api). New keys can take up to 2 hours to activate.

4. Run the server:
```bash
   uvicorn main:app --reload
```

5. Visit `http://127.0.0.1:8000/docs` for interactive API documentation.

## Example

```
GET /weather/london
```

```json
{
  "city": "London",
  "temperature": 20.45,
  "feels_like": 19.54,
  "description": "overcast clouds",
  "humidity": 38
}
```

## Roadmap

- [ ] Save each lookup to a PostgreSQL database
- [ ] Dockerize the app
- [ ] Add more endpoints (forecast, history)

## License

MIT