from enum import Enum
from pathlib import Path
import os
import stat
import paramiko
import typer
from paramiko.sftp_client import SFTPClient as ParamikoSFTPClient
from seedir import FakeDir

ROOT_DIR = Path(__file__).resolve().parent.parent  # CLI root


class SFTPHosts(str, Enum):
    hekla = "hekla.rhi.hi.is"
    katla = "katla.rhi.hi.is"
    krafla = "krafla.rhi.hi.is"


def msg_debug(msg: str):
    typer.secho(
        msg,
        fg=typer.colors.BRIGHT_CYAN,
        bold=True,
        bg=typer.colors.RESET,
    )


def msg_warning(msg: str):
    typer.secho(
        msg,
        fg=typer.colors.YELLOW,
        bold=True,
        bg=typer.colors.RESET,
    )


def msg_success(msg: str):
    typer.secho(
        msg,
        fg=typer.colors.GREEN,
        bold=True,
        bg=typer.colors.RESET,
    )


def msg_error(msg: str):
    typer.secho(
        msg,
        fg=typer.colors.RED,
        bold=True,
        bg=typer.colors.RESET,
    )


def msg_info(msg: str):
    typer.secho(
        msg,
        fg=typer.colors.BRIGHT_BLUE,
        bold=True,
        bg=typer.colors.RESET,
    )


class SFTPClient(ParamikoSFTPClient):
    def put_dir(self, source, target):
        """
        Custom SFTPClient to support directory upload to a target path. The
        target directory needs to exists. All subdirectories in source are
        created under target.
        """

        self.mkdir_target(target.split("/"))

        for item in os.listdir(source):
            if os.path.isfile(os.path.join(source, item)):
                self.put(os.path.join(source, item), "%s/%s" % (target, item))
                msg_success(f"Copied local file to remote {target}/{item}")
            else:
                self.mkdir("%s/%s" % (target, item), ignore_existing=True)
                self.put_dir(os.path.join(source, item), "%s/%s" % (target, item))
                msg_info(f"Created remote dir {target}/{item}")

    def mkdir_target(self, path: list):
        """
        Util function for creating dir hierarchy from target path
        """
        for i, item in enumerate(path, start=1):
            self.mkdir("/".join(path[:i]), ignore_existing=True)

    def mkdir(self, path, mode=511, ignore_existing=False):
        """ Augments mkdir by adding an option to not fail if the folder exists  """
        try:
            super(SFTPClient, self).mkdir(path, mode)
        except IOError:
            if ignore_existing:
                pass
            else:
                raise


def get_connection(host: str, username: str, password: str, port: int = 22):
    msg_info(f"connecting to {host} ...")
    transport = paramiko.Transport((host, port))
    transport.banner_timeout = 200
    transport.connect(None, username, password)

    sftp = SFTPClient.from_transport(transport)
    msg_success(f"successfully connected to {host} ...")
    return sftp, transport


def list_files(sftp: SFTPClient, root_dir: str, tree: FakeDir) -> FakeDir:
    """
    Recursively list all remote files from root dir
    """
    try:
        files = sftp.listdir(root_dir)
    except FileNotFoundError as e:
        msg_error(f"No files found in {root_dir}")
        raise typer.Exit()
    else:
        for f in files:
            file_path = os.path.join(root_dir, f)
            file_attr = sftp.lstat(file_path)
            if stat.S_ISDIR(file_attr.st_mode):
                current = FakeDir(f, tree)
                list_files(sftp, file_path, current)
            elif stat.S_ISREG(file_attr.st_mode):
                tree.create_file(f)
    return tree


def delete_files(sftp: SFTPClient, remote_dir: str):
    """
    TODO: Add as a method to SFTPClient
    Recursively purge all files and directories from root dir
    """
    try:
        files = sftp.listdir(remote_dir)
    except FileNotFoundError:
        msg_error(f"{remote_dir} was not found on remote, skipping..")
    else:
        for f in files:
            filepath = os.path.join(remote_dir, f)
            try:
                sftp.remove(filepath)
                msg_success(f"successfully deleted remote file {filepath}")
            except IOError:
                delete_files(sftp, filepath)
        sftp.rmdir(remote_dir)
        msg_success(f"successfully deleted remote dir {remote_dir}")
