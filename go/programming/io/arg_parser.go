package main

import (
	"fmt"
	"os"
	"sort"
	"strings"
)

// Option represents a command-line option (flag or argument).
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type Option struct {
	Name      string
	ShortName string
	LongName  string
	HelpText  string
	Default   interface{}
	Action    string
	Required  bool
	Nargs     interface{} // int or string "*"
	Value     interface{}
}

// NewOption initializes an Option.
func NewOption(name, shortName, longName, helpText string, def interface{}, action string, required bool, nargs interface{}) *Option {
	return &Option{
		Name:      name,
		ShortName: normalizeShort(shortName),
		LongName:  normalizeLong(longName),
		HelpText:  helpText,
		Default:   def,
		Action:    action,
		Required:  required,
		Nargs:     nargs,
		Value:     def,
	}
}

func normalizeShort(s string) string {
	if s != "" && !strings.HasPrefix(s, "-") {
		return "-" + s
	}
	return s
}

func normalizeLong(s string) string {
	if s != "" && !strings.HasPrefix(s, "--") {
		return "--" + s
	}
	return s
}

// Argument represents a positional argument.
type Argument struct {
	Name     string
	HelpText string
	Default  interface{}
	Required bool
	Nargs    interface{} // int or string "*"
	Value    interface{}
}

// NewArgument initializes an Argument.
func NewArgument(name, helpText string, def interface{}, required bool, nargs interface{}) *Argument {
	return &Argument{
		Name:     name,
		HelpText: helpText,
		Default:  def,
		Required: required,
		Nargs:    nargs,
		Value:    def,
	}
}

// ArgParser is a simple command-line argument parser.
type ArgParser struct {
	Description string
	Options     map[string]*Option
	Arguments   []*Argument
	ParsedArgs  map[string]interface{}
}

// NewArgParser initializes the argument parser.
func NewArgParser(description string) *ArgParser {
	return &ArgParser{
		Description: description,
		Options:     make(map[string]*Option),
		Arguments:   make([]*Argument, 0),
		ParsedArgs:  make(map[string]interface{}),
	}
}

// AddOption adds an option to the parser.
func (p *ArgParser) AddOption(name, shortName, longName, helpText string, def interface{}, action string, required bool, nargs interface{}) {
	option := NewOption(name, shortName, longName, helpText, def, action, required, nargs)
	p.Options[name] = option
}

// AddArgument adds a positional argument to the parser.
func (p *ArgParser) AddArgument(name, helpText string, def interface{}, required bool, nargs interface{}) {
	arg := NewArgument(name, helpText, def, required, nargs)
	p.Arguments = append(p.Arguments, arg)
}

// ParseArgs parses command-line arguments.
func (p *ArgParser) ParseArgs(args []string) (map[string]interface{}, error) {
	if args == nil {
		args = os.Args[1:]
	}

	result := make(map[string]interface{})

	// Set defaults for options
	for name, option := range p.Options {
		if option.Action == "store_true" {
			result[name] = false
		} else if option.Action == "store_false" {
			result[name] = true
		} else {
			result[name] = option.Default
		}
	}

	// Set defaults for arguments
	for _, arg := range p.Arguments {
		result[arg.Name] = arg.Default
	}

	// Handle help
	for _, a := range args {
		if a == "-h" || a == "--help" {
			p.PrintHelp()
			os.Exit(0)
		}
	}

	// Parse options
	i := 0
	for i < len(args) {
		arg := args[i]

		if strings.HasPrefix(arg, "-") {
			matched := false
			for name, option := range p.Options {
				if arg == option.ShortName || arg == option.LongName {
					matched = true

					if option.Action == "store" {
						nargs := option.Nargs
						switch v := nargs.(type) {
						case int:
							if v == 1 {
								if i+1 >= len(args) || strings.HasPrefix(args[i+1], "-") {
									return nil, fmt.Errorf("Option %s requires an argument", arg)
								}
								result[name] = args[i+1]
								i += 2
							} else {
								values := []string{}
								for j := 0; j < v; j++ {
									if i+1+j >= len(args) || strings.HasPrefix(args[i+1+j], "-") {
										return nil, fmt.Errorf("Option %s requires %d arguments", arg, v)
									}
									values = append(values, args[i+1+j])
								}
								if len(values) == 1 {
									result[name] = values[0]
								} else {
									result[name] = values
								}
								i += 1 + v
							}
						case string:
							if v == "*" {
								values := []string{}
								j := i + 1
								for j < len(args) && !strings.HasPrefix(args[j], "-") {
									values = append(values, args[j])
									j++
								}
								if len(values) == 0 {
									return nil, fmt.Errorf("Option %s requires at least one argument", arg)
								}
								result[name] = values
								i = j
							} else {
								return nil, fmt.Errorf("Unrecognized nargs value for option %s", arg)
							}
						default:
							return nil, fmt.Errorf("Unrecognized nargs type for option %s", arg)
						}
					} else {
						if option.Action == "store_true" {
							result[name] = true
						} else if option.Action == "store_false" {
							result[name] = false
						}
						i++
					}
					break
				}
			}
			if !matched {
				return nil, fmt.Errorf("Unrecognized option: %s", arg)
			}
		} else {
			i++
		}
	}

	// Parse positional arguments
	positionalArgs := []string{}
	for _, a := range args {
		if !strings.HasPrefix(a, "-") {
			positionalArgs = append(positionalArgs, a)
		}
	}
	argIdx := 0

	for _, argDef := range p.Arguments {
		if argIdx >= len(positionalArgs) {
			if argDef.Required {
				return nil, fmt.Errorf("Missing required argument: %s", argDef.Name)
			}
			continue
		}

		switch v := argDef.Nargs.(type) {
		case int:
			if v == 1 {
				result[argDef.Name] = positionalArgs[argIdx]
				argIdx++
			} else {
				if argIdx+v > len(positionalArgs) {
					return nil, fmt.Errorf("Not enough values for argument %s", argDef.Name)
				}
				values := positionalArgs[argIdx : argIdx+v]
				if len(values) == 1 {
					result[argDef.Name] = values[0]
				} else {
					result[argDef.Name] = values
				}
				argIdx += v
			}
		case string:
			if v == "*" {
				result[argDef.Name] = positionalArgs[argIdx:]
				argIdx = len(positionalArgs)
			}
		default:
			return nil, fmt.Errorf("Unrecognized nargs type for argument %s", argDef.Name)
		}
	}

	// Check required options
	for name, option := range p.Options {
		if option.Required {
			if result[name] == option.Default {
				key := option.LongName
				if key == "" {
					key = option.ShortName
				}
				return nil, fmt.Errorf("Missing required option: %s", key)
			}
		}
	}

	p.ParsedArgs = result
	return result, nil
}

// PrintHelp prints help message.
func (p *ArgParser) PrintHelp() {
	fmt.Printf("Usage: %s", os.Args[0])

	optionalParts := []string{}
	for _, option := range p.Options {
		if option.Required {
			part := ""
			if option.ShortName != "" {
				part += " " + option.ShortName
			}
			if option.LongName != "" {
				part += " " + option.LongName
			}
			if option.Action == "store" {
				switch v := option.Nargs.(type) {
				case int:
					if v == 1 {
						part += " " + strings.ToUpper(option.Name)
					} else {
						for j := 0; j < v; j++ {
							part += " " + strings.ToUpper(option.Name)
						}
					}
				case string:
					if v == "*" {
						part += " " + strings.ToUpper(option.Name) + "..."
					}
				}
			}
			optionalParts = append(optionalParts, strings.TrimSpace(part))
		}
	}

	if len(optionalParts) > 0 {
		fmt.Printf(" %s", strings.Join(optionalParts, " "))
	}

	for _, arg := range p.Arguments {
		if arg.Required {
			switch v := arg.Nargs.(type) {
			case int:
				if v == 1 {
					fmt.Printf(" %s", strings.ToUpper(arg.Name))
				} else {
					for j := 0; j < v; j++ {
						fmt.Printf(" %s", strings.ToUpper(arg.Name))
					}
				}
			case string:
				if v == "*" {
					fmt.Printf(" %s...", strings.ToUpper(arg.Name))
				}
			}
		} else {
			switch v := arg.Nargs.(type) {
			case int:
				if v == 1 {
					fmt.Printf(" [%s]", strings.ToUpper(arg.Name))
				} else {
					for j := 0; j < v; j++ {
						fmt.Printf(" [%s]", strings.ToUpper(arg.Name))
					}
				}
			case string:
				if v == "*" {
					fmt.Printf(" [%s...]", strings.ToUpper(arg.Name))
				}
			}
		}
	}

	fmt.Println()

	if p.Description != "" {
		fmt.Printf("\n%s\n\n", p.Description)
	}

	if len(p.Arguments) > 0 {
		fmt.Println("Positional arguments:")
		for _, arg := range p.Arguments {
			reqStr := " (required)"
			if !arg.Required {
				reqStr = " (optional)"
			}
			fmt.Printf("  %-15s %s%s\n", arg.Name, arg.HelpText, reqStr)
		}
		fmt.Println()
	}

	if len(p.Options) > 0 {
		fmt.Println("Optional arguments:")
		fmt.Println("  -h, --help      Show this help message and exit")
		for _, option := range p.Options {
			names := []string{}
			if option.ShortName != "" {
				names = append(names, option.ShortName)
			}
			if option.LongName != "" {
				names = append(names, option.LongName)
			}
			nameStr := strings.Join(names, ", ")

			helpParts := []string{option.HelpText}
			if option.Default != nil && option.Action == "store" {
				helpParts = append(helpParts, fmt.Sprintf("(default: %v)", option.Default))
			} else if option.Action == "store_true" || option.Action == "store_false" {
				helpParts = append(helpParts, fmt.Sprintf("(%s)", option.Action))
			}
			if !option.Required {
				helpParts = append(helpParts, "(optional)")
			}
			fmt.Printf("  %-15s %s\n", nameStr, strings.Join(helpParts, " "))
		}
		fmt.Println()
	}
}

func main() {
	parser := NewArgParser("A simple demo of the argument parser")

	parser.AddOption("verbose", "-v", "--verbose", "Enable verbose output", nil, "store_true", false, 1)
	parser.AddOption("output", "-o", "--output", "Output file name", "output.txt", "store", false, 1)
	parser.AddOption("numbers", "-n", "--numbers", "List of numbers", nil, "store", false, "*")
	parser.AddOption("quiet", "-q", "--quiet", "Suppress output", nil, "store_true", false, 1)
	parser.AddOption("format", "-f", "--format", "Output format", nil, "store", true, 1)

	parser.AddArgument("input_file", "Input file to process", nil, true, 1)
	parser.AddArgument("multiplier", "Value multiplier", nil, true, 1)
	parser.AddArgument("optional_args", "Optional additional arguments", nil, false, "*")

	testCases := [][]string{
		{"-f", "json", "data.txt", "2"},
		{"--format", "xml", "-v", "input.txt", "3", "extra1", "extra2"},
		{"-f", "csv", "-o", "result.csv", "-n", "1", "2", "3", "data.txt", "5"},
		{"-h"},
		{"--help"},
	}

	for i, testArgs := range testCases {
		if contains(testArgs, "help") || contains(testArgs, "-h") {
			continue
		}
		fmt.Printf("\n--- Test Case %d: %s ---\n", i+1, strings.Join(testArgs, " "))
		result, err := parser.ParseArgs(testArgs)
		if err != nil {
			fmt.Printf("  Error: %v\n", err)
			continue
		}
		keys := make([]string, 0, len(result))
		for k := range result {
			keys = append(keys, k)
		}
		sort.Strings(keys)
		for _, key := range keys {
			value := result[key]
			fmt.Printf("  %s: %v\n", key, value)
		}
	}
}

func contains(slice []string, target string) bool {
	for _, s := range slice {
		if s == target {
			return true
		}
	}
	return false
}
