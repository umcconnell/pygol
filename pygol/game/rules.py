"""Common Game of Life Rules"""
# pylint: disable=unused-argument
from typing import Callable, Iterator, Tuple

Neighbors = Iterator[Tuple[int, int, int]]
Signature = Callable[[int, int, Neighbors], int]


def conways_life(cell: int, live_count: int, neighbors: Neighbors = None) -> int:
    """Standard Game of Life rule

    This rule can be specified using these strings:
        - ``B3/S23``
        - ``23/3``
        - ``conway``
        - ``conways life``

    Parameters
    ----------
    cell: int
        Value of the current cell. Can be ``1`` (alive) or ``0`` (dead)
    live_count: int
        Count of cells alive (``1``) around the current cell.
    neighbors: Iterator[Tuple[int, int, int]], optional
        Iterator yielding the value, the x- and the y-coordinate of the
        individual neighbors. This parameters might only be required by very few
        rules and is present in every game rule for consistency.

    Returns
    -------
    int
        Computed value of the current cell. Can be ``1`` (alive) or ``0`` (dead).

    Notes
    -----
    The value of ``live_count`` depends on the type of neighborhood you use.
    PyGoL uses the Moore neighborhood by default. See the LifeWiki for more
    information on types of neighborhood:
    https://www.conwaylife.com/wiki/Cellular_automaton#Common_dimensions_and_neighborhoods

    References
    ----------
    Find this rule in the LifeWiki:
    https://www.conwaylife.com/wiki/Conway%27s_Game_of_Life
    """
    if cell == 1 and live_count in [2, 3]:
        return 1
    if cell == 0 and live_count == 3:
        return 1

    return 0


def replicator(cell: int, live_count: int, neighbors: Neighbors = None) -> int:
    """\"Replicator\" Game of Life rule

    This rule can be specified using these strings:
        - ``B1357/S1357``
        - ``1357/1357``
        - ``replicator``

    Parameters
    ----------
    cell: int
        Value of the current cell. Can be ``1`` (alive) or ``0`` (dead)
    live_count: int
        Count of cells alive (``1``) around the current cell.
    neighbors: Iterator[Tuple[int, int, int]], optional
        Iterator yielding the value, the x- and the y-coordinate of the
        individual neighbors. This parameters might only be required by very few
        rules and is present in every game rule for consistency.

    Returns
    -------
    int
        Computed value of the current cell. Can be ``1`` (alive) or ``0`` (dead).

    Notes
    -----
    The value of ``live_count`` depends on the type of neighborhood you use.
    PyGoL uses the Moore neighborhood by default. See the LifeWiki for more
    information on types of neighborhood:
    https://www.conwaylife.com/wiki/Cellular_automaton#Common_dimensions_and_neighborhoods

    References
    ----------
    Find this rule in the LifeWiki:
    https://www.conwaylife.com/wiki/OCA:Replicator
    """
    if live_count % 2 == 1:
        return 1

    return 0


def fredkin(cell: int, live_count: int, neighbors: Neighbors = None) -> int:
    """\"Fredkin\" Game of Life rule

    This rule can be specified using these strings:
        - ``B1357/S02468``
        - ``2468/1357``
        - ``fredkin``

    Parameters
    ----------
    cell: int
        Value of the current cell. Can be ``1`` (alive) or ``0`` (dead)
    live_count: int
        Count of cells alive (``1``) around the current cell.
    neighbors: Iterator[Tuple[int, int, int]], optional
        Iterator yielding the value, the x- and the y-coordinate of the
        individual neighbors. This parameters might only be required by very few
        rules and is present in every game rule for consistency.

    Returns
    -------
    int
        Computed value of the current cell. Can be ``1`` (alive) or ``0`` (dead).

    Notes
    -----
    The value of ``live_count`` depends on the type of neighborhood you use.
    PyGoL uses the Moore neighborhood by default. See the LifeWiki for more
    information on types of neighborhood:
    https://www.conwaylife.com/wiki/Cellular_automaton#Common_dimensions_and_neighborhoods

    References
    ----------
    Find this rule in the LifeWiki:
    https://www.conwaylife.com/wiki/OCA:Replicator#Replicator_2
    """
    if (live_count + cell) % 2 == 1:
        return 1

    return 0


def seeds(cell: int, live_count: int, neighbors: Neighbors = None) -> int:
    """\"Seeds\" Game of Life rule

    This rule can be specified using these strings:
        - ``B2/S``
        - ``/2``
        - ``seeds``

    Parameters
    ----------
    cell: int
        Value of the current cell. Can be ``1`` (alive) or ``0`` (dead)
    live_count: int
        Count of cells alive (``1``) around the current cell.
    neighbors: Iterator[Tuple[int, int, int]], optional
        Iterator yielding the value, the x- and the y-coordinate of the
        individual neighbors. This parameters might only be required by very few
        rules and is present in every game rule for consistency.

    Returns
    -------
    int
        Computed value of the current cell. Can be ``1`` (alive) or ``0`` (dead).

    Notes
    -----
    The value of ``live_count`` depends on the type of neighborhood you use.
    PyGoL uses the Moore neighborhood by default. See the LifeWiki for more
    information on types of neighborhood:
    https://www.conwaylife.com/wiki/Cellular_automaton#Common_dimensions_and_neighborhoods

    References
    ----------
    Find this rule in the LifeWiki:
    https://www.conwaylife.com/wiki/OCA:Seeds
    """
    if not cell and live_count == 2:
        return 1

    return 0


def live_free_or_die(cell: int, live_count: int, neighbors: Neighbors = None) -> int:
    """\"Live Free or Die\" Game of Life rule

    This rule can be specified using these strings:
        - ``B2/S0``
        - ``0/2``
        - ``live free or die``

    Parameters
    ----------
    cell: int
        Value of the current cell. Can be ``1`` (alive) or ``0`` (dead)
    live_count: int
        Count of cells alive (``1``) around the current cell.
    neighbors: Iterator[Tuple[int, int, int]], optional
        Iterator yielding the value, the x- and the y-coordinate of the
        individual neighbors. This parameters might only be required by very few
        rules and is present in every game rule for consistency.

    Returns
    -------
    int
        Computed value of the current cell. Can be ``1`` (alive) or ``0`` (dead).

    Notes
    -----
    The value of ``live_count`` depends on the type of neighborhood you use.
    PyGoL uses the Moore neighborhood by default. See the LifeWiki for more
    information on types of neighborhood:
    https://www.conwaylife.com/wiki/Cellular_automaton#Common_dimensions_and_neighborhoods

    References
    ----------
    Find this rule in the LifeWiki:
    https://www.conwaylife.com/wiki/OCA:Live_Free_or_Die
    """
    if cell and live_count == 0:
        return 1
    if not cell and live_count == 2:
        return 1

    return 0


def life_without_death(cell: int, live_count: int, neighbors: Neighbors = None) -> int:
    """\"Life Without Death\" Game of Life rule

    This rule can be specified using these strings:
        - ``B3/S012345678``
        - ``012345678/3``
        - ``life without death``

    Parameters
    ----------
    cell: int
        Value of the current cell. Can be ``1`` (alive) or ``0`` (dead)
    live_count: int
        Count of cells alive (``1``) around the current cell.
    neighbors: Iterator[Tuple[int, int, int]], optional
        Iterator yielding the value, the x- and the y-coordinate of the
        individual neighbors. This parameters might only be required by very few
        rules and is present in every game rule for consistency.

    Returns
    -------
    int
        Computed value of the current cell. Can be ``1`` (alive) or ``0`` (dead).

    Notes
    -----
    The value of ``live_count`` depends on the type of neighborhood you use.
    PyGoL uses the Moore neighborhood by default. See the LifeWiki for more
    information on types of neighborhood:
    https://www.conwaylife.com/wiki/Cellular_automaton#Common_dimensions_and_neighborhoods

    References
    ----------
    Find this rule in the LifeWiki:
    https://www.conwaylife.com/wiki/OCA:Life_without_death
    """
    if cell:
        return 1
    if not cell and live_count == 3:
        return 1

    return 0


def maze(cell: int, live_count: int, neighbors: Neighbors = None) -> int:
    """\"Maze\" Game of Life rule

    This rule can be specified using these strings:
        - ``B3/S12345``
        - ``12345/3``
        - ``maze``

    Parameters
    ----------
    cell: int
        Value of the current cell. Can be ``1`` (alive) or ``0`` (dead)
    live_count: int
        Count of cells alive (``1``) around the current cell.
    neighbors: Iterator[Tuple[int, int, int]], optional
        Iterator yielding the value, the x- and the y-coordinate of the
        individual neighbors. This parameters might only be required by very few
        rules and is present in every game rule for consistency.

    Returns
    -------
    int
        Computed value of the current cell. Can be ``1`` (alive) or ``0`` (dead).

    Notes
    -----
    The value of ``live_count`` depends on the type of neighborhood you use.
    PyGoL uses the Moore neighborhood by default. See the LifeWiki for more
    information on types of neighborhood:
    https://www.conwaylife.com/wiki/Cellular_automaton#Common_dimensions_and_neighborhoods

    References
    ----------
    Find this rule in the LifeWiki:
    https://www.conwaylife.com/wiki/OCA:Maze
    """
    if cell and 1 <= live_count <= 5:
        return 1
    if not cell and live_count == 3:
        return 1

    return 0


def mazectric(cell: int, live_count: int, neighbors: Neighbors = None) -> int:
    """\"Mazectric\" Game of Life rule

    This rule can be specified using these strings:
        - ``B3/S1234``
        - ``1234/3``
        - ``mazectric``

    Parameters
    ----------
    cell: int
        Value of the current cell. Can be ``1`` (alive) or ``0`` (dead)
    live_count: int
        Count of cells alive (``1``) around the current cell.
    neighbors: Iterator[Tuple[int, int, int]], optional
        Iterator yielding the value, the x- and the y-coordinate of the
        individual neighbors. This parameters might only be required by very few
        rules and is present in every game rule for consistency.

    Returns
    -------
    int
        Computed value of the current cell. Can be ``1`` (alive) or ``0`` (dead).

    Notes
    -----
    The value of ``live_count`` depends on the type of neighborhood you use.
    PyGoL uses the Moore neighborhood by default. See the LifeWiki for more
    information on types of neighborhood:
    https://www.conwaylife.com/wiki/Cellular_automaton#Common_dimensions_and_neighborhoods

    References
    ----------
    Find this rule in the LifeWiki:
    https://www.conwaylife.com/wiki/OCA:Maze#Similar_rules
    """
    if live_count == 5:
        return 0

    return maze(cell, live_count, neighbors)


def two_by_two(cell: int, live_count: int, neighbors: Neighbors = None) -> int:
    """\"2x2\" Game of Life rule

    This rule can be specified using these strings:
        - ``B36/S125``
        - ``125/36``
        - ``two by two``
        - ``2x2``

    Parameters
    ----------
    cell: int
        Value of the current cell. Can be ``1`` (alive) or ``0`` (dead)
    live_count: int
        Count of cells alive (``1``) around the current cell.
    neighbors: Iterator[Tuple[int, int, int]], optional
        Iterator yielding the value, the x- and the y-coordinate of the
        individual neighbors. This parameters might only be required by very few
        rules and is present in every game rule for consistency.

    Returns
    -------
    int
        Computed value of the current cell. Can be ``1`` (alive) or ``0`` (dead).

    Notes
    -----
    The value of ``live_count`` depends on the type of neighborhood you use.
    PyGoL uses the Moore neighborhood by default. See the LifeWiki for more
    information on types of neighborhood:
    https://www.conwaylife.com/wiki/Cellular_automaton#Common_dimensions_and_neighborhoods

    References
    ----------
    Find this rule in the LifeWiki:
    https://www.conwaylife.com/wiki/OCA:2%C3%972
    """
    if cell and live_count in [1, 2, 5]:
        return 1
    if not cell and live_count in [3, 6]:
        return 1

    return 0


def high_life(cell: int, live_count: int, neighbors: Neighbors = None) -> int:
    """\"HighLife\" Game of Life rule

    This rule can be specified using these strings:
        - ``B36/S23``
        - ``23/36``
        - ``high life``

    Parameters
    ----------
    cell: int
        Value of the current cell. Can be ``1`` (alive) or ``0`` (dead)
    live_count: int
        Count of cells alive (``1``) around the current cell.
    neighbors: Iterator[Tuple[int, int, int]], optional
        Iterator yielding the value, the x- and the y-coordinate of the
        individual neighbors. This parameters might only be required by very few
        rules and is present in every game rule for consistency.

    Returns
    -------
    int
        Computed value of the current cell. Can be ``1`` (alive) or ``0`` (dead).

    Notes
    -----
    The value of ``live_count`` depends on the type of neighborhood you use.
    PyGoL uses the Moore neighborhood by default. See the LifeWiki for more
    information on types of neighborhood:
    https://www.conwaylife.com/wiki/Cellular_automaton#Common_dimensions_and_neighborhoods

    References
    ----------
    Find this rule in the LifeWiki:
    https://www.conwaylife.com/wiki/OCA:HighLife
    """
    if cell and live_count in [2, 3]:
        return 1
    if not cell and live_count in [3, 6]:
        return 1

    return 0


def move(cell: int, live_count: int, neighbors: Neighbors = None) -> int:
    """\"Move\" Game of Life rule

    This rule can be specified using these strings:
        - ``B368/S245``
        - ``245/368``
        - ``move``

    Parameters
    ----------
    cell: int
        Value of the current cell. Can be ``1`` (alive) or ``0`` (dead)
    live_count: int
        Count of cells alive (``1``) around the current cell.
    neighbors: Iterator[Tuple[int, int, int]], optional
        Iterator yielding the value, the x- and the y-coordinate of the
        individual neighbors. This parameters might only be required by very few
        rules and is present in every game rule for consistency.

    Returns
    -------
    int
        Computed value of the current cell. Can be ``1`` (alive) or ``0`` (dead).

    Notes
    -----
    The value of ``live_count`` depends on the type of neighborhood you use.
    PyGoL uses the Moore neighborhood by default. See the LifeWiki for more
    information on types of neighborhood:
    https://www.conwaylife.com/wiki/Cellular_automaton#Common_dimensions_and_neighborhoods

    References
    ----------
    Find this rule in the LifeWiki:
    https://www.conwaylife.com/wiki/OCA:Move
    """
    if cell and live_count in [2, 4, 5]:
        return 1
    if not cell and live_count in [3, 6, 8]:
        return 1

    return 0


def day_and_night(cell: int, live_count: int, neighbors: Neighbors = None) -> int:
    """\"Day & Night\" Game of Life rule

    This rule can be specified using these strings:
        - ``B3678/34678``
        - ``34678/3678``
        - ``day and night``

    Parameters
    ----------
    cell: int
        Value of the current cell. Can be ``1`` (alive) or ``0`` (dead)
    live_count: int
        Count of cells alive (``1``) around the current cell.
    neighbors: Iterator[Tuple[int, int, int]], optional
        Iterator yielding the value, the x- and the y-coordinate of the
        individual neighbors. This parameters might only be required by very few
        rules and is present in every game rule for consistency.

    Returns
    -------
    int
        Computed value of the current cell. Can be ``1`` (alive) or ``0`` (dead).

    Notes
    -----
    The value of ``live_count`` depends on the type of neighborhood you use.
    PyGoL uses the Moore neighborhood by default. See the LifeWiki for more
    information on types of neighborhood:
    https://www.conwaylife.com/wiki/Cellular_automaton#Common_dimensions_and_neighborhoods

    References
    ----------
    Find this rule in the LifeWiki:
    https://www.conwaylife.com/wiki/OCA:Day_%26_Night
    """
    if cell and live_count in [3, 4, 6, 7, 8]:
        return 1
    if not cell and live_count in [3, 6, 7, 8]:
        return 1

    return 0


def dry_life(cell: int, live_count: int, neighbors: Neighbors = None) -> int:
    """\"DryLife\" Game of Life rule

    This rule can be specified using these strings:
        - ``B37/S23``
        - ``23/37``
        - ``dry life``

    Parameters
    ----------
    cell: int
        Value of the current cell. Can be ``1`` (alive) or ``0`` (dead)
    live_count: int
        Count of cells alive (``1``) around the current cell.
    neighbors: Iterator[Tuple[int, int, int]], optional
        Iterator yielding the value, the x- and the y-coordinate of the
        individual neighbors. This parameters might only be required by very few
        rules and is present in every game rule for consistency.

    Returns
    -------
    int
        Computed value of the current cell. Can be ``1`` (alive) or ``0`` (dead).

    Notes
    -----
    The value of ``live_count`` depends on the type of neighborhood you use.
    PyGoL uses the Moore neighborhood by default. See the LifeWiki for more
    information on types of neighborhood:
    https://www.conwaylife.com/wiki/Cellular_automaton#Common_dimensions_and_neighborhoods

    References
    ----------
    Find this rule in the LifeWiki:
    https://www.conwaylife.com/wiki/OCA:DryLife
    """
    if cell and live_count in [2, 3]:
        return 1
    if not cell and live_count in [3, 7]:
        return 1

    return 0


def pedestrian_life(cell: int, live_count: int, neighbors: Neighbors = None) -> int:
    """\"Pedestrian Life\" Game of Life rule

    This rule can be specified using these strings:
        - ``B38/S23``
        - ``23/38``
        - ``pedestrian life``

    Parameters
    ----------
    cell: int
        Value of the current cell. Can be ``1`` (alive) or ``0`` (dead)
    live_count: int
        Count of cells alive (``1``) around the current cell.
    neighbors: Iterator[Tuple[int, int, int]], optional
        Iterator yielding the value, the x- and the y-coordinate of the
        individual neighbors. This parameters might only be required by very few
        rules and is present in every game rule for consistency.

    Returns
    -------
    int
        Computed value of the current cell. Can be ``1`` (alive) or ``0`` (dead).

    Notes
    -----
    The value of ``live_count`` depends on the type of neighborhood you use.
    PyGoL uses the Moore neighborhood by default. See the LifeWiki for more
    information on types of neighborhood:
    https://www.conwaylife.com/wiki/Cellular_automaton#Common_dimensions_and_neighborhoods

    References
    ----------
    Find this rule in the LifeWiki:
    https://www.conwaylife.com/wiki/OCA:Pedestrian_Life
    """
    if cell and live_count in [2, 3]:
        return 1
    if not cell and live_count in [3, 8]:
        return 1

    return 0


#: Dict collection of all rule-string aliases. Check the individual rules for
#: available aliases
RULES = {
    "B3/S23": conways_life,
    "23/3": conways_life,
    "conway": conways_life,
    "conways life": conways_life,

    "B1357/S1357": replicator,
    "1357/1357": replicator,
    "replicator": replicator,

    "B1357/S02468": fredkin,
    "02468/1357": fredkin,
    "fredkin": fredkin,

    "B2/S": seeds,
    "/2": seeds,
    "seeds": seeds,

    "B2/S0": live_free_or_die,
    "0/2": live_free_or_die,
    "live free or die": live_free_or_die,

    "B3/S012345678": life_without_death,
    "012345678/3": life_without_death,
    "life without death": life_without_death,

    "B3/S12345": maze,
    "12345/3": maze,
    "maze": maze,

    "B3/S1234": mazectric,
    "1234/3": mazectric,
    "mazectric": mazectric,

    "B36/S125": two_by_two,
    "125/36": two_by_two,
    "two by two": two_by_two,
    "2x2": two_by_two,

    "B36/S23": high_life,
    "23/36": high_life,
    "high life": high_life,

    "B368/S245": move,
    "245/368": move,
    "move": move,

    "B3678/34678": day_and_night,
    "34678/3678": day_and_night,
    "day and night": day_and_night,

    "B37/S23": dry_life,
    "23/37": dry_life,
    "dry life": dry_life,

    "B38/S23": pedestrian_life,
    "23/38": pedestrian_life,
    "pedestrian life": pedestrian_life
}
