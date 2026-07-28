import pickle
from pathlib import Path
import pandas as pd
import sys


def ensure_numpy_compat():
    try:
        import numpy
    except Exception:
        return False

    try:
        import numpy.core as numpy_core
    except Exception:
        numpy_core = None

    if numpy_core is not None:
        sys.modules.setdefault("numpy._core", numpy_core)
        try:
            sys.modules.setdefault("numpy.core._multiarray_umath", numpy_core._multiarray_umath)
        except Exception:
            pass
        try:
            import numpy.core.multiarray as multiarray
            sys.modules.setdefault("numpy.core._multiarray_umath", multiarray)
        except Exception:
            pass
    return True


ensure_numpy_compat()

# import the ml model using a path relative to this file
MODEL_DIR = Path(__file__).resolve().parent
MODEL_PATH = MODEL_DIR / 'model_data.pkl'
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

# ML FLOW
MODEL_VERSION = '1.0.0'


def predict_output(user_input:dict):
    input_df = pd.DataFrame([user_input])
    #Predict
    output = model.predict(input_df)[0]
    return output