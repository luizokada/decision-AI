class InputView:
    def __init__(self):
        self.ibm = input("Enter a IBM: ")
        self.insulin = input("Enter a Insulin: ")
        self.glucose = input("Enter a Glucose: ")
        self.diab_pedigree = input("Enter a Diabetes Pedigree Function: ")

    def calc_prob_has_diab(self, dataset_prob):
        pass

    def calc_prob_has_not_diab(self, dataset_prob):
        pass