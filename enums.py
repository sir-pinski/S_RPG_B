from enum import Enum, auto


class TargetType(Enum):
    SELF = auto()  # Can only target self
    ALLY = auto()  # Can only target allies
    ALLY_SELF = auto()  # Can target allies and self
    ENEMY = auto()  # Can only target enemies
    EVERYONE = auto()  # Can target everyone


class TargetCount(Enum):
    ONE = auto()  # Can hit one character
    TWO = auto()  # Can hit two characters
    THREE = auto()  # Can hit three characters
    FOUR = auto()  # Can hit four characters
    ALL = auto()  # Can hit all characters in range
    ROW = auto()  # Can hit all characters in a row
    COLUMN = auto()  # Placeholder for future implementation, will hit all characters in a column


# Targeting Ranges only apply for Enemy targeting types. In all other types it is assumed to be "Any"
class TargetRange(Enum):
    FRONT_ROW = auto()  # Can target only the front row
    BACK_ROW = auto()  # Can target only the back row
    ANY = auto()  # Can target any row


class TargetPriority(Enum):
    RANDOM = auto()  # Will prioritize random targets
    CLOSEST = auto()  # Will prioritize the closest targets
    DAMAGED = auto()  # Will prioritize the most damaged targets
    NONE = auto()  # Will not prioritize targets (for example, with SELF targeting type)


class Element(Enum):
    FIRE = auto()
    WATER = auto()
    EARTH = auto()
    AIR = auto()
    DREAM = auto()
    NIGHTMARE = auto()


class Row(Enum):
    FRONT = auto()
    MID = auto()
    BACK = auto()

# Overloaded <= and >= operators for sorting. We define closer to the front as less, farther away as greater.
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
                if other == Row.FRONT:
                    return True
                else:
                    return False
            case Row.BACK:
                return True


class Column(Enum):
    LEFT = auto()
    CENTER = auto()
    RIGHT = auto()

# Calculate the distance between two columns, used for Closest targeting priority
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
