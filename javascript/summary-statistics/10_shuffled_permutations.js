// @forge-family statistics

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/**
 * Seeded shuffled-order summation averaged over several permutations.
 *
 * A deterministic seeded PRNG inside the fixture generates several random
 * permutations of the input. The required statistics are computed from each
 * permutation using a standard two-pass algorithm, and the results are averaged.
 * Averaging over ordering errors reduces bias from any single summation order.
 *
 * @param {number[][]} X - data matrix (column 0 used)
 * @param {number[]} y - target values
 * @param {number} lr - unused learning rate (harness contract)
 * @param {number} iters - unused iteration count (harness contract)
 * @returns {{statsX:{mean:number,variance:number}, statsY:{mean:number,variance:number}, correlation:number, covariance:number}}
 */
function shuffledPermutations(X, y, lr, iters) {
    const xs = X.map(row => row[0]);
    const ys = y;
    const n = xs.length;

    // Seeded PRNG local to this fixture.
    let rngState = 20240810 >>> 0;
    function rand() {
        rngState = ((rngState * 1664525 + 1013904223) & 0xFFFFFFFF) >>> 0;
        return rngState / 0x100000000;
    }

    function shuffle(indices) {
        for (let i = indices.length - 1; i > 0; i--) {
            const j = Math.floor(rand() * (i + 1));
            const tmp = indices[i];
            indices[i] = indices[j];
            indices[j] = tmp;
        }
        return indices;
    }

    function permutedStats(order) {
        const px = new Array(n);
        const py = new Array(n);
        for (let i = 0; i < n; i++) {
            px[i] = xs[order[i]];
            py[i] = ys[order[i]];
        }
        let sx = 0;
        let sy = 0;
        for (let i = 0; i < n; i++) {
            sx += px[i];
            sy += py[i];
        }
        const mx = sx / n;
        const my = sy / n;
        let vx = 0;
        let vy = 0;
        let cov = 0;
        for (let i = 0; i < n; i++) {
            const dx = px[i] - mx;
            const dy = py[i] - my;
            vx += dx * dx;
            vy += dy * dy;
            cov += dx * dy;
        }
        return { mx, my, vx: vx / n, vy: vy / n, cov: cov / n };
    }

    const runs = 5;
    let acc = { mx: 0, my: 0, vx: 0, vy: 0, cov: 0 };
    for (let r = 0; r < runs; r++) {
        const order = shuffle(new Array(n).fill(0).map((_, i) => i));
        const p = permutedStats(order);
        acc.mx += p.mx;
        acc.my += p.my;
        acc.vx += p.vx;
        acc.vy += p.vy;
        acc.cov += p.cov;
    }
    acc.mx /= runs;
    acc.my /= runs;
    acc.vx /= runs;
    acc.vy /= runs;
    acc.cov /= runs;

    const correlation = acc.vx > 0 && acc.vy > 0 ? acc.cov / Math.sqrt(acc.vx * acc.vy) : 0;

    return {
        statsX: { mean: acc.mx, variance: acc.vx },
        statsY: { mean: acc.my, variance: acc.vy },
        correlation,
        covariance: acc.cov,
    };
}

globalThis.linearRegressionGD = shuffledPermutations;
const linearRegressionGD = shuffledPermutations;   // Forge Gate harness contract — do not remove
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
    const result = shuffledPermutations(X, y, 0.05, 200);
    assertShape(result);

    const expectedStatsX = {"mean":0.028138823636497064,"variance":0.3741016074855552};
    const expectedStatsY = {"mean":1.827144674980784,"variance":2.0104066132840708};
    const expectedCorrelation = 0.9843117938076356;
    const expectedCovariance = 0.8536295252888613;

    assert(approxEqual(result.statsX, expectedStatsX, 1e-9), 'self-test: statsX mismatch');
    assert(approxEqual(result.statsY, expectedStatsY, 1e-9), 'self-test: statsY mismatch');
    assert(approxEqual(result.correlation, expectedCorrelation, 1e-9), 'self-test: correlation mismatch');
    assert(approxEqual(result.covariance, expectedCovariance, 1e-9), 'self-test: covariance mismatch');
})();

