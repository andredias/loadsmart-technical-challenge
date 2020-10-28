from pytest import mark

from app.main import haversine  # isort: skip


@mark.parametrize(
    'lat1, long1, lat2, long2, distance', [
        (51.509865, -0.118092, 48.8567, 2.3508, 213.36),
        (40.7033962, -74.2351462, 48.8567, 2.3508, 3637.07),
        (48.8567, 2.3508, 40.7033962, -74.2351462, 3637.07),
    ]
)
def test_haversine(lat1: float, long1: float, lat2: float, long2: float, distance: float) -> None:
    assert abs(haversine(lat1, long1, lat2, long2) - distance) < 0.01
