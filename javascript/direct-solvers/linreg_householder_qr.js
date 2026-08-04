// @forge-family linreg
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/**
 * Linear regression via Householder QR reflection.
 * Reduces A = [1 | X] to upper triangular R by orthogonal Householder
 * reflections applied to A and to y, then back-substitutes. This is the
 * remaining reflector-based QR method after batch 2 Gram-Schmidt, batch 3
 * Givens rotations and batch 4 modified Gram-Schmidt.
 *
 * @param {number[][]} X - design matrix
 * @param {number[]} y - target values
 * @param {number} lr - unused (signature compatibility)
 * @param {number} iters - unused (signature compatibility)
 * @returns {{weights: number[], bias: number}}
 */
function householderQrRegression(X, y, lr, iters) {
    const n = X.length;
    const nf = X[0].length;
    const m = nf + 1;

    // A = [1 | X]
    const A = [];
    for (let i = 0; i < n; i++) {
        A.push([1.0].concat(X[i]));
    }
    const c = y.slice();

    // Householder QR: zero out sub-diagonal entries column by column.
    for (let k = 0; k < m; k++) {
        // Norm of the tail A[k..n-1][k]
        let norm = 0.0;
        for (let i = k; i < n; i++) {
            norm += A[i][k] * A[i][k];
        }
        norm = Math.sqrt(norm);
        if (norm < 1e-14) {
            continue;
        }
        const sign = A[k][k] >= 0 ? 1.0 : -1.0;
        const alpha = -sign * norm;

        // v = x - alpha*e1, stored in A[k..n-1][k]
        A[k][k] -= alpha;
        let v0 = A[k][k];

        // beta = 2 / (v^T v)
        let vtv = v0 * v0;
        for (let i = k + 1; i < n; i++) {
            vtv += A[i][k] * A[i][k];
        }
        if (vtv < 1e-28) {
            A[k][k] = alpha;
            continue;
        }
        const beta = 2.0 / vtv;

        // Apply H = I - beta*v*v^T to columns k..m-1 of A and to c.
        for (let j = k; j < m; j++) {
            let w = beta * A[k][k] * A[k][j];
            for (let i = k + 1; i < n; i++) {
                w += beta * A[i][k] * A[i][j];
            }
            A[k][j] -= w * A[k][k];
            for (let i = k + 1; i < n; i++) {
                A[i][j] -= w * A[i][k];
            }
        }
        {
            let w = beta * A[k][k] * c[k];
            for (let i = k + 1; i < n; i++) {
                w += beta * A[i][k] * c[i];
            }
            c[k] -= w * A[k][k];
            for (let i = k + 1; i < n; i++) {
                c[i] -= w * A[i][k];
            }
        }

        // Restore diagonal of R.
        A[k][k] = alpha;
    }

    // Back-substitution using the top m rows of R.
    const theta = new Array(m).fill(0.0);
    for (let i = m - 1; i >= 0; i--) {
        let s = c[i];
        for (let j = i + 1; j < m; j++) {
            s -= A[i][j] * theta[j];
        }
        theta[i] = Math.abs(A[i][i]) > 1e-12 ? s / A[i][i] : 0.0;
    }

    return { weights: theta.slice(1), bias: theta[0] };
}
globalThis.linearRegressionGD = householderQrRegression;
const linearRegressionGD = householderQrRegression;   // Forge Gate harness contract — do not remove
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
    const result = householderQrRegression(X, y, 0.05, 200);
    assertShape(result);

    const expectedWeights = [2.000000000000003,2.9999999999999996];
    const expectedBias = 0.5000000000000008;

    assert(approxEqual(result.weights, expectedWeights, 1e-9), 'self-test: weights mismatch');
    assert(approxEqual(result.bias, expectedBias, 1e-9), 'self-test: bias mismatch');
})();

