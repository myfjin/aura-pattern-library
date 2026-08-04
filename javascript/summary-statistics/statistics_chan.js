// @forge-family statistics
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/**
 * Chan's parallel merge formula for one-pass mean and population variance.
 * Combines partial statistics without re-scanning raw data.
 */
function chanVariance(X, y, lr, iters) {
    function merge(a, b) {
        if (a.n === 0) return b;
        if (b.n === 0) return a;
        const delta = b.mean - a.mean;
        const n = a.n + b.n;
        const mean = (a.n * a.mean + b.n * b.mean) / n;
        const M2 = a.M2 + b.M2 + delta * delta * a.n * b.n / n;
        return { n, mean, M2 };
    }
    function chan(xs) {
        if (xs.length === 0) return { n: 0, mean: 0, M2: 0 };
        if (xs.length === 1) return { n: 1, mean: xs[0], M2: 0 };
        const mid = Math.floor(xs.length / 2);
        const left = chan(xs.slice(0, mid));
        const right = chan(xs.slice(mid));
        return merge(left, right);
    }
    function chanMeanVar(xs) {
        const res = chan(xs);
        return { mean: res.mean, variance: res.M2 / res.n };
    }
    const xs = X.map(row => row[0]);
    const ys = y;
    const n = xs.length;
    const sx = chanMeanVar(xs);
    const sy = chanMeanVar(ys);

    const sortedX = xs.slice().sort((a, b) => a - b);
    const sortedY = ys.slice().sort((a, b) => a - b);
    const median = (sorted) => {
        const len = sorted.length;
        if (len % 2 === 1) return sorted[(len - 1) / 2];
        return (sorted[len / 2 - 1] + sorted[len / 2]) / 2;
    };
    const quantile = (sorted, q) => {
        const len = sorted.length;
        const pos = q * (len - 1);
        const lo = Math.floor(pos);
        const hi = Math.ceil(pos);
        if (lo === hi) return sorted[lo];
        return sorted[lo] + (sorted[hi] - sorted[lo]) * (pos - lo);
    };

    let cov = 0;
    for (let i = 0; i < n; i++) cov += (xs[i] - sx.mean) * (ys[i] - sy.mean);
    cov /= n;
    const correlation = sx.variance > 0 && sy.variance > 0 ? cov / Math.sqrt(sx.variance * sy.variance) : 0;

    return {
        statsX: { mean: sx.mean, variance: sx.variance, median: median(sortedX), q25: quantile(sortedX, 0.25), q75: quantile(sortedX, 0.75) },
        statsY: { mean: sy.mean, variance: sy.variance, median: median(sortedY), q25: quantile(sortedY, 0.25), q75: quantile(sortedY, 0.75) },
        correlation, covariance: cov
    };
}
globalThis.linearRegressionGD = chanVariance;
const linearRegressionGD = chanVariance;   // Forge Gate harness contract — do not remove
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
    const result = chanVariance(X, y, 0.05, 200);
    assertShape(result);

    const expectedStatsX = {"mean":0.02813882363649706,"variance":0.37410160748555527,"median":0.0430804283823818,"q25":-0.37083063181489706,"q75":0.4655052983434871};
    const expectedStatsY = {"mean":1.827144674980784,"variance":2.0104066132840703,"median":1.6016923848697542,"q25":0.749610554400218,"q75":2.7233742102942182};
    const expectedCorrelation = 0.9843117938076356;
    const expectedCovariance = 0.8536295252888612;

    assert(approxEqual(result.statsX, expectedStatsX, 1e-9), 'self-test: statsX mismatch');
    assert(approxEqual(result.statsY, expectedStatsY, 1e-9), 'self-test: statsY mismatch');
    assert(approxEqual(result.correlation, expectedCorrelation, 1e-9), 'self-test: correlation mismatch');
    assert(approxEqual(result.covariance, expectedCovariance, 1e-9), 'self-test: covariance mismatch');
})();

