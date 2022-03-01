import fastbook
from path import Path
fastbook.setup_book()




class GenderClassifier:

    def __init__(self, model_filename):
        model_path = Path(model_filename)
        self.model = fastbook.load_learner(model_path)


    def predict(self, specto_filename):
        return self.model.predict(specto_filename)
