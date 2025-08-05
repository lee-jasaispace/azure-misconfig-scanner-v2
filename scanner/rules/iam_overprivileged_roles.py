def scan_overprivileged_roles(assignments):
    risky_roles = ["Owner", "Contributor"]
    flagged = []

    for a in assignments:
        if a.get("roleDefinitionName") in risky_roles:
            scope = a.get("scope", "")
            principal = a.get("principalName") or a.get("principalId")
            flagged.append({
                "role": a.get("roleDefinitionName"),
                "principal": principal,
                "scope": scope
            })

    return flagged
