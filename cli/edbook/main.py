import importlib
import json
import shutil
from pathlib import Path
from subprocess import call
from typing import List, Optional
from enum import Enum
import typer
from rich import print
from rich.console import Console
from rich.table import Table
import yaml

from edbook.lib.utils import (
    SphinxCmd,
    get_value,
    project_exists,
    build_all,
    sphinx_build,
    get_projects_path,
    get_abs_path,
    get_template_name,
)

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
        str(Path(__file__).parent.resolve().parent / "src" / "data"),
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
        callback=project_exists,
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
        sphinx_build(project.name, SphinxCmd.autobuild)
    sphinx_build(project.name)


@app.command(
    "build-all",
)
def cmd_build():
    """
    Build a specific project or all projects (default).
    """
    build_all()


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
        get_template_name(),
        help="Template course name",
    ),
):
    """
    [bold green]Create new Edbook project from template[/bold green]
    """
    projects = get_abs_path("projects")
    src = projects / template
    dest = projects / name
    shutil.copytree(src, dest, symlinks=False, dirs_exist_ok=True)
    data = {"name": name, "description": description, "author": author, "email": email}
    with open(dest / Path("config.yml"), "w") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
    print()
    print(f"[bold blue]Your course is now available at {dest}[/bold blue]")


@app.command(
    "list",
)
def cmd_list():
    """
    [bold green]List all projects[/bold green]
    """
    projects = sorted(
        [d.name for d in get_projects_path().iterdir() if d.is_dir()], key=str.lower
    )
    table = Table(title="Edbook projects")
    table.add_column("Course", justify="left", style="cyan", no_wrap=True)
    table.add_column("Author", style="magenta")
    table.add_column("Created", justify="right", style="green")

    for p in projects:
        table.add_row(p, "TODO: get author", "TODO: get created")

    print(table)


if __name__ == "__main__":
    app()
