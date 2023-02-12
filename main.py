
import pandas as pd


db = pd.read_csv('./DB/diabetes.csv')
probHasDiabetesDict = {
    "BMI":[],
    "Glucose":[],
    "Insulin":[],
    "DiabetesPedigreeFunction":[],
    
}

probHasNotDiabetesDict = {
    "BMI":[],
    "Glucose":[],
    "Insulin":[],
    "DiabetesPedigreeFunction":[],
    
}
num_total = db.shape[0]
conditonHasDiabetes = db["Outcome"] == 1
num_total_diabetes = db.loc[conditonHasDiabetes].shape[0]
num_not_diabetes = num_total - num_total_diabetes

print("BMIs classes")
print("Class 1: 0 - 30")
print("Class 2: 30 - 50")
print("Class 3: >50")
print()
conditionBMIClass1 = (db["Outcome"]== 1 ) & (db["BMI"] <= 18.5)
conditionBMIClass2 = (db["Outcome"]== 1 ) & (db["BMI"] >18.5) &(db["BMI"] <= 25)
conditionBMIClass3 = (db["Outcome"]== 1 ) & (db["BMI"] >25)

print("Outcome == 1 ")
print("BMI Class 1: ", db.loc[conditionBMIClass1].shape[0])
print("BMI Class 2: ", db.loc[conditionBMIClass2].shape[0])
print("BMI Class 3: ", db.loc[conditionBMIClass3].shape[0])

probHasDiabetesDict["BMI"].append(db.loc[conditionBMIClass1].shape[0]/num_total)
probHasDiabetesDict["BMI"].append(db.loc[conditionBMIClass2].shape[0]/num_total)
probHasDiabetesDict["BMI"].append(db.loc[conditionBMIClass3].shape[0]/num_total)

print()
conditionBMIClass1 = (db["Outcome"]== 0 ) & (db["BMI"] <= 18.5)
conditionBMIClass2 = (db["Outcome"]== 0 ) & (db["BMI"] >18.5) &(db["BMI"] <= 25)
conditionBMIClass3 = (db["Outcome"]== 0 ) & (db["BMI"] > 25)




print("Outcome == 0 ")
print("BMI Class 1: ", db.loc[conditionBMIClass1].shape[0])
print("BMI Class 2: ", db.loc[conditionBMIClass2].shape[0])
print("BMI Class 3: ", db.loc[conditionBMIClass3].shape[0])


probHasNotDiabetesDict["BMI"].append(db.loc[conditionBMIClass1].shape[0]/num_total)
probHasNotDiabetesDict["BMI"].append(db.loc[conditionBMIClass2].shape[0]/num_total)
probHasNotDiabetesDict["BMI"].append(db.loc[conditionBMIClass3].shape[0]/num_total)

print()

print("Glucose classes")
print("Class 1: < 100")
print("Class 2: 100 - 150")
print("Class 3: >150")
print()

conditionGlucoseClass1 = (db["Outcome"]== 1 ) & (db["Glucose"] <= 100)
conditionGlucoseClass2 = (db["Outcome"]== 1 ) & (db["Glucose"] > 100) &(db["Glucose"] <= 125)
conditionGlucoseClass3 = (db["Outcome"]== 1 ) & (db["Glucose"] > 125)

print("Outcome == 1 ")
print("Glucose Class 1: ", db.loc[conditionGlucoseClass1].shape[0])
print("Glucose Class 2: ", db.loc[conditionGlucoseClass2].shape[0])
print("Glucose Class 3: ", db.loc[conditionGlucoseClass3].shape[0])

probHasDiabetesDict["Glucose"].append(db.loc[conditionGlucoseClass1].shape[0]/num_total)
probHasDiabetesDict["Glucose"].append(db.loc[conditionGlucoseClass2].shape[0]/num_total)
probHasDiabetesDict["Glucose"].append(db.loc[conditionGlucoseClass3].shape[0]/num_total)


print()
conditionGlucoseClass1 = (db["Outcome"]== 0 ) & (db["Glucose"] <= 100)
conditionGlucoseClass2 = (db["Outcome"]== 0 ) & (db["Glucose"] > 100) &(db["Glucose"] <= 125)
conditionGlucoseClass3 = (db["Outcome"]== 0 ) & (db["Glucose"] > 125)

print("Outcome == 0 ")
print("Glucose Class 1: ", db.loc[conditionGlucoseClass1].shape[0])
print("Glucose Class 2: ", db.loc[conditionGlucoseClass2].shape[0])
print("Glucose Class 3: ", db.loc[conditionGlucoseClass3].shape[0])

probHasNotDiabetesDict["Glucose"].append(db.loc[conditionGlucoseClass1].shape[0]/num_total)
probHasNotDiabetesDict["Glucose"].append(db.loc[conditionGlucoseClass2].shape[0]/num_total)
probHasNotDiabetesDict["Glucose"].append(db.loc[conditionGlucoseClass3].shape[0]/num_total)

print()

print("Insulin classes")
print("Class 1: 0")
print("Class 2: 0 - 100")
print("Class 3: >100")
print()
conditionInsulinClass1 = (db["Outcome"]== 1 ) & (db["Insulin"] <= 140)
conditionInsulinClass2 = (db["Outcome"]== 1 ) & (db["Insulin"] > 140) &(db["Insulin"] <= 199)
conditionInsulinCLass3 = (db["Outcome"]== 1 ) & (db["Insulin"] > 199)

print("Outcome == 1 ")
print("Insulin Class 1: ", db.loc[conditionInsulinClass1].shape[0])
print("Insulin Class 2: ", db.loc[conditionInsulinClass2].shape[0])
print("Insulin Class 3: ", db.loc[conditionInsulinCLass3].shape[0])

probHasDiabetesDict["Insulin"].append(db.loc[conditionInsulinClass1].shape[0]/num_total)
probHasDiabetesDict["Insulin"].append(db.loc[conditionInsulinClass2].shape[0]/num_total)
probHasDiabetesDict["Insulin"].append(db.loc[conditionInsulinCLass3].shape[0]/num_total)

print()

conditionInsulinClass1 = (db["Outcome"]== 0 ) & (db["Insulin"] <= 140)
conditionInsulinClass2 = (db["Outcome"]== 0 ) & (db["Insulin"] > 140) &(db["Insulin"] <= 199)
conditionInsulinCLass3 = (db["Outcome"]== 0 ) & (db["Insulin"] > 199)

print("Outcome == 0 ")
print("Insulin Class 1: ", db.loc[conditionInsulinClass1].shape[0])
print("Insulin Class 2: ", db.loc[conditionInsulinClass2].shape[0])
print("Insulin Class 3: ", db.loc[conditionInsulinCLass3].shape[0])


probHasNotDiabetesDict["Insulin"].append(db.loc[conditionInsulinClass1].shape[0]/num_total)
probHasNotDiabetesDict["Insulin"].append(db.loc[conditionInsulinClass2].shape[0]/num_total)
probHasNotDiabetesDict["Insulin"].append(db.loc[conditionInsulinCLass3].shape[0]/num_total)
print()

print("DiabetesPedigreeFunction classes")
print("Class 1: <= 0.3")
print("Class 2: > 0.3")
print()

conditionDiaPedigreeClass1 = (db["Outcome"]== 1 ) & (db["DiabetesPedigreeFunction"] <= 0.3)
conditionDiaPedigreeClass2 = (db["Outcome"]== 1 ) & (db["DiabetesPedigreeFunction"] > 0.3) 

print("Outcome == 1 ")
print("DiabetesPedigreeFunction Class 1: ", db.loc[conditionDiaPedigreeClass1].shape[0])
print("DiabetesPedigreeFunction Class 2: ", db.loc[conditionDiaPedigreeClass2].shape[0])

probHasDiabetesDict["DiabetesPedigreeFunction"].append(db.loc[conditionDiaPedigreeClass1].shape[0]/num_total)
probHasDiabetesDict["DiabetesPedigreeFunction"].append(db.loc[conditionDiaPedigreeClass2].shape[0]/num_total)

print()

conditionDiaPedigreeClass1 = (db["Outcome"]== 0 ) & (db["DiabetesPedigreeFunction"] <= 0.3)
conditionDiaPedigreeClass2 = (db["Outcome"]== 0 ) & (db["DiabetesPedigreeFunction"] > 0.3) 

print("Outcome == 0 ")
print("DiabetesPedigreeFunction Class 1: ", db.loc[conditionDiaPedigreeClass1].shape[0])
print("DiabetesPedigreeFunction Class 2: ", db.loc[conditionDiaPedigreeClass2].shape[0])


probHasNotDiabetesDict["DiabetesPedigreeFunction"].append(db.loc[conditionDiaPedigreeClass1].shape[0]/num_total)
probHasNotDiabetesDict["DiabetesPedigreeFunction"].append(db.loc[conditionDiaPedigreeClass2].shape[0]/num_total)

print()

print("P(key)  outcome ==1")
print()

for key in probHasDiabetesDict:
    print(key, ":")
    print()
    for i in range(len(probHasDiabetesDict[key])):
        print("Class ", i+1, ": ", probHasDiabetesDict[key][i])
    print()
        
print("P(key)  outcome ==0")

for key in probHasNotDiabetesDict:
    print(key, ":")
    for i in range(len(probHasNotDiabetesDict[key])):
        print("Class ", i+1, ": ", probHasNotDiabetesDict[key][i])
    print()

