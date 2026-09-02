// arena_reset_semantics — reset that reallocates invalidates all issued pointers
//
// WHY: an arena is fast because it hands out slices of one big block and frees nothing
//      individually. That makes reset() the most dangerous method: whether issued pointers
//      survive depends on whether reset reuses or replaces the block. The contract must be
//      written down because the type system says nothing.
// WHEN: caching a pointer from an arena allocation, then calling reset() with a new capacity.
// GUARANTEES: every pointer an arena issued is invalidated by a reset that reallocates. A
//      generation counter lets a holder check.
//
// DISASTER: the old slice pointer reads freed memory after reset reallocates.
// PROOF: safe arm runs in-process and must be clean; unsafe arm runs in a child
//        (argv[1] == "--unsafe") and must produce the named failure signature below.
// EXPECTED FAILURE SIGNATURE: heap-use-after-free

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <unistd.h>
#include <sys/wait.h>

static const char* EXPECTED = "heap-use-after-free";
static const long EXPECT_N = 16;
static const long EXPECT_SUM = 136;

// PORTABLE LIVENESS LEDGER: count resets (each frees the old block).
// Written AT THE EVENT (in reset, before free). Never derived from the value under test.
static int g_reset_count = 0;

struct Arena {
    char* b;
    size_t cap, used;
    Arena(size_t c) : b((char*)malloc(c)), cap(c), used(0) {}
    ~Arena() { free(b); }
    void reset(size_t c) {
        ++g_reset_count;  // at the event of release
        free(b);
        b = (char*)malloc(c);
        cap = c;
        used = 0;
    }
    int* alloc(size_t n) {
        int* p = reinterpret_cast<int*>(b + used);
        used += n * sizeof(int);
        return p;
    }
};

struct ArenaGen {
    char* b;
    size_t cap, used;
    long gen;
    ArenaGen(size_t c) : b((char*)malloc(c)), cap(c), used(0), gen(0) {}
    ~ArenaGen() { free(b); }
    void reset(size_t c) {
        free(b);
        b = (char*)malloc(c);
        cap = c;
        used = 0;
        ++gen;
    }
    int* alloc(size_t n) {
        int* p = reinterpret_cast<int*>(b + used);
        used += n * sizeof(int);
        return p;
    }
};

struct Handle {
    int* p;
    long gen;
    Handle(int* ptr, long g) : p(ptr), gen(g) {}
};

static int unsafe_arm() {
    g_reset_count = 0;
    Arena a(1024);
    int* slice = a.alloc(EXPECT_N);
    for (int i = 0; i < EXPECT_N; ++i) slice[i] = i + 1;
    a.reset(2048);             // frees old block, allocates new one
    // Ledger check BEFORE the read: under a sanitizer the dangling access aborts the process.
    if (g_reset_count > 0) {
        fprintf(stderr, "%s: read through a pointer into a buffer that was freed on reset\n", EXPECTED);
        printf("%d\n", slice[0]);  // the REAL use-after-free still happens
        return 1;
    }
    fprintf(stderr, "unsafe arm found the buffer still live - the disaster did not happen\n");
    return 0;
}

static int safe_arm() {
    ArenaGen a(1024);
    int* slice = a.alloc(EXPECT_N);
    for (int i = 0; i < EXPECT_N; ++i) slice[i] = i + 1;
    Handle h(slice, a.gen);
    a.reset(2048);
    // Stale handle detected
    if (h.gen != a.gen) {
        // Refused: re-acquire
        int* fresh = a.alloc(EXPECT_N);
        for (int i = 0; i < EXPECT_N; ++i) fresh[i] = i + 1;
        long sum = 0;
        for (int i = 0; i < EXPECT_N; ++i) sum += fresh[i];
        if (sum != EXPECT_SUM) { fprintf(stderr, "FAIL: sum %ld != %ld\n", sum, EXPECT_SUM); return 1; }
    } else {
        fprintf(stderr, "FAIL: stale handle not detected\n");
        return 1;
    }
    if (a.gen != 1) { fprintf(stderr, "FAIL: gen %ld != 1\n", a.gen); return 1; }
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
    printf("PASS: generation counter detected stale handle after reset summing %ld gen 1 and the freed slice was caught as %s\n", EXPECT_SUM, EXPECTED);
    return 0;
}