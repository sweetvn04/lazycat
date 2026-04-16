import docker
from rich.console import Console
from rich.table import Table


console = Console()
table = Table(title="Docker Containers")

# create a docker client instance 
client = docker.from_env()

# get all containers
containers = client.containers.list()

# add columns to the table
table.add_column("Name")
table.add_column("Status")
table.add_column("Image")


for container in containers:
    table.add_row(container.name, container.status, container.image.tags[0])

# print the table
console.print(table)

# container = client.containers.list()[0]
# print(container.labels)
