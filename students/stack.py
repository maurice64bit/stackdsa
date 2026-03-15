"""ADT Stack implementation for the student register.

This module provides a Stack class that stores student records (name + ID).

Space complexity:
- O(n) where n is the number of students in the stack (each student record is stored in memory).

Time complexity (per operation):
- push: O(1)
- pop: O(1)
- peek: O(1)
- is_empty: O(1)
- size: O(1)
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional


class Stack:
    """Simple stack implementation using a Python list."""

    def __init__(self, items: Optional[List[Dict[str, Any]]] = None) -> None:
        self._items: List[Dict[str, Any]] = items or []

    def push(self, value: Dict[str, Any]) -> None:
        """Push a value onto the stack."""
        self._items.append(value)

    def pop(self) -> Optional[Dict[str, Any]]:
        """Pop the top value. Returns None if stack is empty."""
        if self.is_empty():
            return None
        return self._items.pop()

    def peek(self) -> Optional[Dict[str, Any]]:
        """Return the top value without removing it."""
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self) -> bool:
        """Return True if the stack is empty."""
        return len(self._items) == 0

    def size(self) -> int:
        """Return number of items in the stack."""
        return len(self._items)

    def to_list(self) -> List[Dict[str, Any]]:
        """Return a shallow copy of stack contents."""
        return list(self._items)


# Constants describing the stack's theoretical complexity (for display, teaching, etc.)
SPACE_COMPLEXITY = "O(n)"
TIME_COMPLEXITIES = {
    "push": "O(1)",
    "pop": "O(1)",
    "peek": "O(1)",
    "is_empty": "O(1)",
    "size": "O(1)",
}
