from glob import glob
import click
import os
from packager import Packager


@click.group()
def cli():
    """IOPkg 1.0 - Open source Platform-Independent Package Manager"""
    pass


@cli.command()
@click.argument('name')
@click.option('--include', '-i', multiple=True, help='List of files and directories to include')
def create(name, include):
    name += ".iopkg"
    packager = Packager()

    for path in include:
        for file_path in glob(path, recursive=True):
            try:
                if os.path.isfile(file_path):
                    packager.add(file_path)
                elif os.path.isdir(file_path):
                    packager.add(file_path)
            except PermissionError:
                click.echo(f"Permission denied for path: {os.path.abspath(file_path)}")

    packager.exportPkg(name)


@cli.command()
@click.argument('name')
def info(name):
    packager = Packager()
    author, files, details = packager.extractPkgInfo(name)

    def print_files(file_list, indent=''):
        for index, file in enumerate(file_list):
            if index == len(file_list) - 1:
                click.echo(f"{indent}└───{click.style(file.filename, fg='green')}: {file.size} bytes")  # Access the
                # filename attribute
                # of the File object
            else:
                click.echo(f"{indent}├───{click.style(file.filename, fg='green')}: {file.size} bytes")  # Access the
                # filename attribute
                # of the File object

            full_path = os.path.join(os.getcwd(), indent, file.filename)  # Join the current directory, indent, and
            # file name
            if os.path.isdir(full_path):
                print_files(os.listdir(full_path), indent=indent + '     ')

    click.echo(f"Author: {author}")
    click.echo(f"Creation date: {details['date']}")
    click.echo(f"IO Packager version: {details['version']}")
    click.echo("Files:")
    print_files(files)


@cli.command()
@click.argument('name')
@click.option('--target', '-t', default='.', help='Destination directory')
@click.option('--force', '-f', is_flag=True, help='Create the target directory if it does not exist')
def unpack(name, target, force):
    packager = Packager()
    author, files, details = packager.extractPkgInfo(name)

    if not os.path.exists(target):
        if force:
            os.makedirs(target)
        else:
            click.echo(f"The target directory '{target}' does not exist. Use the '-f' flag to create it.")
            return

    for file_info in files:
        file_path = os.path.join(target, file_info.filename)
        file_dir = os.path.dirname(file_path)

        os.makedirs(file_dir, exist_ok=True)

        with open(file_path, "wb") as file:
            file.write(file_info.content)


if __name__ == '__main__':
    cli()