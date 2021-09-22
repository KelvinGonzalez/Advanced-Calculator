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

    "meter": 1,
    "inch": 0.0254,
    "foot": 0.0254 * 12,
    "yard": 0.0254 * 12 * 3,
    "mile": 1609.344,

    "second": 1,
    "minute": 60,
    "hour": 60 * 60,
    "day": 60 * 60 * 24,
    "week": 60 * 60 * 24 * 7,
    "month": 60 * 60 * 24 * 30,
    "year": 60 * 60 * 24 * 365,
    "decade": 60 * 60 * 24 * 365 * 10,
    "century": 60 * 60 * 24 * 365 * 100,
    "millennium": 60 * 60 * 24 * 365 * 1000,

    "degrees": 1,
    "radians": 180/pi,
}


def convert(initial, final):
    # convert from "initial" to "final"
    return units[initial] / units[final]
