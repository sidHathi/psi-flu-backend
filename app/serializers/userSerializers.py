def userEntity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "email": user["email"],
        "role": user["role"],
        "password": user["password"],
        "created_at": user["created_at"],
        "updated_at": user["updated_at"],
        "symptoms": user["symptoms"],
    }


def userResponseEntity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "email": user["email"],
        "role": user["role"],
        "created_at": user["created_at"],
        "updated_at": user["updated_at"],
        "symptoms": user["symptoms"],
    }


def embeddedUserResponse(user) -> dict:
    return {
        "id": str(user["_id"]),
        "email": user["email"],
    }


def userListEntity(users) -> list:
    return [userEntity(user) for user in users]

