class Insulin:
    groups: dict

    def __init__(self, dset):
        self.groups = {
            "Class 1": (0, 140),
            "Class 2": (140, 199),
            "Class 3": (199, 10000),
        }
        self.dset = dset

    def calc_prob_diab(self):
        probs = []
        dset = self.dset
        for key, value in self.groups.items():
            if(value[0] == 0):
                condition = (dset.has_diab()) & (dset.insulin >= value[0]) & (dset.insulin <= value[1])
            else:
                condition = (dset.has_diab()) & (dset.insulin > value[0]) & (dset.insulin <= value[1])
            prob = dset.loc(condition).shape[0]/dset.qtt_total
            probs.append(prob)
        return probs

    def calc_prob_not_diab(self):        
        probs = []
        dset = self.dset
        for key, value in self.groups.items():
            if(value[0] == 0):
                condition = (dset.has_not_diab()) & (dset.insulin >= value[0]) & (dset.insulin <= value[1])
            else:
                condition = (dset.has_not_diab()) & (dset.insulin > value[0]) & (dset.insulin <= value[1])
            prob = dset.loc(condition).shape[0]/dset.qtt_total
            probs.append(prob)
        return probs


# print("Insulin classes")
# print("Class 1: 0")
# print("Class 2: 0 - 100")
# print("Class 3: >100")
# print()
# conditionInsulinClass1 = (dset.has_diab() ) & (db["Insulin"] == 0)
# conditionInsulinClass2 = (dset.has_diab() ) & (db["Insulin"] > 0) &(db["Insulin"] <= 100)
# conditionInsulinCLass3 = (dset.has_diab() ) & (db["Insulin"] > 100)

# print("Outcome == 1 ")
# print("Insulin Class 1: ", db.loc[conditionInsulinClass1].shape[0])
# print("Insulin Class 2: ", db.loc[conditionInsulinClass2].shape[0])
# print("Insulin Class 3: ", db.loc[conditionInsulinCLass3].shape[0])

# prob_has_diabetes["Insulin"].append(db.loc[conditionInsulinClass1].shape[0]/dset.qtt_total)
# prob_has_diabetes["Insulin"].append(db.loc[conditionInsulinClass2].shape[0]/dset.qtt_total)
# prob_has_diabetes["Insulin"].append(db.loc[conditionInsulinCLass3].shape[0]/dset.qtt_total)

# print()

# conditionInsulinClass1 = dset.has_not_diab() & (db["Insulin"] == 0)
# conditionInsulinClass2 = dset.has_not_diab() & (db["Insulin"] > 0) &(db["Insulin"] <= 100)
# conditionInsulinCLass3 = dset.has_not_diab() & (db["Insulin"] > 100)

# print("Outcome == 0 ")
# print("Insulin Class 1: ", db.loc[conditionInsulinClass1].shape[0])
# print("Insulin Class 2: ", db.loc[conditionInsulinClass2].shape[0])
# print("Insulin Class 3: ", db.loc[conditionInsulinCLass3].shape[0])


# prob_has_not_diabetes["Insulin"].append(db.loc[conditionInsulinClass1].shape[0]/dset.qtt_total)
# prob_has_not_diabetes["Insulin"].append(db.loc[conditionInsulinClass2].shape[0]/dset.qtt_total)
# prob_has_not_diabetes["Insulin"].append(db.loc[conditionInsulinCLass3].shape[0]/dset.qtt_total)
# print()