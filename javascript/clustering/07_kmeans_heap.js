// @forge-family kmeans

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/**
 * Heap-based k-means.
 *
 * Maintains each point's upper bound and a max-heap over those bounds. At each
 * iteration the heap is used to process the points most likely to change
 * assignment first, tightening bounds lazily. The final centroids are exact
 * cluster means.
 *
 * @param {number[][]} X - data matrix
 * @param {number[]} y - unused target vector (harness contract)
 * @param {number} lr - unused learning rate (harness contract)
 * @param {number} iters - maximum iterations
 * @returns {{centroids:number[][], k:number, assignments:number[]}}
 */
function kmeansHeap(X, y, lr, iters) {
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

    function nearestFull(x, centroids) {
        let best = 0;
        let bestD = dist2(x, centroids[0]);
        let second = Infinity;
        for (let c = 1; c < k; c++) {
            const d = dist2(x, centroids[c]);
            if (d < bestD) {
                second = bestD;
                bestD = d;
                best = c;
            } else if (d < second) {
                second = d;
            }
        }
        return { best, bestD, second };
    }

    let centroids = new Array(k);
    for (let c = 0; c < k; c++) centroids[c] = X[c].slice();

    const assignments = new Array(n).fill(0);
    const upper = new Array(n).fill(Infinity);
    const lower = new Array(n).fill(0); // lower bound to second closest

    // Initial exact assignment + heap seeding.
    const heap = new Array(n);
    for (let i = 0; i < n; i++) {
        const r = nearestFull(X[i], centroids);
        assignments[i] = r.best;
        upper[i] = Math.sqrt(r.bestD);
        lower[i] = Math.sqrt(r.second);
        heap[i] = i;
    }

    function heapify() {
        for (let i = Math.floor(n / 2) - 1; i >= 0; i--) siftDown(i);
    }
    function siftDown(i) {
        while (true) {
            const l = 2 * i + 1;
            const r = 2 * i + 2;
            let largest = i;
            if (l < n && upper[heap[l]] > upper[heap[i]]) largest = l;
            if (r < n && upper[heap[r]] > upper[heap[largest]]) largest = r;
            if (largest === i) break;
            const tmp = heap[i];
            heap[i] = heap[largest];
            heap[largest] = tmp;
            i = largest;
        }
    }
    function popMax() {
        const top = heap[0];
        heap[0] = heap[n - 1];
        heap[n - 1] = top;
        siftDown(0);
        return top;
    }

    heapify();

    for (let iter = 0; iter < iters; iter++) {
        // Recompute centroids and record movements.
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
        const move = new Array(k);
        for (let c = 0; c < k; c++) {
            if (counts[c] > 0) {
                centroids[c] = new Array(nf);
                for (let f = 0; f < nf; f++) centroids[c][f] = sums[c][f] / counts[c];
            } else {
                centroids[c] = oldCentroids[c].slice();
            }
            move[c] = Math.sqrt(dist2(centroids[c], oldCentroids[c]));
        }

        // Update bounds.
        for (let i = 0; i < n; i++) {
            const r = assignments[i];
            upper[i] += move[r];
            lower[i] = Math.max(0, lower[i] - Math.max(...move));
        }
        heapify();

        let changed = 0;
        let remaining = n;
        while (remaining > 0) {
            const i = popMax();
            remaining--;
            if (upper[i] <= lower[i]) continue;
            const r = assignments[i];
            const dR = Math.sqrt(dist2(X[i], centroids[r]));
            upper[i] = dR;
            if (upper[i] <= lower[i]) continue;

            const full = nearestFull(X[i], centroids);
            if (full.best !== r) {
                assignments[i] = full.best;
                changed++;
            }
            upper[i] = Math.sqrt(full.bestD);
            lower[i] = Math.sqrt(full.second);
        }
        // Restore heap size for next iteration (we never shrank array, just re-heapify).
        heapify();
        if (changed === 0) break;
    }

    // Final centroids matching assignments.
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

globalThis.linearRegressionGD = kmeansHeap;
const linearRegressionGD = kmeansHeap;   // Forge Gate harness contract — do not remove
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
        assert(result.k === 3, 'self-test: expected k=3, got ' + result.k);
        assert(Array.isArray(result.centroids) && result.centroids.length === 3, 'self-test: expected 3 centroids');
        result.centroids.forEach(function (c, i) {
            assert(Array.isArray(c) && c.length === 2, 'self-test: centroid ' + i + ' not length-2');
        });
        assert(Array.isArray(result.assignments) && result.assignments.length === 60, 'self-test: expected 60 assignments');
    }

    const { X, y } = makeHarnessData();
    const result = kmeansHeap(X, y, 0.05, 200);
    assertShape(result);

    const expectedCentroids = [[0.11307742202213614,-0.1340640949477895],[5.011577170107475,-0.09160253629553519],[2.5341394147994447,3.8391060156544703]];
    const expectedAssignments = [0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2];

    assert(approxEqual(result.centroids, expectedCentroids, 1e-9), 'self-test: centroids mismatch');
    assert(approxEqual(result.assignments, expectedAssignments, 1e-9), 'self-test: assignments mismatch');
})();

