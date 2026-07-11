package main

import (
	"fmt"
	"os"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type IdempotentDeploy struct {
	currentVersion    string
	deploymentCount   map[string]int
	hasCurrentVersion bool
}

func NewIdempotentDeploy() *IdempotentDeploy {
	return &IdempotentDeploy{
		deploymentCount: make(map[string]int),
	}
}

func (d *IdempotentDeploy) Deploy(version string, skipIfCurrent bool) bool {
	if _, ok := d.deploymentCount[version]; !ok {
		d.deploymentCount[version] = 0
	}

	if d.hasCurrentVersion && d.currentVersion == version && skipIfCurrent {
		return true
	}

	d.currentVersion = version
	d.hasCurrentVersion = true
	d.deploymentCount[version]++

	return true
}

func (d *IdempotentDeploy) GetCurrentVersion() string {
	if !d.hasCurrentVersion {
		return ""
	}
	return d.currentVersion
}

func (d *IdempotentDeploy) GetDeploymentCount(version string) int {
	if count, ok := d.deploymentCount[version]; ok {
		return count
	}
	return 0
}

func (d *IdempotentDeploy) IsDeployed(version string) bool {
	return d.hasCurrentVersion && d.currentVersion == version
}

func main() {
	// test_idempotent_redeploy
	deployer := NewIdempotentDeploy()
	deployer.Deploy("v1.0", true)
	if !(deployer.GetCurrentVersion() == "v1.0") {
		fmt.Fprintf(os.Stderr, "deploy_idempotency: current version not v1.0 after first deploy\n")
		os.Exit(1)
	}
	if !(deployer.GetDeploymentCount("v1.0") == 1) {
		fmt.Fprintf(os.Stderr, "deploy_idempotency: deployment count not 1 after first deploy\n")
		os.Exit(1)
	}
	deployer.Deploy("v1.0", true)
	if !(deployer.GetCurrentVersion() == "v1.0") {
		fmt.Fprintf(os.Stderr, "deploy_idempotency: current version changed after redeploy\n")
		os.Exit(1)
	}
	if !(deployer.GetDeploymentCount("v1.0") == 1) {
		fmt.Fprintf(os.Stderr, "deploy_idempotency: deployment count changed after idempotent redeploy\n")
		os.Exit(1)
	}

	// test_redeploy_counts_attempts
	deployer2 := NewIdempotentDeploy()
	deployer2.Deploy("v1.0", false)
	if !(deployer2.GetDeploymentCount("v1.0") == 1) {
		fmt.Fprintf(os.Stderr, "deploy_idempotency: count not 1 after first non-skipping deploy\n")
		os.Exit(1)
	}
	deployer2.Deploy("v1.0", false)
	if !(deployer2.GetDeploymentCount("v1.0") == 2) {
		fmt.Fprintf(os.Stderr, "deploy_idempotency: count not 2 after second non-skipping deploy\n")
		os.Exit(1)
	}

	// test_redeploy_without_skip_counts_separately
	deployer3 := NewIdempotentDeploy()
	deployer3.Deploy("v1.0", false)
	deployer3.Deploy("v1.0", false)
	deployer3.Deploy("v1.0", false)
	if !(deployer3.GetDeploymentCount("v1.0") == 3) {
		fmt.Fprintf(os.Stderr, "deploy_idempotency: count not 3 after three non-skipping deploys\n")
		os.Exit(1)
	}

	// test_switch_versions
	deployer4 := NewIdempotentDeploy()
	deployer4.Deploy("v1.0", true)
	if !deployer4.IsDeployed("v1.0") {
		fmt.Fprintf(os.Stderr, "deploy_idempotency: v1.0 not deployed\n")
		os.Exit(1)
	}
	deployer4.Deploy("v2.0", true)
	if !deployer4.IsDeployed("v2.0") {
		fmt.Fprintf(os.Stderr, "deploy_idempotency: v2.0 not deployed\n")
		os.Exit(1)
	}
	if !(!deployer4.IsDeployed("v1.0")) {
		fmt.Fprintf(os.Stderr, "deploy_idempotency: v1.0 still reported as deployed\n")
		os.Exit(1)
	}
	deployer4.Deploy("v3.0", true)
	if !deployer4.IsDeployed("v3.0") {
		fmt.Fprintf(os.Stderr, "deploy_idempotency: v3.0 not deployed\n")
		os.Exit(1)
	}

	// test_idempotent_network_retry
	deployer5 := NewIdempotentDeploy()
	deployer5.Deploy("v1.0", true)
	result := deployer5.Deploy("v1.0", true)
	if !(result == true) {
		fmt.Fprintf(os.Stderr, "deploy_idempotency: retry did not return true\n")
		os.Exit(1)
	}
	if !(deployer5.GetCurrentVersion() == "v1.0") {
		fmt.Fprintf(os.Stderr, "deploy_idempotency: current version not v1.0 after retry\n")
		os.Exit(1)
	}
	if !(deployer5.GetDeploymentCount("v1.0") == 1) {
		fmt.Fprintf(os.Stderr, "deploy_idempotency: count not 1 after idempotent retry\n")
		os.Exit(1)
	}

	// test_multiple_idempotent_redeploys
	deployer6 := NewIdempotentDeploy()
	deployer6.Deploy("v1.0", true)
	for i := 0; i < 10; i++ {
		deployer6.Deploy("v1.0", true)
	}
	if !(deployer6.GetDeploymentCount("v1.0") == 1) {
		fmt.Fprintf(os.Stderr, "deploy_idempotency: count not 1 after many idempotent redeploys\n")
		os.Exit(1)
	}

	// test_deployment_order_matters
	deployer7 := NewIdempotentDeploy()
	versions := []string{"v1.0", "v2.0", "v1.0", "v3.0", "v2.0"}
	for _, ver := range versions {
		deployer7.Deploy(ver, true)
	}
	if !(deployer7.GetCurrentVersion() == "v2.0") {
		fmt.Fprintf(os.Stderr, "deploy_idempotency: current version not v2.0 after sequence\n")
		os.Exit(1)
	}
	if !(deployer7.GetDeploymentCount("v1.0") == 2) {
		fmt.Fprintf(os.Stderr, "deploy_idempotency: v1.0 count not 2\n")
		os.Exit(1)
	}
	if !(deployer7.GetDeploymentCount("v2.0") == 2) {
		fmt.Fprintf(os.Stderr, "deploy_idempotency: v2.0 count not 2\n")
		os.Exit(1)
	}
	if !(deployer7.GetDeploymentCount("v3.0") == 1) {
		fmt.Fprintf(os.Stderr, "deploy_idempotency: v3.0 count not 1\n")
		os.Exit(1)
	}

	fmt.Println("deploy_idempotency passed")
}
