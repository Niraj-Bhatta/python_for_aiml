class MLModel:
    def __init__(self, threshold):
        self.threshold = threshold

    def set_threshold(self, value):
        if 0 <= value <= 1:
            self.threshold = value
        else:
            print("Invalid threshold!")


model = MLModel(0.8)

model.set_threshold(0.9)
print(model.threshold)  # 0.9

model.set_threshold(5.0)  # Invalid threshold!