import importlib
import json
import shutil
from pathlib import Path, PurePath
from subprocess import call
from typing import List, Literal, Optional, Union
from enum import Enum
import typer
from rich import print
from rich.prompt import Prompt
from rich.console import Console

import yaml


class SphinxCmd(str, Enum):
    build = "sphinx-build"
    autobuild = "sphinx-autobuild"


err = Console(stderr=True)
app = typer.Typer(rich_markup_mode="rich", name="edbook")


# TODO: move all getters to generic settings file
def get_template_name():
    return "tmp001g"


def get_sphinx_args():
    return ["-b", "dirhtml"]


def get_abs_path(dir: str):
    return Path.joinpath(Path(__file__).parent.resolve().parent / dir)


def get_output_path(dir: str = "_build"):
    return get_abs_path(dir)


def get_projects_path(dir: str = "projects"):
    return get_abs_path(dir)


def get_value(item):
    if isinstance(item, bytes):
        return item.decode()
    return item


def sphinx_build(project: str, sphinx_cmd: SphinxCmd = SphinxCmd.build):
    project_path = Path(get_projects_path() / project)
    output = Path(get_output_path() / project_path.name)
    cmd = [
        sphinx_cmd,
        str(project_path),
        str(output),
        *get_sphinx_args(),
    ]
    print(
        f"[bold purple]Preparing to build {project_path.name}[/bold purple] :sunglasses:"
    )
    print(f"[dim light_sea_green]{' '.join(cmd)}[/dim light_sea_green]")
    call(cmd)


def _build_all(ctx: typer.Context, param: typer.CallbackParam, value: str):
    if value:
        print(
            "[bold blue]No project defined, building all projects ...[/bold blue] :boom:"
        )
        template = get_template_name()
        for pr in get_projects_path().iterdir():
            if pr.name == get_template_name():
                print(
                    f"[yellow]Skip building {template} template course ...[/yellow] :fast_forward:"
                )
                continue
            sphinx_build(pr.name)
        raise typer.Exit()


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
    project: str = typer.Argument(None, help="build specific project"),
    auto: bool = typer.Option(
        False,
        help="run server on http://localhost:8000 and autobuild and refresh on file save",
    ),
    all: bool = typer.Option(
        False, help="build all projects", callback=_build_all, is_eager=True
    ),
):
    """
    Build a specific project or all projects (default).
    """
    if project and auto:
        sphinx_build(project, SphinxCmd.autobuild)
    sphinx_build(project)


@app.command(
    "create",
)
def cmd_create(
    name: str = typer.Option(..., prompt="Course id"),
    description: str = typer.Option(..., prompt="Course name"),
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


if __name__ == "__main__":
    app()
