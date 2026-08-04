// @forge-family statistics

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/**
 * Long-accumulator style exact summation (bucketed by exponent).
 *
 * Each addend is split into a set of non-overlapping floating-point numbers
 * stored in bins indexed by exponent. Bins are periodically renormalised so
 * that partial sums of similar magnitude are accumulated separately, reducing
 * catastrophic cancellation. Means, variances and covariance use this
 * accumulator.
 *
 * @param {number[][]} X - data matrix (column 0 used)
 * @param {number[]} y - target values
 * @param {number} lr - unused learning rate (harness contract)
 * @param {number} iters - unused iteration count (harness contract)
 * @returns {{statsX:{mean:number,variance:number}, statsY:{mean:number,variance:number}, correlation:number, covariance:number}}
 */
function longAccumulator(X, y, lr, iters) {
    const xs = X.map(row => row[0]);
    const ys = y;
    const n = xs.length;

    // Bucket size equal to the spacing of one ulp at unit magnitude.
    function accumulatorSum(vals) {
        // Collect addends split by exponent using a simple bin array.
        const bins = new Map(); // exponent -> double value
        function addToBin(x) {
            if (x === 0) return;
            const exp = Math.floor(Math.log2(Math.abs(x)));
            const existing = bins.get(exp) || 0;
            const s = existing + x;
            bins.set(exp, s);
            // If the addition overflowed into a higher bin, carry it.
            const newExp = Math.floor(Math.log2(Math.abs(s)));
            if (newExp > exp) {
                bins.set(exp, s - Math.sign(s) * Math.pow(2, newExp));
                const higher = bins.get(newExp) || 0;
                bins.set(newExp, higher + Math.sign(s) * Math.pow(2, newExp));
            }
        }
        for (let i = 0; i < vals.length; i++) addToBin(vals[i]);
        // Sum bins from smallest magnitude to largest.
        const entries = Array.from(bins.entries()).sort((a, b) => a[0] - b[0]);
        let total = 0;
        let c = 0;
        for (const [, v] of entries) {
            const y = v - c;
            const t = total + y;
            c = (t - total) - y;
            total = t;
        }
        return total + c;
    }

    const meanX = accumulatorSum(xs) / n;
    const meanY = accumulatorSum(ys) / n;

    const varianceX = accumulatorSum(xs.map(v => (v - meanX) * (v - meanX))) / n;
    const varianceY = accumulatorSum(ys.map(v => (v - meanY) * (v - meanY))) / n;
    const cov = accumulatorSum(xs.map((v, i) => (v - meanX) * (ys[i] - meanY))) / n;

    const correlation = varianceX > 0 && varianceY > 0 ? cov / Math.sqrt(varianceX * varianceY) : 0;

    return {
        statsX: { mean: meanX, variance: varianceX },
        statsY: { mean: meanY, variance: varianceY },
        correlation,
        covariance: cov,
    };
}

globalThis.linearRegressionGD = longAccumulator;
const linearRegressionGD = longAccumulator;   // Forge Gate harness contract — do not remove
// Self-test: deterministic fixture from the Forge Gate statistics oracle.
(function () {
    function lcg_next(s) {
        return ((s * 1664525 + 1013904223) & 0xFFFFFFFF) >>> 0;
    }
    function makeHarnessData() {
        let st = 12345 >>> 0;
        const xs = [];
        for (let i = 0; i < 30; i++) {
            st = lcg_next(st);
            xs.push((st / 0x100000000) * 2 - 1);
        }
        const ys = [];
        for (let i = 0; i < 30; i++) {
            ys.push(1.5 + 2.3 * xs[i] + 0.7 * xs[i] * xs[i]);
        }
        const X = xs.map(x => [x, 0.0]);
        const y = ys;
        return { X, y };
    }
    function assert(cond, msg) {
        if (!cond) {
            const e = new Error(msg);
            e.name = 'AssertionError';
            throw e;
        }
    }
    function approxEqual(a, b, relTol) {
        if (typeof a === 'number') {
            if (!isFinite(a) || !isFinite(b)) return false;
            if (a === 0 && b === 0) return true;
            return Math.abs(a - b) <= relTol * Math.max(Math.abs(a), Math.abs(b));
        }
        if (Array.isArray(a)) {
            if (!Array.isArray(b) || a.length !== b.length) return false;
            return a.every((v, i) => approxEqual(v, b[i], relTol));
        }
        if (a && typeof a === 'object' && b && typeof b === 'object') {
            const keysA = Object.keys(a).sort();
            const keysB = Object.keys(b).sort();
            if (keysA.length !== keysB.length) return false;
            return keysA.every(k => keysB.includes(k) && approxEqual(a[k], b[k], relTol));
        }
        return a === b;
    }
    function assertShape(result) {
        assert(result && typeof result === 'object', 'self-test: result is not an object');
        assert(result.statsX && typeof result.statsX === 'object' && isFinite(result.statsX.mean) && isFinite(result.statsX.variance), 'self-test: statsX missing or non-finite');
        assert(result.statsY && typeof result.statsY === 'object' && isFinite(result.statsY.mean) && isFinite(result.statsY.variance), 'self-test: statsY missing or non-finite');
        assert(typeof result.correlation === 'number' && isFinite(result.correlation), 'self-test: correlation missing or non-finite');
        assert(typeof result.covariance === 'number' && isFinite(result.covariance), 'self-test: covariance missing or non-finite');
    }

    const { X, y } = makeHarnessData();
    const result = longAccumulator(X, y, 0.05, 200);
    assertShape(result);

    const expectedStatsX = {"mean":0.02813882363649706,"variance":0.37410160748555527};
    const expectedStatsY = {"mean":1.827144674980784,"variance":2.0104066132840708};
    const expectedCorrelation = 0.9843117938076356;
    const expectedCovariance = 0.8536295252888613;

    assert(approxEqual(result.statsX, expectedStatsX, 1e-9), 'self-test: statsX mismatch');
    assert(approxEqual(result.statsY, expectedStatsY, 1e-9), 'self-test: statsY mismatch');
    assert(approxEqual(result.correlation, expectedCorrelation, 1e-9), 'self-test: correlation mismatch');
    assert(approxEqual(result.covariance, expectedCovariance, 1e-9), 'self-test: covariance mismatch');
})();

