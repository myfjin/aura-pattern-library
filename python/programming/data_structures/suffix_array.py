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
                # Adjust positions to be relative to original texts,
                # always as (text1_pos, text2_pos) — the substring is
                # extracted from text1 via the FIRST coordinate, so the
                # former swapped order returned garbage substrings.
                if in_text1_1:
                    positions.append((pos1, pos2 - len(text1) - 1))
                else:
                    positions.append((pos2, pos1 - len(text1) - 1))
    
    if max_len == 0:
        return ("", [])
    
    # Return the actual substring and positions
    first_pos = positions[0][0] if positions else 0
    substring = text1[first_pos:first_pos + max_len]
    return (substring, positions)


def main() -> None:
    """Self-test: the classical banana truths, Kasai LCP vs direct comparison,
    pattern search vs brute-force, and LCS on planted overlaps."""
    import random
    random.seed(42)

    # "banana": the textbook suffix array is [5, 3, 1, 0, 4, 2].
    sa = SuffixArray("banana")
    assert sa.suffixes == [5, 3, 1, 0, 4, 2], f"banana SA wrong: {sa.suffixes}"
    assert sa.to_suffix(0) == "a" and sa.to_suffix(3) == "banana"

    # Kasai LCP for banana: [1, 3, 0, 0, 2, 0] (lcp[i] = LCP(SA[i], SA[i+1])).
    lcp = LCPArray("banana", sa)
    assert lcp.lcp == [1, 3, 0, 0, 2, 0], f"banana LCP wrong: {lcp.lcp}"

    # Pattern search: exact position sets.
    assert sorted(sa.search("ana")) == [1, 3]
    assert sorted(sa.search("na")) == [2, 4]
    assert sa.search("ban") == [0]
    assert sa.search("xyz") == []
    assert sorted(sa.search("a")) == [1, 3, 5]

    # RMQ over LCP[1..3] = [3, 0, 0]: the minimum VALUE must be 0.
    rmq = RMQ(lcp)
    assert lcp[rmq.query(1, 3)] == 0, "RMQ failed to find the 0 in [3,0,0]"
    assert lcp[rmq.query(0, 1)] == 1, "RMQ of [1,3] must return value 1"

    # Oracle fuzz on a random 120-char 'ab' string: SA vs sorted-suffix truth,
    # every adjacent LCP vs direct character comparison, search vs brute force.
    text = "".join(random.choice("ab") for _ in range(120))
    fsa = SuffixArray(text)
    assert fsa.suffixes == sorted(range(120), key=lambda i: text[i:]), \
        "SA diverged from sorted-suffix oracle"
    flcp = LCPArray(text, fsa)
    for i in range(119):
        s1, s2 = text[fsa[i]:], text[fsa[i + 1]:]
        true_lcp = 0
        while true_lcp < min(len(s1), len(s2)) and s1[true_lcp] == s2[true_lcp]:
            true_lcp += 1
        assert flcp[i] == true_lcp, f"LCP[{i}] = {flcp[i]}, direct comparison {true_lcp}"
    for _ in range(20):
        plen = random.randint(1, 6)
        start = random.randint(0, 120 - plen)
        pat = text[start:start + plen]
        want = [i for i in range(120 - plen + 1) if text[i:i + plen] == pat]
        assert sorted(fsa.search(pat)) == want, f"search({pat!r}) diverged from brute force"

    # Longest common substring on a planted 4-char overlap.
    substring, positions = longest_common_substring("abcdef", "cdefgh")
    assert substring == "cdef", f"LCS of abcdef/cdefgh must be 'cdef', got {substring!r}"
    assert (2, 0) in positions, f"LCS position (2,0) missing: {positions}"
    # Disjoint alphabets share nothing.
    assert longest_common_substring("aaa", "bbb") == ("", [])
    # programming/algorithm share only single characters.
    s, _ = longest_common_substring("programming", "algorithm")
    assert len(s) == 1 and s in "programming" and s in "algorithm", \
        f"LCS of programming/algorithm must be a single shared char, got {s!r}"

    # Refusal: non-string input.
    try:
        SuffixArray(42)  # type: ignore[arg-type]
        assert False, "non-string text accepted"
    except TypeError:
        pass

    print("suffix_array: banana SA [5,3,1,0,4,2] + LCP [1,3,0,0,2,0] exact, "
          "120-char oracle (SA/LCP/search) agreed, LCS 'cdef' planted — PASS")


if __name__ == "__main__":
    main()