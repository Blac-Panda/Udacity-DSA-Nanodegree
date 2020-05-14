class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)
        
    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def __repr__(self):
        return f"Group(name: {self.name},\n\tusers: {self.users},\n\tgroups:{self.groups})"

"""Checks if the user is in the group. If found, returns Ture, else, calls subgroups recursively."""
def is_user_in_group(user, group):

    if user in group.get_users():
        return True

    for subgroup in group.get_groups():
        #print("checking group-- ", subgroup.get_name())
        return is_user_in_group(user, subgroup)
        

    return False

"""
    verify the data
"""
def run_test_data():

    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")
    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print("\nCheck if user in group - {}".format(is_user_in_group(sub_child_user, parent)))
    print("\nCheck if user in group - {}".format(is_user_in_group('youngqueenz',parent)))   #Returns false cos sub_child_use doesn't exist
    print("\nCheck if user in group - {}".format(is_user_in_group('',parent)))              #Returns false cos input is null
    print("\nParent Group:")
    print(parent)

run_test_data()
