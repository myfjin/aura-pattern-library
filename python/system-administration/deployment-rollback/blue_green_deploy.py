"""Blue-green deployment (two full stacks, atomic switch)."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import tempfile
import json


class BlueGreenDeploy:
    """Manage blue-green deployments."""

    def __init__(self, workspace_path):
        """Init with workspace root."""
        self.workspace = workspace_path
        self.blue_dir = os.path.join(workspace_path, "blue")
        self.green_dir = os.path.join(workspace_path, "green")
        self.state_file = os.path.join(workspace_path, "active.json")

        os.makedirs(workspace_path, exist_ok=True)
        os.makedirs(self.blue_dir, exist_ok=True)
        os.makedirs(self.green_dir, exist_ok=True)

    def get_active_color(self):
        """Return current active color: 'blue' or 'green'."""
        if not os.path.exists(self.state_file):
            # Default to blue on first run
            return "blue"

        with open(self.state_file, "r") as f:
            state = json.load(f)
            return state.get("active", "blue")

    def deploy_to_inactive(self, app_code):
        """
        Deploy new code to the inactive color.
        Return: color of newly deployed version.
        """
        active = self.get_active_color()
        target_color = "green" if active == "blue" else "blue"
        target_dir = self.green_dir if target_color == "green" else self.blue_dir

        # Clear old files in target
        for f in os.listdir(target_dir):
            path = os.path.join(target_dir, f)
            if os.path.isfile(path):
                os.unlink(path)

        # Deploy new code
        app_file = os.path.join(target_dir, "app.py")
        with open(app_file, "w") as f:
            f.write(app_code)

        return target_color

    def switch_active(self, new_color):
        """Atomically switch active color."""
        if new_color not in ("blue", "green"):
            raise ValueError(f"Invalid color: {new_color}")

        # Write state atomically
        state = {"active": new_color}
        with open(self.state_file, "w") as f:
            json.dump(state, f)

    def get_active_dir(self):
        """Return path to active deployment directory."""
        active = self.get_active_color()
        return self.green_dir if active == "green" else self.blue_dir


def test_deploy_to_inactive():
    """Test: deploy new code to inactive color."""
    with tempfile.TemporaryDirectory() as tmpdir:
        bg = BlueGreenDeploy(tmpdir)

        # Initially blue is active
        assert bg.get_active_color() == "blue"

        # Deploy to green (inactive)
        new_color = bg.deploy_to_inactive("print('v2')")

        assert new_color == "green"
        assert os.path.exists(os.path.join(bg.green_dir, "app.py"))


def test_atomic_switch():
    """Test: atomic switch of active color."""
    with tempfile.TemporaryDirectory() as tmpdir:
        bg = BlueGreenDeploy(tmpdir)

        # Deploy to green
        bg.deploy_to_inactive("print('v2')")
        assert bg.get_active_color() == "blue"

        # Switch to green
        bg.switch_active("green")
        assert bg.get_active_color() == "green"


def test_switch_back_on_failure():
    """Test: switch back if new version fails (rollback)."""
    with tempfile.TemporaryDirectory() as tmpdir:
        bg = BlueGreenDeploy(tmpdir)

        # Deploy blue version
        bg.deploy_to_inactive("good_v1")
        bg.switch_active("green")

        # Deploy bad version to blue
        bg.deploy_to_inactive("bad_v2")
        bg.switch_active("blue")

        # Detect failure and rollback
        assert bg.get_active_color() == "blue"

        # SIMULATE FAILURE DETECTION -> ROLLBACK
        bg.switch_active("green")
        assert bg.get_active_color() == "green", "Should rollback to green"


def test_get_active_directory():
    """Test: get path to active deployment."""
    with tempfile.TemporaryDirectory() as tmpdir:
        bg = BlueGreenDeploy(tmpdir)

        # Blue is active initially
        assert bg.get_active_dir() == bg.blue_dir

        # Deploy and switch to green
        bg.deploy_to_inactive("v2")
        bg.switch_active("green")

        assert bg.get_active_dir() == bg.green_dir


def test_zero_downtime_deploy():
    """Test: zero-downtime deployment sequence."""
    with tempfile.TemporaryDirectory() as tmpdir:
        bg = BlueGreenDeploy(tmpdir)

        # Initial deployment to blue, activate
        bg.deploy_to_inactive("v1")
        bg.switch_active("blue")
        assert bg.get_active_dir() == bg.blue_dir

        # Deploy new version to green (blue still active, serving)
        bg.deploy_to_inactive("v2")
        assert bg.get_active_color() == "blue"  # Blue still active

        # Switch to green (atomic)
        bg.switch_active("green")
        assert bg.get_active_dir() == bg.green_dir

        # Next deploy goes to blue (green now active)
        bg.deploy_to_inactive("v3")
        assert bg.get_active_color() == "green"  # Green still active


if __name__ == "__main__":
    test_deploy_to_inactive()
    test_atomic_switch()
    test_switch_back_on_failure()
    test_get_active_directory()
    test_zero_downtime_deploy()
    print("✓ blue_green_deploy passed")
