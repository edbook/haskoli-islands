import yaml
import shutil
from subprocess import call
from pathlib import Path
import typer


class EdbookBase:
    base_dir = Path.cwd()
    projects_dir = base_dir / "projects"
    sphinx_args = ["-b", "dirhtml"]
    template_name = "tmp001g"
    build_dir = base_dir / "_build"


class EdbookProject(EdbookBase):
    def __init__(self, project: str):
        self.project = project

    def build(self, sphinx_cmd="sphinx-build"):
        project_dir = self.projects_dir.joinpath(self.project)
        build_dir = self.build_dir.joinpath(project_dir.name)
        cmd = [
            sphinx_cmd,
            str(project_dir),
            str(build_dir),
            *self.sphinx_args,
        ]
        print(
            f"[bold purple]Preparing to build {project_dir.name}[/bold purple] :sunglasses:"
        )
        print(f"[dim light_sea_green]{' '.join(cmd)}[/dim light_sea_green]")
        call(cmd)

    def autobuild(self):
        self.build("sphinx-autobuild")


class Edbook(EdbookBase):
    @staticmethod
    def check_authors(ctx: typer.Context, param: typer.CallbackParam, value: str):
        print(ctx.args)
        print(ctx.params)

    @classmethod
    def build_all(cls):
        print(
            "[bold blue]No project defined, building all projects ...[/bold blue] :boom:"
        )
        for pr in cls.projects_dir.iterdir():
            if pr.name == cls.template_name:
                print(
                    f"[yellow]Skip building {cls.template_name} template course ...[/yellow] :fast_forward:"
                )
                continue
            EdbookProject(pr.name).build()
        raise typer.Exit()

    @staticmethod
    def build(project: str):
        EdbookProject(project).build()

    @staticmethod
    def autobuild(project: str):
        EdbookProject(project).autobuild()

    @classmethod
    def project_exists(cls, project: Path):
        project_dir = Path(cls.projects_dir / project)
        if project_dir.exists():
            return project
        raise typer.BadParameter(f"{project.name} does not exist.")

    @classmethod
    def create(cls, name: str, description: str, author: str, email: str):
        src = cls.projects_dir / cls.template_name
        dest = cls.projects_dir / name
        shutil.copytree(src, dest, symlinks=False, dirs_exist_ok=True)
        data = {
            "name": name,
            "description": description,
            "author": author,
            "email": email,
        }
        with open(dest / Path("config.yml"), "w") as f:
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
        print()
        print(f"[bold blue]Your course is now available at {dest}[/bold blue]")

    @classmethod
    def list_projects(cls):
        return sorted(
            [d.name for d in cls.projects_dir.iterdir() if d.is_dir()], key=str.lower
        )
