"""
Simple INI file parser module.

This module provides functionality to parse, manipulate, and write INI files.
It supports typed value retrieval and setting, section management, and default sections.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import Any, Dict, List, Optional, Union
import re


class Section:
    """Represents a section in an INI file."""
    
    def __init__(self, name: str) -> None:
        """Initialize a section with a name."""
        self.name = name
        self._values: Dict[str, str] = {}
    
    def get(self, key: str, default: Optional[str] = None) -> Optional[str]:
        """Get a string value by key."""
        return self._values.get(key, default)
    
    def get_int(self, key: str, default: Optional[int] = None) -> Optional[int]:
        """Get an integer value by key."""
        value = self.get(key)
        if value is None:
            return default
        try:
            return int(value)
        except ValueError:
            return default
    
    def get_float(self, key: str, default: Optional[float] = None) -> Optional[float]:
        """Get a float value by key."""
        value = self.get(key)
        if value is None:
            return default
        try:
            return float(value)
        except ValueError:
            return default
    
    def get_bool(self, key: str, default: Optional[bool] = None) -> Optional[bool]:
        """Get a boolean value by key."""
        value = self.get(key)
        if value is None:
            return default
        return value.lower() in ('1', 'true', 'yes', 'on')
    
    def set(self, key: str, value: Union[str, int, float, bool]) -> None:
        """Set a value for a key."""
        if isinstance(value, bool):
            self._values[key] = str(value).lower()
        else:
            self._values[key] = str(value)
    
    def keys(self) -> List[str]:
        """Get all keys in this section."""
        return list(self._values.keys())
    
    def items(self) -> Dict[str, str]:
        """Get all key-value pairs in this section."""
        return self._values.copy()
    
    def remove(self, key: str) -> bool:
        """Remove a key from this section. Returns True if key existed."""
        if key in self._values:
            del self._values[key]
            return True
        return False


class INIParser:
    """Simple INI file parser."""
    
    def __init__(self) -> None:
        """Initialize an empty INI parser."""
        self._sections: Dict[str, Section] = {}
        self._default_section = Section("")
        self._sections[""] = self._default_section
    
    def add_section(self, name: str) -> Section:
        """Add a new section and return it."""
        if name in self._sections:
            raise ValueError(f"Section '{name}' already exists")
        section = Section(name)
        self._sections[name] = section
        return section
    
    def get_section(self, name: str) -> Optional[Section]:
        """Get a section by name."""
        return self._sections.get(name)
    
    def has_section(self, name: str) -> bool:
        """Check if a section exists."""
        return name in self._sections
    
    def remove_section(self, name: str) -> bool:
        """Remove a section. Returns True if section existed."""
        if name in self._sections and name != "":
            del self._sections[name]
            return True
        return False
    
    def sections(self) -> List[str]:
        """Get all section names except the default section."""
        return [name for name in self._sections.keys() if name != ""]
    
    def get(self, key: str, section: str = "", default: Optional[str] = None) -> Optional[str]:
        """Get a string value from a section."""
        sec = self._sections.get(section)
        if sec is None:
            return default
        return sec.get(key, default)
    
    def get_int(self, key: str, section: str = "", default: Optional[int] = None) -> Optional[int]:
        """Get an integer value from a section."""
        sec = self._sections.get(section)
        if sec is None:
            return default
        return sec.get_int(key, default)
    
    def get_float(self, key: str, section: str = "", default: Optional[float] = None) -> Optional[float]:
        """Get a float value from a section."""
        sec = self._sections.get(section)
        if sec is None:
            return default
        return sec.get_float(key, default)
    
    def get_bool(self, key: str, section: str = "", default: Optional[bool] = None) -> Optional[bool]:
        """Get a boolean value from a section."""
        sec = self._sections.get(section)
        if sec is None:
            return default
        return sec.get_bool(key, default)
    
    def set(self, key: str, value: Union[str, int, float, bool], section: str = "") -> None:
        """Set a value in a section."""
        if section not in self._sections:
            self.add_section(section)
        self._sections[section].set(key, value)
    
    def parse(self, content: str) -> None:
        """Parse INI content from a string."""
        current_section = self._default_section
        section_pattern = re.compile(r"^\[([^\]]+)\]$")
        key_value_pattern = re.compile(r"^([^=]+)=(.*)$")
        
        for line_num, line in enumerate(content.splitlines(), 1):
            line = line.strip()
            
            # Skip empty lines and comments
            if not line or line.startswith(";") or line.startswith("#"):
                continue
            
            # Check for section header
            section_match = section_pattern.match(line)
            if section_match:
                section_name = section_match.group(1).strip()
                if section_name not in self._sections:
                    self._sections[section_name] = Section(section_name)
                current_section = self._sections[section_name]
                continue
            
            # Check for key-value pair
            kv_match = key_value_pattern.match(line)
            if kv_match:
                key = kv_match.group(1).strip()
                value = kv_match.group(2).strip()
                # Remove quotes if present
                if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
                    value = value[1:-1]
                current_section._values[key] = value
                continue
            
            # If we get here, it's an invalid line
            raise ValueError(f"Invalid line {line_num}: {line}")
    
    def dumps(self) -> str:
        """Convert the INI data to a string."""
        lines = []
        
        # Process default section first if it has values
        if self._default_section._values:
            for key, value in self._default_section._values.items():
                lines.append(f"{key}={value}")
            lines.append("")  # Empty line after default section
        
        # Process other sections
        for name, section in self._sections.items():
            if name == "":  # Skip default section as it's already handled
                continue
            lines.append(f"[{name}]")
            for key, value in section._values.items():
                lines.append(f"{key}={value}")
            lines.append("")  # Empty line after each section
        
        # Remove the last empty line if it exists
        if lines and lines[-1] == "":
            lines.pop()
        
        return "\n".join(lines)


if __name__ == "__main__":
    # Demo the INI parser
    ini_content = """
; This is a comment
key1=value1
key2=123
key3=45.67
key4=true

[section1]
name=example
count=42
enabled=true
price=99.99

[section2]
host=localhost
port=8080
debug=false
"""

    # Parse the content
    parser = INIParser()
    parser.parse(ini_content)
    
    # Test default section access
    print("Default section values:")
    print(f"key1: {parser.get('key1')}")
    print(f"key2 (as int): {parser.get_int('key2')}")
    print(f"key3 (as float): {parser.get_float('key3')}")
    print(f"key4 (as bool): {parser.get_bool('key4')}")
    print()
    
    # Test section access
    print("Section1 values:")
    section1 = parser.get_section("section1")
    if section1:
        print(f"name: {section1.get('name')}")
        print(f"count (as int): {section1.get_int('count')}")
        print(f"enabled (as bool): {section1.get_bool('enabled')}")
        print(f"price (as float): {section1.get_float('price')}")
    print()
    
    # Test section2
    print("Section2 values:")
    section2 = parser.get_section("section2")
    if section2:
        print(f"host: {section2.get('host')}")
        print(f"port (as int): {section2.get_int('port')}")
        print(f"debug (as bool): {section2.get_bool('debug')}")
    print()
    
    # Test sections listing
    print(f"Sections: {parser.sections()}")
    print()
    
    # Test adding new values
    print("Adding new values:")
    parser.set("new_key", "new_value")
    parser.set("new_int", 999)
    parser.set("new_bool", True, "section1")
    print(f"new_key in default section: {parser.get('new_key')}")
    print(f"new_int in default section: {parser.get_int('new_int')}")
    print(f"new_bool in section1: {parser.get_bool('new_bool', 'section1')}")
    print()
    
    # Test serialization
    print("Serialized INI content:")
    print(parser.dumps())