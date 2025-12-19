from gtfs_loader import GTFSLoader
from gtfs_validator import GTFSDataValidator
from gtfs_analyzer import GTFSAnalyzer
def main():
  # 1) Load GTFS data
  loader = GTFSLoader(path="/content", zipped=False)
  dfs = loader.load()
  print("GTFS files loaded successfully.")
  
  # 2) Data quality checks
  validator = GTFSDataValidator()
  dfs = validator.validate(dfs)
  print("Data quality checks completed (missing values & duplicates handled).")
  missing_summary = validator.missing_values_summary(dfs)
  for name, summary in missing_summary.items():
    print(f"\nMissing values in {name}:")
    print(summary)

  duplicate_summary = validator.duplicates_summary(dfs)
  for name, count in duplicate_summary.items():  
    print(f"{name} duplicate rows: {count}
  
  # Analyzer Initialization
  analyzer = GTFSAnalyzer(dfs)
  
  # 3a) Trips per route for a day
  service_date = "2025-12-12"
  trips_per_route = analyzer.trips_per_route_for_day(service_date)
  print("\nTrips per route for", service_date)
  print(trips_per_route.head())
  
  # 3b) Top 3 routes with highest number of trips for a day
  top_3_routes = analyzer.top_n_routes_by_trips(trips_per_route, n=3)
  print("\nTop 3 routes with highest number of trips:")
  print(top_3_routes)
  
  # 3c) Top 5 stops with highest number of arrivals during peak hours
  peak_stops = analyzer.top_stops_during_peak(
      peak_start="07:00:00",
      peak_end="09:00:00",
      top_n=10)
  print("\nTop bus stops during peak hours (07:00–09:00):")
  print(peak_stops)
  
  # 3d) Histogram of arrivals distribution for a day
  analyzer.plot_arrival_histogram()
  
  # 4a) Average trip duration per route
  avg_durations = analyzer.average_duration_per_route()
  print("\nAverage trip duration per route (minutes):")
  print(avg_durations.head())
  
  # 4b) Unusually long / short routes
  unusual_trip_durations = analyzer.detect_duration_outliers(avg_durations)
  print("\nRoutes with unusually long or short trip durations:")
  print(unusual_trip_durations[unusual_trip_durations["unusual_trip_durations"] != "Normal"])
