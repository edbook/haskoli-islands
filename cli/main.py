from pathlib import Path, PurePath
from subprocess import call
import typer


app = typer.Typer()


@app.callback()
def callback():
    """
    Edbook CLI toolkit
    """


@app.command(
    "build",
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True},
)
def cmd_build(
    ctx: typer.Context,
    path: str = typer.Option(
        Path(__file__).parent.resolve().parent / "src" / "projects",
        help="Absolute path to edbook projects directory",
    ),
    build_path: str = typer.Option(
        Path(__file__).parent.resolve().parent / "_build",
        help="Build output path",
    ),
):
    """
    Build all projects
    """
    for path in Path(ctx.params["path"]).iterdir():
        project_dir = PurePath(path)
        typer.secho(
            f"""################ Preparing build of project {project_dir.name} ##############""",
            fg=typer.colors.MAGENTA,
        )
        call(["sphinx-build", path, build_path / project_dir.name, *ctx.args])


def run():
    app()
