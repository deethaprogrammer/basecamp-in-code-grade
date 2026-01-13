from databasemanager import DatabaseManager
from climbreporter import ClimbReporter

if __name__ == "__main__":
    databasemanager: DatabaseManager = DatabaseManager(":memory:")
    databasemanager.restore_from_json("backup.json")

    climb_reporter = ClimbReporter(databasemanager)
    print("Total Climbers:", climb_reporter.get_total_climbers())
    print("Fastest Climb:", climb_reporter.get_fastest_climb(1))
    print("Average Duration:", climb_reporter.get_average_duration(1))
    print("Top Climbers:", climb_reporter.get_top_climbers(30))
    print("Climb Summary:", climb_reporter.get_climb_summary(1))
    print("Climber with Most Climbs:", climb_reporter.get_climber_with_most_climbs())
    print("All Climbs from Climber:", climb_reporter.get_all_climbs_from_climber(1))

    databasemanager.close()
