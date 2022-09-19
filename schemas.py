from pydantic import BaseModel


class Circuit(BaseModel):
    id: int
    ref: str
    name: str
    location: str
    country: str
    latitude: float
    longitude: float
    altitude: int

    class Config:
        orm_mode = True


class Constructor(BaseModel):
    id: int
    ref: str
    name: str
    nationality: str

    class Config:
        orm_mode = True


class Driver(BaseModel):
    id: int
    ref: str
    code: str
    name: str
    dob: str
    nationality: str

    class Config:
        orm_mode = True


class Race(BaseModel):
    id: int
    year: int
    round: int
    circuitId: int
    name: str
    date: str
    time: str

    class Config:
        orm_mode = True


class Result(BaseModel):
    id: int
    raceId: int
    driverId: int
    constructorId: int
    number: int
    grid: int
    position: int
    points: int
    laps: int
    time: str
    milliseconds: int
    fastestLap: int
    rank: int
    fastestLapTime: str
    fastestLapSpeed: float
    statusId: int

    class Config:
        orm_mode = True
