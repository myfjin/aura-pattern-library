"""
Capability-Based Access Control System

This module implements a capability-based access control system where
capabilities are unforgeable tokens that grant specific permissions to
principals for accessing resources.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import uuid
from typing import Dict, List, Set, Optional, Any
from enum import Enum
from dataclasses import dataclass


class Permission(Enum):
    """Enumeration of possible permissions."""
    READ = "read"
    WRITE = "write"
    EXECUTE = "execute"
    DELETE = "delete"


@dataclass(frozen=True)
class Resource:
    """Represents a resource that can be accessed."""
    id: str
    name: str
    metadata: Dict[str, Any]

    def __hash__(self) -> int:
        return hash(self.id)


class Principal:
    """Represents an entity that can hold capabilities."""
    
    def __init__(self, name: str) -> None:
        self.name = name
        self.capabilities: Set['Capability'] = set()
    
    def __str__(self) -> str:
        return f"Principal({self.name})"
    
    def __repr__(self) -> str:
        return self.__str__()


class Capability:
    """Represents an unforgeable token granting access to a resource."""
    
    def __init__(
        self,
        principal: Principal,
        resource: Resource,
        permissions: Set[Permission],
        delegable: bool = True,
        attenuated: bool = False,
        parent: Optional['Capability'] = None
    ) -> None:
        self.id = str(uuid.uuid4())
        self.principal = principal
        self.resource = resource
        self.permissions = frozenset(permissions)
        self.delegable = delegable
        self.attenuated = attenuated
        self.parent = parent
        self.children: Set['Capability'] = set()
        
        if parent:
            parent.children.add(self)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Capability):
            return False
        return self.id == other.id
    
    def __hash__(self) -> int:
        return hash(self.id)
    
    def __str__(self) -> str:
        return f"Capability(id={self.id[:8]}, resource={self.resource.name}, " \
               f"permissions={self.permissions}, delegable={self.delegable})"
    
    def __repr__(self) -> str:
        return self.__str__()


class CapabilitySystem:
    """Main system for managing capabilities."""
    
    def __init__(self) -> None:
        self.principals: Dict[str, Principal] = {}
        self.resources: Dict[str, Resource] = {}
        self.capabilities: Dict[str, Capability] = {}
    
    def create_principal(self, name: str) -> Principal:
        """Create a new principal."""
        if name in self.principals:
            raise ValueError(f"Principal {name} already exists")
        
        principal = Principal(name)
        self.principals[name] = principal
        return principal
    
    def create_resource(
        self,
        name: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Resource:
        """Create a new resource."""
        resource_id = str(uuid.uuid4())
        if metadata is None:
            metadata = {}
        
        resource = Resource(id=resource_id, name=name, metadata=metadata)
        self.resources[resource_id] = resource
        return resource
    
    def grant(
        self,
        principal: Principal,
        resource: Resource,
        permissions: Set[Permission],
        delegable: bool = True
    ) -> Capability:
        """
        Grant a new capability to a principal for a resource.
        
        Args:
            principal: The principal to grant the capability to
            resource: The resource to grant access to
            permissions: Set of permissions to grant
            delegable: Whether the capability can be delegated to others
            
        Returns:
            The newly created capability
        """
        if not permissions:
            raise ValueError("At least one permission must be granted")
        
        capability = Capability(
            principal=principal,
            resource=resource,
            permissions=permissions,
            delegable=delegable
        )
        
        principal.capabilities.add(capability)
        self.capabilities[capability.id] = capability
        return capability
    
    def revoke(self, capability: Capability) -> None:
        """
        Revoke a capability and all its descendants.
        
        Args:
            capability: The capability to revoke
        """
        if capability.id not in self.capabilities:
            raise ValueError("Capability does not exist in system")
        
        # Recursively revoke all children
        for child in list(capability.children):
            self.revoke(child)
        
        # Remove from principal
        capability.principal.capabilities.discard(capability)
        
        # Remove from system
        del self.capabilities[capability.id]
        
        # Remove from parent if exists
        if capability.parent:
            capability.parent.children.discard(capability)
    
    def delegate(
        self,
        from_principal: Principal,
        to_principal: Principal,
        capability: Capability,
        permissions: Optional[Set[Permission]] = None
    ) -> Capability:
        """
        Delegate a capability from one principal to another.
        
        Args:
            from_principal: The principal delegating the capability
            to_principal: The principal receiving the capability
            capability: The capability to delegate
            permissions: Optional subset of permissions to delegate
            
        Returns:
            The new delegated capability
        """
        if capability not in from_principal.capabilities:
            raise ValueError("Principal does not hold the specified capability")
        
        if not capability.delegable:
            raise ValueError("Capability is not delegable")
        
        # If no permissions specified, delegate all permissions
        if permissions is None:
            permissions = set(capability.permissions)
        
        # Check that requested permissions are a subset of available permissions
        if not permissions.issubset(capability.permissions):
            raise ValueError("Requested permissions exceed available permissions")
        
        # Create new delegated capability
        delegated_capability = Capability(
            principal=to_principal,
            resource=capability.resource,
            permissions=permissions,
            delegable=capability.delegable,
            parent=capability
        )
        
        to_principal.capabilities.add(delegated_capability)
        self.capabilities[delegated_capability.id] = delegated_capability
        return delegated_capability
    
    def attenuate(
        self,
        principal: Principal,
        capability: Capability,
        permissions: Set[Permission]
    ) -> Capability:
        """
        Create an attenuated (restricted) version of a capability.
        
        Args:
            principal: The principal to create the attenuated capability for
            capability: The capability to attenuate
            permissions: The restricted set of permissions
            
        Returns:
            The new attenuated capability
        """
        if capability not in principal.capabilities:
            raise ValueError("Principal does not hold the specified capability")
        
        # Check that requested permissions are a subset of available permissions
        if not permissions.issubset(capability.permissions):
            raise ValueError("Requested permissions exceed available permissions")
        
        # Create new attenuated capability
        attenuated_capability = Capability(
            principal=principal,
            resource=capability.resource,
            permissions=permissions,
            delegable=capability.delegable,
            attenuated=True,
            parent=capability
        )
        
        principal.capabilities.add(attenuated_capability)
        self.capabilities[attenuated_capability.id] = attenuated_capability
        return attenuated_capability
    
    def check_access(
        self,
        principal: Principal,
        resource: Resource,
        permission: Permission
    ) -> bool:
        """
        Check if a principal has a specific permission for a resource.
        
        Args:
            principal: The principal to check
            resource: The resource to check access to
            permission: The permission to check for
            
        Returns:
            True if access is granted, False otherwise
        """
        for capability in principal.capabilities:
            if (capability.resource == resource and 
                permission in capability.permissions):
                return True
        return False


def main() -> None:
    """Self-test: THE SECURITY LAW — every forbidden action is attempted and
    must be denied; grants/delegation/attenuation/revocation exact."""
    system = CapabilitySystem()
    admin = system.create_principal("admin")
    user1 = system.create_principal("user1")
    user2 = system.create_principal("user2")
    file1 = system.create_resource("confidential.txt", {"sensitivity": "high"})
    file2 = system.create_resource("public.txt", {"sensitivity": "low"})

    admin_cap = system.grant(admin, file1,
                             {Permission.READ, Permission.WRITE, Permission.DELETE},
                             delegable=True)
    user1_cap = system.grant(user1, file2, {Permission.READ}, delegable=False)
    live_perms = sum([system.check_access(admin, file1, Permission.READ),
                      system.check_access(admin, file1, Permission.WRITE),
                      system.check_access(admin, file1, Permission.DELETE)])
    assert live_perms == 3, f"admin grant must confer exactly 3 permissions, got {live_perms}"

    # Grants confer exactly the named permissions — nothing more.
    assert system.check_access(admin, file1, Permission.READ) is True
    assert system.check_access(admin, file1, Permission.DELETE) is True
    assert system.check_access(user1, file2, Permission.READ) is True
    assert system.check_access(user1, file2, Permission.WRITE) is False, \
        "user1 granted READ but can WRITE"
    assert system.check_access(user2, file1, Permission.READ) is False, \
        "user2 has NO capability but can read the confidential file"
    assert system.check_access(user1, file1, Permission.READ) is False

    # Delegation: admin passes READ (a subset) to user1.
    delegated = system.delegate(admin, user1, admin_cap, {Permission.READ})
    assert system.check_access(user1, file1, Permission.READ) is True, \
        "delegation did not confer READ"
    assert system.check_access(user1, file1, Permission.WRITE) is False, \
        "delegating READ leaked WRITE"

    # FORBIDDEN: delegating a non-delegable capability.
    try:
        system.delegate(user1, user2, user1_cap)
        assert False, "non-delegable capability was delegated"
    except ValueError:
        pass

    # FORBIDDEN: delegating permissions the delegator does not hold.
    try:
        system.delegate(admin, user2, admin_cap,
                        {Permission.READ, Permission.EXECUTE})
        assert False, "delegation AMPLIFIED permissions (EXECUTE never granted)"
    except ValueError:
        pass
    assert system.check_access(user2, file1, Permission.READ) is False, \
        "failed delegation still granted access"

    # Attenuation narrows; it must never widen.
    attenuated = system.attenuate(user1, delegated, {Permission.READ})
    assert Permission.READ in attenuated.permissions
    assert len(attenuated.permissions) == 1
    try:
        system.attenuate(user1, attenuated, {Permission.READ, Permission.WRITE})
        assert False, "attenuation WIDENED permissions"
    except ValueError:
        pass

    # Revocation of the root capability cuts the whole delegation chain.
    assert system.check_access(user1, file1, Permission.READ) is True
    system.revoke(admin_cap)
    assert system.check_access(admin, file1, Permission.READ) is False, \
        "revoked capability still grants its holder access"
    assert system.check_access(user1, file1, Permission.READ) is False, \
        "revoking the root left the DELEGATED capability alive"
    # Unrelated capability untouched.
    assert system.check_access(user1, file2, Permission.READ) is True, \
        "revocation of file1's chain damaged file2 access"

    print("capability_access: exact grants, no ambient authority, delegation "
          "subset-only, attenuation narrows, revocation kills the chain — PASS")


if __name__ == "__main__":
    main()