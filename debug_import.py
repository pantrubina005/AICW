import sys
import traceback

sys.path.insert(0, r"c:/Users/nitro/Desktop/Insurance Premium Prediction/model")

try:
    import predict
except Exception:
    traceback.print_exc()
