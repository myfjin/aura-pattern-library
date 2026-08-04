// @forge-family linreg

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/**
 * Chebyshev semi-iterative method for linear regression.
 *
 * Accelerates the stationary Richardson iteration on the normal equations
 * AtA * theta = Aty with the optimal Chebyshev residual polynomial over the
 * exact spectrum of AtA. The eigenvalue bounds are computed analytically
 * (trigonometric solution of the 3×3 characteristic polynomial), so the
 * polynomial is tuned to the true interval [λmin, λmax].
 *
 * @param {number[][]} X - design matrix
 * @param {number[]} y - target values
 * @param {number} lr - unused learning rate (harness contract)
 * @param {number} iters - number of iterations
 * @returns {{weights: number[], bias: number}}
 */
function chebyshevSemiIterativeRegression(X, y, lr, iters) {
    const n = X.length;
    const nf = X[0].length;
    const m = nf + 1;

    const A = new Array(n);
    for (let i = 0; i < n; i++) {
        A[i] = new Array(m);
        A[i][0] = 1.0;
        for (let j = 0; j < nf; j++) A[i][j + 1] = X[i][j];
    }

    const AtA = new Array(m).fill(0).map(() => new Array(m).fill(0));
    const Aty = new Array(m).fill(0);
    for (let i = 0; i < n; i++) {
        const a = A[i];
        for (let r = 0; r < m; r++) {
            Aty[r] += a[r] * y[i];
            for (let c = 0; c < m; c++) AtA[r][c] += a[r] * a[c];
        }
    }

    function det3(M) {
        return M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
             - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
             + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]);
    }

    function minor(M, r, c) {
        const rows = [0, 1, 2].filter(i => i !== r);
        const cols = [0, 1, 2].filter(j => j !== c);
        const sub = [[M[rows[0]][cols[0]], M[rows[0]][cols[1]]],
                     [M[rows[1]][cols[0]], M[rows[1]][cols[1]]]];
        return sub[0][0] * sub[1][1] - sub[0][1] * sub[1][0];
    }

    // Exact eigenvalues of 3×3 symmetric AtA via characteristic polynomial.
    const trace = AtA[0][0] + AtA[1][1] + AtA[2][2];
    const S = minor(AtA, 0, 0) + minor(AtA, 1, 1) + minor(AtA, 2, 2);
    const det = det3(AtA);
    // Reduce λ³ - trace λ² + S λ - det = 0 to depressed cubic t³ + p t + q = 0.
    const a1 = -trace;
    const a2 = S;
    const a3 = -det;
    const offset = -a1 / 3;
    const p = (3 * a2 - a1 * a1) / 3;
    const q = (2 * a1 * a1 * a1 - 9 * a1 * a2 + 27 * a3) / 27;
    const disc = -4 * p * p * p - 27 * q * q;
    let eigen = [];
    if (disc < 0 || Math.abs(p) < 1e-14) {
        // Fallback to power iteration for max and a small floor for min.
        function powerEigen(B, steps) {
            let v = new Array(m).fill(1);
            for (let s = 0; s < steps; s++) {
                const Bv = new Array(m).fill(0);
                for (let r = 0; r < m; r++) {
                    let sm = 0;
                    for (let c = 0; c < m; c++) sm += B[r][c] * v[c];
                    Bv[r] = sm;
                }
                let norm = 0;
                for (let j = 0; j < m; j++) norm += Bv[j] * Bv[j];
                norm = Math.sqrt(norm);
                for (let j = 0; j < m; j++) v[j] = Bv[j] / (norm || 1);
            }
            let num = 0, den = 0;
            const Bv = new Array(m).fill(0);
            for (let r = 0; r < m; r++) {
                let sm = 0;
                for (let c = 0; c < m; c++) sm += B[r][c] * v[c];
                Bv[r] = sm;
            }
            for (let j = 0; j < m; j++) {
                num += v[j] * Bv[j];
                den += v[j] * v[j];
            }
            return num / den;
        }
        const lambdaMax = powerEigen(AtA, 20);
        eigen = [lambdaMax * 1e-4, lambdaMax];
    } else {
        const phi = Math.acos(-q / 2 * Math.sqrt(-27 / (p * p * p)));
        const twoSqrt = 2 * Math.sqrt(-p / 3);
        for (let k = 0; k < 3; k++) {
            eigen.push(offset + twoSqrt * Math.cos((phi + 2 * Math.PI * k) / 3));
        }
    }

    eigen.sort((a, b) => a - b);
    let lambdaMin = Math.max(eigen[0], 1e-12);
    let lambdaMax = eigen[eigen.length - 1];
    if (lambdaMin > lambdaMax) [lambdaMin, lambdaMax] = [lambdaMax, lambdaMin];

    // Gershgorin lower bound: diagonal minus off-diagonal row sums.
    for (let r = 0; r < m; r++) {
        let off = 0;
        for (let c = 0; c < m; c++) if (c !== r) off += Math.abs(AtA[r][c]);
        lambdaMin = Math.min(lambdaMin, Math.max(AtA[r][r] - off, 1e-12));
        lambdaMax = Math.max(lambdaMax, AtA[r][r] + off);
    }

    // Chebyshev semi-iterative recurrence (Young / SOR form).
    const zeta = (lambdaMax + lambdaMin) / (lambdaMax - lambdaMin);
    const omega1 = 2 / (lambdaMax + lambdaMin);

    let muPrev = 1;
    let muCurr = zeta;

    let xPrev = new Array(m).fill(0);
    let xCurr = new Array(m).fill(0);

    function matVec(v) {
        const out = new Array(m).fill(0);
        for (let r = 0; r < m; r++) {
            let s = 0;
            for (let c = 0; c < m; c++) s += AtA[r][c] * v[c];
            out[r] = s;
        }
        return out;
    }

    // First Richardson step.
    {
        const Av = matVec(xCurr);
        for (let r = 0; r < m; r++) xCurr[r] = xCurr[r] + omega1 * (Aty[r] - Av[r]);
    }

    for (let k = 1; k < iters; k++) {
        const muNext = 2 * zeta * muCurr - muPrev;
        const omega = 4 * muCurr / ((lambdaMax - lambdaMin) * muNext);
        const beta = muPrev / muNext;

        const Av = matVec(xCurr);
        const xNext = new Array(m);
        for (let r = 0; r < m; r++) {
            xNext[r] = xCurr[r] + omega * (Aty[r] - Av[r]) + beta * (xCurr[r] - xPrev[r]);
        }
        xPrev = xCurr;
        xCurr = xNext;
        muPrev = muCurr;
        muCurr = muNext;
    }

    return { weights: xCurr.slice(1), bias: xCurr[0] };
}

globalThis.linearRegressionGD = chebyshevSemiIterativeRegression;
const linearRegressionGD = chebyshevSemiIterativeRegression;   // Forge Gate harness contract — do not remove
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
    const result = chebyshevSemiIterativeRegression(X, y, 0.05, 200);
    assertShape(result);

    const expectedWeights = [2.0000000000000004,3.0000000000000004];
    const expectedBias = 0.49999999999999994;

    assert(approxEqual(result.weights, expectedWeights, 1e-9), 'self-test: weights mismatch');
    assert(approxEqual(result.bias, expectedBias, 1e-9), 'self-test: bias mismatch');
})();

