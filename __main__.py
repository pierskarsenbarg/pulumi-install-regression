"""An Azure RM Python Pulumi program"""

import pulumi
from pulumi_azure_native import resources

from pierskarsenbarg_storage import storage

# Create an Azure Resource Group
resource_group = resources.ResourceGroup("resource_group")

my_storage = storage.Storage("storage",
                             resource_group_name=resource_group.name
                             )