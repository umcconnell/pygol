"""Matrix utility"""
import itertools
import math
import random
from typing import Any, List

DX = [0, +1, 0, -1]
DY = [-1, 0, +1, 0]

# remove (0, 0) as this is the point we're looking at
NEIGHBORS = set(itertools.product(DX, repeat=2)) - {(0, 0)}


class Matrix:
    """Matrix utility class.

    This matrix class is iterable (yielding elements from left to right, top to
    bottom) and supports prettyprinting (via the __str__ method) as well as
    square bracket access (`matrix[row][col]`).

    Parameters
    ----------
    width: int
        Width of the resulting matrix.
    height: int, optional
        Height of the resulting matrix. If no height is specified, ``height``
        will default to ``width``, resulting in a square matrix.
    content: `list` [`list` [`Any`]], optional
        Optional content to fill the matrix with. This content must be of the
        same dimensions as the desired matrix. If not specified, the matrix
        will be filled with ``0``.

    Attributes
    ----------
    width: int
        Width of the matrix.
    height: int
        Height of the matrix.
    matrix: `list` [`list` [`Any`]]
        Content of the matrix.

    Examples
    --------
    >>> matrix = Matrix(3, 3)
    >>> matrix[0][0] = 1
    >>> print(matrix)
    1 0 0
    0 0 0
    0 0 0

    >>> print(matrix.fill_random())
    0 1 1
    0 1 1
    1 1 0
    # random

    >>> print(matrix.pad(1, value=2))
    2 2 2 2 2
    2 0 1 1 2
    2 0 1 1 2
    2 1 1 0 2
    2 2 2 2 2
    # random

    """

    def __init__(self, width: int, height: int = None,
                 content: List[List[Any]] = None):
        if not height:
            height = width

        self.height = height
        self.width = width

        self.matrix = content or [
            [0 for x in range(width)] for y in range(height)]

    def __iter__(self):
        yield from self.matrix

    def __str__(self):
        res = ""

        for row in self.matrix:
            for col in row:
                res += str(col) + " "
            res += "\n"

        return res

    def __getitem__(self, key):
        return self.matrix[key]

    def neighbors(self, x, y, wrap=False):
        """Iterate through the neighboors of a point.

        Parameters
        ----------
        x: int
            x-coordinate of the point in the matrix.
        y: int
            y-coordinate of the point in the matrix.
        wrap: bool, optional
            Whether to wrap around the edge of the matrix when checking
            neighborhood. If wrap is ``False`` this method yields ``0`` instead
            of wrapping around the edge; defaults to ``False``.

        Yields
        ------
        `tuple` [`Any`, int, int]
            Tuple of the value, the x- and the y-coordinate of a neighbor.

        Notes
        -----
        This method uses the Moore neighborhood to determine neighboring points.
        See Wikipedia for more information:
        https://en.wikipedia.org/wiki/Moore_neighborhood
        """
        for dir_x, dir_y in NEIGHBORS:
            new_x = (x + dir_x)
            new_y = (y + dir_y)

            # drop entries outside of matrix when no wrapping
            if not wrap and not (0 <= new_x < self.width and 0 <= new_y < self.height):
                # continue
                yield 0, new_x, new_y
                continue

            if wrap:
                new_x %= self.width
                new_y %= self.height

            yield self.matrix[new_y][new_x], new_x, new_y

    def pad_right(self, right: int, value: Any = 0):
        """Pad the right side of the matrix.

        Parameters
        ----------
        right: int
            Amount of columns to add on the right side of the matrix.
        value: `Any`, optional
            Value to pad the matrix with.

        Returns
        -------
        self
            Returns the matrix object to allow chaining.

        Examples
        --------
        >>> matrix = Matrix(2)
        >>> print(matrix)
        0 0
        0 0

        >>> print(matrix.pad_right(1, value=2))
        0 0 2
        0 0 2

        """
        self.width += right

        for row in self.matrix:
            for _ in range(abs(right)):
                if right >= 0:
                    row.append(value)
                else:
                    row.pop()

        return self

    def pad_left(self, left: int, value: Any = 0):
        """Pad the left side of the matrix.

        Parameters
        ----------
        left: int
            Amount of columns to add on the left side of the matrix.
        value: `Any`, optional
            Value to pad the matrix with.

        Returns
        -------
        self
            Returns the matrix object to allow chaining.

        Examples
        --------
        >>> matrix = Matrix(2)
        >>> print(matrix)
        0 0
        0 0

        >>> print(matrix.pad_left(1, value=2))
        2 0 0
        2 0 0

        """
        self.width += left

        for row in self.matrix:
            for _ in range(abs(left)):
                if left >= 0:
                    row.insert(0, value)
                else:
                    row.pop(0)

        return self

    def pad_top(self, top: int, value: Any = 0):
        """Pad the top of the matrix.

        Parameters
        ----------
        top: int
            Amount of rows to add to the top of the matrix.
        value: `Any`, optional
            Value to pad the matrix with.

        Returns
        -------
        self
            Returns the matrix object to allow chaining.

        Examples
        --------
        >>> matrix = Matrix(2)
        >>> print(matrix)
        0 0
        0 0

        >>> print(matrix.pad_top(1, value=2))
        2 2
        0 0
        0 0

        """
        self.height += top

        for _ in range(abs(top)):
            if top >= 0:
                self.matrix.insert(
                    0, [value for x in range(self.width)])
            else:
                self.matrix.pop(0)

        return self

    def pad_bottom(self, bottom: int, value: Any = 0):
        """Pad the bottom of the matrix.

        Parameters
        ----------
        top: int
            Amount of rows to add to the bottom of the matrix.
        value: `Any`, optional
            Value to pad the matrix with.

        Returns
        -------
        self
            Returns the matrix object to allow chaining.

        Examples
        --------
        >>> matrix = Matrix(2)
        >>> print(matrix)
        0 0
        0 0

        >>> print(matrix.pad_bottom(1, value=2))
        0 0
        0 0
        2 2

        """
        self.height += bottom

        for _ in range(abs(bottom)):
            if bottom >= 0:
                self.matrix.append([value for x in range(self.width)])
            else:
                self.matrix.pop()

        return self

    # pylint: disable=too-many-arguments
    def pad(self, top: int, right: int = None, bottom: int = None,
            left: int = None, value: Any = 0):
        """Pad the matrix.

        Parameters
        ----------
        top: int
            Amount of rows to add to the top of the matrix.
        right: int, optional
            Amount of columns to add to the right side of the matrix. If this
            is ``None`` then `right` will default to ``top``
        bottom: int, optional
            Amount of rows to add to the bottom of the matrix. If this is
            ``None`` then `bottom` will default to ``top``
        left: int, optional
            Amount of columns to add to the left side of the matrix. If this is
            ``None`` then `left` will default to right.
        value: `Any`, optional
            Value to pad the matrix with.

        Returns
        -------
        self
            Returns the matrix object to allow chaining.

        Examples
        --------
        >>> matrix = Matrix(2)
        >>> print(matrix.pad(1, value=2))
        2 2 2 2
        2 0 0 2
        2 0 0 2
        2 2 2 2

        >>> matrix = Matrix(2)
        >>> print(matrix.pad(1, 2, value=2))
        2 2 2 2 2 2
        2 2 0 0 2 2
        2 2 0 0 2 2
        2 2 2 2 2 2

        """

        if right is None:
            right = top

        self.pad_top(top, value)
        self.pad_bottom(bottom if (bottom is not None) else top, value)
        self.pad_right(right, value)
        self.pad_left(left if (left is not None) else right, value)

        return self

    def resize(self, width: int, height: int = None, value: Any = 0,
               center: bool = False):
        """Resize the matrix.

        Parameters
        ----------
        width: int
            Desired matrix width.
        height: int, optional
            Desired matrix height. Defaults to ``width`` if not specified.
        value: `Any`, optional
            Value to pad the matrix with if desired dimensions are greater than
            the current matrix.
        center: bool, optional
            Whether to resize relative to the center of the matrix. Default is
            ``False``.

        Returns
        -------
        self
            Returns the matrix object to allow chaining.

        Examples
        --------
        >>> matrix = Matrix(2)
        >>> print(matrix.pad(1, value=1))
        1 1 1 1
        1 0 0 1
        1 0 0 1
        1 1 1 1
        >>> print(matrix.resize(2, 2))
        1 1
        1 0

        >>> matrix = Matrix(2)
        >>> print(matrix.pad(1, value=1))
        1 1 1 1
        1 0 0 1
        1 0 0 1
        1 1 1 1
        >>> print(matrix.resize(2, 2, center=True))
        0 0
        0 0

        """
        if not height:
            height = width

        pad_width = width - self.width
        pad_height = height - self.height

        top = 0 if not center else math.floor(pad_height/2)
        bottom = pad_height if not center else math.ceil(pad_height/2)

        left = 0 if not center else math.floor(pad_width/2)
        right = pad_width if not center else math.ceil(pad_width/2)

        return self.pad(top, right, bottom, left, value)

    def fill_random(self, minimum: int = 0, maximum: int = 1):
        """Fill the matrix with random values.

        Parameters
        ----------
        minimum: int, optional
            Minimum (inclusive) bound for random value.
        maximum: int, optional
            Maximum (inclusive) bound for random value.

        Returns
        -------
        self
            Returns the matrix object to allow chaining.

        Examples
        --------
        >>> matrix = Matrix(2)
        >>> print(matrix.fill_random())
        1 0
        0 1
        # random

        """
        for y in range(self.height):
            for x in range(self.width):
                self[y][x] = random.randint(minimum, maximum)

        return self
