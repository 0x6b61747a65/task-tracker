import argparse


parser = argparse.ArgumentParser(
    description="Simple CLI program to track daily tasks.")
parser.add_argument("-a", "--add", nargs=3, help="Add new task",
                    metavar="'NAME' 'ASSIGNED TO' 'DESCRIPTION'")
parser.add_argument("-d", "--describe",
                    help="Provides full task description.", metavar="TASK ID")
parser.add_argument("-l", "--list", choices=["all", "active",
                    "finished"], default="all", help="List selected set of tasks.")


args = parser.parse_args()
