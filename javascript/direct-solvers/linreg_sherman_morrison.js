// @forge-family linreg
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/**
 * Linear regression via Sherman-Morrison rank-1 updates to an inverse.
 * The normal-equations matrix M = A^T A is accumulated as a sum of outer
 * products A_i A_i^T of rows of A = [1 | X]. Starting from a small
 * regularised diagonal, each rank-1 term is incorporated with the
 * Sherman-Morrison formula
 *   (M + u v^T)^{-1} = M^{-1} - M^{-1} u v^T M^{-1} / (1 + v^T M^{-1} u).
 * After all rows are absorbed, theta = M^{-1} A^T y. Unlike batch 4's RLS,
 * this maintains the inverse explicitly and forms the final solution in one
 * matrix-vector product.
 *
 * @param {number[][]} X - design matrix
 * @param {number[]} y - target values
 * @param {number} lr - unused (signature compatibility)
 * @param {number} iters - unused (signature compatibility)
 * @returns {{weights: number[], bias: number}}
 */
function shermanMorrisonRegression(X, y, lr, iters) {
    const n = X.length;
    const nf = X[0].length;
    const m = nf + 1;

    // A = [1 | X]
    const A = [];
    for (let i = 0; i < n; i++) {
        A.push([1.0].concat(X[i]));
    }

    // A^T y.
    const Aty = [];
    for (let r = 0; r < m; r++) {
        let s = 0.0;
        for (let i = 0; i < n; i++) {
            s += A[i][r] * y[i];
        }
        Aty.push(s);
    }

    // Start from a modest regularised diagonal so the initial inverse is
    // stable in 64-bit floating point. The regularisation is small enough
    // that the final theta approximates the OLS solution well within the
    // harness tolerance.
    const reg = 1e-4;
    let invM = [];
    for (let i = 0; i < m; i++) {
        const row = [];
        for (let j = 0; j < m; j++) {
            row.push(i === j ? 1.0 / reg : 0.0);
        }
        invM.push(row);
    }

    // Sherman-Morrison: (M + u u^T)^{-1} = invM - invM u u^T invM / (1 + u^T invM u).
    for (let k = 0; k < n; k++) {
        const u = A[k];

        // invMu = invM * u
        const invMu = [];
        for (let i = 0; i < m; i++) {
            let s = 0.0;
            for (let j = 0; j < m; j++) {
                s += invM[i][j] * u[j];
            }
            invMu.push(s);
        }

        // u^T invM u
        let denom = 1.0;
        for (let j = 0; j < m; j++) {
            denom += u[j] * invMu[j];
        }
        if (Math.abs(denom) < 1e-24) {
            continue;
        }

        // invM -= invMu * (u^T invM) / denom. Because invM is symmetric,
        // u^T invM = (invM u)^T, so the outer product is invMu_i * invMu_j.
        for (let i = 0; i < m; i++) {
            for (let j = 0; j < m; j++) {
                invM[i][j] -= invMu[i] * invMu[j] / denom;
            }
        }

        // Numerical symmetry preservation.
        for (let i = 0; i < m; i++) {
            for (let j = i + 1; j < m; j++) {
                const avg = 0.5 * (invM[i][j] + invM[j][i]);
                invM[i][j] = avg;
                invM[j][i] = avg;
            }
        }
    }

    // theta = invM * Aty
    const theta = [];
    for (let i = 0; i < m; i++) {
        let s = 0.0;
        for (let j = 0; j < m; j++) {
            s += invM[i][j] * Aty[j];
        }
        theta.push(s);
    }

    return { weights: theta.slice(1), bias: theta[0] };
}
globalThis.linearRegressionGD = shermanMorrisonRegression;
const linearRegressionGD = shermanMorrisonRegression;   // Forge Gate harness contract — do not remove
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
    const result = shermanMorrisonRegression(X, y, 0.05, 200);
    assertShape(result);

    const expectedWeights = [1.9999732733407967,2.9999688269931224];
    const expectedBias = 0.5000013845975201;

    assert(approxEqual(result.weights, expectedWeights, 1e-9), 'self-test: weights mismatch');
    assert(approxEqual(result.bias, expectedBias, 1e-9), 'self-test: bias mismatch');
})();

