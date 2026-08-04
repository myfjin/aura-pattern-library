// @forge-family linreg
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/**
 * Mini-batch gradient descent for linear regression.
 * Deterministic shuffling via a seeded LCG; batch size fixed at 5.
 *
 * @param {number[][]} X - design matrix
 * @param {number[]} y - target values
 * @param {number} lr - learning rate
 * @param {number} iters - outer epochs (each epoch scans all samples in batches)
 * @returns {{weights: number[], bias: number}}
 */
function minibatchGdRegression(X, y, lr, iters) {
    const n = X.length;
    const nf = X[0].length;
    const weights = new Array(nf).fill(0.0);
    let bias = 0.0;

    // Seeded LCG to make the sample shuffle deterministic.
    let state = 42 >>> 0;
    function rand() {
        state = ((state * 1664525 + 1013904223) & 0xFFFFFFFF) >>> 0;
        return state / 0x100000000;
    }

    const batchSize = 5;
    const indices = [];
    for (let i = 0; i < n; i++) indices.push(i);

    function shuffle(arr) {
        for (let i = arr.length - 1; i > 0; i--) {
            const j = Math.floor(rand() * (i + 1));
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
    }

    for (let epoch = 0; epoch < iters; epoch++) {
        shuffle(indices);
        for (let start = 0; start < n; start += batchSize) {
            const end = start + batchSize;
            let db = 0.0;
            const dw = new Array(nf).fill(0.0);
            let count = 0;
            for (let b = start; b < end && b < n; b++) {
                const idx = indices[b];
                let pred = bias;
                for (let j = 0; j < nf; j++) {
                    pred += weights[j] * X[idx][j];
                }
                const err = pred - y[idx];
                db += err;
                for (let j = 0; j < nf; j++) {
                    dw[j] += err * X[idx][j];
                }
                count++;
            }
            if (count > 0) {
                const inv = lr / count;
                bias -= inv * db;
                for (let j = 0; j < nf; j++) {
                    weights[j] -= inv * dw[j];
                }
            }
        }
    }

    return { weights: weights, bias: bias };
}

globalThis.linearRegressionGD = minibatchGdRegression;
const linearRegressionGD = minibatchGdRegression;   // Forge Gate harness contract — do not remove
// Self-test: deterministic fixture from the Forge Gate linreg oracle.
(function () {
    function lcg_next(s) {
        return ((s * 1664525 + 1013904223) & 0xFFFFFFFF) >>> 0;
    }
    function makeHarnessData() {
        let st = 12345 >>> 0;
        const nf = 2;
        const n = 30;
        const X = [];
        for (let i = 0; i < n; i++) {
            const row = [];
            for (let j = 0; j < nf; j++) {
                st = lcg_next(st);
                row.push((st / 0x100000000) * 2 - 1);
            }
            X.push(row);
        }
        const trueWeights = [2.0, 3.0];
        const trueBias = 0.5;
        const y = [];
        for (let i = 0; i < n; i++) {
            let pred = trueBias;
            for (let j = 0; j < nf; j++) pred += trueWeights[j] * X[i][j];
            y.push(pred);
        }
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
        return a === b;
    }
    function assertShape(result) {
        assert(result && typeof result === 'object', 'self-test: result is not an object');
        assert(Array.isArray(result.weights) && result.weights.length === 2, 'self-test: expected 2 weights');
        assert(typeof result.bias === 'number' && isFinite(result.bias), 'self-test: bias missing or non-finite');
    }

    const { X, y } = makeHarnessData();
    const result = minibatchGdRegression(X, y, 0.05, 200);
    assertShape(result);

    const expectedWeights = [1.9999998265678343,2.999999911058384];
    const expectedBias = 0.5000000152316448;

    assert(approxEqual(result.weights, expectedWeights, 1e-9), 'self-test: weights mismatch');
    assert(approxEqual(result.bias, expectedBias, 1e-9), 'self-test: bias mismatch');
})();

