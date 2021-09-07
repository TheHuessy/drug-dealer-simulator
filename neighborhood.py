## Neighborhood

from drugs import Drug, drug_data
from random import randrange

hood_data = {
        "Jamaica Plain": {
            "reputation": 65,
            "supply_network": 3
            },
        "Downtown": {
            "reputation": 95,
            "supply_network": 5
            },
        "Back Bay": {
            "reputation": 80,
            "supply_network": 3
            },
        "Fenway": {
            "reputation": 70,
            "supply_network": 4
            },
        "Mission Hill": {
            "reputation": 50,
            "supply_network": 5
            },
        "The Burbs": {
            "reputation": 100,
            "supply_network": 2
            },
        "Roxbury": {
            "reputation": 50,
            "supply_network": 5
            },
        "Mattapan": {
            "reputation": 60,
            "supply_network": 5
            },
        "Southie": {
            "reputation": 30,
            "supply_network": 5
            }
        }

def get_rep_impact_factor(reputation):
    if reputation <= 60:
        return(1)
    elif reputation < 90:
        return(-1)
    elif reputation <=100:
        return(1)

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

    def _get_rep(self, neighborhood_name):
        return(hood_data[neighborhood_name]['reputation'])

    def _get_sup_net(self, neighborhood_name):
        return(hood_data[neighborhood_name]['supply_network'])

    def _get_drugs_list(self, neighborhood_name):
        rep = self._get_rep(neighborhood_name)
        drugs_list = [x for x in drug_data.keys() if drug_data[x]['max_rep'] >= rep and drug_data[x]['min_rep'] <= rep]
        return(drugs_list)

    def _get_drugs(self, drugs_list):
        drugs = [Drug(drug) for drug in drugs_list]
        return(drugs)

    def _get_quantities(self, neighborhood_name):
        rep = self._get_rep(neighborhood_name)
        rep_index = get_rep_impact_factor(rep)
        supply_network = self._get_sup_net(neighborhood_name)


        for drug_idx in range(len(self.drugs)):
            base = self.drugs[drug_idx][list(self.drugs[drug_idx].keys())[0]]['base_quantity']
            price = self.drugs[drug_idx][list(self.drugs[drug_idx].keys())[0]]['current_cost']
           # base +(2x supply_network) +(rep_index*(0.4*rep)) +(rep*(1/price))
            quant_calc = (base + (rep_index*(0.4*rep)) + (rep*(1/price)) * (supply_netowrk))

            self.drugs[drug_idx][list(self.drugs[drug_idx].keys())[0]]['quantity'] = quant_calc




        
        ## How to decide the quantities?
            ## We should use prices and reputation to decide quantity
                ## Lower prices should mean more quantity
                ## Reputation could mean more quantity because the neighborhood has a better reuputation, but also it could mean the opposite because swankier neighborhoods might have supply issues over a more seedy neighborhood
                    ## Maybe create a band system where a reputation range of X means more quantity and Y less quantity and Z more or quantity, sor something like that
            ## Two multipliers: Reputation/price index, supply_network
            ## Multiply that by a base quantity level
                ## This should be new value


    def __init__(self, neighborhood_name, event=None):
        ## Pick X number of drugs
        number_of_drugs = self._drug_numbers(event)
        ## Get list of drugs based on neighborhood reputation
        drugs_list = self._get_drugs_list(neighborhood_name)
        
        self.drugs = self._get_drugs(drugs_list)
        ## Generate the different drug objects and save as list[?]
            ## Make it an attribute like drugs or soemthing
        self._get_quantities(neighborhood_name)


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

