import csv
from math import asin, cos, radians, sin, sqrt
from pathlib import Path
from typing import Dict, List

import typer


def distance(lat1: float, long1: float, lat2: float, long2: float) -> float:
    '''
    Calculate distance between Latitude/Longitude points in miles

    based on https://en.wikipedia.org/wiki/Haversine_formula
    '''

    EARTH_RADIUS = 3_958.75  # miles

    lat1, long1 = radians(lat1), radians(long1)
    lat2, long2 = radians(lat2), radians(long2)

    delta_lat = lat2 - lat1
    delta_long = long2 - long1
    d = sin(delta_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(delta_long / 2) ** 2
    haversine = 2 * EARTH_RADIUS * asin(sqrt(d))
    return haversine


def possible_routes(cargos: List[Dict], trucks: List[Dict]) -> List[Dict]:
    '''
    Combine all cargos with distance from trucks to produce all possible candidates.
    '''
    result = []
    for cargo in cargos:
        for truck in trucks:
            lat1, long1 = float(cargo['origin_lat']), float(cargo['origin_lng'])
            lat2, long2 = float(truck['lat']), float(truck['lng'])
            dist = round(distance(lat1, long1, lat2, long2), 2)
            result.append(dict(cargo=cargo['product'], truck=truck['truck'], distance=dist))
    return result


def best_routes(routes: List[Dict]) -> List[Dict]:
    '''
    Find the optimal mapping of trucks to cargos to minimize the overall distances
    the trucks must travel​​.
    '''
    routes.sort(key=lambda row: row['distance'])
    result = []
    while len(routes):
        row = routes[0]
        result.append(row)
        routes = [r for r in routes if r['cargo'] != row['cargo'] and r['truck'] != row['truck']]
    return result


def main(cargo_csv: Path, trucks_csv: Path) -> None:
    with cargo_csv.open() as f:
        cargos = [c for c in csv.DictReader(f)]
    with trucks_csv.open() as f:
        trucks = [t for t in csv.DictReader(f)]
    routes = possible_routes(cargos, trucks)
    result = best_routes(routes)
    with Path('./result.csv').open('w') as f:
        fieldnames = ('cargo', 'truck', 'distance')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in result:
            writer.writerow(row)
    return



if __name__ == '__main__':
    typer.run(main)
