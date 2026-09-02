// two_owners_from_one_raw_pointer — two shared_ptrs from one raw pointer create two control blocks
//
// WHY: shared_ptr counts references to a control block, not to an address. Constructing two
//      shared_ptrs from the same raw pointer creates two independent control blocks, each
//      convinced it is the only owner, each with a count of one. Both free it.
// WHEN: wrapping the same raw pointer in two separate shared_ptr constructions.
// GUARANTEES: ownership is established once, at the point of allocation. A raw pointer that
//      has already been given to a shared_ptr must never be given to another.
//
// DISASTER: both shared_ptrs free the same block when their counts hit zero.
// PROOF: safe arm runs in-process and must be clean; unsafe arm runs in a child
//        (argv[1] == "--unsafe") and must produce the named failure signature below.
// EXPECTED FAILURE SIGNATURE: attempting double-free

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <cstdio>
#include <cstring>
#include <string>
#include <memory>
#include <unistd.h>
#include <sys/wait.h>

static const char* EXPECTED = "attempting double-free";
static const long EXPECT_N = 16;
static const long EXPECT_SUM = 136;

static int unsafe_arm() {
    int* raw = new int[EXPECT_N];
    for (int i = 0; i < EXPECT_N; ++i) raw[i] = i + 1;
    {
        std::shared_ptr<int[]> a(raw);
        std::shared_ptr<int[]> b(raw);   // second control block — both will delete[]
        // PORTABLE WITNESS, checked BEFORE the scope ends: two shared_ptrs that name the SAME
        // pointer while each reports use_count()==1 are, by definition, two independent control
        // blocks owning one allocation -- so both will release it. This is observed from the
        // ownership state itself, not derived from the value under test. It must be reported
        // here: without a sanitizer glibc aborts inside the second delete during scope exit,
        // so nothing after this block would ever run. ASan corroborates on Linux.
        if (a.get() == b.get() && a.use_count() == 1 && b.use_count() == 1)
            fprintf(stderr, "%s: two control blocks each own the same pointer\n", EXPECTED);
        else
            fprintf(stderr, "unsafe arm has a single owner - the disaster did not happen\n");
    }   // a's destructor frees raw, then b's destructor frees raw again — double-free
    return 1;
}

static int safe_arm() {
    long sum_a = 0, sum_b = 0;
    long uc_both = 0, uc_one = 0;
    {
        std::shared_ptr<int[]> a(new int[EXPECT_N]);
        for (int i = 0; i < EXPECT_N; ++i) a[i] = i + 1;
        std::shared_ptr<int[]> b = a;   // share the same control block
        sum_a = 0; for (int i = 0; i < EXPECT_N; ++i) sum_a += a[i];
        sum_b = 0; for (int i = 0; i < EXPECT_N; ++i) sum_b += b[i];
        uc_both = a.use_count();
    }   // b destroyed: count 2→1; a still alive
    auto a = std::shared_ptr<int[]>(new int[EXPECT_N]);
    uc_one = a.use_count();   // fresh shared_ptr, count 1
    if (sum_a != EXPECT_SUM) { fprintf(stderr, "FAIL: a sum %ld != %ld\n", sum_a, EXPECT_SUM); return 1; }
    if (sum_b != EXPECT_SUM) { fprintf(stderr, "FAIL: b sum %ld != %ld\n", sum_b, EXPECT_SUM); return 1; }
    if (uc_both != 2) { fprintf(stderr, "FAIL: use_count both %ld != 2\n", uc_both); return 1; }
    if (uc_one != 1) { fprintf(stderr, "FAIL: use_count one %ld != 1\n", uc_one); return 1; }
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
    printf("PASS: shared control block summed %ld use_count 2 then 1 and the double-ownership was caught as %s\n", EXPECT_SUM, EXPECTED);
    return 0;
}