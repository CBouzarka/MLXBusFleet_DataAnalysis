from gtfs_loader import GTFSLoader
from gtfs_validator import GTFSDataValidator
from gtfs_analyzer import GTFSAnalyzer

def main():
  # 1a) load GTFS data
  loader = GTFSLoader(path="/content", zipped=False)
  dfs = loader.load()
  print("GTFS files loaded successfully.")
  
  # 1b) perform data quality checks
  validator = GTFSDataValidator()
  dfs = validator.validate(dfs)
  print("Data quality checks completed (missing values & duplicates handled).")
  print("Report missing values and duplicates")
  missing_summary = validator.missing_values_summary(dfs)
  for name, summary in missing_summary.items():
    print(f"\nMissing values in {name}:")
    print(summary)
  
  # initialize analyzer
  analyzer = GTFSAnalyzer(dfs)
  
  # 2a) calculate total trips per route for a day
  service_date = "2025-12-12"
  trips_per_route = analyzer.trips_per_route_for_day(service_date)
  print("\nTrips per route for", service_date)
  print(trips_per_route.head())
  
  # 2b) find top 3 routes with highest number of trips for a day
  top_3_routes = analyzer.top_n_routes_by_trips(trips_per_route, n=3)
  print("\nTop 3 routes with highest number of trips:")
  print(top_3_routes)
  
  # 3a) find top 5 stops with highest number of arrivals during peak hours
  peak_stops = analyzer.top_stops_during_peak(
      peak_start="07:00:00",
      peak_end="09:00:00",
      top_n=5)
  print("\nTop bus stops during peak hours (07:00–09:00):")
  print(peak_stops)
  
  # 3b) plot histogram of arrivals distribution for a day
  analyzer.plot_arrival_histogram()
  
  # 4a) estimate average trip duration per route
  avg_durations = analyzer.average_duration_per_route()
  print("\nAverage trip duration per route (minutes):")
  print(avg_durations.head())
  
  # 4b) find unusually long / short routes
  unusual_trip_durations = analyzer.detect_unusual_trip_durations(avg_durations)
  print("\nRoutes with unusually long or short trip durations:")
  print(unusual_trip_durations[unusual_trip_durations["unusual_trip_durations"] != "Normal"])
