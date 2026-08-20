import argparse

import mlflow


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-uri", required=True)
    parser.add_argument("--model-name", required=True)
    args = parser.parse_args()

    print(f"Registering model URI: {args.model_uri}")
    print(f"Target UC model: {args.model_name}")

    mlflow.set_registry_uri("databricks-uc")

    model_version = mlflow.register_model(
        model_uri=args.model_uri,
        name=args.model_name,
    )

    print(f"Registered model: {model_version.name}")
    print(f"Registered version: {model_version.version}")


if __name__ == "__main__":
    main()