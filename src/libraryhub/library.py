def fine_tier(days_overdue):
    if days_overdue < 0:
        raise ValueError("Days overdue cannot be negative")
    elif days_overdue == 0:
        return "None"
    elif 1 <= days_overdue <= 7:
        return "Low"
    elif 8 <= days_overdue <= 14:
        return "Medium"
    elif 15 <= days_overdue <= 30:
        return "High"
    else:
        return "Severe"
