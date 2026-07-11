#!/usr/bin/env python3
"""
Trie (Prefix Tree) implementation with autocomplete functionality.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import Dict, List, Optional, Set
import sys


class TrieNode:
    """
    A node in the Trie data structure.
    
    Each node contains:
    - children: mapping of character to child nodes
    - is_end_of_word: flag indicating if this node marks the end of a word
    - word_count: number of words that end at this node
    """
    
    def __init__(self) -> None:
        """Initialize a TrieNode with empty children and default values."""
        self.children: Dict[str, 'TrieNode'] = {}
        self.is_end_of_word: bool = False
        self.word_count: int = 0


class Trie:
    """
    Trie (Prefix Tree) data structure for efficient storage and retrieval of strings.
    
    Supports operations:
    - Insert words
    - Search for complete words
    - Check if any word starts with a prefix
    - Delete words
    - Autocomplete suggestions
    """
    
    def __init__(self) -> None:
        """Initialize an empty Trie with a root node."""
        self.root: TrieNode = TrieNode()
    
    def insert(self, word: str) -> None:
        """
        Insert a word into the Trie.
        
        Args:
            word: The word to insert (case-sensitive)
        """
        if not word:
            return
            
        current_node = self.root
        
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        
        current_node.is_end_of_word = True
        current_node.word_count += 1
    
    def search(self, word: str) -> bool:
        """
        Search for a complete word in the Trie.
        
        Args:
            word: The word to search for
            
        Returns:
            True if the word exists in the Trie, False otherwise
        """
        if not word:
            return False
            
        current_node = self.root
        
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        
        return current_node.is_end_of_word
    
    def starts_with(self, prefix: str) -> bool:
        """
        Check if any word in the Trie starts with the given prefix.
        
        Args:
            prefix: The prefix to check
            
        Returns:
            True if there's at least one word with the prefix, False otherwise
        """
        if not prefix:
            return True
            
        current_node = self.root
        
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        
        return True
    
    def delete(self, word: str) -> bool:
        """
        Delete a word from the Trie.
        
        Args:
            word: The word to delete
            
        Returns:
            True if the word was deleted, False if it didn't exist
        """
        if not word:
            return False
            
        def _delete_helper(node: TrieNode, word: str, index: int) -> bool:
            # Base case: reached the end of the word
            if index == len(word):
                # Word doesn't exist in the Trie
                if not node.is_end_of_word:
                    return False
                
                # Mark as not end of word and decrement count
                node.is_end_of_word = False
                node.word_count -= 1
                
                # Return True if node has no children (can be deleted)
                return len(node.children) == 0 and not node.is_end_of_word
            
            char = word[index]
            if char not in node.children:
                return False
            
            # Recursively delete from child node
            should_delete_child = _delete_helper(node.children[char], word, index + 1)
            
            # If child should be deleted, remove it
            if should_delete_child:
                del node.children[char]
                
                # Return True if current node can also be deleted
                return (len(node.children) == 0 and 
                        not node.is_end_of_word and 
                        node.word_count == 0)
            
            return False
        
        # (The former return `result or self.search(word)` reported False for
        # nearly every successful delete: `result` is only the node-pruning
        # signal, and search() is False precisely when deletion worked.)
        if not self.search(word):
            return False
        _delete_helper(self.root, word, 0)
        return True
    
    def autocomplete(self, prefix: str, max_suggestions: int = 10) -> List[str]:
        """
        Get autocomplete suggestions for a given prefix.
        
        Args:
            prefix: The prefix to find suggestions for
            max_suggestions: Maximum number of suggestions to return
            
        Returns:
            List of words that start with the given prefix
        """
        suggestions: List[str] = []
        
        if not prefix:
            return suggestions
            
        # Find the node corresponding to the prefix
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return suggestions
            current_node = current_node.children[char]
        
        # DFS to collect all words with the prefix
        def _dfs(node: TrieNode, current_word: str) -> None:
            if len(suggestions) >= max_suggestions:
                return
                
            if node.is_end_of_word:
                suggestions.append(current_word)
            
            for char, child_node in node.children.items():
                _dfs(child_node, current_word + char)
        
        _dfs(current_node, prefix)
        return suggestions


def main() -> None:
    """Self-test: exact membership/prefix/autocomplete sets, delete-a-prefix
    without harming longer words, and honest delete return values."""
    trie = Trie()
    words = ["apple", "app", "application", "apply", "apt",
             "banana", "band", "bandana", "bandit",
             "cat", "car", "card", "care", "careful",
             "dog", "door", "down", "download"]
    for word in words:
        trie.insert(word)

    # Membership is exact: whole words yes, prefixes-of-words no.
    for w in ("app", "apple", "bandana", "card"):
        assert trie.search(w) is True, f"inserted word {w!r} not found"
    for w in ("appl", "ban", "xyz", "downloads", ""):
        assert trie.search(w) is False, f"non-word {w!r} reported found"

    # Prefix checks.
    for p in ("app", "ban", "ca", "do"):
        assert trie.starts_with(p) is True
    assert trie.starts_with("xyz") is False
    assert trie.starts_with("") is True, "empty prefix must match everything"

    # Autocomplete returns exactly the words under the prefix.
    assert sorted(trie.autocomplete("app", 10)) == \
        ["app", "apple", "application", "apply"], "autocomplete('app') set wrong"
    assert sorted(trie.autocomplete("band", 10)) == ["band", "bandana", "bandit"]
    assert trie.autocomplete("xyz", 10) == []
    assert len(trie.autocomplete("ca", 2)) == 2, "max_suggestions cap not honored"

    # THE DELETE CONTRACT (the bug this test pins): deleting a word that is a
    # PREFIX of others must succeed, report True, and leave the longer words.
    assert trie.delete("app") is True, "successful delete reported False"
    assert trie.search("app") is False, "deleted word still found"
    assert trie.search("apple") is True and trie.search("application") is True, \
        "deleting a prefix destroyed longer words"
    assert sorted(trie.autocomplete("app", 10)) == ["apple", "application", "apply"]

    # Deleting a leaf-path word prunes without touching siblings.
    assert trie.delete("bandana") is True
    assert trie.search("bandana") is False
    assert trie.search("band") is True and trie.search("bandit") is True

    # Deleting the unknown/already-deleted reports False.
    assert trie.delete("xyz") is False, "deleting a missing word reported success"
    assert trie.delete("app") is False, "double delete reported success"
    assert trie.delete("") is False

    # Insert after delete works (no poisoned nodes on the pruned path).
    trie.insert("bandana")
    assert trie.search("bandana") is True

    # 16 of the original 18 words remain intact (app deleted; bandana re-added).
    survivors = sum(1 for w in words if trie.search(w))
    assert survivors == 17, f"expected 17 surviving words, found {survivors}"

    print("trie: exact sets for search/prefix/autocomplete, prefix-delete safe, "
          "delete returns honest True/False, 17/18 survivors — PASS")


if __name__ == "__main__":
    main()