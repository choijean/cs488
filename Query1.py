[
    {
        '$unwind': {
            'path': '$detectors', 
            'preserveNullAndEmptyArrays': True
        }
    }, {
        '$unwind': {
            'path': '$detectors.loopdata', 
            'preserveNullAndEmptyArrays': True
        }
    }, {
        '$match': {
            '$or': [
                {
                    'detectors.loopdata.speed': {
                        '$gt': 80
                    }
                }, {
                    'detectors.loopdata.speed': {
                        '$lt': 5
                    }
                }
            ]
        }
    }, {
        '$count': 'count'
    }
]