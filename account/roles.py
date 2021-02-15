from rolepermissions.roles import AbstractUserRole

class Administration(AbstractUserRole):
    available_permissions = {
        'creat_demo': True,
        'edit_demo': True,
    }
