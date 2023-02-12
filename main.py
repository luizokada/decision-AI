from dataset import Dataset
from variables.bmi import BMI
from variables.glucose import Glucose
from variables.insulin import Insulin
from variables.diabetes_pedigree import DiabetesPedigreeFunction
from views import InputView, OutputView
from assets.references import references
from assets.references import decision_references


dset = Dataset()
bmi = BMI(dset, references["BMI"])
glucose = Glucose(dset, references["Glucose"])
insulin = Insulin(dset, references["Insulin"])
diab_pedigree = DiabetesPedigreeFunction(dset, references["DiabetesPedigreeFunction"])

prob_has_diabetes = {
    "BMI": bmi.calc_prob_diab(),
    "Glucose": glucose.calc_prob_diab(),
    "Insulin": insulin.calc_prob_diab(),
    "DiabetesPedigreeFunction": diab_pedigree.calc_prob_diab(),
}
prob_has_not_diabetes = {
    "BMI": bmi.calc_prob_not_diab(),
    "Glucose": glucose.calc_prob_not_diab(),
    "Insulin": insulin.calc_prob_not_diab(),
    "DiabetesPedigreeFunction": diab_pedigree.calc_prob_not_diab(),
}

# print("P(key)  outcome = 1")
# for key in prob_has_diabetes:
#     print(key, ":")
#     print()
#     for i in range(len(prob_has_diabetes[key])):
#         print("Class ", i+1, ": ", prob_has_diabetes[key][i])
#     print()
        
# print("P(key)  outcome = 0")
# for key in prob_has_not_diabetes:
#     print(key, ":")
#     for i in range(len(prob_has_not_diabetes[key])):
#         print("Class ", i+1, ": ", prob_has_not_diabetes[key][i])
#     print()

input = InputView()
input.calc_classes(references)

output = OutputView(input.classes,decision_references)
output.calc_utility(prob_has_diabetes)