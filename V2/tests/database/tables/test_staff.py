from .common_test_imports import *

def test_column_data_types_in_staff(db_inspector):
    """Confirm all required columns  are present and have the correct data type"""
    table = 'staff'
    columns = {col['name']: col for col in db_inspector.get_columns(table)}
    expected_types = {
        "id": UUID,
        "password_hash": String,
        "first_name": String,
        "last_name": String,
        "gender": Enum,
        "is_active": Boolean,
        "last_login": DateTime,
        "created_at": DateTime,
        "last_modified_at": DateTime,
        "is_archived": Boolean,
        "archived_at": DateTime,
        "archive_reason": Enum,
        "created_by": UUID,
        "last_modified_by": UUID,
        "access_level": Enum,
        "user_type": Enum,
        "staff_type": Enum,
        "image_url": String,
        "email_address": String,
        "address": String,
        "phone": String,
        "department_id": UUID,
        "role_id": UUID,
        "date_joined": Date,
        "date_left": Date,
    }

    for column, expected_type in expected_types.items():
        assert isinstance(columns[column]['type'], expected_type), f"{column} has incorrect type"

    enum_checks = {
        "gender": Gender,
        "archive_reason": ArchiveReason,
        "access_level": AccessLevel,
        "user_type": UserType,
        "staff_type": StaffType
    }

    for column, enum_class in enum_checks.items():
        col_type = columns[column]['type']
        assert isinstance(col_type, Enum), f"{column} should be Enum"
        assert col_type.enum_class is enum_class or col_type.enums == [e.value for e in enum_class], f"{column} Enum mismatch"

def test_staff_nullable_constraints(db_inspector):
    """verify nullable and not nullable fields"""
    table = 'staff'
    columns = db_inspector.get_columns(table)

    expected_nullable = {
        "id": False,
        "password_hash": False,
        "first_name": False,
        "last_name": False,
        "gender": False,
        "is_active": False,
        "last_login": True,
        "deletion_eligible":False,
        "created_at": False,
        "last_modified_at": False,
        "is_archived": False,
        "archived_at": False,
        "archived_by": False,
        "archive_reason": False,
        "created_by": False,
        "last_modified_by": False,
        "access_level": False,
        "user_type": False,
        "staff_type": False,
        "image_url": False,
        "email_address": False,
        "address": False,
        "phone": False,
        "department_id":False,
        "role_id":False,
        "date_joined":False,
        "date_left":True

    }
    for column in columns:
        column['name'] = column['name']
        assert column['nullable'] == expected_nullable.get(column['name']), \
            f"column {column['name']} is not nullable as expected"

