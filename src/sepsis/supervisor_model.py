import mlflow
from mlflow.models import set_model

from src.sepsis.supervisor import classify_question


class SepsisSupervisorModel(mlflow.pyfunc.PythonModel):
    """MLflow wrapper around the Sepsis Supervisor routing logic."""

    def predict(
        self,
        context,
        model_input: list[dict[str, str]],
        params=None,
    ):
        results = []

        for request in model_input:
            question = request.get("question")

            if not question:
                raise ValueError(
                    "Each request must contain a non-empty 'question'."
                )

            results.append(classify_question(question))

        return results


set_model(SepsisSupervisorModel())