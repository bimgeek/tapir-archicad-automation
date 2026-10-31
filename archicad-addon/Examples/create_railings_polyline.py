import aclib
import math

railingFavorites = aclib.RunTapirCommand ('GetFavoritesByType', {'elementType': 'Railing'})
favoriteName = railingFavorites['favorites'][0] if railingFavorites and railingFavorites.get ('favorites') else None

# A straight railing, an L-shaped one from the first Railing favorite, one with an arc segment
# and one that climbs 2 m over its last segment (z is the node's elevation above the story).
railings = [
    {
        'polylineCoordinates': [{'x': 0.0, 'y': -5.0, 'z': 0.0}, {'x': 6.0, 'y': -5.0, 'z': 0.0}]
    },
    {
        'polylineCoordinates': [
            {'x': 0.0, 'y': -8.0, 'z': 0.0},
            {'x': 6.0, 'y': -8.0, 'z': 0.0},
            {'x': 6.0, 'y': -12.0, 'z': 0.0}
        ]
    },
    {
        'polylineCoordinates': [{'x': 10.0, 'y': -5.0, 'z': 0.0}, {'x': 16.0, 'y': -5.0, 'z': 0.0}],
        'polylineArcs': [{'begIndex': 0, 'endIndex': 1, 'arcAngle': math.pi / 2}]
    },
    {
        'polylineCoordinates': [{'x': 20.0, 'y': -5.0, 'z': 0.0}, {'x': 24.0, 'y': -5.0, 'z': 0.0}, {'x': 28.0, 'y': -5.0, 'z': 2.0}]
    }
]
if favoriteName:
    railings[1]['favoriteName'] = favoriteName

aclib.RunTapirCommand ('CreateRailingsFromPolyline', {'railingsData': railings})
