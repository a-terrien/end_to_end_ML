import joblib
from pprint import pprint
# Chargement le modèle à partir du fichier regmodel.joblib
model = joblib.load('../models/regmodel.joblib')

# Get the model attributes
model_attributes = model.get_params()
model_input = model.get_feature

# Pretty print the model attributes
pprint(model_attributes, width=1)
