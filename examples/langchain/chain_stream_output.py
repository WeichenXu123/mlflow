import os
import mlflow
from langchain.llms import OpenAI
from langchain_core.output_parsers import StrOutputParser

# Ensure the OpenAI API key is set in the environment
assert "OPENAI_API_KEY" in os.environ, "Please set the OPENAI_API_KEY environment variable."

# Initialize the OpenAI model and the prompt template
llm = OpenAI(temperature=0.9, max_tokens=3900)

# Create the LLMChain with the specified model and prompt
chain = llm | StrOutputParser()

with mlflow.start_run() as run:
    model_info = mlflow.langchain.log_model(chain, "model")

loaded_model = mlflow.pyfunc.load_model(model_info.model_uri)

for chunk in loaded_model.predict_stream('Count to 10. E.g., 1, 2, 3, ...'):
    print(chunk, end="|")
