[
    {
        '$match': {
            '$and': [
                {
                    'detectors.loopdata.starttime': {
                        '$regex': '2011-09-15.*'
                    }
                }, {
                    'locationtext': 'Foster NB'
                }
            ]
        }
    }, {
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
        '$group': {
            '_id': '$locationtext', 
            'count': {
                '$sum': '$detectors.loopdata.volume'
            }
        }
    }
]