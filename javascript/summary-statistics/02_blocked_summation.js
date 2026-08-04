// @forge-family statistics

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/**
 * Blocked / tiled summation statistics.
 *
 * Accumulates sums in fixed-size blocks (partial sums) to reduce error growth
 * from naive left-to-right accumulation. Means, variances and covariance are
 * built from the block partial sums.
 *
 * @param {number[][]} X - data matrix (column 0 used)
 * @param {number[]} y - target values
 * @param {number} lr - unused learning rate (harness contract)
 * @param {number} iters - unused iteration count (harness contract)
 * @returns {{statsX:{mean:number,variance:number}, statsY:{mean:number,variance:number}, correlation:number, covariance:number}}
 */
function blockedSummation(X, y, lr, iters) {
    const xs = X.map(row => row[0]);
    const ys = y;
    const n = xs.length;
    const blockSize = 8;

    function blockSum(vals) {
        let total = 0;
        let i = 0;
        for (; i + blockSize <= vals.length; i += blockSize) {
            let block = 0;
            for (let j = 0; j < blockSize; j++) block += vals[i + j];
            total += block;
        }
        for (; i < vals.length; i++) total += vals[i];
        return total;
    }

    const meanX = blockSum(xs) / n;
    const meanY = blockSum(ys) / n;

    function blockSumSq(vals, mean) {
        let total = 0;
        let i = 0;
        for (; i + blockSize <= vals.length; i += blockSize) {
            let block = 0;
            for (let j = 0; j < blockSize; j++) {
                const d = vals[i + j] - mean;
                block += d * d;
            }
            total += block;
        }
        for (; i < vals.length; i++) {
            const d = vals[i] - mean;
            total += d * d;
        }
        return total;
    }

    const varianceX = blockSumSq(xs, meanX) / n;
    const varianceY = blockSumSq(ys, meanY) / n;

    let cov = 0;
    let i = 0;
    for (; i + blockSize <= n; i += blockSize) {
        let block = 0;
        for (let j = 0; j < blockSize; j++) block += (xs[i + j] - meanX) * (ys[i + j] - meanY);
        cov += block;
    }
    for (; i < n; i++) cov += (xs[i] - meanX) * (ys[i] - meanY);
    cov /= n;

    const correlation = varianceX > 0 && varianceY > 0 ? cov / Math.sqrt(varianceX * varianceY) : 0;

    return {
        statsX: { mean: meanX, variance: varianceX },
        statsY: { mean: meanY, variance: varianceY },
        correlation,
        covariance: cov,
    };
}

globalThis.linearRegressionGD = blockedSummation;
const linearRegressionGD = blockedSummation;   // Forge Gate harness contract — do not remove
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
    const result = blockedSummation(X, y, 0.05, 200);
    assertShape(result);

    const expectedStatsX = {"mean":0.02813882363649706,"variance":0.37410160748555515};
    const expectedStatsY = {"mean":1.8271446749807843,"variance":2.0104066132840708};
    const expectedCorrelation = 0.9843117938076357;
    const expectedCovariance = 0.8536295252888613;

    assert(approxEqual(result.statsX, expectedStatsX, 1e-9), 'self-test: statsX mismatch');
    assert(approxEqual(result.statsY, expectedStatsY, 1e-9), 'self-test: statsY mismatch');
    assert(approxEqual(result.correlation, expectedCorrelation, 1e-9), 'self-test: correlation mismatch');
    assert(approxEqual(result.covariance, expectedCovariance, 1e-9), 'self-test: covariance mismatch');
})();

