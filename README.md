# Sepsis Supervisor CI/CD Demo

This demo uses GitHub Actions and Databricks Asset Bundles with two deployment branches:

- `dev` deploys the `dev` Databricks target.
- `qa` deploys the `qa` Databricks target.

Pull requests run Python tests and bundle validation. A push to either environment branch deploys the bundle, provisions the environment infrastructure, and runs the evaluation job. Configure GitHub Environments named `dev` and `qa` with these values:

- Variable: `DATABRICKS_HOST`
- Variable: `DATABRICKS_WAREHOUSE_ID`
- Secret: `DATABRICKS_AZURE_CLIENT_ID`
- Secret: `DATABRICKS_AZURE_CLIENT_SECRET`
- Secret: `DATABRICKS_AZURE_TENANT_ID`

The service principal needs permission to deploy bundles, create or update the Databricks App, run jobs, and manage the vector search and Genie resources in the target workspace.

The workflow is intentionally environment-branch based for the demo. In the client repository, keep the same promotion gates but use the client's repository branch policy, workspace identities, catalogs, schemas, and approval rules.