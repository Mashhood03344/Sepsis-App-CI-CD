import mlflow
from mlflow.models import infer_signature


def main():
    print("Starting MLflow model logging")

    input_example = [
        {
            "question": "Show a certified sepsis answer"
        }
    ]

    expected_output = [
        {
            "route": "CERTIFIED_QA",
            "confidence": 0.95,
            "answer": "Dummy certified Sepsis answer."
        }
    ]

    signature = infer_signature(
        input_example,
        expected_output,
    )

    model_info = mlflow.pyfunc.log_model(
        name="sepsis_supervisor",
        python_model="src/sepsis/supervisor_model.py",
        code_paths=["src"],
        input_example=input_example,
        signature=signature,
    )

    print(f"Model URI: {model_info.model_uri}")

    print("Loading logged MLflow model")

    loaded_model = mlflow.pyfunc.load_model(model_info.model_uri)

    certified_result = loaded_model.predict(
        [{"question": "Show a certified sepsis answer"}]
    )

    genie_result = loaded_model.predict(
        [{"question": "Show the latest sepsis trend"}]
    )

    print(f"Certified result: {certified_result}")
    print(f"Genie result: {genie_result}")

    assert certified_result[0]["route"] == "CERTIFIED_QA"
    assert genie_result[0]["route"] == "GENIE"

    print("MLflow model inference validation successful")


if __name__ == "__main__":
    main()