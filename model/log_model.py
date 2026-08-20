import mlflow


def main():
    print("Starting MLflow model logging")

    model_info = mlflow.pyfunc.log_model(
        name="sepsis_supervisor",
        python_model="src/sepsis/supervisor_model.py",
        code_paths=["src"],
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


if __name__ == "__main__":
    main()