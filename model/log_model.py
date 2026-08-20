import mlflow


def main():
    with mlflow.start_run():
        model_info = mlflow.pyfunc.log_model(
            name="sepsis_supervisor",
            python_model="src/sepsis/supervisor_model.py",
            code_paths=["src"],
        )

        print(f"Model URI: {model_info.model_uri}")


if __name__ == "__main__":
    main()