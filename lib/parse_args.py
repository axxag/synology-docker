import argparse
from datetime import datetime
import os
from typing import TypedDict

current_datetime = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
default_backup_name = f"docker_backup_{current_datetime}.tgz"

parser = argparse.ArgumentParser()

Args = TypedDict(
    "Args",
    backup=str,
    compose_version=str,
    docker_version=str,
    force=bool,
    path=str,
    stage=bool,
    target=str,
)


def parse_args() -> Args:
    parser.add_argument(
        "-b",
        "--backup",
        metavar="NAME",
        dest="backup",
        default=default_backup_name,
        help="Name of the backup (defaults to 'docker_backup_YY-MM-DD-HH-MM-SS.tgz')",
    )
    parser.add_argument(
        "-c",
        "--compose",
        metavar="VERSION",
        dest="compose_version",
        default="latest",
        help="Docker Compose target version (defaults to latest)",
    )
    parser.add_argument(
        "-d",
        "--docker",
        metavar="VERSION",
        dest="docker_version",
        default="latest",
        help="Docker target version (defaults to latest)",
    )
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        dest="force",
        help="Force update (bypass compatibility check and confirmation check)",
    )
    parser.add_argument(
        "-p",
        "--path",
        metavar="PATH",
        dest="path",
        default=os.getcwd(),
        help="Path of the backup (defaults to current directory)",
    )
    parser.add_argument(
        "-s",
        "--stage",
        action="store_true",
        dest="stage",
        help="Stage only, do not actually replace binaries or configuration of log driver",
    )
    parser.add_argument(
        "-t",
        "--target",
        choices=["all", "engine", "compose", "driver"],
        metavar="TARGET",
        dest="target",
        default="all",
        help="Target to update, either 'all' (default), 'engine', 'compose', or 'driver'",
    )
    args = parser.parse_args()
    return {
        "backup": args.backup,
        "compose_version": args.compose_version,
        "docker_version": args.docker_version,
        "force": args.force,
        "path": args.path,
        "stage": args.stage,
        "target": args.target,
    }
