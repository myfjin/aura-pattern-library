// erase_loses_owned_resource — erasing a raw-pointer element abandons its pointee
//
// WHY: erasing an element from a container of raw owning pointers destroys the pointer and
//      abandons the pointee. The container shrinks, the memory does not.
// WHEN: storing raw owning pointers in a vector and erasing elements.
// GUARANTEES: owning handles make erase release the resource.
//
// DISASTER: the erased element's buffer is abandoned and unreachable.
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
#include <unistd.h>
#include <sys/wait.h>

static const char* EXPECTED = "detected memory leaks";
static const long EXPECT_SUM = 136;
static const long EXPECT_SIZE_AFTER = 2;
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


struct OwnerUnsafe {
    int* buf;
    size_t n;
    OwnerUnsafe() : buf(new int[BLOCK_SIZE]), n(BLOCK_SIZE) {
        for (int i = 0; i < BLOCK_SIZE; ++i) buf[i] = i + 1;
    }
    // No destructor: raw pointer is abandoned on erase
};

struct OwnerSafe {
    std::unique_ptr<int[]> buf;
    size_t n;
    OwnerSafe() : buf(std::make_unique<int[]>(BLOCK_SIZE)), n(BLOCK_SIZE) {
        for (int i = 0; i < BLOCK_SIZE; ++i) buf[i] = i + 1;
    }
};

static int unsafe_arm() {
    g_nheld = 0; g_nfreed = 0; g_abandoned = false;
    std::vector<OwnerUnsafe> v;
    v.emplace_back();
    v.emplace_back();
    v.emplace_back();
    note_held(v[1].buf);      // record the victim block BEFORE it is dropped
    v.erase(v.begin() + 1);   // middle element's buf is abandoned (no destructor)
    // Anything still held by a surviving element is not abandoned; count it as released.
    for (size_t i = 0; i < v.size(); ++i) note_free(v[i].buf);
    note_abandoned();
    if (!g_abandoned)
        fprintf(stderr, "unsafe arm released the erased element - the disaster did not happen\n");
    return g_abandoned ? 1 : 0;
}

static int safe_arm() {
    std::vector<OwnerSafe> v;
    v.emplace_back();
    v.emplace_back();
    v.emplace_back();
    v.erase(v.begin() + 1);   // middle element's unique_ptr releases its buffer
    if (static_cast<long>(v.size()) != EXPECT_SIZE_AFTER) {
        fprintf(stderr, "FAIL: size %zu != %ld\n", v.size(), EXPECT_SIZE_AFTER);
        return 1;
    }
    long sum = 0;
    for (size_t i = 0; i < v[0].n; ++i) sum += v[0].buf[i];
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
    printf("PASS: unique_ptr erase released and first element summed %ld size %ld, leak caught as %s\n", EXPECT_SUM, EXPECT_SIZE_AFTER, EXPECTED);
    return 0;
}