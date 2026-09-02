// vector_push_back_strong_guarantee — growth must not free the old buffer until the new one is ready
//
// WHY: push_back promises the strong guarantee — if it throws, the vector is exactly as it was.
// WHEN: a hand-rolled container that frees the old buffer before the new one is safely filled.
// GUARANTEES: do the throwing work first, then swap; the old buffer survives any failure.
//
// DISASTER: the container's storage pointer is freed and dangling after a failed growth.
// PROOF: safe arm runs in-process and must be clean; unsafe arm runs in a child
//        (argv[1] == "--unsafe") and must produce the named failure signature below.
// EXPECTED FAILURE SIGNATURE: heap-use-after-free

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <cstdio>
#include <cstring>
#include <string>
#include <stdexcept>
#include <unistd.h>
#include <sys/wait.h>

static const char* EXPECTED = "heap-use-after-free";

// PORTABLE LEDGER: the address is recorded AT THE RELEASE, and the pointer about to be read is
// looked up in that set BEFORE the read. Both are observed events, not values derived from the
// thing under test. ASan reports heap-use-after-free and corroborates on Linux; with no
// sanitizer (macOS/arm64, or the library's own -O2 harness) this ledger IS the oracle.
// It must report BEFORE the read: the read itself may kill the process.
static const void* g_freed[8];
static int  g_nfreed = 0;
static bool g_uaf    = false;
static void note_free(const void* p) { if (g_nfreed < 8) g_freed[g_nfreed++] = p; }
static void note_read(const void* p) {
    for (int i = 0; i < g_nfreed; ++i)
        if (g_freed[i] == p) {
            g_uaf = true;
            fprintf(stderr, "%s: reading through %p, which was already released\n", EXPECTED, p);
            return;
        }
}
static const long EXPECT_SUM = 10;

struct BadVector {
    int* d;
    size_t n, cap;
    BadVector() : d(nullptr), n(0), cap(0) {}
    ~BadVector() { delete[] d; }

    void push(int val) {
        if (n == cap) {
            size_t newcap = cap ? cap * 2 : 4;
            note_free(d);
            delete[] d;                    // free old buffer, d is now dangling
            // simulate a throwing allocation step on the second growth
            if (newcap == 8) throw std::runtime_error("growth failed");
            d = new int[newcap];           // never reached on throw
            cap = newcap;
        }
        d[n++] = val;
    }

    long sum() const {
        long s = 0;
        for (size_t i = 0; i < n; ++i) s += d[i];
        return s;
    }
};

struct GoodVector {
    int* d;
    size_t n, cap;
    GoodVector() : d(nullptr), n(0), cap(0) {}
    ~GoodVector() { delete[] d; }

    void push(int val) {
        if (n == cap) {
            size_t newcap = cap ? cap * 2 : 4;
            int* newd = new int[newcap];
            for (size_t i = 0; i < n; ++i) newd[i] = d[i];
            if (newcap == 8) {
                delete[] newd;
                throw std::runtime_error("growth failed");
            }
            delete[] d;
            d = newd;
            cap = newcap;
        }
        d[n++] = val;
    }

    long sum() const {
        long s = 0;
        for (size_t i = 0; i < n; ++i) s += d[i];
        return s;
    }
};

static int unsafe_arm() {
    g_nfreed = 0; g_uaf = false;
    BadVector v;
    v.push(1); v.push(2); v.push(3); v.push(4);
    try {
        v.push(5);   // at capacity, frees old buffer, then throws
    } catch (...) {}
    note_read(v.d);
    long acc = 0;
    for (size_t i = 0; i < v.n; ++i) acc += v.d[i];   // reads the freed buffer
    printf("%ld\n", acc);
    if (!g_uaf)
        fprintf(stderr, "unsafe arm's pointer was still valid - the disaster did not happen\n");
    return g_uaf ? 1 : 0;
}

static int safe_arm() {
    GoodVector v;
    v.push(1); v.push(2); v.push(3); v.push(4);
    try {
        v.push(5);   // allocates new buffer first, throws before swap
    } catch (...) {}
    long s = v.sum();
    if (s != EXPECT_SUM) { fprintf(stderr, "FAIL: sum %ld != %ld\n", s, EXPECT_SUM); return 1; }
    if (v.n != 4) { fprintf(stderr, "FAIL: size %zu != 4\n", v.n); return 1; }
    return 0;
}

static int run_child_and_check(const char* self) {
    int fd[2];
    if (pipe(fd) != 0) { fprintf(stderr, "FAIL: pipe\n"); return -1; }
    pid_t pid = fork();
    if (pid < 0) { fprintf(stderr, "FAIL: fork\n"); return -1; }
    if (pid == 0) {
        dup2(fd[1], 2); close(fd[0]); close(fd[1]);
        execl(self, self, "--unsafe", (char*)nullptr);
        _exit(127);
    }
    close(fd[1]);
    std::string err; char buf[4096]; ssize_t n;
    while ((n = read(fd[0], buf, sizeof buf)) > 0) err.append(buf, n);
    close(fd[0]);
    int st = 0; waitpid(pid, &st, 0);
    bool died  = !(WIFEXITED(st) && WEXITSTATUS(st) == 0);
    bool named = err.find(EXPECTED) != std::string::npos;
    if (!died)  { fprintf(stderr, "FAIL: unsafe arm exited 0 - disaster did not happen\n"); return 1; }
    if (!named) { fprintf(stderr, "FAIL: child failed but no '%s' report\n", EXPECTED); return 1; }
    return 0;
}

int main(int argc, char** argv) {
    if (argc > 1 && std::strcmp(argv[1], "--unsafe") == 0) return unsafe_arm();
    if (safe_arm() != 0) { fprintf(stderr, "FAIL: safe arm did not hold\n"); return 2; }
    if (run_child_and_check(argv[0]) != 0) return 3;
    printf("PASS: allocate-first preserved sum %ld size 4 and the dangling storage was caught as %s\n", EXPECT_SUM, EXPECTED);
    return 0;
}