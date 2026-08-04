// @forge-family linreg
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/**
 * Linear regression via power-iteration SVD.
 * Computes the thin SVD of A = [1 | X] by repeated power iteration with
 * deterministic deflation, then forms the Moore-Penrose pseudoinverse
 * theta = V S^+ U^T y. This differs from batch 3's one-sided Jacobi SVD.
 *
 * @param {number[][]} X - design matrix
 * @param {number[]} y - target values
 * @param {number} lr - unused (signature compatibility)
 * @param {number} iters - unused (power iterations converge internally)
 * @returns {{weights: number[], bias: number}}
 */
function powerIterationSvdRegression(X, y, lr, iters) {
    const n = X.length;
    const nf = X[0].length;
    const m = nf + 1;

    // A = [1 | X]
    const A = [];
    for (let i = 0; i < n; i++) {
        A.push([1.0].concat(X[i]));
    }

    // Helpers.
    function matVec(v) {
        const out = [];
        for (let i = 0; i < n; i++) {
            let s = 0.0;
            for (let j = 0; j < m; j++) {
                s += A[i][j] * v[j];
            }
            out.push(s);
        }
        return out;
    }

    function transMatVec(u) {
        const out = [];
        for (let j = 0; j < m; j++) {
            let s = 0.0;
            for (let i = 0; i < n; i++) {
                s += A[i][j] * u[i];
            }
            out.push(s);
        }
        return out;
    }

    function norm(v) {
        let s = 0.0;
        for (let i = 0; i < v.length; i++) {
            s += v[i] * v[i];
        }
        return Math.sqrt(s);
    }

    function normalise(v) {
        const nrm = norm(v);
        if (nrm < 1e-14) {
            return v;
        }
        const out = [];
        for (let i = 0; i < v.length; i++) {
            out.push(v[i] / nrm);
        }
        return out;
    }

    function scale(v, c) {
        const out = [];
        for (let i = 0; i < v.length; i++) {
            out.push(v[i] * c);
        }
        return out;
    }

    function sub(a, b) {
        const out = [];
        for (let i = 0; i < a.length; i++) {
            out.push(a[i] - b[i]);
        }
        return out;
    }

    function dot(a, b) {
        let s = 0.0;
        for (let i = 0; i < a.length; i++) {
            s += a[i] * b[i];
        }
        return s;
    }

    // Power iteration with deflation to recover all right singular vectors.
    let B = [];
    for (let i = 0; i < n; i++) {
        B.push(A[i].slice());
    }
    const V = [];
    const sigmas = [];
    const U = [];

    for (let k = 0; k < m; k++) {
        // Deterministic initial vector.
        let v = new Array(m).fill(1.0 / Math.sqrt(m));
        for (let p = 0; p < 100; p++) {
            const Bv = [];
            for (let i = 0; i < n; i++) {
                let s = 0.0;
                for (let j = 0; j < m; j++) {
                    s += B[i][j] * v[j];
                }
                Bv.push(s);
            }
            const BtBv = transMatVec(Bv);
            v = normalise(BtBv);
        }

        // Compute left singular vector and singular value for the deflated matrix.
        const Bv = [];
        for (let i = 0; i < n; i++) {
            let s = 0.0;
            for (let j = 0; j < m; j++) {
                s += B[i][j] * v[j];
            }
            Bv.push(s);
        }
        const sigma = norm(Bv);
        const u = normalise(Bv);

        sigmas.push(sigma);
        V.push(v.slice());
        U.push(u.slice());

        // Deflate: B -= sigma * u * v^T
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < m; j++) {
                B[i][j] -= sigma * u[i] * v[j];
            }
        }
    }

    // U^T y
    const utY = [];
    for (let j = 0; j < m; j++) {
        let s = 0.0;
        for (let i = 0; i < n; i++) {
            s += U[j][i] * y[i];
        }
        utY.push(s);
    }

    // theta = V * diag(1/sigma) * U^T y
    const theta = [];
    for (let i = 0; i < m; i++) {
        let s = 0.0;
        for (let j = 0; j < m; j++) {
            s += V[j][i] * (sigmas[j] > 1e-12 ? utY[j] / sigmas[j] : 0.0);
        }
        theta.push(s);
    }

    return { weights: theta.slice(1), bias: theta[0] };
}
globalThis.linearRegressionGD = powerIterationSvdRegression;
const linearRegressionGD = powerIterationSvdRegression;   // Forge Gate harness contract — do not remove
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
    const result = powerIterationSvdRegression(X, y, 0.05, 200);
    assertShape(result);

    const expectedWeights = [2.0000000000006097,2.999999999996634];
    const expectedBias = 0.5000000000004455;

    assert(approxEqual(result.weights, expectedWeights, 1e-9), 'self-test: weights mismatch');
    assert(approxEqual(result.bias, expectedBias, 1e-9), 'self-test: bias mismatch');
})();

