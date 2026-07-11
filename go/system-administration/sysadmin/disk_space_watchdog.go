package main

import (
	"fmt"
	"math/rand"
	"os"
	"time"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type DiskGuard struct {
	thresholdBytes int64
	usedBytes      int64
	peakUsed       int64
	refused        int
	tmpdir         string
	writtenFiles   []string
}

func diskSpaceWatchdog(thresholdMb int) (*DiskGuard, error) {
	tmpdir, err := os.MkdirTemp("", "disk_space_watchdog_*")
	if err != nil {
		return nil, err
	}
	return &DiskGuard{
		thresholdBytes: int64(thresholdMb) * 1024 * 1024,
		tmpdir:         tmpdir,
		writtenFiles:   []string{},
	}, nil
}

func (d *DiskGuard) availableSpace() int64 {
	return d.thresholdBytes - d.usedBytes
}

func (d *DiskGuard) canWrite(sizeBytes int64) bool {
	if d.availableSpace() < sizeBytes {
		d.refused++
		return false
	}
	return true
}

func (d *DiskGuard) writeFile(sizeBytes int64) bool {
	if !d.canWrite(sizeBytes) {
		return false
	}
	d.usedBytes += sizeBytes
	if d.usedBytes > d.peakUsed {
		d.peakUsed = d.usedBytes
	}
	f, err := os.CreateTemp(d.tmpdir, "write_")
	if err != nil {
		return false
	}
	defer f.Close()
	buf := make([]byte, sizeBytes)
	for i := range buf {
		buf[i] = 'x'
	}
	if _, err := f.Write(buf); err != nil {
		return false
	}
	d.writtenFiles = append(d.writtenFiles, f.Name())
	return true
}

func (d *DiskGuard) cleanup() {
	for _, fname := range d.writtenFiles {
		os.Remove(fname)
	}
	os.Remove(d.tmpdir)
}

func main() {
	rand.Seed(42)

	guard, err := diskSpaceWatchdog(100)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "disk_space_watchdog: failed to create guard: %v\n", err)
		os.Exit(1)
	}
	defer guard.cleanup()

	writeSize := int64(1024 * 1024)

	numWrote := 0
	numRefused := 0

	for i := 0; i < 1000; i++ {
		if guard.writeFile(writeSize) {
			numWrote++
		} else {
			numRefused++
		}
	}

	peakMb := float64(guard.peakUsed) / (1024 * 1024)

	if !(peakMb <= 100) {
		fmt.Fprintf(os.Stderr, "disk_space_watchdog: Peak disk usage %.1fMB exceeded cap 100MB\n", peakMb)
		os.Exit(1)
	}
	if !(numRefused >= 900) {
		fmt.Fprintf(os.Stderr, "disk_space_watchdog: Guard refused %d, expected >= 900 (out of 1000)\n", numRefused)
		os.Exit(1)
	}
	if !(numWrote <= 100) {
		fmt.Fprintf(os.Stderr, "disk_space_watchdog: Wrote %d files, should be <= 100\n", numWrote)
		os.Exit(1)
	}
	if !(numRefused > numWrote*5) {
		fmt.Fprintf(os.Stderr, "disk_space_watchdog: Refused %d << wrote %d\n", numRefused, numWrote)
		os.Exit(1)
	}

	fmt.Println("disk_space_watchdog passed")
}

var _ = time.Now
