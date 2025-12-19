from datetime import datetime

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
      (self.calendar["start_date"] <= date_int) &
      (self.calendar["end_date"] >= date_int) &
      (self.calendar[day_col] == 1)]["service_id"]

      active_trips = self.trips.merge(active_services, on="service_id")

      return (
        active_trips
        .groupby("route_id")["trip_id"]
        .nunique()
        .reset_index(name="total_trips")
        .merge(self.routes, on="route_id", how="left")
        .sort_values("total_trips", ascending=False))

  # top n routes
  def top_n_routes_by_trips(self, df, n):
    return df.nlargest(n, "total_trips")
