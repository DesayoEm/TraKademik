from ..common_imports import *
from ..enums import ArchiveReason


class EducatorQualificationBase(BaseModel):
    """Base model for educator qualifications"""
    educator_id: UUID
    title: str
    description: str | None = None

    class Config:
        from_attributes = True

    json_schema_extra = {
        "example": {
            "educator_id": "00000000-0000-0000-0000-000000000001",
            "title": "Master of Science in Mathematics",
            "description": "Advanced degree in pure mathematics"
        }
    }


class EducatorQualificationCreate(EducatorQualificationBase):
    """Used for creating new educator qualifications"""
    pass


class EducatorQualificationUpdate(BaseModel):
    """Used for updating educator qualifications"""
    title: str
    description: str | None


class EducatorQualificationResponse(EducatorQualificationBase):
    """Response model for educator qualifications"""
    pass


class EducatorQualificationInDB(EducatorQualificationBase):
    """Represents stored educator qualifications"""
    id: UUID
    created_at: datetime
    created_by: UUID
    last_modified_at: datetime
    last_modified_by: UUID
    is_archived: bool
    archived_at: datetime | None = None
    archived_by: UUID | None = None
    archive_reason: ArchiveReason | None = None

    json_schema_extra = {
        "example": {
            "id": "00000000-0000-0000-0000-000000000000",
            "educator_id": "00000000-0000-0000-0000-000000000001",
            "title": "Master of Science in Mathematics",
            "description": "Advanced degree in pure mathematics",
            "created_at": "2024-02-17T12:00:00Z",
            "created_by": "00000000-0000-0000-0000-000000000000",
            "last_modified_at": "2024-02-17T12:00:00Z",
            "last_modified_by": "00000000-0000-0000-0000-000000000000",
            "is_archived": False,
            "archived_at": None,
            "archived_by": None,
            "archive_reason": None
        }
    }