class Controller:
    def __init__(self):
        self.in_descriptions = {}

    def setData(self, temperature, humidity, time, rules):
        self.in_descriptions['temperature'] = temperature
        self.in_descriptions['humidity'] = humidity
        self.out_description = time
        self.rules = rules

    def compute(self, inputs):
        fuzzy_vals = self._compute_descriptions(inputs)
        print(fuzzy_vals)
        rule_vals = self._compute_rules_fuzzy(fuzzy_vals)
        print(rule_vals)
        # Process for better use (take only result)
        fuzzy_out_vars = [(list(descr[0].values())[0], descr[1]) for descr in rule_vals]
        print(fuzzy_out_vars)
        weighted_total = 0
        weight_sum = 0
        for var in fuzzy_out_vars:
            weight_sum += var[1]
            weighted_total += self.out_description.defuzzify(*var) * var[1]
            print(var, self.out_description.defuzzify(*var))
        print(weighted_total, weight_sum)
        return weighted_total / weight_sum

    def _compute_descriptions(self, inputs):
        return { 
            var_name: self.in_descriptions[var_name].fuzzify(inputs[var_name]) 
                for var_name, val in inputs.items() 
            }

    def _compute_rules_fuzzy(self, fuzzy_vals):
        """
            Returns the fuzzy output of all rules
        """
        return [rule.evaluate(fuzzy_vals) for rule in self.rules
                if rule.evaluate(fuzzy_vals)[1] != 0]