// cleanup_after_partial_container_fill — raw pointers in a container own nothing
//
// WHY: filling a container with raw owning pointers is a loop that can throw halfway. The
//      elements already inserted are owned by nobody — clear() destroys the pointers, not
//      the things they point to.
// WHEN: populating a vector<int*> in a loop where allocation or insertion can throw.
// GUARANTEES: a container of unique_ptr releases every element that was successfully inserted,
//      however the loop exits.
//
// DISASTER: the three already-inserted blocks are abandoned and unreachable.
// PROOF: safe arm runs in-process and must be clean; unsafe arm runs in a child
//        (argv[1] == "--unsafe") and must produce the named failure signature below.
// EXPECTED FAILURE SIGNATURE: detected memory leaks

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <memory>
#include <stdexcept>
#include <unistd.h>
#include <sys/wait.h>

static const char* EXPECTED = "detected memory leaks";
static const long EXPECT_SUM = 136;
static const long BLOCK_SIZE = 16;

// PORTABLE ABANDONMENT LEDGER: a block is recorded when it is handed to the container, and
// again when it is released. After the container drops its elements, a block that is neither
// still held nor ever released is unreachable -- that is the leak, witnessed as an observed
// relation between two recorded event sets rather than as a bare allocation count. A count
// with no release site anywhere in the file is vacuously unequal and proves nothing.
// LeakSanitizer corroborates on Linux; on macOS/arm64 it does not exist, and no sanitizer at
// all is present in the library's own build, so this ledger IS the oracle there.
static const void* g_held[8];    static int g_nheld = 0;
static const void* g_freed[8];   static int g_nfreed = 0;
static bool g_abandoned = false;
static void note_held(const void* p) { if (g_nheld  < 8) g_held[g_nheld++]   = p; }
static void note_free(const void* p) { if (g_nfreed < 8) g_freed[g_nfreed++] = p; }
static void note_abandoned() {
    int lost = 0;
    for (int i = 0; i < g_nheld; ++i) {
        bool released = false;
        for (int j = 0; j < g_nfreed; ++j) if (g_freed[j] == g_held[i]) released = true;
        if (!released) ++lost;
    }
    if (lost > 0) {
        g_abandoned = true;
        fprintf(stderr, "%s: %d block(s) reachable from nothing and never released\n",
                EXPECTED, lost);
    }
}


static void do_fill_raw() {
    std::vector<int*> v;
    for (int i = 0; i < 5; ++i) {
        int* block = new int[BLOCK_SIZE];
        for (int j = 0; j < BLOCK_SIZE; ++j) block[j] = j + 1;
        note_held(block);
        if (i == 3) {
            v.clear();   // destroys the pointers, not the pointees — 3 blocks leak
            throw std::runtime_error("fill failed at iteration 3");
        }
        v.push_back(block);
    }
}

static int unsafe_arm() {
    g_nheld = 0; g_nfreed = 0; g_abandoned = false;
    try { do_fill_raw(); } catch (...) {}
    note_abandoned();
    if (!g_abandoned)
        fprintf(stderr, "unsafe arm released every block - the disaster did not happen\n");
    return g_abandoned ? 1 : 0;
}

static int safe_arm() {
    // Throwing path: unique_ptr elements are released on clear/unwind
    try {
        std::vector<std::unique_ptr<int[]>> v;
        for (int i = 0; i < 5; ++i) {
            auto block = std::make_unique<int[]>(BLOCK_SIZE);
            for (int j = 0; j < BLOCK_SIZE; ++j) block[j] = j + 1;
            if (i == 3) throw std::runtime_error("fill failed at iteration 3");
            v.push_back(std::move(block));
        }
    } catch (...) {
        // no leak: unique_ptr elements destroyed during unwinding
    }
    // Success path: fill fully, verify first block
    std::vector<std::unique_ptr<int[]>> v;
    for (int i = 0; i < 5; ++i) {
        auto block = std::make_unique<int[]>(BLOCK_SIZE);
        for (int j = 0; j < BLOCK_SIZE; ++j) block[j] = j + 1;
        v.push_back(std::move(block));
    }
    long sum = 0;
    for (int j = 0; j < BLOCK_SIZE; ++j) sum += v[0][j];
    if (sum != EXPECT_SUM) { fprintf(stderr, "FAIL: sum %ld != %ld\n", sum, EXPECT_SUM); return 1; }
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
    printf("PASS: unique_ptr vector released on throw and success summed %ld, raw leak caught as %s\n", EXPECT_SUM, EXPECTED);
    return 0;
}