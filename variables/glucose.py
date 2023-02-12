class Glucose:
    groups: dict

    def __init__(self, dset, groups):
        self.groups = groups
        self.dset = dset

    def calc_prob_diab(self):
        probs = []
        dset = self.dset
        for key, value in self.groups.items():
            if(value[0] == 0):
                condition = (dset.has_diab()) & (dset.glucose >= value[0]) & (dset.glucose <= value[1])
            else:
                condition = (dset.has_diab()) & (dset.glucose > value[0]) & (dset.glucose <= value[1])
            prob = dset.loc(condition).shape[0]/dset.qtt_total
            probs.append(prob)
        return probs

    def calc_prob_not_diab(self):
        probs = []
        dset = self.dset
        for key, value in self.groups.items():
            if(value[0] == 0):
                condition = (dset.has_not_diab()) & (dset.glucose >= value[0]) & (dset.glucose <= value[1])
            else:
                condition = (dset.has_not_diab()) & (dset.glucose > value[0]) & (dset.glucose <= value[1])
            condition = (dset.has_not_diab()) & (dset.glucose > value[0]) & (dset.glucose <= value[1])
            prob = dset.loc(condition).shape[0]/dset.qtt_total
            probs.append(prob)
        return probs

# print("Glucose classes")
# print("Class 1: < 100")
# print("Class 2: 100 - 150")
# print("Class 3: >150")
# print()

# cond_glucose_1 = (dset.has_diab() ) & (dset.glucose < 100)
# cond_glucose_2 = (dset.has_diab() ) & (dset.glucose > 100) &(dset.glucose <= 150)
# cond_glucose_3 = (dset.has_diab() ) & (dset.glucose > 150)

# print("Outcome == 1 ")
# print("Glucose Class 1: ", db.loc[cond_glucose_1].shape[0])
# print("Glucose Class 2: ", db.loc[cond_glucose_2].shape[0])
# print("Glucose Class 3: ", db.loc[cond_glucose_3].shape[0])

# prob_has_diabetes["Glucose"].append(db.loc[cond_glucose_1].shape[0]/dset.qtt_total)
# prob_has_diabetes["Glucose"].append(db.loc[cond_glucose_2].shape[0]/dset.qtt_total)
# prob_has_diabetes["Glucose"].append(db.loc[cond_glucose_3].shape[0]/dset.qtt_total)


# print()
# cond_glucose_1 = not dset.has_diab() & (db["Glucose"] < 100)
# cond_glucose_2 = not dset.has_diab() & (db["Glucose"] > 100) &(db["Glucose"] <= 150)
# cond_glucose_3 = not dset.has_diab() & (db["Glucose"] > 150)

# print("Outcome == 0 ")
# print("Glucose Class 1: ", db.loc[cond_glucose_1].shape[0])
# print("Glucose Class 2: ", db.loc[cond_glucose_2].shape[0])
# print("Glucose Class 3: ", db.loc[cond_glucose_3].shape[0])

# prob_has_not_diabetes["Glucose"].append(db.loc[cond_glucose_1].shape[0]/dset.qtt_total)
# prob_has_not_diabetes["Glucose"].append(db.loc[cond_glucose_2].shape[0]/dset.qtt_total)
# prob_has_not_diabetes["Glucose"].append(db.loc[cond_glucose_3].shape[0]/dset.qtt_total)