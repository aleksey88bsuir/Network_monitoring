from db.model import Hosts, Session
from sqlalchemy.exc import IntegrityError
from loger import app_loger


class WorkWithHosts:

    @staticmethod
    def create(host_dict: dict) -> None:
        with Session() as session:
            try:
                new_data = Hosts(
                    ip_add=host_dict.get('ip_add'),
                    name=host_dict.get('name'),
                    music=host_dict.get('music'),
                    descr=host_dict.get('descr'))
                session.add(new_data)
                session.commit()
                app_loger.info(f'Успешно произведена запись в БД '
                               f'{host_dict.get("name")}, '
                               f'{host_dict.get("ip_add")}')
            except IntegrityError:
                app_loger.error(f'Невозможно записать в БД '
                                f'{host_dict.get("name")} c IP-адресом'
                                f'{host_dict.get("ip_add")}')

    @staticmethod
    def read_all_data() -> list:
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
                filter((Hosts.host_id == host_id)).first()
            if host:
                return host

    @staticmethod
    def update_host(host: Hosts) -> None:
        with Session() as session:
            session.query(Hosts).\
                    filter(Hosts.host_id == host.host_id).update(
                    dict(ip_add=host.ip_add,
                         name=host.name,
                         music=host.music,
                         descr=host.descr,
                         ))
            session.commit()
            app_loger.info(f'Успешно обновлена запись в БД '
               f'{host.name}, '
               f'{host.ip_add}')

    @staticmethod
    def delete_host(host: Hosts) -> None:
        with Session() as session:
            host_for_del = session.query(Hosts).\
                    filter(Hosts.host_id == host.host_id).first()
            if host_for_del:
                session.delete(host_for_del)
                session.commit()
                app_loger.info(f'Успешно удалена запись из БД '
                               f'{host_for_del.name}, '
                               f'{host_for_del.ip_add}')
