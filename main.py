import docker
from rich.console import Console
from rich.table import Table
from collections import defaultdict

# create a console instance for printing the table
console = Console()

# create a docker client instance 
client = docker.from_env()

# get all containers
containers = client.containers.list()

# create a table to display all containers
# table = Table(title="Docker Containers")
# table.add_column("Name")
# table.add_column("Status")
# table.add_column("Image")
# for container in containers:
#     table.add_row(container.name, container.status, container.image.tags[0])
# # print the table
# console.print(table)

compose_dict = defaultdict(list) # create a dict to store containers by stack name
for container in containers:
    if "com.docker.compose.project" in container.labels: # check if the container is part of a stack
        stack_name = container.labels["com.docker.compose.project"] # get the stack name
        compose_dict[stack_name].append(container) # append the container to the stack via stack name key
    else:
        compose_dict["standalone"].append(container) # append the container to the standalone stack
for stack_name in compose_dict: # loop through the stacks
    table = Table(title="Stack: " + stack_name)
    # add columns to the table
    table.add_column("Name")
    table.add_column("Status")
    table.add_column("Image")
    # loop through the containers in the stack
    for container in compose_dict[stack_name]:
        table.add_row(container.name, container.status, container.image.tags[0]) # add the container to the table
    console.print(table) # print the table