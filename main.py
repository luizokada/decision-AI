
import pandas as pd


db = pd.read_csv('./DB/diabetes.csv')

prob_has_diabetes = {
    "Age":[],
    "Glucose":[],
    "Insulin":[],
    "DiabetesPedigreeFunction":[],
    
}

prob_has_not_diabetes = {
    "Age":[],
    "Glucose":[],
    "Insulin":[],
    "DiabetesPedigreeFunction":[],
}

num_total = db.shape[0]
cond_diabetes = db["Outcome"] == 1
num_total_diabetes = db.loc[cond_diabetes].shape[0]
num_not_diabetes = num_total - num_total_diabetes

print("Ages classes")
print("Class 1: 0 - 30")
print("Class 2: 30 - 50")
print("Class 3: >50")
print()

cond_age_1 = cond_diabetes & (db["Age"] <= 30)
cond_age_2 = cond_diabetes & (db["Age"] >30) &(db["Age"] <= 50)
cond_age_3 = cond_diabetes & (db["Age"] >50)

print("Outcome == 1 ")
print("Age Class 1: ", db.loc[cond_age_1].shape[0])
print("Age Class 2: ", db.loc[cond_age_2].shape[0])
print("Age Class 3: ", db.loc[cond_age_3].shape[0])

prob_has_diabetes["Age"].append(db.loc[cond_age_1].shape[0]/num_total)
prob_has_diabetes["Age"].append(db.loc[cond_age_2].shape[0]/num_total)
prob_has_diabetes["Age"].append(db.loc[cond_age_3].shape[0]/num_total)

print()
cond_age_1 = (db["Outcome"]== 0 ) & (db["Age"] <= 30)
cond_age_2 = (db["Outcome"]== 0 ) & (db["Age"] >30) &(db["Age"] <= 50)
cond_age_3 = (db["Outcome"]== 0 ) & (db["Age"] >50)


print("Outcome == 0 ")
print("Age Class 1: ", db.loc[cond_age_1].shape[0])
print("Age Class 2: ", db.loc[cond_age_2].shape[0])
print("Age Class 3: ", db.loc[cond_age_3].shape[0])


prob_has_not_diabetes["Age"].append(db.loc[cond_age_1].shape[0]/num_total)
prob_has_not_diabetes["Age"].append(db.loc[cond_age_2].shape[0]/num_total)
prob_has_not_diabetes["Age"].append(db.loc[cond_age_3].shape[0]/num_total)

print()

print("Glucose classes")
print("Class 1: < 100")
print("Class 2: 100 - 150")
print("Class 3: >150")
print()

cond_glucose_1 = (db["Outcome"]== 1 ) & (db["Glucose"] < 100)
cond_glucose_2 = (db["Outcome"]== 1 ) & (db["Glucose"] > 100) &(db["Glucose"] <= 150)
cond_glucose_3 = (db["Outcome"]== 1 ) & (db["Glucose"] > 150)

print("Outcome == 1 ")
print("Glucose Class 1: ", db.loc[cond_glucose_1].shape[0])
print("Glucose Class 2: ", db.loc[cond_glucose_2].shape[0])
print("Glucose Class 3: ", db.loc[cond_glucose_3].shape[0])

prob_has_diabetes["Glucose"].append(db.loc[cond_glucose_1].shape[0]/num_total)
prob_has_diabetes["Glucose"].append(db.loc[cond_glucose_2].shape[0]/num_total)
prob_has_diabetes["Glucose"].append(db.loc[cond_glucose_3].shape[0]/num_total)


print()
cond_glucose_1 = (db["Outcome"]== 0 ) & (db["Glucose"] < 100)
cond_glucose_2 = (db["Outcome"]== 0 ) & (db["Glucose"] > 100) &(db["Glucose"] <= 150)
cond_glucose_3 = (db["Outcome"]== 0 ) & (db["Glucose"] > 150)

print("Outcome == 0 ")
print("Glucose Class 1: ", db.loc[cond_glucose_1].shape[0])
print("Glucose Class 2: ", db.loc[cond_glucose_2].shape[0])
print("Glucose Class 3: ", db.loc[cond_glucose_3].shape[0])

prob_has_not_diabetes["Glucose"].append(db.loc[cond_glucose_1].shape[0]/num_total)
prob_has_not_diabetes["Glucose"].append(db.loc[cond_glucose_2].shape[0]/num_total)
prob_has_not_diabetes["Glucose"].append(db.loc[cond_glucose_3].shape[0]/num_total)

print()

print("Insulin classes")
print("Class 1: 0")
print("Class 2: 0 - 100")
print("Class 3: >100")
print()
conditionInsulinClass1 = (db["Outcome"]== 1 ) & (db["Insulin"] == 0)
conditionInsulinClass2 = (db["Outcome"]== 1 ) & (db["Insulin"] > 0) &(db["Insulin"] <= 100)
conditionInsulinCLass3 = (db["Outcome"]== 1 ) & (db["Insulin"] > 100)

print("Outcome == 1 ")
print("Insulin Class 1: ", db.loc[conditionInsulinClass1].shape[0])
print("Insulin Class 2: ", db.loc[conditionInsulinClass2].shape[0])
print("Insulin Class 3: ", db.loc[conditionInsulinCLass3].shape[0])

prob_has_diabetes["Insulin"].append(db.loc[conditionInsulinClass1].shape[0]/num_total)
prob_has_diabetes["Insulin"].append(db.loc[conditionInsulinClass2].shape[0]/num_total)
prob_has_diabetes["Insulin"].append(db.loc[conditionInsulinCLass3].shape[0]/num_total)

print()

conditionInsulinClass1 = (db["Outcome"]== 0 ) & (db["Insulin"] == 0)
conditionInsulinClass2 = (db["Outcome"]== 0 ) & (db["Insulin"] > 0) &(db["Insulin"] <= 100)
conditionInsulinCLass3 = (db["Outcome"]== 0 ) & (db["Insulin"] > 100)

print("Outcome == 0 ")
print("Insulin Class 1: ", db.loc[conditionInsulinClass1].shape[0])
print("Insulin Class 2: ", db.loc[conditionInsulinClass2].shape[0])
print("Insulin Class 3: ", db.loc[conditionInsulinCLass3].shape[0])


prob_has_not_diabetes["Insulin"].append(db.loc[conditionInsulinClass1].shape[0]/num_total)
prob_has_not_diabetes["Insulin"].append(db.loc[conditionInsulinClass2].shape[0]/num_total)
prob_has_not_diabetes["Insulin"].append(db.loc[conditionInsulinCLass3].shape[0]/num_total)
print()

print("DiabetesPedigreeFunction classes")
print("Class 1: <= 0.3")
print("Class 2: > 0.3")
print()

cond_diab_pedigree_1 = (db["Outcome"]== 1 ) & (db["DiabetesPedigreeFunction"] <= 0.3)
cond_diab_pedigree_2 = (db["Outcome"]== 1 ) & (db["DiabetesPedigreeFunction"] > 0.3)

print("Outcome == 1 ")
print("DiabetesPedigreeFunction Class 1: ", db.loc[cond_diab_pedigree_1].shape[0])
print("DiabetesPedigreeFunction Class 2: ", db.loc[cond_diab_pedigree_2].shape[0])

prob_has_diabetes["DiabetesPedigreeFunction"].append(db.loc[cond_diab_pedigree_1].shape[0]/num_total)
prob_has_diabetes["DiabetesPedigreeFunction"].append(db.loc[cond_diab_pedigree_2].shape[0]/num_total)

print()

cond_diab_pedigree = (db["Outcome"]== 0 ) & (db["DiabetesPedigreeFunction"] <= 0.3)
cond_diab_pedigree_2 = (db["Outcome"]== 0 ) & (db["DiabetesPedigreeFunction"] > 0.3) 

print("Outcome == 0 ")
print("DiabetesPedigreeFunction Class 1: ", db.loc[cond_diab_pedigree].shape[0])
print("DiabetesPedigreeFunction Class 2: ", db.loc[cond_diab_pedigree_2].shape[0])


prob_has_not_diabetes["DiabetesPedigreeFunction"].append(db.loc[cond_diab_pedigree].shape[0]/num_total)
prob_has_not_diabetes["DiabetesPedigreeFunction"].append(db.loc[cond_diab_pedigree_2].shape[0]/num_total)

print()

print("P(key)  outcome ==1")
print()

for key in prob_has_diabetes:
    print(key, ":")
    print()
    for i in range(len(prob_has_diabetes[key])):
        print("Class ", i+1, ": ", prob_has_diabetes[key][i])
    print()
        
print("P(key)  outcome ==0")

for key in prob_has_not_diabetes:
    print(key, ":")
    for i in range(len(prob_has_not_diabetes[key])):
        print("Class ", i+1, ": ", prob_has_not_diabetes[key][i])
    print()

