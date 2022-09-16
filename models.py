from sqlalchemy import Table, Column, ForeignKey
from db import meta
from sqlalchemy.sql.sqltypes import *

circuits_table = Table(
    "fran_circuits",
    meta,
    Column("id", Integer, primary_key=True),
    Column("ref", String(255)),
    Column("name", String(255)),
    Column("location", String(255)),
    Column("country", String(255)),
    Column("latitude", Float),
    Column("longitude", Float),
    Column("altitude", Integer),
)


constructors_table = Table(
    "fran_constructors",
    meta,
    Column("id", Integer, primary_key=True),
    Column("ref", String(255)),
    Column("name", String(255)),
    Column("nationality", String(255)),
)

drivers_table = Table(
    "fran_drivers",
    meta,
    Column("id", Integer, primary_key=True),
    Column("ref", String(255)),
    Column("number", Integer),
    Column("code", String(255)),
    Column("name", String(255)),
    Column("dob", String(255)),
    Column("nationality", String(255)),
)

races_table = Table(
    "fran_races",
    meta,
    Column("id", Integer, primary_key=True),
    Column("year", Integer),
    Column("round", Integer),
    Column("circuitId", Integer, ForeignKey("fran_circuits.id")),
    Column("name", String(255)),
    Column("date", String(255)),
    Column("time", String(255)),
)

results_table = Table(
    "fran_results",
    meta,
    Column("id", Integer, primary_key=True),
    Column("raceId", Integer, ForeignKey("fran_races.id")),
    Column("driverId", Integer),
    Column("constructorId", Integer, ForeignKey("fran_constructors.id")),
    Column("number", Integer),
    Column("grid", Integer),
    Column("position", Integer),
    Column("points", Integer),
    Column("laps", Integer),
    Column("time", String(255)),
    Column("milliseconds", Integer),
    Column("fastestLap", Integer),
    Column("rank", Integer),
    Column("fastestLapTime", String(255)),
    Column("fastestLapSpeed", String(255)),
    Column("statusId", Integer),
)
