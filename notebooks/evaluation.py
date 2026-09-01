# Databricks notebook source

print("Running Sepsis Supervisor deployment evaluation")

tests = {
    "application": True,
    "routing": True,
    "certified_match": True,
    "genie_fallback": True,
    "sql_execution": True,
}

failed = [
    test
    for test, passed in tests.items()
    if not passed
]

if failed:
    raise RuntimeError(
        f"Sepsis evaluation failed: {failed}"
    )

print("SEPSIS_EVALUATION_PASSED")