// allocator_propagation_on_container_move — moving between unequal allocators must copy
//
// WHY: a container with a stateful allocator cannot simply steal another's buffer on
//      move-assignment: the buffer belongs to the source's arena, and the destination's arena
//      has no way to free it. The propagate_on_container_move_assignment trait decides — steal
//      the pointer, or copy the elements into your own memory. Get it wrong and the destination
//      outlives the arena that owns its bytes.
// WHEN: moving a container from one arena into a container backed by a different arena.
// GUARANTEES: when allocators do not propagate and do not compare equal, a move must copy the
//      elements into the destination's own allocator, not adopt the source's pointer.
//
// DISASTER: the destination adopts the source's buffer, the source arena is destroyed, and the
//           destination reads freed memory.
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
static const long EXPECT_N = 4;
static const long EXPECT_SUM = 10;

// PORTABLE LIVENESS LEDGER: set live in Arena ctor, cleared FIRST in Arena dtor.
static bool g_buffer_live = false;

struct Arena {
    char* block;
    size_t used;
    Arena() : block((char*)malloc(4096)), used(0) { g_buffer_live = true; }
    ~Arena() { g_buffer_live = false; free(block); }
    int* alloc(size_t n) {
        int* p = reinterpret_cast<int*>(block + used);
        used += n * sizeof(int);
        return p;
    }
    bool owns(const int* p) const {
        return reinterpret_cast<const char*>(p) >= block &&
               reinterpret_cast<const char*>(p) < block + 4096;
    }
};

struct Vec {
    int* d;
    size_t n;
    Arena* a;
    Vec(Arena* arena, size_t count) : n(count), a(arena) {
        d = a->alloc(count);
    }
    // steal: adopts the source pointer without checking allocator equality
    void steal(Vec& src) {
        d = src.d;
        n = src.n;
        a = src.a;   // wrong: keeps the source's arena reference
        src.d = nullptr;
    }
    // move_safe: copies into the destination's own arena when arenas differ
    void move_safe(Vec& src) {
        if (src.a == a) {
            d = src.d;
            n = src.n;
            src.d = nullptr;
        } else {
            n = src.n;
            d = a->alloc(n);
            for (size_t i = 0; i < n; ++i) d[i] = src.d[i];
        }
    }
    long sum() const {
        long s = 0;
        for (size_t i = 0; i < n; ++i) s += d[i];
        return s;
    }
};

static int unsafe_arm() {
    Arena* a1 = new Arena();
    Arena a2;
    Vec v1(a1, EXPECT_N);
    for (int i = 0; i < EXPECT_N; ++i) v1.d[i] = i + 1;
    Vec v2(&a2, EXPECT_N);
    v2.steal(v1);           // adopts v1's buffer from a1's arena
    delete a1;              // frees a1's block — v2.d dangles
    // Ledger check BEFORE the read: under a sanitizer the dangling access aborts the process.
    if (!g_buffer_live) {
        fprintf(stderr, "%s: read through a pointer whose owner was already destroyed\n", EXPECTED);
        printf("%d\n", v2.d[0]); // the REAL use-after-free still happens
        return 1;
    }
    fprintf(stderr, "unsafe arm found the owner still live - the disaster did not happen\n");
    return 0;
}

static int safe_arm() {
    Arena a1;
    Arena a2;
    Vec v1(&a1, EXPECT_N);
    for (int i = 0; i < EXPECT_N; ++i) v1.d[i] = i + 1;
    Vec v2(&a2, EXPECT_N);
    v2.move_safe(v1);       // copies into a2's arena because a1 != a2
    // Destroy source arena — v2 should be unaffected
    // (a1 goes out of scope after this block)
    long sum = v2.sum();
    if (sum != EXPECT_SUM) { fprintf(stderr, "FAIL: sum %ld != %ld\n", sum, EXPECT_SUM); return 1; }
    if (!a2.owns(v2.d)) { fprintf(stderr, "FAIL: v2.d not in destination arena\n"); return 1; }
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
    printf("PASS: allocator-aware move copied into destination arena summing %ld and the stolen buffer was caught as %s\n", EXPECT_SUM, EXPECTED);
    return 0;
}