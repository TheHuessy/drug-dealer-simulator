## Drugs

## Attributes

## Methods


from random import shuffle

#drug_types = ["Acid", "Speed", "Weed", "Coke", "Shrooms", "Aderall", "Glue", "Heroin"]

drug_data = {
                "Acid": {
                    "min_rep": 10,
                    "max_rep": 100,
                    "floor_price": 15,
                    "max_price": 50,
                    "base_quantity": 10
                    },
                "Speed": {
                    "min_rep": 10,
                    "max_rep": 100,
                    "floor_price": 25,
                    "max_price": 50,
                    "base_quantity": 15
                    },
                "Weed": {
                    "min_rep": 0,
                    "max_rep": 100,
                    "floor_price": 5,
                    "max_price": 60,
                    "base_quantity": 20
                    },
                "Coke": {
                    "min_rep": 35,
                    "max_rep": 100,
                    "floor_price": 50,
                    "max_price": 100,
                    "base_quantity": 10
                    },
                "Shrooms": {
                    "min_rep": 0,
                    "max_rep": 70,
                    "floor_price": 10,
                    "max_price": 50,
                    "base_quantity": 15
                    },
                "Aderall": {
                    "min_rep": 50,
                    "max_rep": 100,
                    "floor_price": 50,
                    "max_price": 75,
                    "base_quantity": 10
                    },
                "Molly": {
                    "min_rep": 50,
                    "max_rep": 100,
                    "floor_price": 30,
                    "max_price": 70,
                    "base_quantity": 7
                    },
                "Meth": {
                    "min_rep": 0,
                    "max_rep": 25,
                    "floor_price": 15,
                    "max_price": 75,
                    "base_quantity": 20
                    },
                "Glue": {
                    "min_rep": 0,
                    "max_rep": 15,
                    "floor_price": 2,
                    "max_price": 10,
                    "base_quantity": 50
                    },
                "Heroin": {
                    "min_rep": 0,
                    "max_rep": 90,
                    "floor_price": 10,
                    "max_price": 60,
                    "base_quantity": 10
                    }
                }

def check_drug_type(drug_type):
    global drug_data
    #drug_types = ["Acid", "Speed", "Weed", "Coke", "Shrooms", "Aderall", "Glue", "Heroin"]

    if drug_type not in drug_data.keys():
        return(False)

    return(True)

class Drug:

    def _get_drug_metadata(self, drug_type):
        global drug_data
        return(drug_data[drug_type])

    def _get_drug_price(self):
        self.current_cost = random.choice(range(self.floor_price, self.max_price+1))

#    def _get_drug_quantity(self):
#        self.quantity = #How to gauge quantity based on no neighborhood data?    ###random.choice(range(self.floor_price, self.max_price+1))


    def __init__(self, drug_type, value=None):
        if not check_drug_type(drug_type):
            raise NameError("{} is not a valid drug type".format(drug_type))

        self.name = drug_type

        if value:
            self.value = value
        else:
            self.value = 0

        drug_metadata = self._get_drug_metadata(self.name)

        for key in drug_metadata:
            setattr(Drug, key, drug_metadata[key])

        ## Generate 'current_cost' value
        self._get_drug_price()

