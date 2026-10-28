import aclib
import math

# An extruded vault: an arched profile swept 8 m along the project Y axis.
# A revolved dome with a round hole cut through its top.
# A ruled shell between a straight and a curved edge.
aclib.RunTapirCommand (
    'CreateShells', {
        'shellsData': [
            {
                'shellClass': 'Extruded',
                'thickness': 0.2,
                'profile': {
                    'coordinates': [{'x': -3.0, 'y': 0.0}, {'x': 3.0, 'y': 0.0}],
                    'arcs': [{'begIndex': 0, 'endIndex': 1, 'arcAngle': -math.pi / 2}]
                },
                'basePlane': {
                    'origin': {'x': 0.0, 'y': 0.0, 'z': 0.0},
                    'xAxis': {'x': 1.0, 'y': 0.0, 'z': 0.0},
                    'yAxis': {'x': 0.0, 'y': 0.0, 'z': 1.0},
                    'zAxis': {'x': 0.0, 'y': -1.0, 'z': 0.0}
                },
                'extrusionVector': {'x': 0.0, 'y': 0.0, 'z': -8.0}
            },
            {
                'shellClass': 'Revolved',
                'thickness': 0.15,
                'basePlane': {'origin': {'x': 15.0, 'y': 0.0, 'z': 0.0}},
                'profile': {
                    'coordinates': [{'x': 4.0, 'y': 0.0}, {'x': 0.0, 'y': 4.0}],
                    'arcs': [{'begIndex': 0, 'endIndex': 1, 'arcAngle': math.pi / 2}]
                },
                'holes': [
                    {
                        'coordinates': [
                            {'x': 1.0 * math.cos (a * math.pi / 8), 'y': 1.0 * math.sin (a * math.pi / 8)} for a in range (16)
                        ],
                        'plane': {'origin': {'x': 15.0, 'y': 0.0, 'z': 6.0}},
                        'depth': -6.0
                    }
                ]
            },
            {
                'shellClass': 'Ruled',
                'thickness': 0.1,
                'basePlane': {'origin': {'x': 30.0, 'y': 0.0, 'z': 0.0}},
                'profile': {
                    'coordinates': [{'x': 0.0, 'y': 0.0}, {'x': 6.0, 'y': 0.0}]
                },
                'profilePlane': {
                    'xAxis': {'x': 1.0, 'y': 0.0, 'z': 0.0},
                    'yAxis': {'x': 0.0, 'y': 0.0, 'z': 1.0},
                    'zAxis': {'x': 0.0, 'y': -1.0, 'z': 0.0}
                },
                'secondProfile': {
                    'coordinates': [{'x': 0.0, 'y': 3.0}, {'x': 6.0, 'y': 3.0}],
                    'arcs': [{'begIndex': 0, 'endIndex': 1, 'arcAngle': math.pi / 3}]
                },
                'secondProfilePlane': {
                    'origin': {'x': 0.0, 'y': 5.0, 'z': 0.0},
                    'xAxis': {'x': 1.0, 'y': 0.0, 'z': 0.0},
                    'yAxis': {'x': 0.0, 'y': 0.0, 'z': 1.0},
                    'zAxis': {'x': 0.0, 'y': -1.0, 'z': 0.0}
                }
            }
        ]
    })
