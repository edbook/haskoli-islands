import logging
import os
from pathlib import Path
import shutil
from subprocess import call
from typing import List
import typer
from typer.params import Argument
from .server import app as server_app
from .utils import msg_debug, msg_info, msg_success, ROOT_DIR, msg_warning

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = typer.Typer()
app.add_typer(server_app, name="server")


@app.command("run")
def cmd_build():
    """
    Run a simple webserver that loads the build dir
    """
    call(
        [
            "python",
            "-m",
            "http.server",
            "8000",
            "--directory",
            ROOT_DIR.joinpath("_build", "html"),
        ]
    )


@app.command("build")
def cmd_build(
    source_dir: str = typer.Argument(
        ROOT_DIR,
        help="Source files relative dir",
    ),
    build_dir: str = typer.Argument(
        ROOT_DIR.joinpath("_build"),
        help="Build output relative dir",
    ),
    builder: str = typer.Option("html", "--builder", "-b", help="Builder type"),
    clean: bool = typer.Option(
        True, help="Delete the build directory before building."
    ),
):
    """
    Build edbook from source directory and optionally delete the output dir first.
    """
    if clean:
        msg_warning(f"Deleting {build_dir} before building ...")
        call(["sphinx-build", "-M", "clean", source_dir, build_dir])
    msg_info(f"Building edbook from {source_dir}")

    call(["sphinx-build", source_dir, build_dir])

    msg_success(f"Done!")


@app.command(
    "autobuild",
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True},
)
def cmd_autobuild(
    ctx: typer.Context,
    source_dir: str = typer.Argument(
        ROOT_DIR.joinpath("docs"),
        help="Source files relative dir",
    ),
    build_dir: str = typer.Argument(
        ROOT_DIR.joinpath("_build"),
        help="Build output relative dir",
    ),
):
    """
    TODO: Needs work. A naive wrapper for sphinx-autobuild.
    """
    params = [param for param in ctx.params.values() if str(param).startswith("-")]
    default_args = [param.default for param in ctx.command.params]
    args: list
    if params:
        args = ctx.args or [param.default for param in ctx.command.params] + params
    else:
        args = [*default_args, *params]
    call(["sphinx-autobuild", *args])


if __name__ == "__main__":
    app()