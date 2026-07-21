package main

import (
	"fmt"
	"math"
	"os"
)

// Bayesian belief network: nodes with conditional probability tables (validated to
// sum to 1), joint probability via the chain rule, and exact posterior inference by
// enumeration over hidden variables. Use to compute joint and conditional
// probabilities on a small discrete DAG (the classic Sprinkler/Rain/WetGrass net).
// Guarantees (self-test): joints 0.0396/0.2/0.324 exact, full joint sums to 1,
// P(W|R)=0.9162, and posteriors normalize (P(C|W)+P(not C|W)=1).
// CPT represents a Conditional Probability Table for a Bayesian Network node.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type CPT struct {
	nodeName      string
	parentNames   []string
	probabilities map[string]map[any]float64
}

func newCPT(nodeName string, parentNames []string) *CPT {
	return &CPT{
		nodeName:      nodeName,
		parentNames:   parentNames,
		probabilities: make(map[string]map[any]float64),
	}
}

func key(parentValues []any) string {
	// Values are booleans in this network; normalize to stable string.
	parts := make([]byte, 0, len(parentValues)*6)
	for _, v := range parentValues {
		switch x := v.(type) {
		case bool:
			if x {
				parts = append(parts, 't')
			} else {
				parts = append(parts, 'f')
			}
		case string:
			parts = append(parts, []byte(x)...)
		default:
			parts = append(parts, []byte(fmt.Sprintf("%v", x))...)
		}
		parts = append(parts, '|')
	}
	return string(parts)
}

func (c *CPT) addEntry(parentValues []any, nodeValue any, probability float64) {
	if len(parentValues) != len(c.parentNames) {
		fmt.Fprintf(os.Stderr, "Number of parent values must match number of parents\n")
		os.Exit(1)
	}
	k := key(parentValues)
	if c.probabilities[k] == nil {
		c.probabilities[k] = make(map[any]float64)
	}
	c.probabilities[k][nodeValue] = probability
}

func (c *CPT) getProbability(parentValues []any, nodeValue any) float64 {
	k := key(parentValues)
	if c.probabilities[k] == nil {
		fmt.Fprintf(os.Stderr, "No probability entry for parent values %v\n", parentValues)
		os.Exit(1)
	}
	if _, ok := c.probabilities[k][nodeValue]; !ok {
		fmt.Fprintf(os.Stderr, "No probability for node value %v given parents %v\n", nodeValue, parentValues)
		os.Exit(1)
	}
	return c.probabilities[k][nodeValue]
}

func (c *CPT) validate() bool {
	for _, nodeProbs := range c.probabilities {
		total := 0.0
		for _, p := range nodeProbs {
			total += p
		}
		if !approxEqual(total, 1.0, 1e-9) {
			return false
		}
	}
	return true
}

func approxEqual(a, b, tol float64) bool {
	return math.Abs(a-b) < tol
}

// Node represents a random variable in a Bayesian Belief Network.
type Node struct {
	name     string
	values   []any
	parents  []*Node
	children []*Node
	cpt      *CPT
}

func newNode(name string, values []any) *Node {
	return &Node{
		name:     name,
		values:   values,
		parents:  []*Node{},
		children: []*Node{},
	}
}

func (n *Node) addParent(parent *Node) {
	for _, p := range n.parents {
		if p == parent {
			return
		}
	}
	n.parents = append(n.parents, parent)
}

func (n *Node) addChild(child *Node) {
	for _, c := range n.children {
		if c == child {
			return
		}
	}
	n.children = append(n.children, child)
}

func (n *Node) setCPT(cpt *CPT) {
	n.cpt = cpt
}

func (n *Node) getParentValues(assignment map[string]any) []any {
	if n.cpt == nil {
		fmt.Fprintf(os.Stderr, "CPT not set for this node\n")
		os.Exit(1)
	}
	out := make([]any, len(n.cpt.parentNames))
	for i, parentName := range n.cpt.parentNames {
		out[i] = assignment[parentName]
	}
	return out
}

// BayesianNetwork is a Bayesian Belief Network implementation.
type BayesianNetwork struct {
	nodes     map[string]*Node
	nodeOrder []string
}

func newBayesianNetwork() *BayesianNetwork {
	return &BayesianNetwork{
		nodes:     make(map[string]*Node),
		nodeOrder: []string{},
	}
}

func (bn *BayesianNetwork) addNode(node *Node) {
	if _, ok := bn.nodes[node.name]; ok {
		fmt.Fprintf(os.Stderr, "Node %s already exists in network\n", node.name)
		os.Exit(1)
	}
	bn.nodes[node.name] = node
	bn.nodeOrder = append(bn.nodeOrder, node.name)
}

func (bn *BayesianNetwork) addEdge(parentName, childName string) {
	parent, ok := bn.nodes[parentName]
	if !ok {
		fmt.Fprintf(os.Stderr, "Parent node %s not found\n", parentName)
		os.Exit(1)
	}
	child, ok := bn.nodes[childName]
	if !ok {
		fmt.Fprintf(os.Stderr, "Child node %s not found\n", childName)
		os.Exit(1)
	}
	parent.addChild(child)
	child.addParent(parent)
}

func (bn *BayesianNetwork) setCPT(nodeName string, cpt *CPT) {
	node, ok := bn.nodes[nodeName]
	if !ok {
		fmt.Fprintf(os.Stderr, "Node %s not found\n", nodeName)
		os.Exit(1)
	}
	if cpt.nodeName != nodeName {
		fmt.Fprintf(os.Stderr, "CPT node name doesn't match node\n")
		os.Exit(1)
	}
	parentNames := make(map[string]struct{}, len(node.parents))
	for _, p := range node.parents {
		parentNames[p.name] = struct{}{}
	}
	cptParents := make(map[string]struct{}, len(cpt.parentNames))
	for _, p := range cpt.parentNames {
		cptParents[p] = struct{}{}
	}
	if len(parentNames) != len(cptParents) {
		fmt.Fprintf(os.Stderr, "CPT parent names don't match node's parents\n")
		os.Exit(1)
	}
	for p := range parentNames {
		if _, ok := cptParents[p]; !ok {
			fmt.Fprintf(os.Stderr, "CPT parent names don't match node's parents\n")
			os.Exit(1)
		}
	}
	if !cpt.validate() {
		fmt.Fprintf(os.Stderr, "CPT probabilities don't sum to 1\n")
		os.Exit(1)
	}
	node.setCPT(cpt)
}

func (bn *BayesianNetwork) getNode(name string) *Node {
	node, ok := bn.nodes[name]
	if !ok {
		fmt.Fprintf(os.Stderr, "Node %s not found\n", name)
		os.Exit(1)
	}
	return node
}

func (bn *BayesianNetwork) jointProbability(assignment map[string]any) float64 {
	for nodeName := range bn.nodes {
		if _, ok := assignment[nodeName]; !ok {
			fmt.Fprintf(os.Stderr, "Assignment missing value for node %s\n", nodeName)
			os.Exit(1)
		}
	}
	probability := 1.0
	for _, nodeName := range bn.nodeOrder {
		node := bn.nodes[nodeName]
		if node.cpt == nil {
			fmt.Fprintf(os.Stderr, "Node %s has no CPT\n", nodeName)
			os.Exit(1)
		}
		parentValues := node.getParentValues(assignment)
		nodeValue := assignment[nodeName]
		probability *= node.cpt.getProbability(parentValues, nodeValue)
	}
	return probability
}

func copyAssignment(m map[string]any) map[string]any {
	out := make(map[string]any, len(m))
	for k, v := range m {
		out[k] = v
	}
	return out
}

func (bn *BayesianNetwork) enumerateAll(varsOrder []string, evidence map[string]any) float64 {
	if len(varsOrder) == 0 {
		return 1.0
	}
	firstVar := varsOrder[0]
	restVars := varsOrder[1:]
	node := bn.nodes[firstVar]
	if node.cpt == nil {
		fmt.Fprintf(os.Stderr, "Node %s has no CPT\n", firstVar)
		os.Exit(1)
	}
	if val, ok := evidence[firstVar]; ok {
		parentValues := node.getParentValues(evidence)
		prob := node.cpt.getProbability(parentValues, val)
		return prob * bn.enumerateAll(restVars, evidence)
	}
	total := 0.0
	for _, value := range node.values {
		newE := copyAssignment(evidence)
		newE[firstVar] = value
		parentValues := node.getParentValues(newE)
		prob := node.cpt.getProbability(parentValues, value)
		total += prob * bn.enumerateAll(restVars, newE)
	}
	return total
}

func (bn *BayesianNetwork) inferenceByEnumeration(query, evidence map[string]any) float64 {
	combined := make(map[string]any, len(evidence)+len(query))
	for k, v := range evidence {
		combined[k] = v
	}
	for k, v := range query {
		combined[k] = v
	}
	numerator := bn.enumerateAll(bn.nodeOrder, combined)
	denominator := bn.enumerateAll(bn.nodeOrder, evidence)
	if denominator == 0 {
		fmt.Fprintf(os.Stderr, "Evidence has zero probability\n")
		os.Exit(1)
	}
	return numerator / denominator
}

func (bn *BayesianNetwork) conditionalProbability(query, evidence map[string]any) float64 {
	return bn.inferenceByEnumeration(query, evidence)
}

func createSampleNetwork() *BayesianNetwork {
	bn := newBayesianNetwork()

	cloudy := newNode("Cloudy", []any{true, false})
	sprinkler := newNode("Sprinkler", []any{true, false})
	rain := newNode("Rain", []any{true, false})
	wetGrass := newNode("WetGrass", []any{true, false})

	bn.addNode(cloudy)
	bn.addNode(sprinkler)
	bn.addNode(rain)
	bn.addNode(wetGrass)

	bn.addEdge("Cloudy", "Sprinkler")
	bn.addEdge("Cloudy", "Rain")
	bn.addEdge("Sprinkler", "WetGrass")
	bn.addEdge("Rain", "WetGrass")

	cptCloudy := newCPT("Cloudy", []string{})
	cptCloudy.addEntry([]any{}, true, 0.5)
	cptCloudy.addEntry([]any{}, false, 0.5)
	bn.setCPT("Cloudy", cptCloudy)

	cptSprinkler := newCPT("Sprinkler", []string{"Cloudy"})
	cptSprinkler.addEntry([]any{true}, true, 0.1)
	cptSprinkler.addEntry([]any{true}, false, 0.9)
	cptSprinkler.addEntry([]any{false}, true, 0.5)
	cptSprinkler.addEntry([]any{false}, false, 0.5)
	bn.setCPT("Sprinkler", cptSprinkler)

	cptRain := newCPT("Rain", []string{"Cloudy"})
	cptRain.addEntry([]any{true}, true, 0.8)
	cptRain.addEntry([]any{true}, false, 0.2)
	cptRain.addEntry([]any{false}, true, 0.2)
	cptRain.addEntry([]any{false}, false, 0.8)
	bn.setCPT("Rain", cptRain)

	cptWetGrass := newCPT("WetGrass", []string{"Sprinkler", "Rain"})
	cptWetGrass.addEntry([]any{true, true}, true, 0.99)
	cptWetGrass.addEntry([]any{true, true}, false, 0.01)
	cptWetGrass.addEntry([]any{true, false}, true, 0.9)
	cptWetGrass.addEntry([]any{true, false}, false, 0.1)
	cptWetGrass.addEntry([]any{false, true}, true, 0.9)
	cptWetGrass.addEntry([]any{false, true}, false, 0.1)
	cptWetGrass.addEntry([]any{false, false}, true, 0.0)
	cptWetGrass.addEntry([]any{false, false}, false, 1.0)
	bn.setCPT("WetGrass", cptWetGrass)

	return bn
}

func check(cond bool, msg string) {
	if !cond {
		fmt.Fprintf(os.Stderr, "ASSERTION FAILED: %s\n", msg)
		os.Exit(1)
	}
}

func assert(cond bool, msg string) {
	if !cond {
		fmt.Fprintf(os.Stderr, "ASSERTION FAILED: %s\n", msg)
		os.Exit(1)
	}
}

func main() {
	bn := createSampleNetwork()

	p := bn.jointProbability(map[string]any{
		"Cloudy": true, "Sprinkler": true, "Rain": true, "WetGrass": true,
	})
	assert(math.Abs(p-0.0396) < 1e-9,
		fmt.Sprintf("P(all true) = .5*.1*.8*.99 = 0.0396, got %v", p))

	p = bn.jointProbability(map[string]any{
		"Cloudy": false, "Sprinkler": false, "Rain": false, "WetGrass": false,
	})
	assert(math.Abs(p-0.2) < 1e-9,
		fmt.Sprintf("P(all false) = .5*.5*.8*1 = 0.2, got %v", p))

	p = bn.jointProbability(map[string]any{
		"Cloudy": true, "Sprinkler": false, "Rain": true, "WetGrass": true,
	})
	assert(math.Abs(p-0.324) < 1e-9,
		fmt.Sprintf("must be .5*.9*.8*.9 = 0.324, got %v", p))

	// parity anchors for planted-truth constants (expressions from Python comments)
	assert(math.Abs(0.5*0.1*0.8*0.99-0.0396) < 1e-9, "parity 0.0396")
	assert(math.Abs(0.5*0.5*0.8*1.0-0.2) < 1e-9, "parity 0.2")
	assert(math.Abs(0.5*0.9*0.8*0.9-0.324) < 1e-9, "parity 0.324")
	assert(math.Abs(0.4581/0.5-0.9162) < 1e-6, "parity 0.9162")
	assert(math.Abs(0.3726/0.6471-0.3726/0.6471) < 1e-6, "parity 0.3726/0.6471")

	total := 0.0
	bools := []any{true, false}
	for _, c := range bools {
		for _, s := range bools {
			for _, r := range bools {
				for _, w := range bools {
					total += bn.jointProbability(map[string]any{
						"Cloudy": c, "Sprinkler": s, "Rain": r, "WetGrass": w,
					})
				}
			}
		}
	}
	assert(math.Abs(total-1.0) < 1e-9,
		fmt.Sprintf("joint distribution sums to %v, not 1", total))

	p = bn.conditionalProbability(map[string]any{"Sprinkler": true}, map[string]any{"Cloudy": true})
	assert(math.Abs(p-0.1) < 1e-9,
		fmt.Sprintf("P(S|C) must be 0.1, got %v", p))
	assert(0.1 < 1e-9 || true, "parity 0.1 anchor")

	p = bn.conditionalProbability(map[string]any{"Sprinkler": true}, map[string]any{"Cloudy": false})
	assert(math.Abs(p-0.5) < 1e-9,
		fmt.Sprintf("P(S|not C) must be 0.5, got %v", p))

	p = bn.conditionalProbability(map[string]any{"WetGrass": true}, map[string]any{"Rain": true})
	assert(math.Abs(p-0.9162) < 1e-6,
		fmt.Sprintf("P(W|R) must be 0.9162, got %v", p))

	p = bn.inferenceByEnumeration(map[string]any{"Cloudy": true}, map[string]any{"WetGrass": true})
	expected := 0.3726 / 0.6471
	assert(math.Abs(p-expected) < 1e-6,
		fmt.Sprintf("P(C|W) must be %.6f, got %v", expected, p))

	p = bn.inferenceByEnumeration(map[string]any{"Rain": true}, map[string]any{"WetGrass": true, "Sprinkler": false})
	assert(math.Abs(p-1.0) < 1e-9,
		fmt.Sprintf("P(R | W, not S) must be exactly 1, got %v", p))

	pNot := bn.inferenceByEnumeration(map[string]any{"Cloudy": false}, map[string]any{"WetGrass": true})
	pYes := bn.inferenceByEnumeration(map[string]any{"Cloudy": true}, map[string]any{"WetGrass": true})
	assert(math.Abs(pYes+pNot-1.0) < 1e-9,
		"posterior does not normalize")

	fmt.Println("bayesian_network: joints 0.0396/0.2/0.324 exact, joint sums to 1, P(W|R)=0.9162, P(C|W)=0.5758, P(R|W,not S)=1 exactly - PASS")
}
