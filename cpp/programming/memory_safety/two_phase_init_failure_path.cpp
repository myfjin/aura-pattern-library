// two_phase_init_failure_path — failed init must leave the object refusing use
//
// WHY: two-phase init (ctor then init()) means an object can exist in a failed state. The
//      dangerous version allocates, rolls back, and leaves the pointer looking valid.
// WHEN: a constructor cannot complete, so init() does the heavy lifting — but failure cleanup
//      leaves a dangling pointer instead of clearing it.
// GUARANTEES: a failed init() must clear the pointer AND record the failure; callers must check
//      the return value before any accessor.
//
// DISASTER: the caller ignores the failure return and reads through the dangling pointer.
// PROOF: safe arm runs in-process and must be clean; unsafe arm runs in a child
//        (argv[1] == "--unsafe") and must produce the named failure signature below.
// EXPECTED FAILURE SIGNATURE: heap-use-after-free

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <cstdio>
#include <cstring>
#include <string>
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
static const long EXPECT_SUM = 136;
static const long EXPECT_N = 16;

struct TwoPhase {
    int* buf;
    size_t n;
    bool ok;

    TwoPhase() : buf(nullptr), n(0), ok(false) {}
    ~TwoPhase() { delete[] buf; }

    bool init(bool succeed) {
        delete[] buf;
        buf = new int[EXPECT_N];
        n = EXPECT_N;
        for (int i = 0; i < EXPECT_N; ++i) buf[i] = i + 1;
        if (!succeed) {
            note_free(buf);
            delete[] buf;       // free the buffer...
            // BUG: do NOT clear buf — it still points at the freed block
            n = EXPECT_N;       // and n still looks valid
            ok = false;
            return false;
        }
        ok = true;
        return true;
    }

    long sum() const {
        long s = 0;
        for (size_t i = 0; i < n; ++i) s += buf[i];
        return s;
    }
};

struct TwoPhaseSafe {
    int* buf;
    size_t n;
    bool ok;

    TwoPhaseSafe() : buf(nullptr), n(0), ok(false) {}
    ~TwoPhaseSafe() { delete[] buf; }

    bool init(bool succeed) {
        delete[] buf;
        buf = nullptr;
        n = 0;
        ok = false;
        if (!succeed) return false;
        buf = new int[EXPECT_N];
        n = EXPECT_N;
        for (int i = 0; i < EXPECT_N; ++i) buf[i] = i + 1;
        ok = true;
        return true;
    }

    long sum() const {
        if (!ok) return -1;
        long s = 0;
        for (size_t i = 0; i < n; ++i) s += buf[i];
        return s;
    }
};

static int unsafe_arm() {
    g_nfreed = 0; g_uaf = false;
    TwoPhase tp;
    tp.init(false);   // allocates, frees, leaves buf dangling — return value ignored
    note_read(tp.buf);
    long acc = 0;
    for (size_t i = 0; i < tp.n; ++i) acc += tp.buf[i];   // reads the freed buffer
    printf("%ld\n", acc);
    if (!g_uaf)
        fprintf(stderr, "unsafe arm's pointer was still valid - the disaster did not happen\n");
    return g_uaf ? 1 : 0;
}

static int safe_arm() {
    TwoPhaseSafe tp;
    if (!tp.init(false)) {
        // accessor refuses
        if (tp.sum() != -1) { fprintf(stderr, "FAIL: accessor did not refuse after failed init\n"); return 1; }
    } else {
        fprintf(stderr, "FAIL: init(false) returned true\n"); return 1;
    }
    // success path
    if (!tp.init(true)) { fprintf(stderr, "FAIL: init(true) returned false\n"); return 1; }
    long s = tp.sum();
    if (s != EXPECT_SUM) { fprintf(stderr, "FAIL: sum %ld != %ld\n", s, EXPECT_SUM); return 1; }
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
    printf("PASS: safe accessor refused after failed init and success summed %ld, dangling was caught as %s\n", EXPECT_SUM, EXPECTED);
    return 0;
}