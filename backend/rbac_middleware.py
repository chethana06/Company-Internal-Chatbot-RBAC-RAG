from fastapi import HTTPException, status

def enforce_role(user_role: str, allowed_roles: list):
    if user_role not in allowed_roles:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied for your role"
        )
