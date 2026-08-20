import mlflow

import os


def main():
    print("Starting MLflow model logging")

    input_example = [
        {
            "question": "Show a certified sepsis answer"
        }
    ]

    model_info = mlflow.pyfunc.log_model(
        name="sepsis_supervisor",
        python_model="src/sepsis/supervisor_model.py",
        code_paths=["src"],
        input_example=input_example,
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

    

    github_output = os.getenv("GITHUB_OUTPUT")

    if github_output:
        with open(github_output, "a", encoding="utf-8") as output_file:
            output_file.write(f"model_uri={model_info.model_uri}\n")

    print(f"Model URI exported: {model_info.model_uri}")


if __name__ == "__main__":
    main()