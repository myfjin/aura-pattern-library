package main

import (
	"fmt"
	"math"
	"os"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type Split struct {
	FeatureIndex int
	Threshold    float64
}

type Node struct {
	Samples    [][]float64
	Labels     []int
	Split      *Split
	Left       *Node
	Right      *Node
	Prediction int
	IsLeafNode bool
}

func (n *Node) IsLeaf() bool {
	return n.IsLeafNode
}

type DecisionTree struct {
	MaxDepth        int
	MinSamplesSplit int
	Root            *Node
}

func NewDecisionTree(maxDepth, minSamplesSplit int) *DecisionTree {
	return &DecisionTree{
		MaxDepth:        maxDepth,
		MinSamplesSplit: minSamplesSplit,
	}
}

func (dt *DecisionTree) entropy(labels []int) float64 {
	if len(labels) == 0 {
		return 0.0
	}
	counts := make(map[int]int)
	for _, label := range labels {
		counts[label]++
	}
	total := float64(len(labels))
	entropy := 0.0
	for _, count := range counts {
		p := float64(count) / total
		entropy -= p * math.Log2(p)
	}
	return entropy
}

func (dt *DecisionTree) informationGain(samples [][]float64, labels []int, split Split) float64 {
	parentEntropy := dt.entropy(labels)

	var leftSamples [][]float64
	var leftLabels []int
	var rightSamples [][]float64
	var rightLabels []int

	for i, sample := range samples {
		if sample[split.FeatureIndex] <= split.Threshold {
			leftSamples = append(leftSamples, sample)
			leftLabels = append(leftLabels, labels[i])
		} else {
			rightSamples = append(rightSamples, sample)
			rightLabels = append(rightLabels, labels[i])
		}
	}

	totalSamples := len(samples)
	if totalSamples == 0 {
		return 0.0
	}

	leftWeight := float64(len(leftSamples)) / float64(totalSamples)
	rightWeight := float64(len(rightSamples)) / float64(totalSamples)

	weightedEntropy := leftWeight*dt.entropy(leftLabels) + rightWeight*dt.entropy(rightLabels)
	return parentEntropy - weightedEntropy
}

func (dt *DecisionTree) findBestSplit(samples [][]float64, labels []int) *Split {
	uniqueLabels := make(map[int]bool)
	for _, label := range labels {
		uniqueLabels[label] = true
	}
	if len(uniqueLabels) <= 1 {
		return nil
	}

	bestGain := -1.0
	var bestSplit *Split
	nFeatures := 0
	if len(samples) > 0 {
		nFeatures = len(samples[0])
	}

	for featureIndex := 0; featureIndex < nFeatures; featureIndex++ {
		valueSet := make(map[float64]bool)
		for _, sample := range samples {
			valueSet[sample[featureIndex]] = true
		}
		values := make([]float64, 0, len(valueSet))
		for v := range valueSet {
			values = append(values, v)
		}
		insertionSortFloats(values)

		for i := 0; i < len(values)-1; i++ {
			threshold := (values[i] + values[i+1]) / 2.0
			split := Split{FeatureIndex: featureIndex, Threshold: threshold}
			gain := dt.informationGain(samples, labels, split)
			if gain > bestGain {
				bestGain = gain
				bestSplit = &Split{FeatureIndex: featureIndex, Threshold: threshold}
			}
		}
	}

	return bestSplit
}

func insertionSortFloats(a []float64) {
	for i := 1; i < len(a); i++ {
		for j := i; j > 0 && a[j] < a[j-1]; j-- {
			a[j], a[j-1] = a[j-1], a[j]
		}
	}
}

func (dt *DecisionTree) buildTree(samples [][]float64, labels []int, depth int) *Node {
	node := &Node{Samples: samples, Labels: labels}

	uniqueLabels := make(map[int]bool)
	for _, label := range labels {
		uniqueLabels[label] = true
	}

	if depth >= dt.MaxDepth || len(samples) < dt.MinSamplesSplit || len(uniqueLabels) <= 1 {
		node.IsLeafNode = true
		if len(labels) > 0 {
			node.Prediction = mostCommon(labels)
		}
		return node
	}

	bestSplit := dt.findBestSplit(samples, labels)
	if bestSplit == nil {
		node.IsLeafNode = true
		if len(labels) > 0 {
			node.Prediction = mostCommon(labels)
		}
		return node
	}

	node.Split = bestSplit
	node.IsLeafNode = false

	var leftSamples [][]float64
	var leftLabels []int
	var rightSamples [][]float64
	var rightLabels []int

	for i, sample := range samples {
		if sample[bestSplit.FeatureIndex] <= bestSplit.Threshold {
			leftSamples = append(leftSamples, sample)
			leftLabels = append(leftLabels, labels[i])
		} else {
			rightSamples = append(rightSamples, sample)
			rightLabels = append(rightLabels, labels[i])
		}
	}

	node.Left = dt.buildTree(leftSamples, leftLabels, depth+1)
	node.Right = dt.buildTree(rightSamples, rightLabels, depth+1)
	return node
}

func mostCommon(labels []int) int {
	counts := make(map[int]int)
	for _, label := range labels {
		counts[label]++
	}
	maxCount := -1
	var result int
	for label, count := range counts {
		if count > maxCount {
			maxCount = count
			result = label
		}
	}
	return result
}

func (dt *DecisionTree) Fit(samples [][]float64, labels []int) {
	if len(samples) == 0 || len(labels) == 0 || len(samples) != len(labels) {
		panic("Invalid training data")
	}
	dt.Root = dt.buildTree(samples, labels, 0)
}

func (dt *DecisionTree) predictSample(sample []float64, node *Node) int {
	if node.IsLeaf() {
		return node.Prediction
	}
	if sample[node.Split.FeatureIndex] <= node.Split.Threshold {
		return dt.predictSample(sample, node.Left)
	}
	return dt.predictSample(sample, node.Right)
}

func (dt *DecisionTree) Predict(samples [][]float64) []int {
	if dt.Root == nil {
		panic("Model not trained yet")
	}
	predictions := make([]int, len(samples))
	for i, sample := range samples {
		predictions[i] = dt.predictSample(sample, dt.Root)
	}
	return predictions
}

func (dt *DecisionTree) Prune(validationSamples [][]float64, validationLabels []int) {
	if dt.Root == nil {
		panic("Model not trained yet")
	}
	dt.Root = dt.pruneNode(dt.Root, validationSamples, validationLabels)
}

func (dt *DecisionTree) pruneNode(node *Node, validationSamples [][]float64, validationLabels []int) *Node {
	if node.IsLeaf() {
		return node
	}

	if len(validationSamples) == 0 {
		return node
	}

	var leftSamples [][]float64
	var leftLabels []int
	var rightSamples [][]float64
	var rightLabels []int

	for i, sample := range validationSamples {
		if sample[node.Split.FeatureIndex] <= node.Split.Threshold {
			leftSamples = append(leftSamples, sample)
			leftLabels = append(leftLabels, validationLabels[i])
		} else {
			rightSamples = append(rightSamples, sample)
			rightLabels = append(rightLabels, validationLabels[i])
		}
	}

	node.Left = dt.pruneNode(node.Left, leftSamples, leftLabels)
	node.Right = dt.pruneNode(node.Right, rightSamples, rightLabels)

	if node.Left.IsLeaf() && node.Right.IsLeaf() {
		accuracyWithoutPruning := accuracy(dt.Predict(validationSamples), validationLabels)

		originalSplit := node.Split
		originalLeft := node.Left
		originalRight := node.Right

		node.Split = nil
		node.IsLeafNode = true
		node.Left = nil
		node.Right = nil
		if len(node.Labels) > 0 {
			node.Prediction = mostCommon(node.Labels)
		}

		predictions := make([]int, len(validationSamples))
		for i := range predictions {
			predictions[i] = node.Prediction
		}
		accuracyWithPruning := accuracy(predictions, validationLabels)

		if accuracyWithoutPruning > accuracyWithPruning {
			node.Split = originalSplit
			node.IsLeafNode = false
			node.Left = originalLeft
			node.Right = originalRight
			node.Prediction = 0
		}
	}

	return node
}

func accuracy(predictions, labels []int) float64 {
	if len(labels) == 0 {
		return 0.0
	}
	correct := 0
	for i := range predictions {
		if predictions[i] == labels[i] {
			correct++
		}
	}
	return float64(correct) / float64(len(labels))
}

func printTree(node *Node, indent int) {
	if node == nil {
		fmt.Println("None")
		return
	}
	prefix := ""
	for i := 0; i < indent; i++ {
		prefix += "  "
	}
	if node.IsLeaf() {
		fmt.Printf("%sLeaf: %d (%d samples)\n", prefix, node.Prediction, len(node.Samples))
		return
	}
	fmt.Printf("%sSplit: feature[%d] <= %.2f (%d samples)\n", prefix, node.Split.FeatureIndex, node.Split.Threshold, len(node.Samples))
	printTree(node.Left, indent+1)
	printTree(node.Right, indent+1)
}

func main() {
	samples := [][]float64{
		{170, 65}, {175, 70}, {160, 55}, {180, 80}, {155, 50},
		{165, 60}, {172, 75}, {158, 52}, {178, 78}, {162, 58},
		{185, 90}, {150, 45}, {168, 68}, {176, 76}, {159, 54},
	}

	labels := []int{1, 1, 0, 2, 0, 0, 1, 0, 2, 0, 2, 0, 1, 2, 0}

	tree := NewDecisionTree(5, 2)
	tree.Fit(samples, labels)

	fmt.Println("Original Tree:")
	printTree(tree.Root, 0)
	fmt.Println()

	testSamples := [][]float64{{165, 62}, {180, 85}, {155, 48}}
	predictions := tree.Predict(testSamples)

	fmt.Println("Predictions:")
	for i, sample := range testSamples {
		fmt.Printf("Sample %v -> Prediction: %d\n", sample, predictions[i])
	}
	fmt.Println()

	validationSamples := [][]float64{
		{167, 63}, {177, 77}, {157, 51}, {182, 82},
	}
	validationLabels := []int{1, 2, 0, 2}

	tree.Prune(validationSamples, validationLabels)

	fmt.Println("Pruned Tree:")
	printTree(tree.Root, 0)
	fmt.Println()

	predictionsAfter := tree.Predict(testSamples)
	fmt.Println("Predictions after pruning:")
	for i, sample := range testSamples {
		fmt.Printf("Sample %v -> Prediction: %d\n", sample, predictionsAfter[i])
	}
	fmt.Println()

	emptyTree := NewDecisionTree(10, 2)
	func() {
		defer func() {
			if r := recover(); r != nil {
				fmt.Printf("Error handling works: Model not trained yet\n")
			}
		}()
		emptyTree.Predict([][]float64{{1, 2}})
		fmt.Fprintf(os.Stderr, "Expected panic for untrained model\n")
		os.Exit(1)
	}()
}
