import importlib
import json
from pathlib import Path
from typing import List
import typer
from rich import print
from rich.console import Console
from rich.table import Table
import yaml

from edbook.lib.utils import get_value

from edbook.models import Edbook

err = Console(stderr=True)
app = typer.Typer(no_args_is_help=True, rich_markup_mode="rich", name="edbook")


@app.callback()
def callback():
    """
    Edbook CLI toolkit
    """


@app.command("export-word-dict")
def cmd_export_word_dict(
    extension: str = typer.Option(
        "hoverrole",
        help="Extension name",
    ),
    package: str = typer.Option(
        "minstae",
        help="File name to import",
    ),
    output: str = typer.Option(
        str(Path(Path.cwd() / "src" / "data")),
        help="Output directory for yaml and json files",
    ),
):
    """
    Import word dictionary file from path
    """
    word_mod = importlib.import_module(
        f"src.extensions.{extension}.{extension}.{package}"
    )
    word_data: dict = getattr(word_mod, package)
    data = {}
    v: dict
    for k, v in word_data.items():
        for r, s in v.items():
            values = [get_value(word) for word in s]
            data.update({get_value(k): {get_value(r): values}})

    data_dir = Path(output)
    data_dir.mkdir(parents=True, exist_ok=True)

    json_file = data_dir / f"{package}.json"
    yaml_file = data_dir / f"{package}.yaml"

    typer.secho(
        f"Exporting word list to {json_file}, hold on ...",
        fg=typer.colors.BLUE,
    )
    json_file.write_text(
        json.dumps(data, ensure_ascii=False, indent=4), encoding="utf-8"
    )
    typer.secho(
        f"Success: {json_file}",
        fg=typer.colors.GREEN,
    )
    typer.secho(
        f"Exporting word list to {yaml_file}, hold on ...",
        fg=typer.colors.BLUE,
    )
    yaml_file.write_text(
        yaml.safe_dump(data, sort_keys=True, allow_unicode=True), encoding="utf-8"
    )
    typer.secho(
        f"Success: {yaml_file}",
        fg=typer.colors.GREEN,
    )


@app.command(
    "build",
)
def cmd_build(
    project: Path = typer.Argument(
        ...,
        help="build specific project",
        callback=Edbook.project_exists,
    ),
    auto: bool = typer.Option(
        False,
        help="run server on http://localhost:8000 and autobuild and refresh on file save",
    ),
):
    """
    Build a specific project or all projects (default).
    """
    if auto:
        Edbook.autobuild(project.name)
    Edbook.build(project.name)


@app.command(
    "build-all",
)
def cmd_build_all():
    """
    Build a specific project or all projects (default).
    """
    Edbook.build_all()


@app.command(
    "create",
)
def cmd_create(
    name: str = typer.Option(..., prompt="Course id"),
    description: str = typer.Option(..., prompt="Course name"),
    num_authors: List[str] = typer.Option(None),
    author: str = typer.Option(..., prompt="Author name"),
    email: str = typer.Option(..., prompt="Author email"),
    template: str = typer.Option(
        Edbook.template_name,
        help="Template course name",
    ),
):
    """
    [bold green]Create new Edbook project from template[/bold green]
    """
    Edbook.create(name, description, author, email)


@app.command(
    "list",
)
def cmd_list():
    """
    [bold green]List all projects[/bold green]
    """

    table = Table(title="Edbook projects")
    table.add_column("Course", justify="left", style="cyan", no_wrap=True)
    table.add_column("Author", style="magenta")
    table.add_column("Created", justify="right", style="green")

    for p in Edbook.list_projects():
        table.add_row(p, "TODO: get author", "TODO: get created")

    print(table)


if __name__ == "__main__":
    app()
