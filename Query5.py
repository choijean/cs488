[
    {
        '$match': {
            'highwayid': 3
        }
    }, {
        '$graphLookup': {
            'from': 'testclean', 
            'startWith': '$downstream', 
            'connectFromField': 'downstream', 
            'connectToField': 'stationid', 
            'as': 'route', 
            'depthField': 'order'
        }
    }, {
        '$match': {
            'locationtext': 'Johnson Cr NB'
        }
    }, {
        '$unwind': {
            'path': '$route', 
            'preserveNullAndEmptyArrays': True
        }
    }, {
        '$sort': {
            'downstream': 1, 
            'route.order': 1
        }
    }, {
        '$group': {
            '_id': '$locationtext', 
            'route': {
                '$push': '$route.locationtext'
            }
        }
    }
]