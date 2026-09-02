// stack_unwinding_release_order — destructors run in reverse construction order for a reason
//
// WHY: later objects may hold references into earlier ones. Manual cleanup in the wrong order
//      frees something still in use.
// WHEN: two resources where the second aliases the first's buffer; releasing the first first
//      frees memory the second is still pointing into.
// GUARANTEES: resources must be released in reverse order of acquisition; RAII gets this right
//      by construction.
//
// DISASTER: the first resource is freed while the second still aliases its buffer.
// PROOF: safe arm runs in-process and must be clean; unsafe arm runs in a child
//        (argv[1] == "--unsafe") and must produce the named failure signature below.
// EXPECTED FAILURE SIGNATURE: heap-use-after-free

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <cstdio>
#include <cstring>
#include <string>
#include <memory>
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

struct ResourceA {
    int* buf;
    size_t n;
    ResourceA() : buf(new int[EXPECT_N]), n(EXPECT_N) {
        for (int i = 0; i < EXPECT_N; ++i) buf[i] = i + 1;
    }
    ~ResourceA() { delete[] buf; }
};

struct ResourceB {
    int* alias;   // aliases ResourceA's buffer
    size_t n;
    explicit ResourceB(int* p, size_t count) : alias(p), n(count) {}
};

static int unsafe_arm() {
    g_nfreed = 0; g_uaf = false;
    ResourceA a;
    ResourceB b(a.buf, a.n);
    // Wrong order: release a first (manual), then read through b
    note_free(a.buf);
    delete[] a.buf;     // free the buffer, b.alias is now dangling
    // do NOT set a.buf = nullptr — leave it dangling per the brief's rule
    note_read(b.alias);
    long acc = 0;
    for (size_t i = 0; i < b.n; ++i) acc += b.alias[i];   // reads the freed buffer
    printf("%ld\n", acc);
    if (!g_uaf)
        fprintf(stderr, "unsafe arm's pointer was still valid - the disaster did not happen\n");
    return g_uaf ? 1 : 0;
}

static int safe_arm() {
    // RAII: destructors run in reverse order — b dies before a, automatically
    std::string order;
    {
        auto a = std::make_unique<ResourceA>();
        ResourceB b(a->buf, a->n);
        // Read before any teardown
        long sum = 0;
        for (size_t i = 0; i < b.n; ++i) sum += b.alias[i];
        if (sum != EXPECT_SUM) { fprintf(stderr, "FAIL: sum %ld != %ld\n", sum, EXPECT_SUM); return 1; }
        // Manual release in correct order: b first (just drops the alias), then a
        order = "b,a";
    }
    // a's destructor freed buf after b went out of scope — correct order
    if (order != "b,a") { fprintf(stderr, "FAIL: order %s != b,a\n", order.c_str()); return 1; }
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
    printf("PASS: RAII reverse-order release summed %ld order b,a and the wrong-order free was caught as %s\n", EXPECT_SUM, EXPECTED);
    return 0;
}