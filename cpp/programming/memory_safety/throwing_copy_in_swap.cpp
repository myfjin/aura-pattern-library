// throwing_copy_in_swap — a swap that can throw leaves both objects broken
//
// WHY: swap must be noexcept. A swap that throws halfway leaves both objects sharing or
//      losing buffers, and the object you did not touch is the one that breaks.
// WHEN: writing a swap that copies data instead of just exchanging pointers.
// GUARANTEES: a correct swap only exchanges pointers — no allocation, no copying.
//
// DISASTER: the swap frees one side's buffer and throws, leaving a dangling pointer.
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
#include <algorithm>
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
static const long EXPECT_SUM = 36;

struct Buf {
    int* d;
    size_t n;
    Buf(const int* src, size_t count) : n(count) {
        d = new int[count];
        std::memcpy(d, src, count * sizeof(int));
    }
    ~Buf() { delete[] d; }

    long sum() const {
        long s = 0;
        for (size_t i = 0; i < n; ++i) s += d[i];
        return s;
    }
};

// Bad swap: frees one side's buffer, then throws before completing the exchange
void bad_swap(Buf& a, Buf& b) {
    note_free(b.d);
    delete[] b.d;                        // free b's buffer, b.d is now dangling
    throw std::runtime_error("swap threw halfway");
    // never reached: b.d is dangling, a is untouched
}

// Good swap: pointer-only, noexcept
void good_swap(Buf& a, Buf& b) noexcept {
    std::swap(a.d, b.d);
    std::swap(a.n, b.n);
}

static int unsafe_arm() {
    g_nfreed = 0; g_uaf = false;
    int vals[8] = {1, 2, 3, 4, 5, 6, 7, 8};
    Buf x(vals, 8);
    Buf y(vals, 8);
    try {
        bad_swap(x, y);
    } catch (...) {}
    // y.d was freed and is dangling — read it
    note_read(y.d);
    long acc = 0;
    for (size_t i = 0; i < y.n; ++i) acc += y.d[i];   // heap-use-after-free
    printf("%ld\n", acc);
    if (!g_uaf)
        fprintf(stderr, "unsafe arm's pointer was still valid - the disaster did not happen\n");
    return g_uaf ? 1 : 0;
}

static int safe_arm() {
    int vals[8] = {1, 2, 3, 4, 5, 6, 7, 8};
    Buf x(vals, 8);
    Buf y(vals, 8);
    good_swap(x, y);
    // x now holds what y held, y holds what x held
    long sx = x.sum();
    long sy = y.sum();
    if (sx != EXPECT_SUM) { fprintf(stderr, "FAIL: x sum %ld != %ld\n", sx, EXPECT_SUM); return 1; }
    if (sy != EXPECT_SUM) { fprintf(stderr, "FAIL: y sum %ld != %ld\n", sy, EXPECT_SUM); return 1; }
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
    printf("PASS: noexcept swap preserved sum %ld on both sides and the throwing swap was caught as %s\n", EXPECT_SUM, EXPECTED);
    return 0;
}