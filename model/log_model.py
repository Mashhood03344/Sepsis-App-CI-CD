# Validate that the packaged model can load without repository PYTHONPATH.

import os

import mlflow


def main():
    print("Starting MLflow model logging")

    mlflow.set_tracking_uri("databricks")
    mlflow.set_experiment("/Shared/sepsis-supervisor-mlflow-poc")

    conda_env = {
        "name": "mlflow-env",
        "channels": ["conda-forge"],
        "dependencies": [
            "python=3.12",
            "pip",
            {
                "pip": [
                    "mlflow==3.12.0",
                ]
            },
        ],
    }

    print(f"MLflow serving environment: {conda_env}")

    input_example = [
        {
            "question": "Show a certified sepsis answer"
        }
    ]

    with mlflow.start_run(
        run_name="sepsis-supervisor-model-build"
    ) as run:
        print(f"MLflow Run ID: {run.info.run_id}")

        model_info = mlflow.pyfunc.log_model(
            name="sepsis_supervisor",
            python_model="src/sepsis/supervisor_model.py",
            code_paths=["src/sepsis"],
            input_example=input_example,
            conda_env=conda_env,
        )

        print(f"Model URI: {model_info.model_uri}")

        loaded_model = mlflow.pyfunc.load_model(
            model_info.model_uri
        )

        certified_result = loaded_model.predict(
            [
                {
                    "question":
                    "Show a certified sepsis answer"
                }
            ]
        )

        genie_result = loaded_model.predict(
            [
                {
                    "question":
                    "Show the latest sepsis trend"
                }
            ]
        )

        print(f"Certified result: {certified_result}")
        print(f"Genie result: {genie_result}")

        assert certified_result[0]["route"] == "CERTIFIED_QA"
        assert genie_result[0]["route"] == "GENIE"

        print(
            "MLflow model inference validation successful"
        )

    # Export AFTER successful logging + validation
    github_output = os.getenv("GITHUB_OUTPUT")

    if github_output:
        with open(
            github_output,
            "a",
            encoding="utf-8",
        ) as output_file:
            output_file.write(
                f"model_uri={model_info.model_uri}\n"
            )

    print(
        f"Model URI exported: {model_info.model_uri}"
    )


if __name__ == "__main__":
    main()