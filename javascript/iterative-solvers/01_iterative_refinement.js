// @forge-family linreg

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/**
 * Iterative refinement for linear regression.
 *
 * Computes an initial solution via normal equations, then repeatedly refines it
 * by solving the same normal system for the residual correction. This reduces
 * numerical error in the computed weights and bias.
 *
 * @param {number[][]} X - design matrix
 * @param {number[]} y - target values
 * @param {number} lr - unused learning rate (harness contract)
 * @param {number} iters - number of refinement iterations
 * @returns {{weights: number[], bias: number}}
 */
function iterativeRefinementRegression(X, y, lr, iters) {
    const n = X.length;
    const nf = X[0].length;
    const m = nf + 1;

    // A = [1 | X]
    const A = new Array(n);
    for (let i = 0; i < n; i++) {
        A[i] = new Array(m);
        A[i][0] = 1.0;
        for (let j = 0; j < nf; j++) A[i][j + 1] = X[i][j];
    }

    // Normal equations: AtA * theta = Aty.
    const AtA = new Array(m).fill(0).map(() => new Array(m).fill(0));
    const Aty = new Array(m).fill(0);
    for (let i = 0; i < n; i++) {
        const a = A[i];
        for (let r = 0; r < m; r++) {
            Aty[r] += a[r] * y[i];
            for (let c = 0; c < m; c++) AtA[r][c] += a[r] * a[c];
        }
    }

    function solveNormal(aug) {
        const dim = m;
        for (let col = 0; col < dim; col++) {
            let pivot = col;
            for (let row = col + 1; row < dim; row++) {
                if (Math.abs(aug[row][col]) > Math.abs(aug[pivot][col])) pivot = row;
            }
            [aug[col], aug[pivot]] = [aug[pivot], aug[col]];
            const piv = aug[col][col];
            if (Math.abs(piv) < 1e-12) continue;
            for (let j = col; j <= dim; j++) aug[col][j] /= piv;
            for (let row = 0; row < dim; row++) {
                if (row === col) continue;
                const factor = aug[row][col];
                for (let j = col; j <= dim; j++) aug[row][j] -= factor * aug[col][j];
            }
        }
        return aug.map(row => row[dim]);
    }

    const aug0 = new Array(m);
    for (let r = 0; r < m; r++) aug0[r] = AtA[r].slice().concat(Aty[r]);
    let theta = solveNormal(aug0);

    // Iterative refinement.
    const maxRef = Math.max(1, Math.floor(iters / 2));
    for (let ref = 0; ref < maxRef; ref++) {
        let residualSum = 0;
        for (let i = 0; i < n; i++) {
            let pred = 0;
            for (let j = 0; j < m; j++) pred += A[i][j] * theta[j];
            residualSum += Math.abs(y[i] - pred);
        }
        if (residualSum < 1e-12) break;

        const rhs = new Array(m).fill(0);
        for (let i = 0; i < n; i++) {
            let pred = 0;
            for (let j = 0; j < m; j++) pred += A[i][j] * theta[j];
            const err = y[i] - pred;
            for (let j = 0; j < m; j++) rhs[j] += A[i][j] * err;
        }
        const aug = new Array(m);
        for (let r = 0; r < m; r++) aug[r] = AtA[r].slice().concat(rhs[r]);
        const delta = solveNormal(aug);
        for (let j = 0; j < m; j++) theta[j] += delta[j];
    }

    return { weights: theta.slice(1), bias: theta[0] };
}

globalThis.linearRegressionGD = iterativeRefinementRegression;
const linearRegressionGD = iterativeRefinementRegression;   // Forge Gate harness contract — do not remove
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
    const result = iterativeRefinementRegression(X, y, 0.05, 200);
    assertShape(result);

    const expectedWeights = [2,2.9999999999999996];
    const expectedBias = 0.5;

    assert(approxEqual(result.weights, expectedWeights, 1e-9), 'self-test: weights mismatch');
    assert(approxEqual(result.bias, expectedBias, 1e-9), 'self-test: bias mismatch');
})();

