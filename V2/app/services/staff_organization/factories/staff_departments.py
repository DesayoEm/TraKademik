from typing import List
from uuid import uuid4, UUID
from sqlalchemy.orm import Session
from V2.app.services.staff_organization.validators import StaffOrganizationValidators
from V2.app.database.models.staff_organization import StaffDepartments
from V2.app.database.db_repositories.sqlalchemy_repos.core_repo import SQLAlchemyRepository
from V2.app.database.models.data_enums import ArchiveReason


SYSTEM_USER_ID = UUID('00000000-0000-0000-0000-000000000000')

class StaffDepartmentsFactory:
    """Factory class for managing staff department operations."""

    def __init__(self, session: Session):
        self.repository = SQLAlchemyRepository(StaffDepartments, session)
        self.validator = StaffOrganizationValidators()

    def create_staff_department(self, new_department) -> StaffDepartments:
        """Create a new staff department.
        Args:
            new_department: Department data containing name and description
        Returns:
            StaffDepartments: Created department record
        """
        department = StaffDepartments(
            id=uuid4(),
            created_by=SYSTEM_USER_ID,
            last_modified_by=SYSTEM_USER_ID,
            name=self.validator.validate_name(new_department.name),
            description=self.validator.validate_name(new_department.description)
        )
        return self.repository.create(department)


    def get_staff_departments(self) -> List[StaffDepartments]:
        """Get all active staff departments.
        Returns:
            List[StaffDepartments]: List of active department records
        """
        return self.repository.get_all()


    def get_staff_department(self, department_id: UUID) -> StaffDepartments:
        """Get a specific staff department by ID.
        Args:
            department_id (UUID): ID of department to retrieve
        Returns:
            StaffDepartments: Retrieved department record
        """
        return self.repository.get_by_id(department_id)


    def update_staff_department(self, department_id: UUID, data: dict) -> StaffDepartments:
        """Update a staff department's information.
        Args:
            department_id (UUID): ID of department to update
            data (dict): Dictionary containing fields to update
        Returns:
            StaffDepartments: Updated department record
        """
        existing = self.get_staff_department(department_id)
        if 'name' in data:
            existing.name = self.validator.validate_name(data['name'])
        if 'description' in data:
            existing.description = self.validator.validate_name(data['description'])
        existing.last_modified_by = SYSTEM_USER_ID

        return self.repository.update(department_id, existing)


    def archive_department(self, department_id: UUID, reason: ArchiveReason) -> StaffDepartments:
        """Archive a staff department.
        Args:
            department_id (UUID): ID of department to archive
            reason (ArchiveReason): Reason for archiving
        Returns:
            StaffDepartments: Archived department record
        """
        return self.repository.archive(department_id, SYSTEM_USER_ID, reason)


    def delete_department(self, department_id: UUID) -> None:
        """Permanently delete a staff department.
        Args:
            department_id (UUID): ID of department to delete
        """
        self.repository.delete(department_id)