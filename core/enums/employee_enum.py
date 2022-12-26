from core.enums.base_enum import BaseEnum


class LanguageEnum(BaseEnum):
    PY = "Python"
    JS = "JavaScript"


class SexEnum(BaseEnum):
    MALE = "Male"
    FEMALE = "Female"


class SizeEnum(BaseEnum):
    S = "S"
    M = "M"
    L = "L"


class LevelEnum(BaseEnum):
    TRAINEE = "Trainee"
    JUNIOR = "Junior"
    MIDDLE = "Middle"
    SENIOR = "Senior"
    TECH_LEAD = "Tech lead"
    TEAM_LEAD = "Team lead"
