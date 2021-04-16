from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
from azure.devops.v6_0.member_entitlement_management import *


personal_access_token = "j3hy4iby2l24qa5c3nvpqbukvz2lk4ol5554vn425jy6jwkw6rwa"
organization_url = 'https://dev.azure.com/pavantikkani'

credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

user_client = connection.clients_v6_0.get_member_entitlement_management_client()
graph_client = connection.clients_v6_0.get_graph_client()
user_client_old = connection.clients_v5_1.get_member_entitlement_management_client()
core_client = connection.clients_v6_0.get_core_client()

user_summary = user_client.get_users_summary()
get_members = user_client_old.get_user_entitlements()
list_projects = core_client.get_projects()

for project in list_projects:
    print(project.id)


access_level = AccessLevel(account_license_type='express')
graph_user = GraphUser(subject_kind='user', principal_name="glaringfireball@gmail.com")
project_reference = ProjectRef(id='26a29516-2420-448f-8b5e-0520799218f3')
grp = Group(group_type={'project_contributor'})
project_entitlement = ProjectEntitlement(project_ref=project_reference, group={'group': grp})
user_entitlement = UserEntitlement(access_level=access_level, user=graph_user, project_entitlements=[project_entitlement])
add_user = user_client.add_user_entitlement(user_entitlement)
print(add_user)



