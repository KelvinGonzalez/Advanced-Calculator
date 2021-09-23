from math import pi

units = {
    "deci": 1e-1,
    "centi": 1e-2,
    "milli": 1e-3,
    "micro": 1e-6,
    "nano": 1e-9,
    "pico": 1e-12,
    "femto": 1e-15,
    "deca": 1e1,
    "hecto": 1e2,
    "kilo": 1e3,
    "mega": 1e6,
    "giga": 1e9,
    "tera": 1e12,
    "peta": 1e15,

    "meters": 1,
    "inches": 0.0254,
    "feet": 0.0254 * 12,
    "yards": 0.0254 * 12 * 3,
    "miles": 1609.344,

    "seconds": 1,
    "minutes": 60,
    "hours": 60 * 60,
    "days": 60 * 60 * 24,
    "weeks": 60 * 60 * 24 * 7,
    "months": 60 * 60 * 24 * 30,
    "years": 60 * 60 * 24 * 365,
    "decades": 60 * 60 * 24 * 365 * 10,
    "centuries": 60 * 60 * 24 * 365 * 100,
    "millenniums": 60 * 60 * 24 * 365 * 1000,

    "degrees": 1,
    "radians": 180/pi,
}


def convert(initial, final):
    # convert from "initial" to "final"
    return units[initial] / units[final]
