from env import PLATFORM_NUMBER, STOP_TIME


if __name__ == "__main__":

    trucks_count = 0
    platforms_busy_time = dict()
    trucks_queues = []
    with open("log.log") as log_file:
        for line in log_file:
            if "plat" in line and "busy for" in line:
                splitted_line = line.split()
                trucks_count += 1
                plat_id = splitted_line[1]
                busy_for = splitted_line[-1]
                if plat_id in platforms_busy_time.keys():
                    platforms_busy_time[plat_id] += float(busy_for)
                else:
                    platforms_busy_time[plat_id] = float(busy_for)
            elif "trucks queue" in line:
                trucks_queues.append(int(line.split()[-1]))

    print(f"avg truck queue: {sum(trucks_queues) / len(trucks_queues)}")

    complete_busy_time = 0.0
    busy_koefs = []
    for platform, platform_busy_for in platforms_busy_time.items():
        complete_busy_time += platform_busy_for
        platform_busy_koef = platform_busy_for / STOP_TIME
        print(f"platform {platform} was busy for: {platform_busy_koef}")
        busy_koefs.append(platform_busy_koef)

    avg_unload_time = complete_busy_time / trucks_count
    print(f"average unload time: {avg_unload_time}")

    avg_busy_koef = sum(busy_koefs) / PLATFORM_NUMBER
    print(f"average busy koef: {avg_busy_koef}")
