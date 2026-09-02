// overlapping_copy_requires_memmove — memcpy on overlapping regions is undefined
//
// WHY: memcpy is allowed to be fast precisely because it may assume the regions do not overlap —
//      it can copy in any order, in any width. Shifting elements within one buffer is exactly the
//      overlapping case, and it arises every time you insert or delete in the middle of an array.
// WHEN: shifting data within a single buffer using memcpy instead of memmove.
// GUARANTEES: any copy whose source and destination lie in the same buffer must use memmove.
//
// DISASTER: memcpy on overlapping regions is flagged by the sanitizer as memcpy-param-overlap.
// PROOF: safe arm runs in-process and must be clean; unsafe arm runs in a child
//        (argv[1] == "--unsafe") and must produce the named failure signature below.
// EXPECTED FAILURE SIGNATURE: memcpy-param-overlap

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <unistd.h>
#include <sys/wait.h>

static const char* EXPECTED = "memcpy-param-overlap";

// PORTABLE WITNESS: the two ranges are compared BEFORE the copy. Overlap is a property of the
// arguments, observed independently of the result. ASan's interceptor reports
// memcpy-param-overlap and corroborates on Linux; with no sanitizer this comparison IS the
// oracle.
static bool g_overlap = false;
static void note_overlap(const void* dst, const void* src, size_t n) {
    const unsigned char* d = (const unsigned char*)dst;
    const unsigned char* s2 = (const unsigned char*)src;
    if (d < s2 + n && s2 < d + n) {
        g_overlap = true;
        fprintf(stderr, "%s: dst=%p src=%p len=%zu overlap\n", EXPECTED, dst, src, n);
    }
}
static const long EXPECT_N = 16;
static const long EXPECT_SUM_BEFORE = 136;
static const long EXPECT_SUM_AFTER = 120;

static size_t opaque(size_t x) { return x; }

static int unsafe_arm() {
    unsigned char* b = (unsigned char*)malloc(EXPECT_N);
    for (int i = 0; i < EXPECT_N; ++i) b[i] = static_cast<unsigned char>(i + 1);
    note_overlap(b + 2, b, (size_t)opaque(8));
    memcpy(b + 2, b, opaque(8));   // overlapping: src=b, dst=b+2, len=8
    free(b);
    if (!g_overlap)
        fprintf(stderr, "unsafe arm was well-formed - the disaster did not happen\n");
    return g_overlap ? 1 : 0;
}

static int safe_arm() {
    unsigned char* b = (unsigned char*)malloc(EXPECT_N);
    for (int i = 0; i < EXPECT_N; ++i) b[i] = static_cast<unsigned char>(i + 1);
    long sum_before = 0;
    for (int i = 0; i < EXPECT_N; ++i) sum_before += b[i];
    if (sum_before != EXPECT_SUM_BEFORE) { fprintf(stderr, "FAIL: before %ld != %ld\n", sum_before, EXPECT_SUM_BEFORE); free(b); return 1; }
    std::memmove(b + 2, b, 8);
    if (b[2] != 1) { fprintf(stderr, "FAIL: b[2] %d != 1\n", b[2]); free(b); return 1; }
    if (b[3] != 2) { fprintf(stderr, "FAIL: b[3] %d != 2\n", b[3]); free(b); return 1; }
    long sum_after = 0;
    for (int i = 0; i < EXPECT_N; ++i) sum_after += b[i];
    free(b);
    if (sum_after != EXPECT_SUM_AFTER) { fprintf(stderr, "FAIL: after %ld != %ld\n", sum_after, EXPECT_SUM_AFTER); return 1; }
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
    printf("PASS: memmove summed %ld after overlap b[2]=1 b[3]=2 and the memcpy overlap was caught as %s\n", EXPECT_SUM_AFTER, EXPECTED);
    return 0;
}