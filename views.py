class InputView:
    def __init__(self):
        self.ibm = float(input("Enter a IBM: "))
        self.glucose = float(input("Enter a Glucose: "))
        self.insulin = float(input("Enter a Insulin: "))
        self.pedigree = float(input("Enter a Diabetes Pedigree Function: "))
        self.classes = []

    def calc_classes(self, references):
        classes = self.classes
        classes = []

        for k, v in references.items():

            attrib = getattr(self, k)

            for key, value in v.items():
                condition_to_equal = value[0] == 0

                if condition_to_equal:
                    condition = (attrib >= value[0]) & (attrib <= value[1])
                else:
                    condition = (attrib > value[0]) & (attrib <= value[1])

                if condition:
                    classes.append(k + key)
                    break
    
        print(classes)

class OutputView:
    def __init__(self, classes):
        self.classes = classes
    
    def calc_utility(self):
        pass