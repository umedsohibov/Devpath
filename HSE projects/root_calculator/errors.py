def safe_calculate(func):
    try:
        return func()
    except Exception:
        return"Error"