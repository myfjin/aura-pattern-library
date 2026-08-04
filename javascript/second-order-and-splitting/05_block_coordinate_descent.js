// @forge-family linreg

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/**
 * Block coordinate descent for linear regression.
 *
 * Updates blocks of coordinates jointly rather than one coordinate at a time.
 * Here the parameter vector is split into a bias block and a weights block;
 * each block is updated with the exact least-squares solution conditioned on
 * the other block. This is structurally different from single-coordinate descent.
 *
 * @param {number[][]} X - design matrix
 * @param {number[]} y - target values
 * @param {number} lr - unused learning rate (harness contract)
 * @param {number} iters - number of block sweeps
 * @returns {{weights: number[], bias: number}}
 */
function blockCoordinateDescentRegression(X, y, lr, iters) {
    const n = X.length;
    const nf = X[0].length;

    const weights = new Array(nf).fill(0.0);
    let bias = 0.0;

    // Precompute column sums for the weights block update.
    const XtX = new Array(nf).fill(0).map(() => new Array(nf).fill(0));
    const Xty = new Array(nf).fill(0);
    const colSums = new Array(nf).fill(0);
    for (let i = 0; i < n; i++) {
        const x = X[i];
        for (let a = 0; a < nf; a++) {
            colSums[a] += x[a];
            Xty[a] += x[a] * y[i];
            for (let b = 0; b < nf; b++) XtX[a][b] += x[a] * x[b];
        }
    }

    function solve2x2(M, v) {
        const a = M[0][0], b = M[0][1], c = M[1][0], d = M[1][1];
        const det = a * d - b * c;
        if (Math.abs(det) < 1e-14) return [0, 0];
        return [(d * v[0] - b * v[1]) / det, (-c * v[0] + a * v[1]) / det];
    }

    for (let pass = 0; pass < iters; pass++) {
        // Bias block update: b = mean(y - X w).
        let s = 0;
        for (let i = 0; i < n; i++) {
            let pred = bias;
            for (let j = 0; j < nf; j++) pred += weights[j] * X[i][j];
            s += y[i] - pred;
        }
        bias += s / n;

        // Weights block update: solve normal equations for the residual block.
        // rhs[a] = sum_i x_{ia} (y_i - bias).
        const rhs = new Array(nf);
        for (let a = 0; a < nf; a++) rhs[a] = Xty[a] - bias * colSums[a];

        if (nf === 2) {
            const sol = solve2x2(XtX, rhs);
            weights[0] = sol[0];
            weights[1] = sol[1];
        } else {
            // General tiny-system Gaussian elimination.
            const aug = new Array(nf);
            for (let r = 0; r < nf; r++) aug[r] = XtX[r].slice().concat(rhs[r]);
            for (let col = 0; col < nf; col++) {
                let pivot = col;
                for (let row = col + 1; row < nf; row++) {
                    if (Math.abs(aug[row][col]) > Math.abs(aug[pivot][col])) pivot = row;
                }
                [aug[col], aug[pivot]] = [aug[pivot], aug[col]];
                const piv = aug[col][col];
                if (Math.abs(piv) < 1e-14) continue;
                for (let j = col; j <= nf; j++) aug[col][j] /= piv;
                for (let row = 0; row < nf; row++) {
                    if (row === col) continue;
                    const factor = aug[row][col];
                    for (let j = col; j <= nf; j++) aug[row][j] -= factor * aug[col][j];
                }
            }
            for (let r = 0; r < nf; r++) weights[r] = aug[r][nf];
        }
    }

    return { weights, bias };
}

globalThis.linearRegressionGD = blockCoordinateDescentRegression;
const linearRegressionGD = blockCoordinateDescentRegression;   // Forge Gate harness contract — do not remove
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
    const result = blockCoordinateDescentRegression(X, y, 0.05, 200);
    assertShape(result);

    const expectedWeights = [2.0000000000000004,3.0000000000000004];
    const expectedBias = 0.5;

    assert(approxEqual(result.weights, expectedWeights, 1e-9), 'self-test: weights mismatch');
    assert(approxEqual(result.bias, expectedBias, 1e-9), 'self-test: bias mismatch');
})();

