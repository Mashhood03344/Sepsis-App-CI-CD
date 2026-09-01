def classify_question(question: str):
    """
    Dummy replacement for Gated_QA_Sepsis_Supervisor_Agent.

    Production implementation should:
      1. query certified Q&A vector index
      2. apply match threshold
      3. execute certified SQL when matched
      4. otherwise delegate to Genie
      5. gate unsafe responses
    """

    if "certified" in question.lower():
        return {
            "route": "CERTIFIED_QA",
            "confidence": 0.95,
            "answer": "Dummy certified Sepsis answer."
        }

    return {
        "route": "GENIE",
        "confidence": 0.50,
        "answer": "Dummy Genie fallback answer."
    }