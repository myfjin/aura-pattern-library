// @forge-family kmeans

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/**
 * Elkan's triangle-inequality accelerated k-means.
 *
 * Uses per-point upper and lower distance bounds to avoid redundant distance
 * computations. With exact arithmetic the final partition is identical to
 * Lloyd's algorithm; the implementation is structurally different.
 *
 * @param {number[][]} X - data matrix
 * @param {number[]} y - unused target vector (harness contract)
 * @param {number} lr - unused learning rate (harness contract)
 * @param {number} iters - maximum iterations
 * @returns {{centroids:number[][], k:number, assignments:number[]}}
 */
function kmeansElkan(X, y, lr, iters) {
    const n = X.length;
    const nf = X[0].length;
    const k = 3;

    function dist2(a, b) {
        let s = 0;
        for (let f = 0; f < nf; f++) {
            const d = a[f] - b[f];
            s += d * d;
        }
        return s;
    }

    function sqrtDist2(a, b) {
        return Math.sqrt(dist2(a, b));
    }

    function nearestExact(x, centroids) {
        let best = 0;
        let bestD = dist2(x, centroids[0]);
        for (let c = 1; c < k; c++) {
            const d = dist2(x, centroids[c]);
            if (d < bestD) {
                bestD = d;
                best = c;
            }
        }
        return { c: best, d2: bestD };
    }

    // Initialize with first k points.
    let centroids = new Array(k);
    for (let c = 0; c < k; c++) centroids[c] = X[c].slice();

    const assignments = new Array(n).fill(0);
    const lower = new Array(n); // lower[c] = lower bound distance to centroid c
    const upper = new Array(n).fill(Infinity);

    // Initial full distance computation.
    for (let i = 0; i < n; i++) {
        lower[i] = new Array(k).fill(0);
        let best = 0;
        let bestD = dist2(X[i], centroids[0]);
        lower[i][0] = Math.sqrt(bestD);
        for (let c = 1; c < k; c++) {
            const d2 = dist2(X[i], centroids[c]);
            lower[i][c] = Math.sqrt(d2);
            if (d2 < bestD) {
                bestD = d2;
                best = c;
            }
        }
        assignments[i] = best;
        upper[i] = Math.sqrt(bestD);
    }

    for (let iter = 0; iter < iters; iter++) {
        // Recompute centroids.
        const sums = new Array(k).fill(0).map(() => new Array(nf).fill(0));
        const counts = new Array(k).fill(0);
        for (let i = 0; i < n; i++) {
            const c = assignments[i];
            counts[c]++;
            const x = X[i];
            for (let f = 0; f < nf; f++) sums[c][f] += x[f];
        }
        const oldCentroids = centroids;
        centroids = new Array(k);
        for (let c = 0; c < k; c++) {
            if (counts[c] > 0) {
                centroids[c] = new Array(nf);
                for (let f = 0; f < nf; f++) centroids[c][f] = sums[c][f] / counts[c];
            } else {
                centroids[c] = oldCentroids[c].slice();
            }
        }

        // Centroid movements.
        const move = new Array(k);
        for (let c = 0; c < k; c++) move[c] = sqrtDist2(centroids[c], oldCentroids[c]);

        // Update bounds.
        for (let i = 0; i < n; i++) {
            upper[i] += move[assignments[i]];
            for (let c = 0; c < k; c++) {
                lower[i][c] = Math.max(0, lower[i][c] - move[c]);
            }
        }

        // Assignment step with pruning.
        let changed = 0;
        for (let i = 0; i < n; i++) {
            const r = assignments[i];
            let z = Infinity;
            for (let c = 0; c < k; c++) {
                if (c !== r && lower[i][c] < z) z = lower[i][c];
            }
            if (upper[i] <= z) continue;

            // Tighten upper bound against current assigned centroid.
            const dR2 = dist2(X[i], centroids[r]);
            upper[i] = Math.sqrt(dR2);
            lower[i][r] = upper[i];
            if (upper[i] <= z) continue;

            let best = r;
            let bestD2 = dR2;
            for (let c = 0; c < k; c++) {
                if (c === r) continue;
                if (upper[i] <= lower[i][c]) continue;
                const d2 = dist2(X[i], centroids[c]);
                lower[i][c] = Math.sqrt(d2);
                if (d2 < bestD2) {
                    bestD2 = d2;
                    best = c;
                }
            }
            if (best !== r) {
                assignments[i] = best;
                upper[i] = Math.sqrt(bestD2);
                changed++;
            }
        }
        if (changed === 0) break;
    }

    // Final centroids matching the assignments.
    const sums = new Array(k).fill(0).map(() => new Array(nf).fill(0));
    const counts = new Array(k).fill(0);
    for (let i = 0; i < n; i++) {
        const c = assignments[i];
        counts[c]++;
        const x = X[i];
        for (let f = 0; f < nf; f++) sums[c][f] += x[f];
    }
    for (let c = 0; c < k; c++) {
        if (counts[c] > 0) {
            for (let f = 0; f < nf; f++) centroids[c][f] = sums[c][f] / counts[c];
        }
    }

    return { centroids, k, assignments };
}

globalThis.linearRegressionGD = kmeansElkan;
const linearRegressionGD = kmeansElkan;   // Forge Gate harness contract — do not remove
// Self-test: deterministic fixture from the Forge Gate kmeans oracle.
(function () {
    function lcg_next(s) {
        return ((s * 1664525 + 1013904223) & 0xFFFFFFFF) >>> 0;
    }
    function makeHarnessData() {
        let st = 12345 >>> 0;
        function normal_pair() {
            st = lcg_next(st);
            const u1 = Math.max(st / 0x100000000, 1e-10);
            st = lcg_next(st);
            const u2 = st / 0x100000000;
            const r = Math.sqrt(-2.0 * Math.log(u1));
            const theta = 2.0 * Math.PI * u2;
            return [r * Math.cos(theta), r * Math.sin(theta)];
        }
        const centers = [[0.0, 0.0], [5.0, 0.0], [2.5, 4.0]];
        const sigma = 0.5;
        const clusters = [[], [], []];
        for (let c = 0; c < 3; c++) {
            for (let i = 0; i < 20; i++) {
                const z = normal_pair();
                clusters[c].push([centers[c][0] + sigma * z[0], centers[c][1] + sigma * z[1]]);
            }
        }
        const X = [];
        for (let i = 0; i < 20; i++) {
            for (let c = 0; c < 3; c++) {
                X.push(clusters[c][i]);
            }
        }
        const y = [];
        return { X, y };
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
        if (!result || typeof result !== 'object') throw new Error('self-test: result is not an object');
        if (result.k !== 3) throw new Error('self-test: expected k=3, got ' + result.k);
        if (!Array.isArray(result.centroids) || result.centroids.length !== 3) {
            throw new Error('self-test: expected 3 centroids');
        }
        result.centroids.forEach(function (c, i) {
            if (!Array.isArray(c) || c.length !== 2) throw new Error('self-test: centroid ' + i + ' not length-2');
        });
        if (!Array.isArray(result.assignments) || result.assignments.length !== 60) {
            throw new Error('self-test: expected 60 assignments');
        }
    }

    const { X, y } = makeHarnessData();
    const result = kmeansElkan(X, y, 0.05, 200);
    assertShape(result);

    const expectedCentroids = [[0.11307742202213614,-0.1340640949477895],[5.011577170107475,-0.09160253629553519],[2.5341394147994447,3.8391060156544703]];
    const expectedAssignments = [0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2];

    if (!approxEqual(result.centroids, expectedCentroids, 1e-9)) {
        throw new Error('self-test: centroids mismatch');
    }
    if (!approxEqual(result.assignments, expectedAssignments, 1e-9)) {
        throw new Error('self-test: assignments mismatch');
    }
})();

