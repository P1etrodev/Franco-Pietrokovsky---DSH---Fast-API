import json
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from db import engine
from alias import *

app = FastAPI(title="Franco Pietrokovsky - DSH - FastAPI", version="1.0")

with open("tokens.json", encoding="utf-8") as f:
    TOKENS = json.load(f)
    TOKENS = TOKENS.values()


@app.get("/dev/{token}")
def development_enviroment(token):
    if token in TOKENS:
        raise HTTPException(
            status_code=418,
            detail="Congratulations, you have access. Welcome to Development Department, where we don't do absolutely nothing. Have a cup of tea.",
        )
    raise HTTPException(status_code=401, detail="Invalid token. Access not granted.")


@app.get("/")
def home():
    return RedirectResponse("https://henryapi.up.railway.app/docs")


@app.get("/races/most_races_yr")
def get_most_races():
    query = (
        sql_select(
            [
                races_cols.year,
                sql_count(races_cols.year).label("race_count"),
            ]
        )
        .group_by(races_cols.year)
        .order_by(sql_text("race_count desc"))
    )

    most_races = dict(engine.execute(query).first())

    query = races_select().filter_by(year=most_races["year"])

    most_races["races"] = engine.execute(query).fetchall()

    return most_races


@app.get("/drivers/most_first_pos")
def get_most_first_position():
    query = (
        sql_select(
            [
                results_cols.driverId.label("id"),
                sql_sum(results_cols.position).label("wins"),
            ]
        )
        .where(results_cols.position == 1)
        .group_by(results_cols.driverId)
        .order_by(sql_text("wins desc"))
    )
    driver = engine.execute(query).first()
    wins = driver["wins"]
    query = drivers_select().filter_by(id=driver["id"])
    most_first = dict(engine.execute(query).first())
    most_first["wins"] = wins
    return most_first


@app.get("/circuits/most_used_circuit")
def get_most_used_circuit():
    query = (
        sql_select(
            [
                races_cols.circuitId.label("most_used_circuit"),
                sql_count(races_cols.circuitId).label("times_used"),
            ]
        )
        .group_by(races_cols.circuitId)
        .order_by(sql_text("times_used desc"))
    )
    most_used = engine.execute(query).first()
    times_used = most_used["times_used"]
    query = circuits_select().where(circuits_cols.id == most_used["most_used_circuit"])
    most_used = dict(engine.execute(query).first())
    most_used["times_used"] = times_used
    return most_used


@app.get("/drivers/driver_with_most_points")
def get_driver_with_most_points():
    subquery = (
        sql_select([constructors_cols.id])
        .where(constructors_cols.nationality.in_(("British", "American")))
        .subquery()
    )
    query = (
        sql_select(
            [
                results_cols.driverId.label("id"),
                sql_sum(results_cols.points).label("points_sum"),
            ]
        )
        .where(results_cols.constructorId.in_(subquery))
        .group_by("driverId")
        .order_by(sql_text("points_sum desc"))
    )

    driver = engine.execute(query).first()
    driver_points = driver["points_sum"]
    query = drivers_select(whereclause=drivers_cols.id == driver["id"])
    driver = dict(engine.execute(query).first())
    driver["points"] = driver_points

    return driver


@app.get("/drivers")
def get_drivers(id: int = None):
    if id:
        return engine.execute(drivers_select().where(drivers_cols.id == id)).first()
    return engine.execute(drivers_select()).fetchall()


@app.get("/races")
def get_drivers(id: int = None):
    if id:
        return engine.execute(races_select().where(races_cols.id == id)).first()
    return engine.execute(races_select()).fetchall()


@app.get("/results")
def get_drivers(id: int):
    if id:
        return engine.execute(results_select().where(results_cols.id == id)).first()
    return engine.execute(results_select()).fetchall()


@app.get("/circuits")
def get_drivers(id: int = None):
    if id:
        return engine.execute(circuits_select().where(circuits_cols.id == id)).first()
    return engine.execute(circuits_select()).fetchall()


@app.get("/constructors")
def get_drivers(id: int = None):
    if id:
        return engine.execute(
            constructors_select().where(constructors_cols.id == id)
        ).first()
    return engine.execute(constructors_select()).fetchall()
