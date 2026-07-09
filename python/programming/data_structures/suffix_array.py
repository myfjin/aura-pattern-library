#!/usr/bin/env python3
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Tuple, Optional
import sys


class SuffixArray:
    """A class to build and query suffix arrays."""
    
    def __init__(self, text: str) -> None:
        """
        Initialize the suffix array with the given text.
        
        Args:
            text: The input string to build the suffix array for.
        """
        if not isinstance(text, str):
            raise TypeError("Text must be a string")
        
        self.text = text
        self.suffixes: List[int] = []
        self._build()
    
    def _build(self) -> None:
        """Build the suffix array using the naive O(n^2 log n) approach."""
        n = len(self.text)
        # Create list of (suffix, index) pairs
        suffix_array = [(self.text[i:], i) for i in range(n)]
        # Sort by suffixes
        suffix_array.sort()
        # Extract indices
        self.suffixes = [index for _, index in suffix_array]
    
    def __len__(self) -> int:
        """Return the length of the suffix array."""
        return len(self.suffixes)
    
    def __getitem__(self, index: int) -> int:
        """Get the suffix index at the given position."""
        return self.suffixes[index]
    
    def to_suffix(self, index: int) -> str:
        """
        Get the actual suffix string at the given suffix array index.
        
        Args:
            index: Position in the suffix array.
            
        Returns:
            The suffix string.
        """
        if index < 0 or index >= len(self.suffixes):
            raise IndexError("Index out of range")
        return self.text[self.suffixes[index]:]
    
    def search(self, pattern: str) -> List[int]:
        """
        Find all occurrences of a pattern in the text using binary search.
        
        Args:
            pattern: The pattern to search for.
            
        Returns:
            List of starting positions where the pattern occurs.
        """
        if not pattern:
            return []
        
        left = self._binary_search_left(pattern)
        right = self._binary_search_right(pattern)
        
        result = []
        for i in range(left, right):
            result.append(self.suffixes[i])
        return sorted(result)
    
    def _binary_search_left(self, pattern: str) -> int:
        """Find the leftmost position where pattern could be inserted."""
        low, high = 0, len(self.suffixes)
        while low < high:
            mid = (low + high) // 2
            suffix = self.text[self.suffixes[mid]:]
            if suffix.startswith(pattern):
                # Find the first occurrence
                high = mid
            elif suffix < pattern:
                low = mid + 1
            else:
                high = mid
        return low
    
    def _binary_search_right(self, pattern: str) -> int:
        """Find the rightmost position where pattern could be inserted."""
        low, high = 0, len(self.suffixes)
        while low < high:
            mid = (low + high) // 2
            suffix = self.text[self.suffixes[mid]:]
            if suffix.startswith(pattern):
                # Find the last occurrence
                low = mid + 1
            elif suffix < pattern:
                low = mid + 1
            else:
                high = mid
        return low


class LCPArray:
    """A class to build and query the LCP (Longest Common Prefix) array."""
    
    def __init__(self, text: str, suffix_array: SuffixArray) -> None:
        """
        Initialize the LCP array.
        
        Args:
            text: The input string.
            suffix_array: A precomputed suffix array for the text.
        """
        if not isinstance(text, str):
            raise TypeError("Text must be a string")
        
        self.text = text
        self.suffix_array = suffix_array
        self.lcp: List[int] = []
        self._build()
    
    def _build(self) -> None:
        """Build the LCP array using Kasai's algorithm."""
        n = len(self.text)
        if n == 0:
            self.lcp = []
            return
            
        # Create inverse suffix array
        inv_sa = [0] * n
        for i in range(n):
            inv_sa[self.suffix_array[i]] = i
        
        # Calculate LCP values
        self.lcp = [0] * n
        k = 0
        
        for i in range(n):
            if inv_sa[i] == n - 1:
                k = 0
                continue
            
            j = self.suffix_array[inv_sa[i] + 1]
            while i + k < n and j + k < n and self.text[i + k] == self.text[j + k]:
                k += 1
            
            self.lcp[inv_sa[i]] = k
            if k > 0:
                k -= 1
    
    def __len__(self) -> int:
        """Return the length of the LCP array."""
        return len(self.lcp)
    
    def __getitem__(self, index: int) -> int:
        """Get the LCP value at the given position."""
        return self.lcp[index]


class RMQ:
    """Range Minimum Query data structure for LCP array."""
    
    def __init__(self, lcp_array: LCPArray) -> None:
        """
        Initialize the RMQ structure.
        
        Args:
            lcp_array: The LCP array to build RMQ for.
        """
        self.lcp_array = lcp_array
        self.n = len(lcp_array)
        if self.n == 0:
            self.sparse_table = []
            return
            
        # Precompute sparse table for RMQ
        from math import log2, ceil
        self.log_n = int(ceil(log2(self.n))) if self.n > 0 else 0
        self.sparse_table = [[0] * self.log_n for _ in range(self.n)]
        
        # Initialize the first column
        for i in range(self.n):
            self.sparse_table[i][0] = i
        
        # Fill the rest of the table
        j = 1
        while (1 << j) <= self.n:
            i = 0
            while (i + (1 << j) - 1) < self.n:
                left = self.sparse_table[i][j - 1]
                right = self.sparse_table[i + (1 << (j - 1))][j - 1]
                self.sparse_table[i][j] = left if self.lcp_array[left] <= self.lcp_array[right] else right
                i += 1
            j += 1
    
    def query(self, left: int, right: int) -> int:
        """
        Find the position of the minimum element in the range [left, right].
        
        Args:
            left: Left boundary (inclusive).
            right: Right boundary (inclusive).
            
        Returns:
            Index of the minimum element in the LCP array.
        """
        if left > right or left < 0 or right >= self.n:
            raise ValueError("Invalid range")
        
        if left == right:
            return left
            
        from math import log2
        k = int(log2(right - left + 1))
        i = right - (1 << k) + 1
        
        left_min = self.sparse_table[left][k]
        right_min = self.sparse_table[i][k]
        
        return left_min if self.lcp_array[left_min] <= self.lcp_array[right_min] else right_min


def longest_common_substring(text1: str, text2: str) -> Tuple[str, List[Tuple[int, int]]]:
    """
    Find the longest common substring between two texts.
    
    Args:
        text1: First text.
        text2: Second text.
        
    Returns:
        Tuple of (longest substring, list of (pos1, pos2) positions).
    """
    # Create combined text with separator
    separator = chr(0)  # Use null character as separator
    combined = text1 + separator + text2
    sa = SuffixArray(combined)
    lcp = LCPArray(combined, sa)
    rmq = RMQ(lcp)
    
    max_len = 0
    positions = []
    
    # Find the longest common substring
    for i in range(len(lcp) - 1):
        # Check if suffixes belong to different texts
        pos1 = sa[i]
        pos2 = sa[i + 1]
        in_text1_1 = pos1 < len(text1)
        in_text1_2 = pos2 < len(text1)
        
        # Only consider if they are from different texts
        if in_text1_1 != in_text1_2 and lcp[i] > 0:
            if lcp[i] > max_len:
                max_len = lcp[i]
                positions = []
            if lcp[i] == max_len:
                # Adjust positions to be relative to original texts
                if in_text1_1:
                    positions.append((pos1, pos2 - len(text1) - 1))
                else:
                    positions.append((pos1 - len(text1) - 1, pos2))
    
    if max_len == 0:
        return ("", [])
    
    # Return the actual substring and positions
    first_pos = positions[0][0] if positions else 0
    substring = text1[first_pos:first_pos + max_len]
    return (substring, positions)


def main() -> None:
    """Demo the suffix array and LCP array functionality."""
    # Test text
    text = "banana"
    print(f"Text: {text}")
    
    # Build suffix array
    sa = SuffixArray(text)
    print("\nSuffix Array:")
    for i in range(len(sa)):
        print(f"SA[{i}] = {sa[i]} -> '{sa.to_suffix(i)}'")
    
    # Build LCP array
    lcp = LCPArray(text, sa)
    print("\nLCP Array:")
    for i in range(len(lcp)):
        print(f"LCP[{i}] = {lcp[i]}")
    
    # Test pattern search
    patterns = ["ana", "na", "ban", "xyz"]
    print("\nPattern Search:")
    for pattern in patterns:
        positions = sa.search(pattern)
        print(f"'{pattern}' found at positions: {positions}")
    
    # Test RMQ
    if len(lcp) > 0:
        rmq = RMQ(lcp)
        if len(lcp) >= 3:
            min_pos = rmq.query(1, 3)
            print(f"\nRMQ of LCP[1..3]: min at index {min_pos} with value {lcp[min_pos]}")
    
    # Test longest common substring
    print("\nLongest Common Substring:")
    text1 = "programming"
    text2 = "algorithm"
    substring, positions = longest_common_substring(text1, text2)
    print(f"LCS of '{text1}' and '{text2}': '{substring}' at {positions}")
    
    # Additional test case
    text1 = "abcdef"
    text2 = "cdefgh"
    substring, positions = longest_common_substring(text1, text2)
    print(f"LCS of '{text1}' and '{text2}': '{substring}' at {positions}")


if __name__ == "__main__":
    main()