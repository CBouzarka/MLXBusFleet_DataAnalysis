class TimeUtils:
  @staticmethod
  def gtfs_time_to_seconds(t:str) -> int:
    h, m, s = map(int, t.split(":"))
    return h * 3600 + m * 60 + s
