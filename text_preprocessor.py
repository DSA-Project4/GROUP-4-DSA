"""
Text Preprocessing Engineer
============================
Handles text normalization and tokenization.

Responsibilities:
- Convert text to lowercase
- Remove punctuation
- Split text into tokens
"""

import re


class TextPreprocessor:
    def preprocess(self, text: str) -> list[str]:
        """
        Full pipeline: normalize and tokenize text.

        Args:
            text: Raw input string.

        Returns:
            List of clean lowercase tokens.
        """
        text = self.to_lowercase(text)
        text = self.remove_punctuation(text)
        tokens = self.tokenize(text)
        return tokens

    def to_lowercase(self, text: str) -> str:
        """Convert all characters in text to lowercase."""
        return text.lower()

    def remove_punctuation(self, text: str) -> str:
        """Remove all punctuation characters from text."""
        return re.sub(r'[^\w\s]', '', text)

    def tokenize(self, text: str) -> list[str]:
        """Split text into individual word tokens."""
        return text.split()


# ── Quick demo ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    preprocessor = TextPreprocessor()

    samples = [
        "Hello, World! This is a Search Engine.",
        "Data Structures & Algorithms are FUN!",
        "Python is great... isn't it?",
    ]

    for sample in samples:
        tokens = preprocessor.preprocess(sample)
        print(f"Input : {sample}")
        print(f"Tokens: {tokens}")
        print()
