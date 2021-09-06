## Neighborhood

from drugs import Drug, drug_data
from random import randrange, sample, choice

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

class Market:
                                                                                                                                                def _drug_numbers(self, event=None):
        if not event:
            return(randrange(4,7,1))
        ## Possible place for event logic

    def _get_drugs_list(self, neighborhood_name):
        rep = hood_data[neighborhood_name]['reputation']
        drugs_list = [x for x in drug_data.keys() if drug_data[x]['max_rep'] >= rep and drug_data[x]['min_rep'] <= rep]
        return(drugs_list)

    def _get_drugs(self, drugs_list):
        drugs = [Drug(drug) for drug in drugs_list]
        return(drugs)


    def __init__(self, neighborhood_name, event=None):
        ## Pick X number of drugs
        number_of_drugs = self._drug_numbers(event)
        ## Get list of drugs based on neighborhood reputation
        drugs_list = self._get_drugs_list(neighborhood_name)
        self.drugs = self._get_drugs(drugs_list)
        ## Generate the different drug objects and save as list[?]
            ## Make it an attribute like drugs or soemthing





class Neighborhood:

    def __init__(self, neighborhood_name):

        if not check_neighborhood_name(neighborhood_name):
            raise NameError("{} is not a valid neighborhood name".format(neighborhood_name))

        self.name = neighborhood_name
        
        for key in hood_data[self.name]:
            setattr(Neighborhood, key, hood_data[self.name][key])

        self.market = Market(self.name)

    ##Name
    ##Reputation
    ##Market

