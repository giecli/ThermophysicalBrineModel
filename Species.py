class Species:

    def __init__(self, rkt_name, cp_name, elements, Mr, charge, phase):
        self.name = rkt_name
        self.alias = {"RKT": rkt_name, "CP": cp_name}
        self.elements = elements
        self.Mr = Mr
        self.charge = charge
        self.phase = phase

    def __str__(self):
        text = "Species Name: {} \n".format(self.name)

        text = text + "Phase: {}\n".format(self.phase.value)

        text = text + "Aliases: \n"
        for alias in self.alias:
            text = text + "\t{}: {}\n".format(alias, self.alias[alias])

        text = text + "Elements:\n"
        for element in self.elements:
            text = text + "\t{}\n".format(element)

        text = text + "Molecular Weight: {} kg/mol\n".format(self.Mr)
        text = text + "Charge: {} \n".format(self.charge)

        return text

