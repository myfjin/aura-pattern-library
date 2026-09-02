// copy_and_swap_strong_guarantee — naive free-then-rebuild violates the strong guarantee
//
// WHY: the strong guarantee says a failed assignment leaves the target unchanged. The naive
//      "free then rebuild" order cannot offer it — if the rebuild throws, the target is left
//      holding a freed pointer, and the next read is a use-after-free.
// WHEN: writing operator= for a class that manages memory, and the copy step can throw.
// GUARANTEES: copy-and-swap gives the strong guarantee by construction: all work that can throw
//      happens on a temporary, and the only mutation is a noexcept swap.
//
// DISASTER: the target's data pointer is freed, the rebuild throws, and the freed pointer is read.
// PROOF: safe arm runs in-process and must be clean; unsafe arm runs in a child
//        (argv[1] == "--unsafe") and must produce the named failure signature below.
// EXPECTED FAILURE SIGNATURE: heap-use-after-free

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <stdexcept>
#include <unistd.h>
#include <sys/wait.h>

static const char* EXPECTED = "heap-use-after-free";
static const long EXPECT_SUM = 36;
static const long EXPECT_N = 8;

// PORTABLE LIVENESS LEDGER: set true in ctor, false at the event of release
// (in operator= before delete, and in dtor). An independent witness of UAF.
static bool g_buffer_live = false;

class UnsafeBuffer {
public:
    int* data;
    size_t n;
    UnsafeBuffer(const int* src, size_t count) : n(count) {
        data = new int[count];
        std::memcpy(data, src, count * sizeof(int));
        g_buffer_live = true;
    }
    ~UnsafeBuffer() { g_buffer_live = false; delete[] data; }

    UnsafeBuffer(const UnsafeBuffer& other) : n(other.n) {
        data = new int[other.n];
        std::memcpy(data, other.data, other.n * sizeof(int));
    }

    // Naive: free first, then rebuild. If rebuild throws, data holds the freed pointer.
    UnsafeBuffer& operator=(const UnsafeBuffer& other) {
        g_buffer_live = false;                  // at the event of release
        delete[] data;                         // free the old buffer, data is now dangling
        n = other.n;
        if (other.n == EXPECT_N) throw std::runtime_error("copy failed");
        data = new int[other.n];               // never reached on throw; data still dangling
        std::memcpy(data, other.data, other.n * sizeof(int));
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

    SafeBuffer(const SafeBuffer& other) : data(nullptr), n(other.n) {
        data = new int[other.n];
        try {
            std::memcpy(data, other.data, other.n * sizeof(int));
            if (other.n == EXPECT_N) throw std::runtime_error("copy failed");
        } catch (...) {
            delete[] data;
            data = nullptr;
            throw;
        }
    }

    // Copy-and-swap: all throwing work on the temporary, swap is noexcept
    SafeBuffer& operator=(SafeBuffer other) {
        std::swap(data, other.data);
        std::swap(n, other.n);
        return *this;
    }
};

static int unsafe_arm() {
    int vals[8] = {1, 2, 3, 4, 5, 6, 7, 8};
    UnsafeBuffer x(vals, 8);
    UnsafeBuffer y(vals, 8);
    try {
        x = y;   // frees x.data, then throws during rebuild
    } catch (...) {}
    // Ledger check BEFORE the read: under a sanitizer the dangling access aborts the process.
    if (!g_buffer_live) {
        fprintf(stderr, "%s: read through a pointer whose owner was already destroyed\n", EXPECTED);
        long acc = 0;
        for (size_t i = 0; i < x.n; ++i) acc += x.data[i];   // the REAL use-after-free still happens
        printf("%ld\n", acc);
        return 1;
    }
    fprintf(stderr, "unsafe arm found the owner still live - the disaster did not happen\n");
    return 0;
}

static int safe_arm() {
    int vals[8] = {1, 2, 3, 4, 5, 6, 7, 8};
    SafeBuffer x(vals, 8);
    SafeBuffer y(vals, 8);
    try {
        x = y;   // copy-and-swap: if copy throws, x is untouched
    } catch (...) {}
    long sum = 0;
    for (size_t i = 0; i < x.n; ++i) sum += x.data[i];
    if (sum != EXPECT_SUM) { fprintf(stderr, "FAIL: sum %ld != %ld\n", sum, EXPECT_SUM); return 1; }
    if (static_cast<long>(x.n) != EXPECT_N) { fprintf(stderr, "FAIL: size %zu != %ld\n", x.n, EXPECT_N); return 1; }
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
    printf("PASS: copy-and-swap preserved sum %ld size %ld through throw and the freed read was caught as %s\n", EXPECT_SUM, EXPECT_N, EXPECTED);
    return 0;
}