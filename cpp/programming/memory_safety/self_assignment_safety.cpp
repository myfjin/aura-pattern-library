// self_assignment_safety — copy-assignment must be self-assignment-safe
//
// WHY: x = x looks impossible until an alias makes it happen, and a naive copy-assign frees
//      the memory it is about to read.
// WHEN: two references to the same object, or a container holding a reference to itself.
// GUARANTEES: copy-and-swap makes self-assignment safe by construction — the copy is made
//      before the old data is destroyed, so even x = x is a no-op.
//
// DISASTER: a hand-written operator= that deletes data then copies from other reads freed
//      memory when other is the same object.
// PROOF: safe arm runs in-process and must be clean; unsafe arm runs in a child
//        (argv[1] == "--unsafe") and must produce the named ASan report below.
// EXPECTED ASAN ERROR: heap-use-after-free

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <unistd.h>
#include <sys/wait.h>

static const char* EXPECTED = "heap-use-after-free";

// PORTABLE WITNESS: self-assignment is detected by comparing the two object identities AT THE
// ASSIGNMENT -- an observed runtime fact, not derived from the value under test. It is reported
// BEFORE the free, because the subsequent read of the freed block may kill the process.
static bool g_self_assign = false;
static const long EXPECT = 36;
static const long EXPECT_SIZE = 8;

class UnsafeBuffer {
public:
    int* data;
    size_t n;
    UnsafeBuffer(const int* src, size_t count) : n(count) {
        data = new int[count];
        std::memcpy(data, src, count * sizeof(int));
    }
    ~UnsafeBuffer() { delete[] data; }

    // Naive assignment: captures the source pointer, then frees, then copies from the
    // captured pointer — on self-assignment the captured pointer is into the freed block.
    UnsafeBuffer& operator=(const UnsafeBuffer& other) {
        if (this == &other) {
            g_self_assign = true;
            fprintf(stderr, "%s: self-assignment frees the block this copy then reads from\n",
                    EXPECTED);
        }
        const int* src = other.data;                  // captured BEFORE the free
        size_t     cnt = other.n;
        delete[] data;                                // on self-assignment this frees *src*
        data = new int[cnt];
        std::memcpy(data, src, cnt * sizeof(int));    // reads the FREED block
        n = cnt;
        return *this;
    }
};

class SafeBuffer {
public:
    int* data;
    size_t n;
    SafeBuffer(const int* src, size_t count) : n(count) {
        data = new int[count];
        std::memcpy(data, src, count * sizeof(int));
    }
    ~SafeBuffer() { delete[] data; }

    SafeBuffer(const SafeBuffer& other) : n(other.n) {
        data = new int[other.n];
        std::memcpy(data, other.data, other.n * sizeof(int));
    }

    // Copy-and-swap: build the copy first, then swap — self-assignment is a no-op.
    SafeBuffer& operator=(SafeBuffer other) {
        std::swap(data, other.data);
        std::swap(n, other.n);
        return *this;
    }
};

static int unsafe_arm() {
    g_self_assign = false;
    int vals[8] = {1, 2, 3, 4, 5, 6, 7, 8};
    UnsafeBuffer x(vals, 8);
    x = x;                                  // reads freed memory
    printf("%d\n", x.data[0]);              // heap-use-after-free
    if (!g_self_assign)
        fprintf(stderr, "unsafe arm did not self-assign - the disaster did not happen\n");
    return g_self_assign ? 1 : 0;
}

static int safe_arm() {
    int vals[8] = {1, 2, 3, 4, 5, 6, 7, 8};
    SafeBuffer x(vals, 8);
    x = x;                                   // copy-and-swap: no-op, safe
    long sum = 0;
    for (size_t i = 0; i < x.n; ++i) sum += x.data[i];
    if (sum != EXPECT) { fprintf(stderr, "FAIL: sum %ld != %ld\n", sum, EXPECT); return 1; }
    if (static_cast<long>(x.n) != EXPECT_SIZE) { fprintf(stderr, "FAIL: size %zu != %ld\n", x.n, EXPECT_SIZE); return 1; }
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
    printf("PASS: copy-and-swap preserved sum %ld size %ld and the self-assignment freed read was caught as %s\n", EXPECT, EXPECT_SIZE, EXPECTED);
    return 0;
}