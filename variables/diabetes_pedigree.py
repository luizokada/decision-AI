class DiabetesPedigreeFunction:
    groups: dict

    def __init__(self, dset):
        self.groups = {
            "Class 1": (0, 0.3),
            "Class 2": (0.3, 1),
        }
        self.dset = dset

    def calc_prob_diab(self):
        probs = []
        dset = self.dset
        for key, value in self.groups.items():
            condition = (dset.has_diab()) & (dset.diab_pedigree > value[0]) & (dset.diab_pedigree <= value[1])
            prob = dset.loc(condition).shape[0]/dset.qtt_total
            probs.append(prob)
        return probs

    def calc_prob_not_diab(self):
        probs = []
        dset = self.dset
        for key, value in self.groups.items():
            condition = (dset.has_not_diab()) & (dset.diab_pedigree > value[0]) & (dset.diab_pedigree <= value[1])
            prob = dset.loc(condition).shape[0]/dset.qtt_total
            probs.append(prob)
        return probs

# print("DiabetesPedigreeFunction classes")
# print("Class 1: <= 0.3")
# print("Class 2: > 0.3")
# print()

# cond_diab_pedigree_1 = (dset.has_diab() ) & (db["DiabetesPedigreeFunction"] <= 0.3)
# cond_diab_pedigree_2 = (dset.has_diab() ) & (db["DiabetesPedigreeFunction"] > 0.3)

# print("Outcome == 1 ")
# print("DiabetesPedigreeFunction Class 1: ", db.loc[cond_diab_pedigree_1].shape[0])
# print("DiabetesPedigreeFunction Class 2: ", db.loc[cond_diab_pedigree_2].shape[0])

# prob_has_diabetes["DiabetesPedigreeFunction"].append(db.loc[cond_diab_pedigree_1].shape[0]/dset.qtt_total)
# prob_has_diabetes["DiabetesPedigreeFunction"].append(db.loc[cond_diab_pedigree_2].shape[0]/dset.qtt_total)

# print()

# cond_diab_pedigree = dset.has_not_diab() & (db["DiabetesPedigreeFunction"] <= 0.3)
# cond_diab_pedigree_2 = dset.has_not_diab() & (db["DiabetesPedigreeFunction"] > 0.3) 

# print("Outcome == 0 ")
# print("DiabetesPedigreeFunction Class 1: ", db.loc[cond_diab_pedigree].shape[0])
# print("DiabetesPedigreeFunction Class 2: ", db.loc[cond_diab_pedigree_2].shape[0])


# prob_has_not_diabetes["DiabetesPedigreeFunction"].append(db.loc[cond_diab_pedigree].shape[0]/dset.qtt_total)
# prob_has_not_diabetes["DiabetesPedigreeFunction"].append(db.loc[cond_diab_pedigree_2].shape[0]/dset.qtt_total)