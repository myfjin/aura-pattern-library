// move_only_resource_handle — a move that copies the pointer but does not neuter the source
//
// WHY: writing your own move constructor is the moment you take responsibility for the moved-from
//      object. Copying the pointer out of the source is only half a move — the source still
//      holds it, so both destructors run and the resource is released twice.
// WHEN: implementing move semantics for a resource handle without nulling the source.
// GUARANTEES: a move must neuter the source. After a move the moved-from object must be
//      destructible and release nothing.
//
// DISASTER: both destructors free the same block because the source was not neutered.
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
    int* p;
    HandleBad() : p(new int[EXPECT_N]) {
        for (int i = 0; i < EXPECT_N; ++i) p[i] = i + 1;
    }
    HandleBad(HandleBad&& o) : p(o.p) {}   // copies pointer, does NOT null o.p
    ~HandleBad() { note_release(p); delete[] p; }
};

struct HandleGood {
    int* p;
    HandleGood() : p(new int[EXPECT_N]) {
        for (int i = 0; i < EXPECT_N; ++i) p[i] = i + 1;
    }
    HandleGood(HandleGood&& o) noexcept : p(o.p) { o.p = nullptr; }
    ~HandleGood() { if (p) { delete[] p; ++g_releases; } }
};

// Inside a helper that returns, so both destructors run and the double-free is unreachable-safe
static int unsafe_arm() {
    g_nreleased = 0; g_double_free = false;
    {
        HandleBad a;
        HandleBad b(std::move(a));
        // both a and b have the same p; both destructors will delete[] it
    }
    if (!g_double_free)
        fprintf(stderr, "unsafe arm released each pointer once - the disaster did not happen\n");
    return g_double_free ? 1 : 0;
}

static int safe_arm() {
    g_releases = 0;
    int* src_p_after = nullptr;
    long dst_sum = 0;
    {
        HandleGood a;
        HandleGood b(std::move(a));
        src_p_after = a.p;          // should be nullptr after move
        dst_sum = 0;
        for (int i = 0; i < EXPECT_N; ++i) dst_sum += b.p[i];
    }
    if (dst_sum != EXPECT_SUM) { fprintf(stderr, "FAIL: dst sum %ld != %ld\n", dst_sum, EXPECT_SUM); return 1; }
    if (src_p_after != nullptr) { fprintf(stderr, "FAIL: source not neutered\n"); return 1; }
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
    printf("PASS: neutered move summed %ld released once and the non-neutered double-free was caught as %s\n", EXPECT_SUM, EXPECTED);
    return 0;
}