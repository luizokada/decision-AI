class BMI:

    groups: dict

    def __init__(self, dset):
        self.groups = {
            "Class 1": (0, 18.5),
            "Class 2": (18.5, 25),
            "Class 3": (25, 1000),
        }
        self.dset = dset

    def calc_prob_diab(self):
        probs = []
        dset = self.dset
        for key, value in self.groups.items():
            condition = (dset.has_diab()) & (dset.bmi > value[0]) & (dset.bmi <= value[1])
            prob = dset.loc(condition).shape[0]/dset.qtt_total
            probs.append(prob)
        return probs
    
    def calc_prob_not_diab(self):
        probs = []
        dset = self.dset
        for key, value in self.groups.items():
            condition = (dset.has_not_diab()) & (dset.bmi > value[0]) & (dset.bmi <= value[1])
            prob = dset.loc(condition).shape[0]/dset.qtt_total
            probs.append(prob)
        return probs