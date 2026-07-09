"""
Plugin registry with lazy loading, dependency management, and entry point discovery.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import importlib
import sys
from abc import ABC, abstractmethod
from collections import defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple, Type


class PluginError(Exception):
    """Base exception for plugin-related errors."""
    pass


class PluginNotFoundError(PluginError):
    """Raised when a plugin is not found."""
    pass


class CircularDependencyError(PluginError):
    """Raised when circular dependencies are detected."""
    pass


class Plugin(ABC):
    """
    Abstract base class for all plugins.
    
    Attributes:
        name: Unique identifier for the plugin.
        version: Plugin version string.
        dependencies: List of plugin names this plugin depends on.
    """
    
    def __init__(self, name: str, version: str = "1.0.0", dependencies: Optional[List[str]] = None):
        self.name = name
        self.version = version
        self.dependencies = dependencies or []
        self._loaded = False
    
    @abstractmethod
    def load(self) -> None:
        """Initialize the plugin. Called once during first access."""
        pass
    
    @abstractmethod
    def execute(self, *args: Any, **kwargs: Any) -> Any:
        """Execute the plugin's main functionality."""
        pass
    
    def is_loaded(self) -> bool:
        """Check if the plugin has been loaded."""
        return self._loaded
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', version='{self.version}')"


class PluginRegistry:
    """
    Manages plugin registration, discovery, dependency resolution, and lazy loading.
    """
    
    def __init__(self) -> None:
        self._plugins: Dict[str, Type[Plugin]] = {}
        self._instances: Dict[str, Plugin] = {}
        self._dependency_graph: Dict[str, Set[str]] = defaultdict(set)
        self._reverse_dependencies: Dict[str, Set[str]] = defaultdict(set)
    
    def register(self, plugin_class: Type[Plugin]) -> None:
        """
        Register a plugin class.
        
        Args:
            plugin_class: The plugin class to register.
            
        Raises:
            PluginError: If a plugin with the same name is already registered.
        """
        if plugin_class.name in self._plugins:
            raise PluginError(f"Plugin '{plugin_class.name}' is already registered")
        
        self._plugins[plugin_class.name] = plugin_class
        # Update dependency graph
        for dep in plugin_class.dependencies:
            self._dependency_graph[plugin_class.name].add(dep)
            self._reverse_dependencies[dep].add(plugin_class.name)
    
    def discover_from_entry_points(self, entry_point_group: str) -> None:
        """
        Discover and register plugins from entry points.
        
        Args:
            entry_point_group: The entry point group to scan.
        """
        # In a real implementation, this would use importlib.metadata.entry_points()
        # For this demo, we'll simulate it
        pass
    
    def get_plugin(self, name: str) -> Plugin:
        """
        Get a plugin instance by name, loading it if necessary.
        
        Args:
            name: The name of the plugin to retrieve.
            
        Returns:
            The plugin instance.
            
        Raises:
            PluginNotFoundError: If the plugin is not registered.
        """
        if name not in self._plugins:
            raise PluginNotFoundError(f"Plugin '{name}' not found")
        
        if name not in self._instances:
            self._instances[name] = self._plugins[name](name)
        
        plugin = self._instances[name]
        if not plugin.is_loaded():
            # Load dependencies first
            for dep_name in plugin.dependencies:
                if dep_name not in self._plugins:
                    raise PluginNotFoundError(f"Dependency '{dep_name}' for plugin '{name}' not found")
                self.get_plugin(dep_name)  # This will load the dependency
            
            plugin.load()
            plugin._loaded = True
            
        return plugin
    
    def list_plugins(self) -> List[str]:
        """
        List all registered plugin names.
        
        Returns:
            A list of plugin names.
        """
        return list(self._plugins.keys())
    
    def resolve_load_order(self) -> List[str]:
        """
        Resolve plugin load order based on dependencies using topological sort.
        
        Returns:
            A list of plugin names in load order.
            
        Raises:
            CircularDependencyError: If circular dependencies are detected.
        """
        # Kahn's algorithm for topological sorting
        in_degree: Dict[str, int] = {name: 0 for name in self._plugins}
        
        # Calculate in-degrees
        for plugin_name in self._plugins:
            for dep in self._dependency_graph[plugin_name]:
                if dep in self._plugins:  # Only count if dependency is registered
                    in_degree[dep] += 1
        
        # Find all nodes with no incoming edges
        queue: deque = deque([name for name, degree in in_degree.items() if degree == 0])
        result: List[str] = []
        
        while queue:
            current = queue.popleft()
            result.append(current)
            
            # Remove edges from current node
            for neighbor in self._reverse_dependencies[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Check for circular dependencies
        if len(result) != len(self._plugins):
            raise CircularDependencyError("Circular dependencies detected in plugin graph")
        
        return result
    
    def load_all_plugins(self) -> None:
        """Load all registered plugins in dependency order."""
        load_order = self.resolve_load_order()
        for plugin_name in load_order:
            self.get_plugin(plugin_name)


# Sample plugins for demonstration
class LoggerPlugin(Plugin):
    """A simple logging plugin."""
    
    name = "logger"
    version = "1.0.0"
    dependencies = []
    
    def __init__(self, name: str):
        super().__init__(name, self.version, self.dependencies)
        self.messages: List[str] = []
    
    def load(self) -> None:
        """Initialize the logger."""
        self.messages.append("Logger plugin loaded")
    
    def execute(self, message: str) -> str:
        """Log a message."""
        formatted = f"[LOG] {message}"
        self.messages.append(formatted)
        return formatted


class DatabasePlugin(Plugin):
    """A database plugin that depends on the logger."""
    
    name = "database"
    version = "1.2.0"
    dependencies = ["logger"]
    
    def __init__(self, name: str):
        super().__init__(name, self.version, self.dependencies)
        self.connected = False
    
    def load(self) -> None:
        """Initialize database connection."""
        # Simulate getting logger plugin
        registry = getattr(sys.modules[__name__], '_demo_registry', None)
        if registry:
            logger = registry.get_plugin("logger")
            logger.execute("Database plugin loading...")
        self.connected = True
    
    def execute(self, query: str) -> str:
        """Execute a database query."""
        if not self.connected:
            raise PluginError("Database not connected")
        return f"Executed: {query}"


class WebServerPlugin(Plugin):
    """A web server plugin that depends on both logger and database."""
    
    name = "webserver"
    version = "2.1.0"
    dependencies = ["logger", "database"]
    
    def __init__(self, name: str):
        super().__init__(name, self.version, self.dependencies)
        self.routes: Dict[str, str] = {}
    
    def load(self) -> None:
        """Initialize web server."""
        # Simulate getting dependencies
        registry = getattr(sys.modules[__name__], '_demo_registry', None)
        if registry:
            logger = registry.get_plugin("logger")
            logger.execute("WebServer plugin loading...")
            db = registry.get_plugin("database")
            db.execute("CREATE TABLE IF NOT EXISTS users")
        self.routes["/"] = "Welcome to the web server"
    
    def execute(self, route: str) -> str:
        """Handle a web request."""
        if route in self.routes:
            return self.routes[route]
        return "404 Not Found"


def main() -> None:
    """Demo the plugin registry with sample plugins."""
    print("=== Plugin Registry Demo ===")
    
    # Create registry and register plugins
    registry = PluginRegistry()
    # Store registry in module for plugins to access during load
    sys.modules[__name__]._demo_registry = registry
    
    registry.register(LoggerPlugin)
    registry.register(DatabasePlugin)
    registry.register(WebServerPlugin)
    
    print(f"Registered plugins: {registry.list_plugins()}")
    
    # Show dependency resolution
    try:
        load_order = registry.resolve_load_order()
        print(f"Plugin load order: {load_order}")
    except CircularDependencyError as e:
        print(f"Error resolving load order: {e}")
        return
    
    # Demonstrate lazy loading - only logger should be loaded initially
    print("\n--- Before accessing plugins ---")
    logger_instance = registry._instances.get("logger")
    print(f"Logger loaded: {logger_instance.is_loaded() if logger_instance else False}")
    
    # Access webserver plugin (should trigger loading of dependencies)
    print("\n--- Accessing webserver plugin ---")
    webserver = registry.get_plugin("webserver")
    print(f"WebServer loaded: {webserver.is_loaded()}")
    
    # Check that dependencies were also loaded
    logger = registry.get_plugin("logger")
    database = registry.get_plugin("database")
    print(f"Logger loaded: {logger.is_loaded()}")
    print(f"Database loaded: {database.is_loaded()}")
    
    # Execute plugins
    print("\n--- Executing plugins ---")
    result = logger.execute("Application started")
    print(result)
    
    result = database.execute("SELECT * FROM users")
    print(result)
    
    result = webserver.execute("/")
    print(result)
    
    result = webserver.execute("/missing")
    print(result)
    
    # Show logger messages
    print(f"\nLogger messages: {logger.messages}")
    
    # Try to get non-existent plugin
    print("\n--- Error handling ---")
    try:
        registry.get_plugin("nonexistent")
    except PluginNotFoundError as e:
        print(f"Caught expected error: {e}")


if __name__ == "__main__":
    main()