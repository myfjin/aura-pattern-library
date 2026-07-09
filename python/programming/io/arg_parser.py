#!/usr/bin/env python3
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import sys
from typing import List, Dict, Optional, Union, Callable, Any


class Option:
    """Represents a command-line option (flag or argument)."""
    
    def __init__(
        self,
        name: str,
        short_name: Optional[str] = None,
        long_name: Optional[str] = None,
        help_text: str = "",
        default: Any = None,
        action: str = "store",
        required: bool = False,
        nargs: Union[int, str] = 1,
    ):
        """
        Initialize an Option.
        
        Args:
            name: Internal name for the option
            short_name: Short form (e.g., '-v')
            long_name: Long form (e.g., '--verbose')
            help_text: Help description
            default: Default value
            action: 'store', 'store_true', or 'store_false'
            required: Whether option is required
            nargs: Number of arguments (int or '*' for any)
        """
        self.name = name
        self.short_name = short_name
        self.long_name = long_name
        self.help_text = help_text
        self.default = default
        self.action = action
        self.required = required
        self.nargs = nargs
        self.value: Any = default
        
    def __repr__(self) -> str:
        return f"Option(name={self.name}, short={self.short_name}, long={self.long_name})"


class Argument:
    """Represents a positional argument."""
    
    def __init__(
        self,
        name: str,
        help_text: str = "",
        default: Any = None,
        required: bool = True,
        nargs: Union[int, str] = 1,
    ):
        """
        Initialize an Argument.
        
        Args:
            name: Name of the argument
            help_text: Help description
            default: Default value
            required: Whether argument is required
            nargs: Number of arguments (int or '*' for any)
        """
        self.name = name
        self.help_text = help_text
        self.default = default
        self.required = required
        self.nargs = nargs
        self.value: Any = default
        
    def __repr__(self) -> str:
        return f"Argument(name={self.name})"


class ArgParser:
    """Simple command-line argument parser."""
    
    def __init__(self, description: str = ""):
        """
        Initialize the argument parser.
        
        Args:
            description: Program description
        """
        self.description = description
        self.options: Dict[str, Option] = {}
        self.arguments: List[Argument] = []
        self.parsed_args: Dict[str, Any] = {}
        
    def add_option(
        self,
        name: str,
        short_name: Optional[str] = None,
        long_name: Optional[str] = None,
        help_text: str = "",
        default: Any = None,
        action: str = "store",
        required: bool = False,
        nargs: Union[int, str] = 1,
    ) -> None:
        """
        Add an option to the parser.
        
        Args:
            name: Internal name for the option
            short_name: Short form (e.g., '-v')
            long_name: Long form (e.g., '--verbose')
            help_text: Help description
            default: Default value
            action: 'store', 'store_true', or 'store_false'
            required: Whether option is required
            nargs: Number of arguments (int or '*' for any)
        """
        if short_name and not short_name.startswith('-'):
            short_name = f"-{short_name}"
        if long_name and not long_name.startswith('--'):
            long_name = f"--{long_name}"
            
        option = Option(
            name, short_name, long_name, help_text, 
            default, action, required, nargs
        )
        self.options[name] = option
        
    def add_argument(
        self,
        name: str,
        help_text: str = "",
        default: Any = None,
        required: bool = True,
        nargs: Union[int, str] = 1,
    ) -> None:
        """
        Add a positional argument to the parser.
        
        Args:
            name: Name of the argument
            help_text: Help description
            default: Default value
            required: Whether argument is required
            nargs: Number of arguments (int or '*' for any)
        """
        arg = Argument(name, help_text, default, required, nargs)
        self.arguments.append(arg)
        
    def parse_args(self, args: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Parse command-line arguments.
        
        Args:
            args: List of arguments (defaults to sys.argv[1:])
            
        Returns:
            Dictionary of parsed arguments
            
        Raises:
            ValueError: If arguments are invalid
        """
        if args is None:
            args = sys.argv[1:]
            
        # Initialize with defaults
        result: Dict[str, Any] = {}
        
        # Set defaults for options
        for name, option in self.options.items():
            result[name] = option.default
            if option.action in ("store_true", "store_false"):
                result[name] = option.default if option.default is not None else (
                    True if option.action == "store_true" else False
                )
                
        # Set defaults for arguments
        for arg in self.arguments:
            result[arg.name] = arg.default
            
        # Handle help
        if "-h" in args or "--help" in args:
            self.print_help()
            sys.exit(0)
            
        # Parse options
        i = 0
        while i < len(args):
            arg = args[i]
            
            # Check if it's an option
            if arg.startswith('-'):
                matched = False
                for name, option in self.options.items():
                    if arg in (option.short_name, option.long_name):
                        matched = True
                        
                        if option.action == "store":
                            if option.nargs == 1:
                                if i + 1 >= len(args) or args[i+1].startswith('-'):
                                    raise ValueError(f"Option {arg} requires an argument")
                                result[name] = args[i+1]
                                i += 2
                            elif option.nargs == '*':
                                values = []
                                j = i + 1
                                while j < len(args) and not args[j].startswith('-'):
                                    values.append(args[j])
                                    j += 1
                                if not values:
                                    raise ValueError(f"Option {arg} requires at least one argument")
                                result[name] = values
                                i = j
                            else:  # nargs is integer
                                values = []
                                for j in range(option.nargs):
                                    if i + 1 + j >= len(args) or args[i+1+j].startswith('-'):
                                        raise ValueError(f"Option {arg} requires {option.nargs} arguments")
                                    values.append(args[i+1+j])
                                result[name] = values if len(values) > 1 else values[0]
                                i += 1 + option.nargs
                        else:  # store_true or store_false
                            result[name] = not (option.action == "store_false")
                            i += 1
                        break
                        
                if not matched:
                    raise ValueError(f"Unrecognized option: {arg}")
            else:
                i += 1
                
        # Parse positional arguments
        positional_args = [arg for arg in args if not arg.startswith('-')]
        arg_idx = 0
        
        for arg_def in self.arguments:
            if arg_idx >= len(positional_args):
                if arg_def.required:
                    raise ValueError(f"Missing required argument: {arg_def.name}")
                continue
                
            if arg_def.nargs == 1:
                result[arg_def.name] = positional_args[arg_idx]
                arg_idx += 1
            elif arg_def.nargs == '*':
                result[arg_def.name] = positional_args[arg_idx:]
                arg_idx = len(positional_args)
            else:  # nargs is integer
                if arg_idx + arg_def.nargs > len(positional_args):
                    raise ValueError(f"Not enough values for argument {arg_def.name}")
                values = positional_args[arg_idx:arg_idx + arg_def.nargs]
                result[arg_def.name] = values if len(values) > 1 else values[0]
                arg_idx += arg_def.nargs
                
        # Check required options
        for name, option in self.options.items():
            if option.required and result[name] == option.default:
                raise ValueError(f"Missing required option: {option.long_name or option.short_name}")
                
        self.parsed_args = result
        return result.copy()
        
    def print_help(self) -> None:
        """Print help message."""
        print(f"Usage: {sys.argv[0]}", end="")
        
        # Print options usage
        optional_parts = []
        for option in self.options.values():
            if option.required:
                part = ""
                if option.short_name:
                    part += f" {option.short_name}"
                if option.long_name:
                    part += f" {option.long_name}"
                if option.action == "store":
                    if option.nargs == 1:
                        part += f" {option.name.upper()}"
                    elif option.nargs == '*':
                        part += f" {option.name.upper()}..."
                    else:
                        part += f" {option.name.upper()}" * option.nargs
                optional_parts.append(part.strip())
                
        if optional_parts:
            print(" " + " ".join(optional_parts), end="")
            
        # Print arguments usage
        for arg in self.arguments:
            if arg.required:
                if arg.nargs == 1:
                    print(f" {arg.name.upper()}", end="")
                elif arg.nargs == '*':
                    print(f" {arg.name.upper()}...", end="")
                else:
                    print(f" {arg.name.upper()}" * arg.nargs, end="")
            else:
                if arg.nargs == 1:
                    print(f" [{arg.name.upper()}]", end="")
                elif arg.nargs == '*':
                    print(f" [{arg.name.upper()}...]", end="")
                else:
                    print(f" [{arg.name.upper()}]" * arg.nargs, end="")
                    
        print()  # Newline
        
        if self.description:
            print(f"\n{self.description}\n")
            
        # Print arguments
        if self.arguments:
            print("Positional arguments:")
            for arg in self.arguments:
                req_str = " (required)" if arg.required else " (optional)"
                print(f"  {arg.name:<15} {arg.help_text}{req_str}")
            print()
            
        # Print options
        if self.options:
            print("Optional arguments:")
            # Add help option
            print("  -h, --help      Show this help message and exit")
            for option in self.options.values():
                names = []
                if option.short_name:
                    names.append(option.short_name)
                if option.long_name:
                    names.append(option.long_name)
                name_str = ", ".join(names)
                
                help_parts = [option.help_text]
                if option.default is not None and option.action == "store":
                    help_parts.append(f"(default: {option.default})")
                elif option.action in ("store_true", "store_false"):
                    help_parts.append(f"({option.action})")
                    
                if not option.required:
                    help_parts.append("(optional)")
                    
                print(f"  {name_str:<15} {' '.join(help_parts)}")
            print()


def main():
    """Demo the argument parser."""
    # Create parser
    parser = ArgParser(description="A simple demo of the argument parser")
    
    # Add options
    parser.add_option(
        "verbose", 
        short_name="-v", 
        long_name="--verbose",
        help_text="Enable verbose output",
        action="store_true"
    )
    
    parser.add_option(
        "output", 
        short_name="-o", 
        long_name="--output",
        help_text="Output file name",
        default="output.txt"
    )
    
    parser.add_option(
        "numbers",
        short_name="-n",
        long_name="--numbers",
        help_text="List of numbers",
        nargs="*"
    )
    
    parser.add_option(
        "quiet",
        short_name="-q",
        long_name="--quiet",
        help_text="Suppress output",
        action="store_true"
    )
    
    # Add required option
    parser.add_option(
        "format",
        short_name="-f",
        long_name="--format",
        help_text="Output format",
        required=True
    )
    
    # Add positional arguments
    parser.add_argument(
        "input_file",
        help_text="Input file to process"
    )
    
    parser.add_argument(
        "multiplier",
        help_text="Value multiplier",
        nargs=1
    )
    
    parser.add_argument(
        "optional_args",
        help_text="Optional additional arguments",
        required=False,
        nargs="*"
    )
    
    # Test cases
    test_cases = [
        ["-f", "json", "data.txt", "2"],
        ["--format", "xml", "-v", "input.txt", "3", "extra1", "extra2"],
        ["-f", "csv", "-o", "result.csv", "-n", "1", "2", "3", "data.txt", "5"],
        ["-h"],
        ["--help"]
    ]
    
    for i, test_args in enumerate(test_cases):
        if "help" in test_args or "-h" in test_args:
            continue  # Skip help as it exits
            
        print(f"\n--- Test Case {i+1}: {' '.join(test_args)} ---")
        try:
            result = parser.parse_args(test_args)
            for key, value in result.items():
                print(f"  {key}: {value}")
        except ValueError as e:
            print(f"  Error: {e}")
        except SystemExit:
            pass  # Handle help exit


if __name__ == "__main__":
    main()