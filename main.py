def check_permissions(user_level):
    """This function contains an unreachable code bug."""
    if user_level == "admin":
        return "Access Granted"
    else:
        return "Access Denied"
        print("This log is unreachable and will be flagged as a bug.") # Lỗi ở đây
