def read_current_hosts() -> list[int]:
    with open('db/current_hosts.txt', 'r') as current_hosts:
        list_of_hosts_we_work_with = list(map(int, current_hosts.readlines()))
    return list_of_hosts_we_work_with


def write_current_hosts(list_with_id_hosts: list[int]) -> None:
    with open('db/current_hosts.txt', 'w') as current_hosts:
        for id_host in list_with_id_hosts:
            current_hosts.write(str(id_host) + '\n')


if __name__ == "__main__":
    write_current_hosts([i+1 for i in range(5, 15)])
    read_current_hosts()
