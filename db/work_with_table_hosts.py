from model import Hosts, Session


class WorkWithHosts:

    @staticmethod
    def create(host_dict: dict) -> None:
        with Session() as session:
            # host = self.read_info_about_host()
            new_data = Hosts(
                ip_add=host_dict.get('ip_add'),
                name=host_dict.get('name'),
                music=host_dict.get('music'),
                descr=host_dict.get('descr'))
            session.add(new_data)
            session.commit()

    @staticmethod
    def read_all_data():
        with Session() as session:
            hosts = session.query(Hosts).all()
            hosts_list = []
            if hosts:
                for host in hosts:
                    Hosts(host_id=host.host_id,
                          ip_add=host.ip_add,
                          name=host.name,
                          music=host.music,
                          descr=host.descr,
                          )
                    hosts_list.append(host)
            return hosts_list

    @staticmethod
    def read_info_about_host(host_id: int) -> Hosts:
        with Session() as session:
            host = session.query(Hosts).\
                filter_by(Hosts.host_id == host_id).first()
            if host:
                Hosts(host_id=host.host_id,
                      ip_add=host.ip_add,
                      name=host.name,
                      music=host.music,
                      descr=host.descr,
                      )
                return host

    @staticmethod
    def update_host(host: Hosts) -> None:
        with Session() as session:
            session.query(Hosts).\
                    filter(Hosts.host_id == host.host_id).update(
                    dict(host_id=host.host_id,
                         ip_add=host.ip_add,
                         name=host.name,
                         music=host.music,
                         descr=host.descr,
                         ))
            session.commit()

    @staticmethod
    def delete_host(host: Hosts) -> None:
        with Session() as session:
            host_for_del = session.query(Hosts).\
                    filter(Hosts.host_id == host.host_id).first()
            if host_for_del:
                session.delete(host_for_del)
                session.commit()
