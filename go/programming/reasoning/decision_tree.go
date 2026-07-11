// decision_tree: simple decision tree classifier with information gain and pruning.
package main

import (
	"fmt"
	"math"
	"os"
	"sort"
)

// Split represents a split in the decision tree.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type Split struct {
	FeatureIndex int
	Threshold    float64
}

// Node represents a node in the decision tree.
type Node struct {
	Samples       [][]float64
	Labels        []int
	Split         *Split
	Left          *Node
	Right         *Node
	Prediction    int
	HasPrediction bool
}

// IsLeaf reports whether the node has no split.
func (n *Node) IsLeaf() bool {
	return n.Split == nil
}

// DecisionTree is a simple decision tree classifier.
type DecisionTree struct {
	MaxDepth        int
	MinSamplesSplit int
	Root            *Node
}

// NewDecisionTree creates a decision tree.
func NewDecisionTree(maxDepth, minSamplesSplit int) *DecisionTree {
	return &DecisionTree{MaxDepth: maxDepth, MinSamplesSplit: minSamplesSplit}
}

// entropy computes the Shannon entropy of labels.
func (dt *DecisionTree) entropy(labels []int) float64 {
	if len(labels) == 0 {
		return 0.0
	}
	counts := make(map[int]int)
	for _, l := range labels {
		counts[l]++
	}
	total := float64(len(labels))
	e := 0.0
	for _, c := range counts {
		p := float64(c) / total
		e -= p * math.Log2(p)
	}
	return e
}

// informationGain computes the gain of a split.
func (dt *DecisionTree) informationGain(samples [][]float64, labels []int, split *Split) float64 {
	parentEntropy := dt.entropy(labels)
	var leftSamples, rightSamples [][]float64
	var leftLabels, rightLabels []int
	for i, sample := range samples {
		if sample[split.FeatureIndex] <= split.Threshold {
			leftSamples = append(leftSamples, sample)
			leftLabels = append(leftLabels, labels[i])
		} else {
			rightSamples = append(rightSamples, sample)
			rightLabels = append(rightLabels, labels[i])
		}
	}
	total := float64(len(samples))
	if total == 0 {
		return 0.0
	}
	leftWeight := float64(len(leftSamples)) / total
	rightWeight := float64(len(rightSamples)) / total
	return parentEntropy - (leftWeight*dt.entropy(leftLabels) + rightWeight*dt.entropy(rightLabels))
}

// findBestSplit finds the best threshold split for the data.
func (dt *DecisionTree) findBestSplit(samples [][]float64, labels []int) *Split {
	if len(uniqueLabels(labels)) <= 1 {
		return nil
	}
	bestGain := -1.0
	var bestSplit *Split
	nFeatures := len(samples[0])
	for feature := 0; feature < nFeatures; feature++ {
		values := uniqueValues(samples, feature)
		sort.Float64s(values)
		for i := 0; i < len(values)-1; i++ {
			threshold := (values[i] + values[i+1]) / 2
			split := &Split{FeatureIndex: feature, Threshold: threshold}
			gain := dt.informationGain(samples, labels, split)
			if gain > bestGain {
				bestGain = gain
				bestSplit = split
			}
		}
	}
	return bestSplit
}

// buildTree recursively builds the tree.
func (dt *DecisionTree) buildTree(samples [][]float64, labels []int, depth int) *Node {
	node := &Node{Samples: samples, Labels: labels}

	if depth >= dt.MaxDepth || len(samples) < dt.MinSamplesSplit || len(uniqueLabels(labels)) <= 1 {
		if len(labels) > 0 {
			node.Prediction = majorityLabel(labels)
			node.HasPrediction = true
		}
		return node
	}

	best := dt.findBestSplit(samples, labels)
	if best == nil {
		if len(labels) > 0 {
			node.Prediction = majorityLabel(labels)
			node.HasPrediction = true
		}
		return node
	}

	var leftSamples, rightSamples [][]float64
	var leftLabels, rightLabels []int
	for i, sample := range samples {
		if sample[best.FeatureIndex] <= best.Threshold {
			leftSamples = append(leftSamples, sample)
			leftLabels = append(leftLabels, labels[i])
		} else {
			rightSamples = append(rightSamples, sample)
			rightLabels = append(rightLabels, labels[i])
		}
	}
	node.Split = best
	node.Left = dt.buildTree(leftSamples, leftLabels, depth+1)
	node.Right = dt.buildTree(rightSamples, rightLabels, depth+1)
	return node
}

// Fit trains the decision tree.
func (dt *DecisionTree) Fit(samples [][]float64, labels []int) {
	if len(samples) == 0 || len(labels) == 0 || len(samples) != len(labels) {
		panic("Invalid training data")
	}
	dt.Root = dt.buildTree(samples, labels, 0)
}

// predictSample predicts the label for one sample.
func (dt *DecisionTree) predictSample(sample []float64, node *Node) int {
	if node.IsLeaf() {
		if !node.HasPrediction {
			panic("Leaf node has no prediction")
		}
		return node.Prediction
	}
	if sample[node.Split.FeatureIndex] <= node.Split.Threshold {
		return dt.predictSample(sample, node.Left)
	}
	return dt.predictSample(sample, node.Right)
}

// Predict predicts labels for many samples.
func (dt *DecisionTree) Predict(samples [][]float64) []int {
	if dt.Root == nil {
		panic("Model not trained yet")
	}
	out := make([]int, len(samples))
	for i, sample := range samples {
		out[i] = dt.predictSample(sample, dt.Root)
	}
	return out
}

// pruneNode prunes a subtree using validation data.
func (dt *DecisionTree) pruneNode(node *Node, valSamples [][]float64, valLabels []int) *Node {
	if node.IsLeaf() {
		return node
	}
	if len(valSamples) == 0 {
		return node
	}

	var leftSamples, rightSamples [][]float64
	var leftLabels, rightLabels []int
	for i, sample := range valSamples {
		if sample[node.Split.FeatureIndex] <= node.Split.Threshold {
			leftSamples = append(leftSamples, sample)
			leftLabels = append(leftLabels, valLabels[i])
		} else {
			rightSamples = append(rightSamples, sample)
			rightLabels = append(rightLabels, valLabels[i])
		}
	}

	node.Left = dt.pruneNode(node.Left, leftSamples, leftLabels)
	node.Right = dt.pruneNode(node.Right, rightSamples, rightLabels)

	if node.Left.IsLeaf() && node.Right.IsLeaf() {
		accWithout := accuracy(dt.Predict(valSamples), valLabels)

		origSplit := node.Split
		origLeft := node.Left
		origRight := node.Right
		origPred := node.Prediction
		origHas := node.HasPrediction

		node.Split = nil
		node.Left = nil
		node.Right = nil
		if len(node.Labels) > 0 {
			node.Prediction = majorityLabel(node.Labels)
			node.HasPrediction = true
		}
		pred := make([]int, len(valSamples))
		for i := range pred {
			pred[i] = node.Prediction
		}
		accWith := accuracy(pred, valLabels)

		if accWithout > accWith {
			node.Split = origSplit
			node.Left = origLeft
			node.Right = origRight
			node.Prediction = origPred
			node.HasPrediction = origHas
		}
	}
	return node
}

// Prune prunes the tree using validation data.
func (dt *DecisionTree) Prune(valSamples [][]float64, valLabels []int) {
	if dt.Root == nil {
		panic("Model not trained yet")
	}
	dt.Root = dt.pruneNode(dt.Root, valSamples, valLabels)
}

// helpers

func uniqueLabels(labels []int) []int {
	seen := make(map[int]struct{})
	var out []int
	for _, l := range labels {
		if _, ok := seen[l]; !ok {
			seen[l] = struct{}{}
			out = append(out, l)
		}
	}
	sort.Ints(out)
	return out
}

func majorityLabel(labels []int) int {
	counts := make(map[int]int)
	for _, l := range labels {
		counts[l]++
	}
	bestLabel := labels[0]
	bestCount := -1
	for label, count := range counts {
		if count > bestCount || (count == bestCount && label < bestLabel) {
			bestCount = count
			bestLabel = label
		}
	}
	return bestLabel
}

func uniqueValues(samples [][]float64, feature int) []float64 {
	seen := make(map[float64]struct{})
	var out []float64
	for _, s := range samples {
		v := s[feature]
		if _, ok := seen[v]; !ok {
			seen[v] = struct{}{}
			out = append(out, v)
		}
	}
	return out
}

func accuracy(pred, truth []int) float64 {
	if len(truth) == 0 {
		return 0
	}
	correct := 0
	for i := range truth {
		if pred[i] == truth[i] {
			correct++
		}
	}
	return float64(correct) / float64(len(truth))
}

func main() {
	// Planted rule: label = 0 if weight < 57, 1 if 57 <= weight < 73, else 2.
	samples := [][]float64{
		{170, 65}, {175, 70}, {160, 55}, {180, 80}, {155, 50},
		{165, 60}, {172, 75}, {158, 52}, {178, 78}, {162, 58},
		{185, 90}, {150, 45}, {168, 68}, {176, 76}, {159, 54},
	}
	labels := []int{1, 1, 0, 2, 0, 1, 2, 0, 2, 1, 2, 0, 1, 2, 0}

	tree := NewDecisionTree(5, 2)
	tree.Fit(samples, labels)

	trainPreds := tree.Predict(samples)
	trainAcc := accuracy(trainPreds, labels)
	if !(trainAcc == 1.0) {
		fmt.Fprintf(os.Stderr, "separable data must fit exactly, accuracy %v\n", trainAcc)
		os.Exit(1)
	}

	testSamples := [][]float64{{165, 62}, {180, 85}, {155, 48}, {163, 59}, {179, 74}}
	truth := []int{1, 2, 0, 1, 2}
	preds := tree.Predict(testSamples)
	if !(preds[0] == truth[0] && preds[1] == truth[1] && preds[2] == truth[2] && preds[3] == truth[3] && preds[4] == truth[4]) {
		fmt.Fprintf(os.Stderr, "planted rule not generalized: %v != %v\n", preds, truth)
		os.Exit(1)
	}
	sum := 0
	for _, p := range preds {
		sum += p
	}
	if !(sum == 6) {
		fmt.Fprintf(os.Stderr, "prediction classes 1+2+0+1+2 must sum to 6, got %d\n", sum)
		os.Exit(1)
	}

	validationSamples := [][]float64{{167, 63}, {177, 77}, {157, 51}, {182, 82}}
	validationLabels := []int{1, 2, 0, 2}
	before := tree.Predict(validationSamples)
	accBefore := accuracy(before, validationLabels)
	tree.Prune(validationSamples, validationLabels)
	after := tree.Predict(validationSamples)
	accAfter := accuracy(after, validationLabels)
	if !(accAfter >= accBefore) {
		fmt.Fprintf(os.Stderr, "pruning reduced validation accuracy %v -> %v\n", accBefore, accAfter)
		os.Exit(1)
	}
	if !(accAfter == 1.0) {
		fmt.Fprintf(os.Stderr, "rule-consistent validation must stay perfect, got %v\n", accAfter)
		os.Exit(1)
	}

	// Single-class data collapses to a leaf that always answers that class.
	flat := NewDecisionTree(3, 2)
	flat.Fit([][]float64{{1, 1}, {2, 2}, {3, 3}}, []int{7, 7, 7})
	flatPreds := flat.Predict([][]float64{{9, 9}, {0, 0}})
	if !(flatPreds[0] == 7 && flatPreds[1] == 7) {
		fmt.Fprintf(os.Stderr, "constant labels not learned: %v\n", flatPreds)
		os.Exit(1)
	}
	if !(len(flatPreds) == 2 && flat.Predict([][]float64{{9, 9}})[0] == 7) {
		fmt.Fprintf(os.Stderr, "sample 9,9 must predict 7: %v\n", flat.Predict([][]float64{{9, 9}}))
		os.Exit(1)
	}

	// Untrained refusal for Predict.
	{
		caught := false
		func() {
			defer func() {
				if r := recover(); r != nil {
					caught = true
				}
			}()
			NewDecisionTree(10, 2).Predict([][]float64{{1, 2}})
		}()
		if !(caught == true) {
			fmt.Fprintln(os.Stderr, "untrained tree predicted")
			os.Exit(1)
		}
	}

	// Untrained refusal for Prune.
	{
		caught := false
		func() {
			defer func() {
				if r := recover(); r != nil {
					caught = true
				}
			}()
			NewDecisionTree(10, 2).Prune([][]float64{{1, 2}}, []int{0})
		}()
		if !(caught == true) {
			fmt.Fprintln(os.Stderr, "untrained tree pruned")
			os.Exit(1)
		}
	}

	fmt.Println("decision_tree: separable rule fit 15/15, generalized 5/5 (sum 6), " +
		"pruning kept validation at 1.0, constant leaf, refusals — PASS")
}
