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

	// Set defaults for options. An unset store_true flag is OFF (false)
	// and an unset store_false flag is ON (true).
	for name, option := range p.Options {
		result[name] = option.Default
		if option.Action == "store_true" {
			if option.Default != nil {
				result[name] = option.Default
			} else {
				result[name] = false
			}
		} else if option.Action == "store_false" {
			if option.Default != nil {
				result[name] = option.Default
			} else {
				result[name] = true
			}
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

	// Parse options, recording which argv indices each option consumed.
	consumed := make(map[int]bool)
	i := 0
	for i < len(args) {
		arg := args[i]

		if strings.HasPrefix(arg, "-") {
			consumed[i] = true
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
								consumed[i+1] = true
								i += 2
							} else {
								values := []string{}
								for j := 0; j < v; j++ {
									if i+1+j >= len(args) || strings.HasPrefix(args[i+1+j], "-") {
										return nil, fmt.Errorf("Option %s requires %d arguments", arg, v)
									}
									values = append(values, args[i+1+j])
									consumed[i+1+j] = true
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
									consumed[j] = true
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

	// Positional arguments = tokens no option consumed.
	positionalArgs := []string{}
	for k, a := range args {
		if !consumed[k] && !strings.HasPrefix(a, "-") {
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
		if option.Required && result[name] == option.Default {
			key := option.LongName
			if key == "" {
				key = option.ShortName
			}
			return nil, fmt.Errorf("Missing required option: %s", key)
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

	// Self-test: exact parse results for flags/values/nargs/positionals,
	// defaults applied, missing-required refused.

	// Short flag + positionals; unset flag false; default applied.
	r, err := parser.ParseArgs([]string{"-f", "json", "data.txt", "2"})
	if err != nil {
		panic(err)
	}
	if !(r["format"] == "json") {
		panic("format")
	}
	if !(r["input_file"] == "data.txt") {
		panic("input_file")
	}
	multiplier := r["multiplier"]
	if m, ok := multiplier.([]string); ok {
		if !(len(m) == 1 && m[0] == "2") {
			panic(fmt.Sprintf("multiplier: %v", multiplier))
		}
	} else if !(multiplier == "2") {
		panic(fmt.Sprintf("multiplier: %v", multiplier))
	}
	if !(r["verbose"] == false) {
		panic("unset store_true flag must default false")
	}
	if !(r["output"] == "output.txt") {
		panic("default not applied")
	}

	// Long option + store_true + trailing variadic positionals.
	r, err = parser.ParseArgs([]string{"--format", "xml", "-v", "input.txt", "3", "extra1", "extra2"})
	if err != nil {
		panic(err)
	}
	if !(r["format"] == "xml") {
		panic("format")
	}
	if !(r["verbose"] == true) {
		panic("store_true flag not set by -v")
	}
	if !(r["input_file"] == "input.txt") {
		panic("input_file")
	}
	optionalArgs := r["optional_args"].([]string)
	if !(len(optionalArgs) == 2 && optionalArgs[0] == "extra1" && optionalArgs[1] == "extra2") {
		panic(fmt.Sprintf("variadic tail wrong: %v", optionalArgs))
	}

	// nargs='*' option is greedy to the next dash, so positionals go first.
	r, err = parser.ParseArgs([]string{"-f", "csv", "-o", "result.csv", "data.txt", "5", "-n", "1", "2", "3"})
	if err != nil {
		panic(err)
	}
	if !(r["format"] == "csv" && r["output"] == "result.csv") {
		panic("format/output")
	}
	numbers := r["numbers"].([]string)
	if !(len(numbers) == 3 && numbers[0] == "1" && numbers[1] == "2" && numbers[2] == "3") {
		panic(fmt.Sprintf("nargs='*' option wrong: %v", numbers))
	}
	if !(r["input_file"] == "data.txt") {
		panic("input_file")
	}
	if !(sumInts(numbers) == 6) {
		panic("-n 1 2 3 must sum to 6")
	}

	// Missing REQUIRED option is refused, naming the option.
	_, err = parser.ParseArgs([]string{"input.txt", "2"})
	if err == nil {
		panic("missing required --format accepted")
	}
	if !strings.Contains(strings.ToLower(err.Error()), "format") {
		panic(fmt.Sprintf("error must mention 'format': %v", err))
	}

	// Missing required positional is refused.
	_, err = parser.ParseArgs([]string{"-f", "json"})
	if err == nil {
		panic("missing positionals accepted")
	}

	// Unknown option is refused.
	_, err = parser.ParseArgs([]string{"-f", "json", "--bogus", "x", "in.txt", "2"})
	if err == nil {
		panic("unknown option accepted")
	}

	fmt.Println("arg_parser: flags/defaults/nargs exact (-n sums 6), variadic tail " +
		"['extra1','extra2'], required option+positional refused — PASS")

	// Demo output for non-test invocations
	testCases := [][]string{
		{"-f", "json", "data.txt", "2"},
		{"--format", "xml", "-v", "input.txt", "3", "extra1", "extra2"},
		{"-f", "csv", "-o", "result.csv", "data.txt", "5", "-n", "1", "2", "3"},
	}

	for i, testArgs := range testCases {
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

func sumInts(strs []string) int {
	sum := 0
	for _, s := range strs {
		var v int
		fmt.Sscanf(s, "%d", &v)
		sum += v
	}
	return sum
}
