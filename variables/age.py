# print("Ages classes")
# print("Class 1: 0 - 30")
# print("Class 2: 30 - 50")
# print("Class 3: >50")
# print()

# cond_age_1 = dset.has_diab() & (dset.age <= 30)
# cond_age_2 = dset.has_diab() & (dset.age >30)&(dset.age <= 50)
# cond_age_3 = dset.has_diab() & (dset.age >50)

# print("Outcome == 1 ")
# print("Age Class 1: ", db.loc[cond_age_1].shape[0])
# print("Age Class 2: ", db.loc[cond_age_2].shape[0])
# print("Age Class 3: ", db.loc[cond_age_3].shape[0])

# prob_has_diabetes["Age"].append(db.loc[cond_age_1].shape[0]/dset.qtt_total)
# prob_has_diabetes["Age"].append(db.loc[cond_age_2].shape[0]/dset.qtt_total)
# prob_has_diabetes["Age"].append(db.loc[cond_age_3].shape[0]/dset.qtt_total)

# print()
# cond_age_1 = dset.has_not_diab() & (dset.age <= 30)
# cond_age_2 = dset.has_not_diab() & (dset.age >30) &(dset.age <= 50)
# cond_age_3 = dset.has_not_diab() & (dset.age >50)


# print("Outcome == 0 ")
# print("Age Class 1: ", db.loc[cond_age_1].shape[0])
# print("Age Class 2: ", db.loc[cond_age_2].shape[0])
# print("Age Class 3: ", db.loc[cond_age_3].shape[0])


# prob_has_not_diabetes["Age"].append(db.loc[cond_age_1].shape[0]/dset.qtt_total)
# prob_has_not_diabetes["Age"].append(db.loc[cond_age_2].shape[0]/dset.qtt_total)
# prob_has_not_diabetes["Age"].append(db.loc[cond_age_3].shape[0]/dset.qtt_total)