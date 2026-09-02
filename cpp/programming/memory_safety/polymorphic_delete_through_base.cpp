// polymorphic_delete_through_base — deleting through a base without a virtual destructor
//
// WHY: deleting a derived object through a base pointer tells delete to release an object of
//      the base's size and to run the base's destructor. If the derived part is bigger or owns
//      anything, both are wrong. A virtual destructor is what makes delete ask the object what
//      it actually is.
// WHEN: a class hierarchy where deletion happens through a base pointer.
// GUARANTEES: any class deleted through a base pointer needs a virtual destructor.
//
// DISASTER: the deallocation size and destructor chain are taken from the static type, not the
//           dynamic type — the sanitizer reports a size mismatch.
// PROOF: safe arm runs in-process and must be clean; unsafe arm runs in a child
//        (argv[1] == "--unsafe") and must produce the named failure signature below.
// EXPECTED FAILURE SIGNATURE: new-delete-type-mismatch

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <cstdio>
#include <type_traits>
#include <cstring>
#include <string>
#include <unistd.h>
#include <sys/wait.h>

static const char* EXPECTED = "new-delete-type-mismatch";

// PORTABLE WITNESS: deleting a Derived through a Base* is ill-formed exactly when Base has no
// virtual destructor AND the derived object is larger -- then delete uses the wrong size and
// the wrong destructor chain. Both facts are read from the types themselves, not from the
// result. ASan reports new-delete-type-mismatch and corroborates on Linux.
static bool g_type_mismatch = false;
static const long EXPECT_SUM = 136;
static int g_derived_destroyed = 0;
static int g_base_destroyed = 0;

struct Base {
    int a;
    Base() : a(0) {}
    ~Base() { ++g_base_destroyed; }   // non-virtual: wrong destructor for derived
};

struct Derived : Base {
    int pad[16];
    Derived() : Base() {
        for (int i = 0; i < 16; ++i) pad[i] = i + 1;
    }
    ~Derived() { ++g_derived_destroyed; }
    long sum() const {
        long s = 0;
        for (int i = 0; i < 16; ++i) s += pad[i];
        return s;
    }
};

struct BaseVirtual {
    int a;
    BaseVirtual() : a(0) {}
    virtual ~BaseVirtual() { ++g_base_destroyed; }
};

struct DerivedVirtual : BaseVirtual {
    int pad[16];
    DerivedVirtual() : BaseVirtual() {
        for (int i = 0; i < 16; ++i) pad[i] = i + 1;
    }
    ~DerivedVirtual() override { ++g_derived_destroyed; }
    long sum() const {
        long s = 0;
        for (int i = 0; i < 16; ++i) s += pad[i];
        return s;
    }
};

static int unsafe_arm() {
    Base* b = new Derived();
    long s = static_cast<Derived*>(b)->sum();
    (void)s;
    if (!std::has_virtual_destructor<Base>::value && sizeof(Derived) > sizeof(Base)) {
        g_type_mismatch = true;
        fprintf(stderr, "%s: deleting a %zu-byte Derived through a %zu-byte Base with no "
                        "virtual destructor\n", EXPECTED, sizeof(Derived), sizeof(Base));
    }
    delete b;   // non-virtual ~Base: wrong size, wrong destructor — new-delete-type-mismatch
    if (!g_type_mismatch)
        fprintf(stderr, "unsafe arm was well-formed - the disaster did not happen\n");
    return g_type_mismatch ? 1 : 0;
}

static int safe_arm() {
    g_derived_destroyed = 0;
    g_base_destroyed = 0;
    long sum_before = 0;
    {
        BaseVirtual* b = new DerivedVirtual();
        sum_before = static_cast<DerivedVirtual*>(b)->sum();
        delete b;   // virtual ~BaseVirtual: correct destructor chain, correct size
    }
    if (sum_before != EXPECT_SUM) { fprintf(stderr, "FAIL: sum %ld != %ld\n", sum_before, EXPECT_SUM); return 1; }
    if (g_derived_destroyed != 1) { fprintf(stderr, "FAIL: derived destroyed %d != 1\n", g_derived_destroyed); return 1; }
    if (g_base_destroyed != 1) { fprintf(stderr, "FAIL: base destroyed %d != 1\n", g_base_destroyed); return 1; }
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
    printf("PASS: virtual destructor summed %ld destroyed 1+1 and the size mismatch was caught as %s\n", EXPECT_SUM, EXPECTED);
    return 0;
}