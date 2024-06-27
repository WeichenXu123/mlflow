import os

from mlflow.pyfunc import load_model, scoring_server

raise RuntimeError("Test failure 123423")
app = scoring_server.init(load_model(os.environ[scoring_server._SERVER_MODEL_PATH]))
