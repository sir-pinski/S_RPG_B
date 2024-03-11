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
    COLUMN = auto()
    SPLASH = auto()


class TargetRange(Enum):
    FRONT_ROW = auto()
    FRONT_MID = auto()
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

