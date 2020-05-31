class FuzzyDescriptions:
    def __init__(self):
        self.regions = {}
        self.inverse = {}

    def add_region(self, var_vame, membership_function, inverse=None):
        self.regions[var_vame] = membership_function
        self.inverse[var_vame] = inverse

    def fuzzify(self, value):
        return {name: membership_function(value) for name, membership_function in self.regions.items()}

    def defuzzify(self, var_name, value):
        return self.inverse[var_name](value)


class FuzzyRule:
    def __init__(self, inputs, output):
        self.inputs = inputs
        self.output = output

    def evaluate(self, fuzzifiedValues):
        # Operator AND -> intersection (minimum) of 2 sets
        return [self.output, min(fuzzifiedValues[descr_name][var_name] for descr_name, var_name in self.inputs.items())]