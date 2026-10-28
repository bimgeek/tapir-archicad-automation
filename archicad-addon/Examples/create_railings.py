import aclib
import math

railingFavorites = aclib.RunTapirCommand ('GetFavoritesByType', {'elementType': 'Railing'})
favoriteName = railingFavorites['favorites'][0] if railingFavorites and railingFavorites.get ('favorites') else None

# A straight railing, an L-shaped one from the first Railing favorite, and one with an arc segment.
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
        'bottomOffset': 0.5,
        'polylineCoordinates': [{'x': 10.0, 'y': -5.0, 'z': 0.0}, {'x': 16.0, 'y': -5.0, 'z': 0.0}],
        'polylineArcs': [{'begIndex': 0, 'endIndex': 1, 'arcAngle': math.pi / 2}]
    }
]
if favoriteName:
    railings[1]['favoriteName'] = favoriteName

aclib.RunTapirCommand ('CreateRailings', {'railingsData': railings})
