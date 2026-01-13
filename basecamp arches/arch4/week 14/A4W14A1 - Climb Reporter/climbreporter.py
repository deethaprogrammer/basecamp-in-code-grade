from databasemanager import DatabaseManager

def to_minute(HHMM: str) -> int:
    h, m = map(int, HHMM.split(":"))
    return h * 60 + m

def to_HH_MM_Format(Minutes: int) -> str:
    h = Minutes // 60
    m = Minutes % 60
    return f"{h:02}:{m:02}"

class ClimbReporter:
    def __init__(self, db_manager: 'DatabaseManager'):
        self.db_manager = db_manager

    def get_total_climbers(self) -> int:
        row = self.db_manager.fetchone("SELECT COUNT(*) FROM climber")
        return row[0]


    def get_fastest_climb(self, rout_id: int) -> dict:
        rows = self.db_manager.fetchall("""
                                        SELECT c.first_name, c.last_name, cl.start_time, cl.end_time
                                        FROM climb cl
                                        JOIN climber c on c.id = cl.climber_id
                                        WHERE cl.route_id = ?
                                        """, (rout_id,))
        if not rows:
            return {}
        best = None
        best_minutes = None
        for first, last, start, end in rows:
            dur = to_minute(end) - to_minute(start)
            if best_minutes is None or dur < best_minutes:
                best_minutes = dur
                best = f"{first} {last}"
        return {
            "climber": best,
            "duration": to_HH_MM_Format(best_minutes)
        }

    def get_average_duration(self, route_id: int) -> str:
        rows = self.db_manager.fetchall("""
                                        SELECT start_time, end_time
                                        FROM climb
                                        WHERE route_id = ?
                                        """, (route_id,))
        if not rows:
            return "00:00"
        duration = [(to_minute(end) - to_minute(start)) for start, end in rows]
        avg = round(sum(duration) / len(duration))
        return to_HH_MM_Format(avg)

    def get_top_climbers(self, faster_than_minutes: int) -> list:
        rows = self.db_manager.fetchall("""
                                        SELECT c.first_name, c.last_name, cl.start_time, cl.end_time
                                        FROM climb cl
                                        JOIN climber c on c.id = cl.climber_id
                                        """)
        if not rows:
            return []
        
        best = []
        for first, last, start, end in rows:
            dur = to_minute(end) - to_minute(start)
            if dur < faster_than_minutes and f"{first} {last}" not in best:
                best.append(f"{first} {last}")
        return sorted(best)

    def get_climb_summary(self, climb_id) -> dict:
        row = self.db_manager.fetchone("""
                                        SELECT cl.start_time, cl.end_time, c.first_name, c.last_name, r.name, r.id
                                        FROM climb cl
                                        JOIN climber c ON c.id = cl.climber_id
                                        JOIN route r ON r.id = cl.route_id
                                        WHERE cl.id = ?
                                        """, (climb_id,))
        if not row:
            return {}
        start, end, first, last, route_name, route_id = row
        dur = to_minute(end) - to_minute(start)
        avg = to_minute(self.get_average_duration(route_id))
        
        return {
            "climber": f"{first} {last}",
            "route": route_name,
            "duration": to_HH_MM_Format(dur),
            "faster_than_average": dur < avg
        }

    def get_climber_with_most_climbs(self) -> str:
        row = self.db_manager.fetchone("""
                                        SELECT c.first_name, c.last_name, COUNT(*)
                                        FROM climb cl
                                        JOIN climber c ON c.id = cl.climber_id
                                        GROUP BY cl.climber_id
                                        ORDER BY COUNT(*) DESC LIMIT 1
                                        """)
        if not row:
            return ""
        
        first, last, count = row
        return f"{first} {last}"
        
    def get_all_climbs_from_climber(self, climber_id: int) -> list[dict]:
        rows = self.db_manager.fetchall("""
                                        SELECT cl.id, r.name, cl.start_time, cl.end_time
                                        FROM climb cl
                                        JOIN route r ON r.id = cl.route_id
                                        WHERE cl.climber_id = ?
                                        ORDER BY cl.start_time
                                        """, (climber_id,))
        result = []
        for _id, route_name, start, end in rows:
            dur = to_minute(end) - to_minute(start)
            result.append({
                "id": _id,
                "route": route_name,
                "start": start,
                "end": end,
                "duration": to_HH_MM_Format(dur)
            })
        return result
