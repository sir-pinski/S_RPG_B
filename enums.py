from enum import Enum, auto


class TargetType(Enum):
    SELF = auto()
    ALLY = auto()
    ALLY_SELF = auto()
    ENEMY = auto()
    EVERYONE = auto()


class TargetCount(Enum):
    ONE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    ALL = auto()
    ROW = auto()
    COLUMN = auto()  # Placeholder for future implementation
    SPLASH = auto()  # Placeholder for future implementation


# Targeting Ranges only apply for Enemy targeting types. In all other types it is assumed to be "Any"
class TargetRange(Enum):
    FRONT_ROW = auto()
    BACK_ROW = auto()
    ANY = auto()


class TargetPriority(Enum):
    RANDOM = auto()
    CLOSEST = auto()
    DAMAGED = auto()
    NONE = auto()


class Element(Enum):
    FIRE = auto()
    WATER = auto()
    EARTH = auto()
    AIR = auto()
    DREAM = auto()
    NIGHTMARE = auto()


# class Location(Enum):
#     FRONT_LEFT = auto()
#     FRONT_CENTER = auto()
#     FRONT_RIGHT = auto()
#     MID_LEFT = auto()
#     MID_RIGHT = auto()
#     BACK_LEFT = auto()
#     BACK_CENTER = auto()
#     BACK_RIGHT = auto()


class Row(Enum):
    FRONT = auto()
    MID = auto()
    BACK = auto()

    def __le__(self, other):
        match self:
            case Row.FRONT:
                return True
            case Row.MID:
                if other == Row.FRONT:
                    return False
                else:
                    return True
            case Row.BACK:
                return False

    def __ge__(self, other):
        match self:
            case Row.FRONT:
                return False
            case Row.MID:
                if other == Row.BACK:
                    return False
                else:
                    return True
            case Row.BACK:
                return True


class Column(Enum):
    LEFT = auto()
    CENTER = auto()
    RIGHT = auto()

    def distance(self, other):
        if self == other:
            return 0
        elif self == Column.LEFT and other == Column.RIGHT:
            return 2
        elif self == Column.RIGHT and other == Column.LEFT:
            return 2
        else:
            return 1


def element_multiplier(attacker, defender):
    # This function is a placeholder for the actual implementation
    offElem = attacker.element
    defElem = defender.element
    match offElem:
        case Element.FIRE:
            match defElem:
                case Element.FIRE:
                    return 1
                case Element.WATER:
                    return 1
                case Element.EARTH:
                    return 1.5
                case Element.AIR:
                    return 0.67
                case Element.DREAM:
                    return 1
                case Element.NIGHTMARE:
                    return 1
        case Element.WATER:
            match defElem:
                case Element.FIRE:
                    return 1.5
                case Element.WATER:
                    return 1
                case Element.EARTH:
                    return 0.67
                case Element.AIR:
                    return 1
                case Element.DREAM:
                    return 1
                case Element.NIGHTMARE:
                    return 1
        case Element.EARTH:
            match defElem:
                case Element.FIRE:
                    return 1
                case Element.WATER:
                    return 0.67
                case Element.EARTH:
                    return 1
                case Element.AIR:
                    return 1.5
                case Element.DREAM:
                    return 1
                case Element.NIGHTMARE:
                    return 1
        case Element.AIR:
            match defElem:
                case Element.FIRE:
                    return 0.67
                case Element.WATER:
                    return 1.5
                case Element.EARTH:
                    return 1
                case Element.AIR:
                    return 1
                case Element.DREAM:
                    return 1
                case Element.NIGHTMARE:
                    return 1
        case Element.DREAM:
            match defElem:
                case Element.FIRE:
                    return 1
                case Element.WATER:
                    return 1
                case Element.EARTH:
                    return 1
                case Element.AIR:
                    return 1
                case Element.DREAM:
                    return 1
                case Element.NIGHTMARE:
                    return 1.5
        case Element.NIGHTMARE:
            match defElem:
                case Element.FIRE:
                    return 1
                case Element.WATER:
                    return 1
                case Element.EARTH:
                    return 1
                case Element.AIR:
                    return 1
                case Element.DREAM:
                    return 1.5
                case Element.NIGHTMARE:
                    return 1
