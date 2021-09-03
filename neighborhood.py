## Neighborhood

hood_data = {
        "Jamaica Plain": {
            "reputation": 65
            },
        "Downtown": {
            "reputation": 95
            },
        "Back Bay": {
            "reputation": 80
            },
        "Fenway": {
            "reputation": 70
            },
        "Mission Hill": {
            "reputation": 50
            },
        "The Burbs": {
            "reputation": 100
            },
        "Roxbury": {
            "reputation": 50
            },
        "Mattapan": {
            "reputation": 60
            },
        "Southie": {
            "reputation": 30
            }
        }

def check_neighborhood_name(neighborhood_name):
    global hood_data
    if neighborhood_name not in hood_data.keys():
        return(False)
    return(True)


class Neighborhood:

    def __init__(self, neighborhood_name):

        if not check_neighborhood_name(neighborhood_name):
            raise NameError("{} is not a valid neighborhood name".format(neighborhood_name))

        self.name = neighborhood_name
        
        for key in hood_data[self.name]:
            setattr(Neighborhood, key, hood_data[self.name][key])

        self.market = None ## NEED TO BUILD THIS OUT STILL

    ##Name
    ##Reputation
    ##Market

