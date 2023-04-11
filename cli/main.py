import importlib
import json
import shutil
from pathlib import Path, PurePath
from subprocess import call
from typing import List, Optional

import typer
from rich import print
from rich.prompt import Prompt
from rich.console import Console

import yaml

err = Console(stderr=True)
app = typer.Typer(rich_markup_mode="rich", name="edbook")


# TODO: move to generic settings file
def get_template_name():
    return "tmp001g"


def get_value(item):
    if isinstance(item, bytes):
        return item.decode()
    return item


def build_project(project: Path, build_path: Path, *args):
    cmd = ["sphinx-build", str(project), str(Path(build_path / project.name)), *args]
    print(f"[bold purple]Preparing to build {project.name}[/bold purple] :sunglasses:")
    print(f"[dim light_sea_green]{' '.join(cmd)}[/dim light_sea_green]")
    call(cmd)

def autobuild_project(project: Path, build_path: Path, *args):
    cmd = ["sphinx-autobuild", str(project), str(Path(build_path / project.name)), *args]
    print(f"[bold purple]Preparing to build {project.name}[/bold purple] :sunglasses:")
    print(f"[dim light_sea_green]{' '.join(cmd)}[/dim light_sea_green]")
    call(cmd)

def get_abs_path(dir: str):
    return Path.joinpath(Path(__file__).parent.resolve().parent / dir)


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
    word_mod = importlib.import_module(f"src.extensions.{extension}.{extension}.{package}")
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
    json_file.write_text(json.dumps(data, ensure_ascii=False, indent=4), encoding="utf-8")
    typer.secho(
        f"Success: {json_file}",
        fg=typer.colors.GREEN,
    )
    typer.secho(
        f"Exporting word list to {yaml_file}, hold on ...",
        fg=typer.colors.BLUE,
    )
    yaml_file.write_text(yaml.safe_dump(data, sort_keys=True, allow_unicode=True), encoding="utf-8")
    typer.secho(
        f"Success: {yaml_file}",
        fg=typer.colors.GREEN,
    )


@app.command(
    "build",
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True},
)
def cmd_build(
    ctx: typer.Context,
    project: Optional[str] = typer.Option(None, help="build specific project"),
    projects_dir: str = typer.Option(
        "projects",
        help="Projects directory relative from root",
    ),
    build_path: str = typer.Option(
        "_build",
        help="Build output path relative from root",
    ),
):
    """
    Build a specific project or all projects (default).
    """
    projects = get_abs_path(projects_dir)
    build = get_abs_path(build_path)
    ctx.args += ["-b", "dirhtml"]
    template = get_template_name()
    if project:
        build_project(Path.joinpath(projects / project), build, *ctx.args)
    else:
        print("[bold blue]No project defined, building all projects ...[/bold blue] :boom:")
        for pr in projects.iterdir():
            if pr.name == template:
                print(
                    f"[yellow]Skip building {template} template course ...[/yellow] :fast_forward:"
                )
                continue
            build_project(pr, build, *ctx.args)

@app.command(
    "autobuild",
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True},
)
def cmd_autobuild(
    ctx: typer.Context,
    project: Optional[str] = typer.Option(None, help="build specific project"),
    projects_dir: str = typer.Option(
        "projects",
        help="Projects directory relative from root",
    ),
    build_path: str = typer.Option(
        "_build",
        help="Build output path relative from root",
    ),
):
    """
    Build a specific project or all projects (default).
    """
    projects = get_abs_path(projects_dir)
    build = get_abs_path(build_path)
    ctx.args += ["-b", "dirhtml"]
    template = get_template_name()
    if project:
        autobuild_project(Path.joinpath(projects / project), build, *ctx.args)
    else:
        print("[bold blue]No project defined, building all projects ...[/bold blue] :boom:")
        for pr in projects.iterdir():
            if pr.name == template:
                print(
                    f"[yellow]Skip building {template} template course ...[/yellow] :fast_forward:"
                )
                continue
            autobuild_project(pr, build, *ctx.args)

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
