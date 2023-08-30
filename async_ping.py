import asyncio
import platform
import subprocess


async def ping_host(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    process = await asyncio.create_subprocess_exec(
        "ping", param, "3", host,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = await process.communicate()
    return stdout.decode(), stderr.decode()


async def monitor():
    hosts = ["google.com", "example.com", "openai.com"]
    while True:
        tasks = [ping_host(host) for host in hosts]
        result = await asyncio.gather(*tasks)

        for host, (stdout, stderr) in zip(hosts, result):
            print(f'Ping results for {host[1]} with id={host[0]}:\n{stdout}'
                  f'end_res')

asyncio.run(monitor())


async def run_ping(list_with_hosts):
    tasks = [ping_host(host[1]) for host in list_with_hosts]
    result = await asyncio.gather(*tasks)

    for host, (stdout, stderr) in zip(list_with_hosts, result):
        print(f'Ping results for {host[1]} with id={host[0]}:\n{stdout}'
              f'end_res')
