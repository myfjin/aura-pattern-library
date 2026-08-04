// @forge-family statistics

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/**
 * Double-double accumulation statistics.
 *
 * Each scalar is represented as a non-overlapping hi/lo float pair. Sums and
 * sum-of-products are accumulated in double-double arithmetic, then the
 * results are flattened back to a single Number for return.
 *
 * @param {number[][]} X - data matrix (column 0 used)
 * @param {number[]} y - target values
 * @param {number} lr - unused learning rate (harness contract)
 * @param {number} iters - unused iteration count (harness contract)
 * @returns {{statsX:{mean:number,variance:number}, statsY:{mean:number,variance:number}, correlation:number, covariance:number}}
 */
function doubleDoubleSum(X, y, lr, iters) {
    const xs = X.map(row => row[0]);
    const ys = y;
    const n = xs.length;

    // Split a double into a leading and trailing part (Veltkamp/Vecsplit).
    const factor = 134217729; // 2^27 + 1
    function split(a) {
        const c = factor * a;
        const x = c - a;
        const xh = c - x;
        const xl = a - xh;
        return { hi: xh, lo: xl };
    }

    function twoSum(a, b) {
        const s = a + b;
        const z = s - a;
        const e = (a - (s - z)) + (b - z);
        return { s, e };
    }

    function twoProduct(a, b) {
        const p = a * b;
        const sa = split(a);
        const sb = split(b);
        const e = ((sa.hi * sb.hi - p) + sa.hi * sb.lo + sa.lo * sb.hi) + sa.lo * sb.lo;
        return { p, e };
    }

    // Double-double addition: returns {hi, lo} for (a+b).
    function ddAdd(aHi, aLo, bHi, bLo) {
        const t1 = aHi + bHi;
        let e = t1 - aHi;
        let t2 = ((bHi - e) + (aHi - (t1 - e))) + aLo + bLo;
        const hi = t1 + t2;
        t2 = t2 - (hi - t1);
        return { hi, lo: t2 };
    }

    // Sum an array in double-double.
    function ddSum(vals) {
        let hi = 0;
        let lo = 0;
        for (let i = 0; i < vals.length; i++) {
            const r = ddAdd(hi, lo, vals[i], 0);
            hi = r.hi;
            lo = r.lo;
        }
        return hi + lo;
    }

    // Double-double product accumulation of two arrays.
    function ddDot(xv, yv) {
        let hi = 0;
        let lo = 0;
        for (let i = 0; i < xv.length; i++) {
            const p = twoProduct(xv[i], yv[i]);
            const r = ddAdd(hi, lo, p.p, p.e);
            hi = r.hi;
            lo = r.lo;
        }
        return hi + lo;
    }

    const meanX = ddSum(xs) / n;
    const meanY = ddSum(ys) / n;

    const dx = xs.map(v => v - meanX);
    const dy = ys.map(v => v - meanY);
    const varianceX = ddDot(dx, dx) / n;
    const varianceY = ddDot(dy, dy) / n;
    const cov = ddDot(dx, dy) / n;

    const correlation = varianceX > 0 && varianceY > 0 ? cov / Math.sqrt(varianceX * varianceY) : 0;

    return {
        statsX: { mean: meanX, variance: varianceX },
        statsY: { mean: meanY, variance: varianceY },
        correlation,
        covariance: cov,
    };
}

globalThis.linearRegressionGD = doubleDoubleSum;
const linearRegressionGD = doubleDoubleSum;   // Forge Gate harness contract — do not remove
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
    const result = doubleDoubleSum(X, y, 0.05, 200);
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

