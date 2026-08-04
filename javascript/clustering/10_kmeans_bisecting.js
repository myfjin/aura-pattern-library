// @forge-family kmeans

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/**
 * Bisecting k-means.
 *
 * Starts with one cluster containing all points, then repeatedly splits the
 * cluster with the largest within-cluster SSE using 2-means until k clusters
 * exist. Bisecting k-means may stop at a non-Lloyd configuration, so the final
 * step runs full Lloyd iterations on the complete data set.
 *
 * @param {number[][]} X - data matrix
 * @param {number[]} y - unused target vector (harness contract)
 * @param {number} lr - unused learning rate (harness contract)
 * @param {number} iters - maximum iterations
 * @returns {{centroids:number[][], k:number, assignments:number[]}}
 */
function kmeansBisecting(X, y, lr, iters) {
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

    function nearest(x, centroids) {
        let best = 0;
        let bestD = dist2(x, centroids[0]);
        for (let c = 1; c < centroids.length; c++) {
            const d = dist2(x, centroids[c]);
            if (d < bestD) {
                bestD = d;
                best = c;
            }
        }
        return best;
    }

    function centroidOf(indices) {
        const mean = new Array(nf).fill(0);
        if (indices.length === 0) return mean;
        for (let i = 0; i < indices.length; i++) {
            const x = X[indices[i]];
            for (let f = 0; f < nf; f++) mean[f] += x[f];
        }
        for (let f = 0; f < nf; f++) mean[f] /= indices.length;
        return mean;
    }

    function lloyd2(indices) {
        // 2-means on a subset; farthest-point seeding within the subset.
        const subset = indices.map(i => X[i]);
        const c0 = subset[0].slice();
        let far = 0;
        let farD = dist2(c0, subset[0]);
        for (let i = 1; i < subset.length; i++) {
            const d = dist2(c0, subset[i]);
            if (d > farD) {
                farD = d;
                far = i;
            }
        }
        let centroids = [c0, subset[far].slice()];
        const assigns = new Array(indices.length).fill(0);
        for (let iter = 0; iter < iters; iter++) {
            let changed = 0;
            for (let i = 0; i < subset.length; i++) {
                const c = nearest(subset[i], centroids);
                if (assigns[i] !== c) {
                    assigns[i] = c;
                    changed++;
                }
            }
            const sums = [new Array(nf).fill(0), new Array(nf).fill(0)];
            const counts = [0, 0];
            for (let i = 0; i < subset.length; i++) {
                const c = assigns[i];
                counts[c]++;
                const x = subset[i];
                for (let f = 0; f < nf; f++) sums[c][f] += x[f];
            }
            for (let c = 0; c < 2; c++) {
                if (counts[c] > 0) {
                    for (let f = 0; f < nf; f++) centroids[c][f] = sums[c][f] / counts[c];
                }
            }
            if (changed === 0) break;
        }
        return centroids;
    }

    // Initially one cluster with all points.
    let clusters = [{ indices: new Array(n).fill(0).map((_, i) => i), centroid: centroidOf(new Array(n).fill(0).map((_, i) => i)) }];

    while (clusters.length < k) {
        // Pick cluster with largest SSE.
        let worst = 0;
        let worstSSE = 0;
        for (let c = 0; c < clusters.length; c++) {
            const ctr = clusters[c].centroid;
            let sse = 0;
            for (const i of clusters[c].indices) sse += dist2(X[i], ctr);
            if (sse > worstSSE) {
                worstSSE = sse;
                worst = c;
            }
        }
        const parent = clusters[worst];
        const children = lloyd2(parent.indices);
        // Replace parent with its two children in the list.
        const left = { indices: [], centroid: children[0] };
        const right = { indices: [], centroid: children[1] };
        for (const i of parent.indices) {
            if (dist2(X[i], children[0]) <= dist2(X[i], children[1])) {
                left.indices.push(i);
            } else {
                right.indices.push(i);
            }
        }
        if (left.indices.length === 0 || right.indices.length === 0) {
            // Degenerate split: force split by halves.
            const half = Math.floor(parent.indices.length / 2);
            left.indices = parent.indices.slice(0, half);
            right.indices = parent.indices.slice(half);
        }
        left.centroid = centroidOf(left.indices);
        right.centroid = centroidOf(right.indices);
        clusters.splice(worst, 1, left, right);
    }

    let centroids = clusters.map(c => c.centroid);

    // Final full-data Lloyd pass to enforce the fixed-point condition.
    const assignments = new Array(n).fill(0);
    for (let iter = 0; iter < iters; iter++) {
        let changed = 0;
        for (let i = 0; i < n; i++) {
            const c = nearest(X[i], centroids);
            if (assignments[i] !== c) {
                assignments[i] = c;
                changed++;
            }
        }
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
        if (changed === 0) break;
    }

    for (let i = 0; i < n; i++) assignments[i] = nearest(X[i], centroids);
    return { centroids, k, assignments };
}

globalThis.linearRegressionGD = kmeansBisecting;
const linearRegressionGD = kmeansBisecting;   // Forge Gate harness contract — do not remove
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
    const result = kmeansBisecting(X, y, 0.05, 200);
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

