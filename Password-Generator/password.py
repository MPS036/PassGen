"""
Password generation and strength utilities.

This module provides:
- Secure password generation using `secrets`
- Shannon-style entropy estimation (bits)
- Simple strength categories based on entropy thresholds
"""

from enum import IntEnum
from math import log2
import secrets

class StrengthToEntropy(IntEnum):
    """
    Password strength categories mapped to minimum entropy thresholds (bits).
    """
    Pathetic = 0
    Weak = 30
    Good = 50
    Strong = 70
    Excellent = 120

def create_new(length: int, characters: str) -> str:
    """
    Generate a new password using cryptographically secure randomness.

    Args:
        length: Desired password length.
        characters: String of allowed characters.

    Returns:
        Generated password.

    Raises:
        ValueError: If `length` is negative or `characters` is empty.
    """
    if length < 0:
        raise ValueError("length must be >= 0")
    if not characters:
        raise ValueError("characters set is empty")
    return "".join(secrets.choice(characters) for _ in range(length))

def get_entropy(length: int, character_number: int) -> float:
    """
    Estimate password entropy in bits.

    Entropy is estimated as:
        H = length * log2(character_number)

    Args:
        length: Password length.
        character_number: Size of the allowed character set.

    Returns:
        Entropy value in bits (rounded to 2 decimals). Returns 0.0 if invalid.
    """
    try:
        entropy = length * log2(character_number)
    except ValueError:
        return 0.0
    return round(entropy, 2)
