from app.main import best_routes, possible_routes

cargos = [
    {
        'product': 'Oranges',
        'origin_lat': 40.6297634,
        'origin_lng': -91.31453499999999,
    },
    {
        'product': 'Wood',
        'origin_lat': 44.4582983,
        'origin_lng': -93.161604,
    },
]
trucks = [
    {
        'truck': 'Wisebuys Stores Incouverneur',
        'lat': 39.244853,
        'lng': -81.6637765,
    },
    {
        'truck': 'Hartford Plastics Incartford',
        'lat': 34.79981,
        'lng': -87.677251,
    },
]


def test_routes() -> None:
    routes = possible_routes(cargos, trucks)
    assert len(routes) == 4

    routes = best_routes(routes)
    assert len(routes) == 2
    assert routes == [{
        'cargo': 'Oranges',
        'truck': 'Hartford Plastics Incartford',
        'distance': 449.09
    }, {
        'cargo': 'Wood',
        'truck': 'Wisebuys Stores Incouverneur',
        'distance': 691.79
    }]
