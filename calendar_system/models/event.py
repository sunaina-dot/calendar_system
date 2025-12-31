from models.db import get_db_connection



def add_event(user_id, title, start, end, category, color):
    conn = get_db_connection()
    conn.execute(
        """
        INSERT INTO events (user_id, title, start, end, category, color)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (user_id, title, start, end, category, color)
    )
    conn.commit()
    conn.close()



def get_all_events(user_id):
    conn = get_db_connection()
    events = conn.execute(
        "SELECT * FROM events WHERE user_id = ?",
        (user_id,)
    ).fetchall()
    conn.close()

    return [
        {
            "id": e["id"],
            "title": e["title"],
            "start": e["start"],
            "end": e["end"],
            "color": e["color"]
        }
        for e in events
    ]



def update_event_time(event_id, start, end):
    conn = get_db_connection()
    conn.execute(
        "UPDATE events SET start = ?, end = ? WHERE id = ?",
        (start, end, event_id)
    )
    conn.commit()
    conn.close()
