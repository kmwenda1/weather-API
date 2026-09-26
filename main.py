import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
import httpx
from pydantic import BaseModel

class weatherResponse(BaseModel):
    city: str
    temperature: float
    feels_like: float
    description: str
    humidity: int



load_dotenv()
app = FastAPI()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.get("/")
def read_root():
    return {"Message": "weather API running", "key_loaded": WEATHER_API_KEY is not None}

@app.get("/weather/{city}", response_model=weatherResponse)
async def get_weather(city: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            WEATHER_API_URL,
            params={"q": city, "appid": WEATHER_API_KEY, "units": "metric"}
        )

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Could not fetch weather data")
        



        data = response.json()
        return weatherResponse(
            city=data["name"],
            temperature=data["main"]["temp"],
            feels_like=data["main"]["feels_like"],
            description=data["weather"][0]["description"],
            humidity=data["main"]["humidity"]
        )
    
    


