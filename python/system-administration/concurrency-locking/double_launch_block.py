"""
double_launch_block: prevent launching the same service twice; a pidfile lock ensures
only one instance can run. Failure simulated: two processes try to start the same service
concurrently. Recovery asserted: (1) the first obtains the lock and starts, (2) the second
tries to acquire the lock, finds the pidfile held, and fails/returns False without starting,
(3) only the first writes to the output file (proving only one ran). A no-op launch guard
would allow both instances to start, corrupting shared state.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import sys
import tempfile
import fcntl
import signal
import time
import multiprocessing
import random

class ServiceLauncher:
    """Ensure only one instance of a service runs; use pidfile + lock."""
    def __init__(self, service_name, tmpdir):
        self.service_name = service_name
        self.pidfile = os.path.join(tmpdir, f"{service_name}.pid")
        self.lockfile = os.path.join(tmpdir, f"{service_name}.lock")
        self.output_file = os.path.join(tmpdir, f"{service_name}.output")
        self.running = False

    def try_launch(self):
        """
        Try to launch; if lock is held by a live process, reject.
        Returns (success, reason).
        """
        # Try to acquire the lock (creates lockfile atomically)
        try:
            fd = os.open(self.lockfile, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
            # We got the lock; write our pid and launch
            with os.fdopen(fd, "w") as f:
                f.write(str(os.getpid()))
        except FileExistsError:
            # Lock is held; check if the holder is alive
            holder_pid = None
            try:
                # Read lock file (may race with holder writing it)
                for _ in range(5):
                    try:
                        with open(self.lockfile, "r") as f:
                            pid_str = f.read().strip()
                            if pid_str:
                                holder_pid = int(pid_str)
                                break
                    except (ValueError, IOError):
                        time.sleep(0.01)
            except Exception:
                pass

            if holder_pid is not None:
                # Check if the holder process is alive
                try:
                    os.kill(holder_pid, 0)  # Signal 0: check if process exists
                    # Process is alive, so we can't launch
                    return (False, "already_running")
                except OSError:
                    # Process is dead; try to break the stale lock and retry
                    try:
                        os.remove(self.lockfile)
                    except:
                        pass
                    # Retry once
                    try:
                        fd = os.open(self.lockfile, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
                        with os.fdopen(fd, "w") as f:
                            f.write(str(os.getpid()))
                    except FileExistsError:
                        return (False, "stale_lock_contention")
            else:
                return (False, "could_not_read_pidfile")

        # We have the lock; launch the service
        try:
            # Simulate service work: write to output file
            with open(self.output_file, "a") as f:
                f.write(f"Service {self.service_name} started by pid {os.getpid()}\n")
            self.running = True
            time.sleep(0.3)  # Simulate service work
            with open(self.output_file, "a") as f:
                f.write(f"Service {self.service_name} running by pid {os.getpid()}\n")
            return (True, "launched")
        except Exception as e:
            return (False, f"launch_error: {e}")
        finally:
            # Clean up lock
            try:
                os.remove(self.lockfile)
            except:
                pass

def launcher_process(service_name, tmpdir, results_dict, launcher_id):
    """Launch a service from a process; record result."""
    launcher = ServiceLauncher(service_name, tmpdir)
    success, reason = launcher.try_launch()
    results_dict[f"launcher_{launcher_id}_success"] = success
    results_dict[f"launcher_{launcher_id}_reason"] = reason

if __name__ == "__main__":
    random.seed(42)
    tmpdir = tempfile.mkdtemp()

    with multiprocessing.Manager() as manager:
        results = manager.dict()

        service_name = "my_service"
        num_launchers = 2

        # Launch two instances of the same service concurrently
        processes = []
        for i in range(num_launchers):
            p = multiprocessing.Process(target=launcher_process, args=(service_name, tmpdir, results, i))
            processes.append(p)

        for p in processes:
            p.start()
        for p in processes:
            p.join(timeout=5)

        # Exactly one launcher should have succeeded
        success_count = sum(1 for i in range(num_launchers) if results.get(f"launcher_{i}_success"))
        assert success_count == 1, f"Expected 1 successful launch, got {success_count}"

        # The other should have failed due to lock held by running instance
        fail_count = num_launchers - success_count
        assert fail_count == 1, f"Expected 1 failed launch, got {fail_count}"

        # The failed launcher should have gotten "already_running"
        for i in range(num_launchers):
            if not results.get(f"launcher_{i}_success"):
                reason = results.get(f"launcher_{i}_reason")
                assert reason == "already_running", f"Expected 'already_running', got '{reason}'"

        # The output file should contain exactly one "started" and one "running" entry
        output_file = os.path.join(tmpdir, f"{service_name}.output")
        try:
            with open(output_file, "r") as f:
                content = f.read()
            started_count = content.count("started")
            running_count = content.count("running")
            assert started_count == 1, f"Expected 1 'started' entry, got {started_count}"
            assert running_count == 1, f"Expected 1 'running' entry, got {running_count}"
        except FileNotFoundError:
            raise AssertionError("Service output file not created (service never launched?)")

    import shutil
    shutil.rmtree(tmpdir)
    print(f"double_launch_block: 2 launches attempted; 1 succeeded, 1 rejected (lock held by running); output shows 1 service instance")
    print("double_launch_block PASS")
    sys.exit(0)
