package main

import (
	"errors"
	"fmt"
	"math"
	"os"
)

// CPT represents a conditional probability table P(Node | Parents).
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type CPT struct {
	NodeName    string
	ParentNames []string
	// probabilities maps parent-value tuple -> node-value -> probability
	probabilities map[string]map[interface{}]float64
}

// NewCPT creates a CPT for a node with the given parents.
func NewCPT(nodeName string, parentNames []string) *CPT {
	return &CPT{
		NodeName:      nodeName,
		ParentNames:   parentNames,
		probabilities: make(map[string]map[interface{}]float64),
	}
}

// key converts a tuple of parent values to a map key.
func key(parentValues []interface{}) string {
	return fmt.Sprintf("%v", parentValues)
}

// AddEntry adds P(nodeValue | parentValues) to the table.
func (c *CPT) AddEntry(parentValues []interface{}, nodeValue interface{}, probability float64) error {
	if len(parentValues) != len(c.ParentNames) {
		return errors.New("number of parent values must match number of parents")
	}
	k := key(parentValues)
	if c.probabilities[k] == nil {
		c.probabilities[k] = make(map[interface{}]float64)
	}
	c.probabilities[k][nodeValue] = probability
	return nil
}

// GetProbability returns P(nodeValue | parentValues).
func (c *CPT) GetProbability(parentValues []interface{}, nodeValue interface{}) (float64, error) {
	k := key(parentValues)
	nodeProbs, ok := c.probabilities[k]
	if !ok {
		return 0, errors.New("no probability entry for parent values")
	}
	p, ok := nodeProbs[nodeValue]
	if !ok {
		return 0, errors.New("no probability for node value given parents")
	}
	return p, nil
}

// Validate checks that each distribution sums to 1 within tolerance.
func (c *CPT) Validate() bool {
	for _, nodeProbs := range c.probabilities {
		total := 0.0
		for _, p := range nodeProbs {
			total += p
		}
		if math.Abs(total-1.0) > 1e-9 {
			return false
		}
	}
	return true
}

// Node is a random variable in the network.
type Node struct {
	Name     string
	Values   []interface{}
	Parents  []*Node
	Children []*Node
	CPT      *CPT
}

// NewNode creates a node with the given possible values.
func NewNode(name string, values []interface{}) *Node {
	return &Node{Name: name, Values: values}
}

// AddParent adds a parent reference.
func (n *Node) AddParent(parent *Node) {
	for _, p := range n.Parents {
		if p == parent {
			return
		}
	}
	n.Parents = append(n.Parents, parent)
}

// AddChild adds a child reference.
func (n *Node) AddChild(child *Node) {
	for _, c := range n.Children {
		if c == child {
			return
		}
	}
	n.Children = append(n.Children, child)
}

// SetCPT assigns a CPT to the node.
func (n *Node) SetCPT(cpt *CPT) {
	n.CPT = cpt
}

// ParentValues extracts parent values for this node's CPT from an assignment.
func (n *Node) ParentValues(assignment map[string]interface{}) ([]interface{}, error) {
	if n.CPT == nil {
		return nil, errors.New("CPT not set for this node")
	}
	out := make([]interface{}, len(n.CPT.ParentNames))
	for i, name := range n.CPT.ParentNames {
		v, ok := assignment[name]
		if !ok {
			return nil, errors.New("assignment missing parent value")
		}
		out[i] = v
	}
	return out, nil
}

// BayesianNetwork is a belief network with enumeration-based inference.
type BayesianNetwork struct {
	nodes     map[string]*Node
	nodeOrder []string
}

// NewBayesianNetwork creates an empty network.
func NewBayesianNetwork() *BayesianNetwork {
	return &BayesianNetwork{
		nodes:     make(map[string]*Node),
		nodeOrder: make([]string, 0),
	}
}

// AddNode adds a node to the network.
func (bn *BayesianNetwork) AddNode(node *Node) error {
	if _, exists := bn.nodes[node.Name]; exists {
		return errors.New("node already exists in network")
	}
	bn.nodes[node.Name] = node
	bn.nodeOrder = append(bn.nodeOrder, node.Name)
	return nil
}

// AddEdge adds a directed edge from parent to child.
func (bn *BayesianNetwork) AddEdge(parentName, childName string) error {
	parent, ok := bn.nodes[parentName]
	if !ok {
		return errors.New("parent node not found")
	}
	child, ok := bn.nodes[childName]
	if !ok {
		return errors.New("child node not found")
	}
	parent.AddChild(child)
	child.AddParent(parent)
	return nil
}

// SetCPT assigns a validated CPT to a node.
func (bn *BayesianNetwork) SetCPT(nodeName string, cpt *CPT) error {
	node, ok := bn.nodes[nodeName]
	if !ok {
		return errors.New("node not found")
	}
	if cpt.NodeName != nodeName {
		return errors.New("CPT node name doesn't match node")
	}
	parentNames := make(map[string]bool)
	for _, p := range node.Parents {
		parentNames[p.Name] = true
	}
	cptParents := make(map[string]bool)
	for _, p := range cpt.ParentNames {
		cptParents[p] = true
	}
	if len(parentNames) != len(cptParents) {
		return errors.New("CPT parent names don't match node's parents")
	}
	for p := range cptParents {
		if !parentNames[p] {
			return errors.New("CPT parent names don't match node's parents")
		}
	}
	if !cpt.Validate() {
		return errors.New("CPT probabilities don't sum to 1")
	}
	node.SetCPT(cpt)
	return nil
}

// GetNode returns a node by name.
func (bn *BayesianNetwork) GetNode(name string) (*Node, error) {
	node, ok := bn.nodes[name]
	if !ok {
		return nil, errors.New("node not found")
	}
	return node, nil
}

// JointProbability computes P(assignment) over all nodes.
func (bn *BayesianNetwork) JointProbability(assignment map[string]interface{}) (float64, error) {
	for name := range bn.nodes {
		if _, ok := assignment[name]; !ok {
			return 0, errors.New("assignment missing value for node")
		}
	}
	probability := 1.0
	for _, nodeName := range bn.nodeOrder {
		node := bn.nodes[nodeName]
		if node.CPT == nil {
			return 0, errors.New("node has no CPT")
		}
		parentValues, err := node.ParentValues(assignment)
		if err != nil {
			return 0, err
		}
		p, err := node.CPT.GetProbability(parentValues, assignment[nodeName])
		if err != nil {
			return 0, err
		}
		probability *= p
	}
	return probability, nil
}

func (bn *BayesianNetwork) enumerateAll(varsOrder []string, evidence map[string]interface{}) (float64, error) {
	if len(varsOrder) == 0 {
		return 1.0, nil
	}
	firstVar := varsOrder[0]
	restVars := varsOrder[1:]
	node := bn.nodes[firstVar]
	if node.CPT == nil {
		return 0, errors.New("node has no CPT")
	}

	if v, ok := evidence[firstVar]; ok {
		parentValues, err := node.ParentValues(evidence)
		if err != nil {
			return 0, err
		}
		p, err := node.CPT.GetProbability(parentValues, v)
		if err != nil {
			return 0, err
		}
		rest, err := bn.enumerateAll(restVars, evidence)
		if err != nil {
			return 0, err
		}
		return p * rest, nil
	}

	total := 0.0
	for _, value := range node.Values {
		newE := copyMap(evidence)
		newE[firstVar] = value
		parentValues, err := node.ParentValues(newE)
		if err != nil {
			return 0, err
		}
		p, err := node.CPT.GetProbability(parentValues, value)
		if err != nil {
			return 0, err
		}
		rest, err := bn.enumerateAll(restVars, newE)
		if err != nil {
			return 0, err
		}
		total += p * rest
	}
	return total, nil
}

// InferenceByEnumeration returns P(query | evidence).
func (bn *BayesianNetwork) InferenceByEnumeration(query, evidence map[string]interface{}) (float64, error) {
	combined := copyMap(evidence)
	for k, v := range query {
		combined[k] = v
	}
	numerator, err := bn.enumerateAll(bn.nodeOrder, combined)
	if err != nil {
		return 0, err
	}
	denominator, err := bn.enumerateAll(bn.nodeOrder, evidence)
	if err != nil {
		return 0, err
	}
	if denominator == 0 {
		return 0, errors.New("evidence has zero probability")
	}
	return numerator / denominator, nil
}

// ConditionalProbability is an alias for InferenceByEnumeration.
func (bn *BayesianNetwork) ConditionalProbability(query, evidence map[string]interface{}) (float64, error) {
	return bn.InferenceByEnumeration(query, evidence)
}

func copyMap(m map[string]interface{}) map[string]interface{} {
	out := make(map[string]interface{}, len(m))
	for k, v := range m {
		out[k] = v
	}
	return out
}

func createSampleNetwork() (*BayesianNetwork, error) {
	bn := NewBayesianNetwork()

	cloudy := NewNode("Cloudy", []interface{}{true, false})
	sprinkler := NewNode("Sprinkler", []interface{}{true, false})
	rain := NewNode("Rain", []interface{}{true, false})
	wetGrass := NewNode("WetGrass", []interface{}{true, false})

	for _, n := range []*Node{cloudy, sprinkler, rain, wetGrass} {
		if err := bn.AddNode(n); err != nil {
			return nil, err
		}
	}

	for _, edge := range [][2]string{{"Cloudy", "Sprinkler"}, {"Cloudy", "Rain"}, {"Sprinkler", "WetGrass"}, {"Rain", "WetGrass"}} {
		if err := bn.AddEdge(edge[0], edge[1]); err != nil {
			return nil, err
		}
	}

	cptCloudy := NewCPT("Cloudy", []string{})
	_ = cptCloudy.AddEntry([]interface{}{}, true, 0.5)
	_ = cptCloudy.AddEntry([]interface{}{}, false, 0.5)
	if err := bn.SetCPT("Cloudy", cptCloudy); err != nil {
		return nil, err
	}

	cptSprinkler := NewCPT("Sprinkler", []string{"Cloudy"})
	_ = cptSprinkler.AddEntry([]interface{}{true}, true, 0.1)
	_ = cptSprinkler.AddEntry([]interface{}{true}, false, 0.9)
	_ = cptSprinkler.AddEntry([]interface{}{false}, true, 0.5)
	_ = cptSprinkler.AddEntry([]interface{}{false}, false, 0.5)
	if err := bn.SetCPT("Sprinkler", cptSprinkler); err != nil {
		return nil, err
	}

	cptRain := NewCPT("Rain", []string{"Cloudy"})
	_ = cptRain.AddEntry([]interface{}{true}, true, 0.8)
	_ = cptRain.AddEntry([]interface{}{true}, false, 0.2)
	_ = cptRain.AddEntry([]interface{}{false}, true, 0.2)
	_ = cptRain.AddEntry([]interface{}{false}, false, 0.8)
	if err := bn.SetCPT("Rain", cptRain); err != nil {
		return nil, err
	}

	cptWetGrass := NewCPT("WetGrass", []string{"Sprinkler", "Rain"})
	_ = cptWetGrass.AddEntry([]interface{}{true, true}, true, 0.99)
	_ = cptWetGrass.AddEntry([]interface{}{true, true}, false, 0.01)
	_ = cptWetGrass.AddEntry([]interface{}{true, false}, true, 0.9)
	_ = cptWetGrass.AddEntry([]interface{}{true, false}, false, 0.1)
	_ = cptWetGrass.AddEntry([]interface{}{false, true}, true, 0.9)
	_ = cptWetGrass.AddEntry([]interface{}{false, true}, false, 0.1)
	_ = cptWetGrass.AddEntry([]interface{}{false, false}, true, 0.0)
	_ = cptWetGrass.AddEntry([]interface{}{false, false}, false, 1.0)
	if err := bn.SetCPT("WetGrass", cptWetGrass); err != nil {
		return nil, err
	}

	return bn, nil
}

func main() {
	fmt.Println("Bayesian Network Demo")
	fmt.Println("=====================")

	bn, err := createSampleNetwork()
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "network: %v\n", err)
		os.Exit(1)
	}

	fmt.Println("\n1. Joint Probability Calculations:")
	assignments := []map[string]interface{}{
		{"Cloudy": true, "Sprinkler": true, "Rain": true, "WetGrass": true},
		{"Cloudy": false, "Sprinkler": false, "Rain": false, "WetGrass": false},
		{"Cloudy": true, "Sprinkler": false, "Rain": true, "WetGrass": true},
	}
	for i, assignment := range assignments {
		prob, err := bn.JointProbability(assignment)
		if !(err == nil) {
			fmt.Fprintf(os.Stderr, "   Assignment %d: Error - %v\n", i+1, err)
			os.Exit(1)
		}
		fmt.Printf("   Assignment %d: P(%v) = %.6f\n", i+1, assignment, prob)
	}

	fmt.Println("\n2. Conditional Probability Inference:")
	queries := []struct {
		query    map[string]interface{}
		evidence map[string]interface{}
		desc     string
	}{
		{map[string]interface{}{"WetGrass": true}, map[string]interface{}{"Rain": true}, "P(WetGrass=True | Rain=True)"},
		{map[string]interface{}{"WetGrass": true}, map[string]interface{}{"Rain": false}, "P(WetGrass=True | Rain=False)"},
		{map[string]interface{}{"Sprinkler": true}, map[string]interface{}{"Cloudy": true}, "P(Sprinkler=True | Cloudy=True)"},
		{map[string]interface{}{"Sprinkler": true}, map[string]interface{}{"Cloudy": false}, "P(Sprinkler=True | Cloudy=False)"},
	}
	for _, q := range queries {
		prob, err := bn.ConditionalProbability(q.query, q.evidence)
		if !(err == nil) {
			fmt.Fprintf(os.Stderr, "   %s: Error - %v\n", q.desc, err)
			os.Exit(1)
		}
		fmt.Printf("   %s = %.6f\n", q.desc, prob)
	}

	fmt.Println("\n3. Complex Inference:")
	prob, err := bn.InferenceByEnumeration(map[string]interface{}{"Cloudy": true}, map[string]interface{}{"WetGrass": true})
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "complex inference: %v\n", err)
		os.Exit(1)
	}
	fmt.Printf("   P(Cloudy=True | WetGrass=True) = %.6f\n", prob)

	prob, err = bn.InferenceByEnumeration(map[string]interface{}{"Rain": true}, map[string]interface{}{"WetGrass": true, "Sprinkler": false})
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "complex inference: %v\n", err)
		os.Exit(1)
	}
	fmt.Printf("   P(Rain=True | WetGrass=True, Sprinkler=False) = %.6f\n", prob)

	fmt.Println("\nDemo completed successfully!")
}
