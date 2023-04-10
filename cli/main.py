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
app = typer.Typer()


def get_value(item):
    if isinstance(item, bytes):
        return item.decode()
    return item


def build_project(project: Path, build_path: Path, *args):
    cmd = ["sphinx-build", str(project), str(Path(build_path / project.name)), *args]
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
    if project:
        build_project(Path.joinpath(projects / project), build, *ctx.args)
    else:
        print("[bold blue]No project defined, building all projects ...[/bold blue] :boom:")
        for pr in projects.iterdir():
            build_project(pr, build, *ctx.args)


# @app.command(
#     "build",
#     # context_settings={"allow_extra_args": True, "ignore_unknown_options": True},
# )
# def cmd_build(
#     ctx: typer.Context,
#     all: bool = typer.Option(False, help="build all projects"),
#     project: str = typer.Option(..., help="build specific project"),
#     build_path: str = typer.Option(
#         Path(__file__).parent.resolve().parent / "_build",
#         help="Build output path",
#     ),
#     sphinx_args: str = typer.Option("-b dirhtml", help="Extra Sphinx arguments"),
# ):
#     """
#     Building projects
#     """
#     projects = get_projects_dir()
#     if all:
#         print("[bold blue]Building all projects[/bold blue] :boom:")
#         for pr in projects.iterdir():
#             build_project(pr, build_path, *sphinx_args.split(" "), *ctx.args)
#     elif project:
#         # return Path.joinpath(Path(__file__).parent.resolve().parent / "projects")

#         build_project(
#             Path.joinpath(projects / project), build_path, *sphinx_args.split(" "), *ctx.args
#         )


# @app.command(
#     "create",
#     context_settings={"allow_extra_args": True, "ignore_unknown_options": True},
# )
# def cmd_create(
#     ctx: typer.Context,
#     name: str = Prompt.ask("The name of the new Edbook course :sunglasses:"),
#     template: str = typer.Option(
#         "tmp001g",
#         help="Template course name",
#     ),
# ):
#     """
#     Create new Edbook project from template
#     """
#     # # print(Path(ctx.params["path"].iterdir()))
#     # for project in Path(ctx.params["path"]).iterdir():
#     #     project_path = PurePath(project)
#     #     typer.secho(
#     #         f"""################ Preparing build of project {project_path.name} ##############""",
#     #         fg=typer.colors.MAGENTA,
#     #     )
#     #     call(["sphinx-build", project_path, Path(build_path) / project_path.name, *ctx.args])
#     src = get_projects_dir() / template
#     dest = get_projects_dir() / name

#     print(f"test: {name}")
#     shutil.copytree(src, dest, symlinks=False, dirs_exist_ok=True)


if __name__ == "__main__":
    app()
