// small_buffer_boundary — crossing the inline/heap boundary invalidates all pointers
//
// WHY: small-buffer optimisation keeps a few elements inside the object and spills to the heap
//      only when it must. A pointer into such a container is valid or dangling depending on a
//      size change that crosses the boundary in either direction, moving the data.
// WHEN: caching data() from an SBO container, then resizing across the inline/heap boundary.
// GUARANTEES: a pointer obtained from an SBO container is invalidated by any size change that
//      crosses the inline/heap boundary. data() must be re-read after every resize.
//
// DISASTER: the old heap pointer reads freed memory after shrink copies data back to inline.
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

// PORTABLE WITNESS: the captured pointer is compared against the container's CURRENT storage.
// After shrink() the data lives inline again, so a differing address means `old` names the
// freed heap block. Observed at the moment of the read, reported before it.
static bool g_dangling = false;
static void note_moved(const void* captured, const void* current) {
    if (captured != current) {
        g_dangling = true;
        fprintf(stderr, "%s: captured %p but the storage moved to %p - the capture is freed\n",
                EXPECTED, captured, current);
    }
}
static const long INLINE_CAP = 4;
static const long EXPECT_SUM_SMALL = 10;
static const long EXPECT_SUM_BIG = 136;

struct SBO {
    int inl[4];
    int* p;
    size_t n;
    bool heap;

    SBO() : p(inl), n(0), heap(false) {}

    void grow(size_t target) {
        if (target <= 4) {
            n = target;
            return;
        }
        int* newbuf = (int*)malloc(target * sizeof(int));
        for (size_t i = 0; i < n; ++i) newbuf[i] = inl[i];
        p = newbuf;
        heap = true;
        n = target;
    }

    void shrink(size_t target) {
        if (target > 4) {
            n = target;
            return;
        }
        for (size_t i = 0; i < target; ++i) inl[i] = p[i];
        free(p);
        p = inl;
        heap = false;
        n = target;
    }

    long sum() const {
        long s = 0;
        for (size_t i = 0; i < n; ++i) s += p[i];
        return s;
    }
};

static int unsafe_arm() {
    g_dangling = false;
    SBO c;
    c.grow(16);
    for (int i = 0; i < 16; ++i) c.p[i] = i + 1;
    int* old = c.p;           // pointer into the heap block
    c.shrink(4);              // copies back to inline, frees the heap block
    note_moved(old, c.p);
    printf("%d\n", old[0]);   // heap-use-after-free: reads the freed heap block
    if (!g_dangling)
        fprintf(stderr, "unsafe arm's pointer was still valid - the disaster did not happen\n");
    return g_dangling ? 1 : 0;
}

static int safe_arm() {
    SBO c;
    c.grow(16);
    for (int i = 0; i < 16; ++i) c.p[i] = i + 1;
    long big_sum = c.sum();
    if (big_sum != EXPECT_SUM_BIG) { fprintf(stderr, "FAIL: big sum %ld != %ld\n", big_sum, EXPECT_SUM_BIG); return 1; }

    c.shrink(4);
    // Re-read p after shrink
    int* fresh = c.p;
    long small_sum = 0;
    for (size_t i = 0; i < c.n; ++i) small_sum += fresh[i];
    if (small_sum != EXPECT_SUM_SMALL) { fprintf(stderr, "FAIL: small sum %ld != %ld\n", small_sum, EXPECT_SUM_SMALL); return 1; }
    if (c.p != c.inl) { fprintf(stderr, "FAIL: not inline after shrink\n"); return 1; }
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
    printf("PASS: re-read after shrink summed %ld big %ld small inline and the old heap pointer was caught as %s\n", EXPECT_SUM_BIG, EXPECT_SUM_SMALL, EXPECTED);
    return 0;
}