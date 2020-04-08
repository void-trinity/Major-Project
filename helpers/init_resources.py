from model.resource import Resource
from config.resources import RESOURCES

def init_resources(total_resources):
    instance_per_resource = int(total_resources/len(RESOURCES))

    resources_dict = dict()
    id = 0

    for resource in RESOURCES:
        for i in range(instance_per_resource):
            resources_dict[id] = Resource(id = id, type = resource['type'], cu = resource['cu'], price = resource['price'])
            id = id + 1

    return resources_dict
