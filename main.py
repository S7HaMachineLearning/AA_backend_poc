from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins= [ "*" ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SensorType(Enum):
    TEMPERATURE = 'temperature'
    HUMIDITY = 'humidity'

class Sensor(BaseModel):
    id: str
    name: str
    type: SensorType	
    enabled: bool

class Automation(BaseModel):
    id: str
    name: str
    enabled: bool

sensors = {
    0: Sensor(id="1", name="Temperature inside", type=SensorType.TEMPERATURE, enabled=True),
    1: Sensor(id="2", name="Humidity inside", type=SensorType.HUMIDITY, enabled=False),
    2: Sensor(id="3", name="Temperature outside", type=SensorType.TEMPERATURE, enabled=True),
    3: Sensor(id="4", name="Humidity outside", type=SensorType.HUMIDITY, enabled=True),
}

automations = {
    0: Automation(id="1", name="Turn on the light when it's dark", enabled=True),
    1: Automation(id="2", name="Turn on the fan when it's hot", enabled=True),
    2: Automation(id="3", name="Turn on the heater when it's cold", enabled=False),
    3: Automation(id="4", name="Turn on the air conditioner when it's hot", enabled=True),
}




# FastAPI handles JSON serialization and deserialization for us.
# We can simply use built-in python and Pydantic types, in this case dict[int, Item].
@app.get("/sensors")
def getSensors() -> dict[str, dict[int, Sensor]]:
    return {"sensors": sensors}

@app.get("/automations")
def getAutomations() -> dict[str, dict[int, Automation]]:
    return {"automations": automations}

@app.post("/ml")
def callML():
    # Do ML stuff here
    return {"result": "success"}