from datetime import datetime
from TimeUtils import TimeUtils

class GTFSAnalyzer:
  def __init__(self, dfs):
    self.routes = dfs["routes"]
    self.trips = dfs["trips"]
    self.stops = dfs["stops"]
    self.stop_times = dfs["stop_times"]
    self.calendar = dfs["calendar_dates"]
    self.shapes = dfs["shapes"]
    self.transfers = dfs["transfers"]
    self.feed_info = dfs["feed_info"]
    self.fare_rules = dfs["fare_rules"]
    self.fare_attributes = dfs["fare_attributes"]
    self.agency = dfs["agency"]

  def trips_per_route_for_day(self, date_str):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    day_col = date.strftime("%A").lower()
    date_int = int(date.strftime("%Y%m%d"))
  
    active_services = self.calendar[
      (self.calendar["date"] == date_int)["service_id"]

      active_trips = self.trips.merge(active_services, on="service_id")

    return (
      active_trips
      .groupby("route_id")["trip_id"]
      .nunique()
      .reset_index(name="total_trips")
      .merge(self.routes, on="route_id", how="left")
      .sort_values("total_trips", ascending=False))

  # find top n routes
  def top_n_routes_by_trips(self, df, n):
    return df.nlargest(n, "total_trips")

  # find peak hours stops
  def top_stops_during_peak(self, peak_start, peak_end, top_n):
    start_sec = TimeUtils.gtfs_time_to_seconds(peak_start)
    end_sec = TimeUtils.gtfs_time_to_seconds(peak_end)

    self.stop_times["arrival_secs"] = self.stop_times["arrival_time"].apply(TimeUtils.gtfs_time_to_seconds)

    peak = self.stop_times[
      (self.stop_times["arrival_secs"] >= start_sec) &
      (self.stop_times["arrival_secs"] <= end_sec)]

    return (
      peak.groupby("stop_id")
      .size()
      .reset_index(name="arrival_count")
      .merge(self.stops, on="stop_id", how="left")
      .sort_values("arrival_count", ascending=False)
      .head(top_n))
