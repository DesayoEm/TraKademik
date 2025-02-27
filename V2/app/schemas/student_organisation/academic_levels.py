from ..common_imports import *
from ..enums import ArchiveReason

class AcademicLevelBase(BaseModel):
    """Base model for class levels"""
    name: str
    description: str

    class Config:
        from_attributes = True

    json_schema_extra = {
        "example": {
            "name": "JSS1",
            "description": "First Level in the Secondary School System",
        }}

class AcademicLevelUpdate(AcademicLevelBase):
    """Used for updating class levels"""
    order: int | None = None

    json_schema_extra = {
        "example": {
            "name": "JSS2",
            "description": "Second Level in the Secondary School System",
            "order": "1",
        }}

class AcademicLevelCreate(AcademicLevelUpdate):
    """Used for creating new class levels"""
    pass

class AcademicLevelResponse(AcademicLevelBase):
    """Response model for class levels"""
    order: int

class AcademicLevelInDB(AcademicLevelBase):
    """Represents stored class levels"""
    id: UUID
    created_at: datetime
    created_by: UUID
    last_modified_at: datetime
    last_modified_by: UUID
    is_archived: bool
    archived_at: datetime | None = None
    archived_by: UUID | None = None
    archive_reason: ArchiveReason | None = None
    order: int

    json_schema_extra = {
        "example": {
            "name": "JSS2",
            "description": "Second Level in the Secondary School System",
            "order": "1",
            "created_at": "2024-02-17T12:00:00Z",
            "created_by": "00000000-0000-0000-0000-000000000000",
            "last_modified_at": "2024-02-17T12:00:00Z",
            "last_modified_by": "00000000-0000-0000-0000-000000000000",
            "is_archived": False,
            "archived_at": None,
            "archived_by": None,
            "archive_reason": None
        }}