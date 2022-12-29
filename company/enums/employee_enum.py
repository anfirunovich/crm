from core.base_enum import BaseEnum


class LanguageEnum(BaseEnum):
    PY = "Python"
    JS = "JavaScript"


class SexEnum(BaseEnum):
    MALE = "Male"
    FEMALE = "Female"


class ClothingSizesEnum(BaseEnum):
    S = "S"
    M = "M"
    L = "L"


class KnowledgeLevelsEnum(BaseEnum):
    TRAINEE = "Trainee"
    JUNIOR = "Junior"
    MIDDLE = "Middle"
    SENIOR = "Senior"
    TECH_LEAD = "Tech lead"
    TEAM_LEAD = "Team lead"
