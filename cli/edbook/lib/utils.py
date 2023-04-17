from subprocess import call
from enum import Enum
from pathlib import Path
import typer


class SphinxCmd(str, Enum):
    build = "sphinx-build"
    autobuild = "sphinx-autobuild"


# TODO: move all getters to generic settings file
def get_template_name():
    return "tmp001g"


def get_sphinx_args():
    return ["-b", "dirhtml"]


def get_abs_path(dir: str):
    return Path.joinpath(Path(__file__).parent.parent.parent.parent / dir)


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


def build_all():
    print("[bold blue]No project defined, building all projects ...[/bold blue] :boom:")
    template = get_template_name()
    for pr in get_projects_path().iterdir():
        if pr.name == get_template_name():
            print(
                f"[yellow]Skip building {template} template course ...[/yellow] :fast_forward:"
            )
            continue
        sphinx_build(pr.name)
    raise typer.Exit()


def check_authors(ctx: typer.Context, param: typer.CallbackParam, value: str):
    print(ctx.args)
    print(ctx.params)


def project_exists(project: Path):
    project = Path(get_projects_path() / project)
    if project.exists():
        return project
    raise typer.BadParameter(f"{project.name} does not exist.")
