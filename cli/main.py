import importlib
import json
from pathlib import Path, PurePath
from subprocess import call

import typer
import yaml

app = typer.Typer()


def get_value(item):
    if isinstance(item, bytes):
        return item.decode()
    return item


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
    path: str = typer.Option(
        Path(__file__).parent.resolve().parent / "projects",
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
    # print(Path(ctx.params["path"].iterdir()))
    for project in Path(ctx.params["path"]).iterdir():
        project_path = PurePath(project)
        typer.secho(
            f"""################ Preparing build of project {project_path.name} ##############""",
            fg=typer.colors.MAGENTA,
        )
        call(["sphinx-build", project_path, Path(build_path) / project_path.name, *ctx.args])


if __name__ == "__main__":
    app()
