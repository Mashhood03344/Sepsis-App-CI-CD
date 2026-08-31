import argparse
import os

import mlflow


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-uri", required=True)
    parser.add_argument("--model-name", required=True)
    args = parser.parse_args()

    if not args.model_uri:
        raise ValueError(
            "Model URI is empty. The MLflow logging step "
            "did not export model_uri correctly."
        )

    print(f"Registering model URI: {args.model_uri}")
    print(f"Target UC model: {args.model_name}")

    mlflow.set_tracking_uri("databricks")
    mlflow.set_registry_uri("databricks-uc")

    model_version = mlflow.register_model(
        model_uri=args.model_uri,
        name=args.model_name,
    )

    print(f"Registered model: {model_version.name}")
    print(f"Registered version: {model_version.version}")

    github_output = os.getenv("GITHUB_OUTPUT")

    if github_output:
        with open(github_output, "a", encoding="utf-8") as output:
            output.write(f"model_version={model_version.version}\n")


if __name__ == "__main__":
    main()