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

def get_rep_impact_factor(reputation: int) -> int:
    if reputation <= 60:
        return 1
    elif reputation < 90:
        return -1
    elif reputation <=100:
        return 1

def check_neighborhood_name(neighborhood_name: str) -> bool:
    return neighborhood_name.upper() in [x.upper() for x in hood_data]

class Market:

    def _drug_numbers(self, event: str = None) -> int:
        if not event:
            return randrange(4,7,1)
        ## Possible place for event logic

    def _get_rep(self, neighborhood_name: str) -> int:
        return hood_data[neighborhood_name]['reputation']

    def _get_sup_net(self, neighborhood_name: str) -> int:
        return hood_data[neighborhood_name]['supply_network']

    def _get_drugs_list(self, neighborhood_name: str) -> list:
        rep = self._get_rep(neighborhood_name)
        return [x for x in drug_data if drug_data[x]['max_rep'] >= rep and drug_data[x]['min_rep'] <= rep]

    def _get_drugs(self, drugs_list: list) -> list:
        return [Drug(drug) for drug in drugs_list]

    def _get_quantities(self, neighborhood_name: str) -> None:
        rep = self._get_rep(neighborhood_name)
        rep_index = get_rep_impact_factor(rep)
        supply_network = self._get_sup_net(neighborhood_name)

        for drug_idx in range(len(self.drugs)):
#            breakpoint()
            #base = self.drugs[drug_idx][list(self.drugs[drug_idx].keys())[0]]['base_quantity']
            base = self.drugs[drug_idx].base_quantity
            #price = self.drugs[drug_idx][list(self.drugs[drug_idx].keys())[0]]['current_cost']
            price = self.drugs[drug_idx].current_cost
           # base +(2x supply_network) +(rep_index*(0.4*rep)) +(rep*(1/price))
            quant_calc = (base + (rep_index*(0.05*rep)) + (rep*(1/price)) * (supply_network))

            #self.drugs[drug_idx][list(self.drugs[drug_idx].keys())[0]]['quantity'] = quant_calc
            self.drugs[drug_idx].quantity = int(quant_calc)

    def show(self):
        [print("{}: ${} [{}]".format(drug.name, drug.current_cost, drug.quantity)) for drug in self.drugs if drug.quantity > 0] 

#    def buy_drug(self, drug_name, quantity):



        
        ## How to decide the quantities?
            ## We should use prices and reputation to decide quantity
                ## Lower prices should mean more quantity
                ## Reputation could mean more quantity because the neighborhood has a better reuputation, but also it could mean the opposite because swankier neighborhoods might have supply issues over a more seedy neighborhood
                    ## Maybe create a band system where a reputation range of X means more quantity and Y less quantity and Z more or quantity, sor something like that
            ## Two multipliers: Reputation/price index, supply_network
            ## Multiply that by a base quantity level
                ## This should be new value


    def __init__(self, neighborhood_name: str, event: str = None):
        ## Pick X number of drugs
        number_of_drugs = self._drug_numbers(event)
        ## Get list of drugs based on neighborhood reputation
        drugs_list = self._get_drugs_list(neighborhood_name)

        self.drugs = self._get_drugs(drugs_list)
        ## Generate the different drug objects and save as list[?]
            ## Make it an attribute like drugs or soemthing
        self._get_quantities(neighborhood_name)


class Neighborhood:

    def __init__(self, neighborhood_name: str):

        if not check_neighborhood_name(neighborhood_name):
            raise NameError("{} is not a valid neighborhood name".format(neighborhood_name))

        self.name = neighborhood_name

        for key in hood_data[self.name]:
            setattr(Neighborhood, key, hood_data[self.name][key])

        self.market = Market(self.name)

    ##Name
    ##Reputation
    ##Market

