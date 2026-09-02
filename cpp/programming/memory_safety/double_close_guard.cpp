// double_close_guard — explicit close plus destructor close is a double-free
//
// WHY: an explicit close() plus a destructor that also closes is two releases for one
//      acquisition. Each looks correct on its own; together they are fatal.
// WHEN: adding a close() method to a handle class that already releases in its destructor.
// GUARANTEES: a handle must record that it has been released, so the destructor is a no-op
//      after an explicit close — release must be idempotent.
//
// DISASTER: both close() and the destructor free the same block.
// PROOF: safe arm runs in-process and must be clean; unsafe arm runs in a child
//        (argv[1] == "--unsafe") and must produce the named failure signature below.
// EXPECTED FAILURE SIGNATURE: attempting double-free

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <cstdio>
#include <cstring>
#include <string>
#include <unistd.h>
#include <sys/wait.h>

static const char* EXPECTED = "attempting double-free";

// PORTABLE LEDGER: every release is recorded AT THE RELEASE SITE. A pointer offered a second
// time is an independent witness of a double-free; it is not derived from the value under test.
// ASan reports "attempting double-free" and corroborates on Linux; with no sanitizer
// (macOS/arm64, or the library's own -O2 harness) this ledger IS the oracle.
static const void* g_released[8];
static int  g_nreleased   = 0;
static bool g_double_free = false;
static void note_release(const void* p) {
    for (int i = 0; i < g_nreleased; ++i)
        if (g_released[i] == p) {
            g_double_free = true;
            // Report HERE, not at the end of the arm: without a sanitizer glibc aborts the
            // process inside the second delete, so a deferred check never runs.
            fprintf(stderr, "%s: the same pointer was released twice\n", EXPECTED);
            return;
        }
    if (g_nreleased < 8) g_released[g_nreleased++] = p;
}
static const long EXPECT_N = 16;
static const long EXPECT_SUM = 136;
static int g_releases = 0;

struct HandleBad {
    int* h;
    HandleBad() : h(new int[EXPECT_N]) {
        for (int i = 0; i < EXPECT_N; ++i) h[i] = i + 1;
    }
    void close() { note_release(h); delete[] h; }       // does NOT null h
    ~HandleBad() { note_release(h); delete[] h; }        // double-free if close() was called
};

struct HandleGood {
    int* h;
    HandleGood() : h(new int[EXPECT_N]) {
        for (int i = 0; i < EXPECT_N; ++i) h[i] = i + 1;
    }
    void close() { delete[] h; h = nullptr; ++g_releases; }
    ~HandleGood() { if (h) { delete[] h; ++g_releases; } }
    long sum() const {
        long s = 0;
        for (int i = 0; i < EXPECT_N; ++i) s += h[i];
        return s;
    }
};

static int unsafe_arm() {
    g_nreleased = 0; g_double_free = false;
    {
        HandleBad hb;
        hb.close();        // frees h, h is still pointing at freed memory
    }                     // ~HandleBad() calls delete[] h again — double-free
    if (!g_double_free)
        fprintf(stderr, "unsafe arm released each pointer once - the disaster did not happen\n");
    return g_double_free ? 1 : 0;
}

static int safe_arm() {
    g_releases = 0;
    {
        HandleGood hg;
        long s = hg.sum();
        if (s != EXPECT_SUM) { fprintf(stderr, "FAIL: sum %ld != %ld\n", s, EXPECT_SUM); return 1; }
        hg.close();         // frees h, nulls h, increments counter
    }                       // ~HandleGood() sees h == nullptr, no-op
    if (g_releases != 1) { fprintf(stderr, "FAIL: releases %d != 1\n", g_releases); return 1; }
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
    printf("PASS: idempotent close summed %ld released once and the double-free was caught as %s\n", EXPECT_SUM, EXPECTED);
    return 0;
}