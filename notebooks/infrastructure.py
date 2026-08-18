# Databricks notebook source

print("Starting Sepsis infrastructure provisioning")

catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")

spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog}.{schema}")

spark.sql(
    f"""
    CREATE TABLE IF NOT EXISTS {catalog}.{schema}.sepsis_certified_qa (
        id STRING,
        question STRING,
        approved_answer STRING
    )
    USING DELTA
    TBLPROPERTIES ('delta.enableChangeDataFeed' = 'true')
    """
)

print("Dummy Sepsis infrastructure successfully created")