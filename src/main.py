import typer

from mlops_management.databricks_operations import database_operations

app = typer.Typer(name="mlops-management", help="CLI to Centralize MLOPS Management")

