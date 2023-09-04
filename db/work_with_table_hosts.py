from db.model import Hosts, Session, LostPackets, InfoAboutStatus
from sqlalchemy.exc import IntegrityError
from loger import app_loger, log_exceptions


class WorkWithHosts:

    @staticmethod
    @log_exceptions(logger=app_loger)
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
    @log_exceptions(logger=app_loger)
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
    @log_exceptions(logger=app_loger)
    def read_info_about_host(host_id: int) -> Hosts:
        with Session() as session:
            host = session.query(Hosts).\
                filter((Hosts.host_id == host_id)).first()
            if host:
                return host

    @staticmethod
    @log_exceptions(logger=app_loger)
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
            app_loger.info(f'Успешно обновлена запись в БД {host.name} '
                           f'{host.ip_add}')

    @staticmethod
    @log_exceptions(logger=app_loger)
    def delete_host(host_id: Hosts) -> None:
        with Session() as session:
            host_for_del = session.query(Hosts).\
                    filter(Hosts.host_id == host_id).first()
            if host_for_del:
                session.delete(host_for_del)
                session.commit()
                app_loger.info(f'Успешно удалена запись из БД '
                               f'{host_for_del.name}, '
                               f'{host_for_del.ip_add}')


class WorkWithUnionTables:

    @staticmethod
    @log_exceptions(logger=app_loger)
    def read_info_about_status(host_id: int) -> list:
        with Session() as session:
            info = session.query(
                Hosts.name,
                Hosts.ip_add,
                InfoAboutStatus.status,
                InfoAboutStatus.time_event
            ).join(
                InfoAboutStatus,
                Hosts.host_id == InfoAboutStatus.host_id
            ).filter(
                Hosts.host_id == host_id
            ).all()
        if info:
            return info

    @staticmethod
    @log_exceptions(logger=app_loger)
    def read_info_about_status_with_time(host_id, st_time, fin_time):
        with Session() as session:
            info = session.query(
                Hosts.name,
                Hosts.ip_add,
                InfoAboutStatus.status,
                InfoAboutStatus.time_event
            ).join(
                InfoAboutStatus,
                Hosts.host_id == InfoAboutStatus.host_id
            ).filter(
                Hosts.host_id == host_id,
                InfoAboutStatus.time_event.between(st_time, fin_time)
            ).order_by(InfoAboutStatus.time_event).all()
        if info:
            return info

    @staticmethod
    @log_exceptions(logger=app_loger)
    def read_info_about_lp(host_id: int) -> list:
        with Session() as session:
            info = session.query(
                Hosts.name,
                Hosts.ip_add,
                LostPackets.number_of_packages,
                LostPackets.time_event
            ).join(
                LostPackets,
                Hosts.host_id == LostPackets.host_id
            ).filter(
                Hosts.host_id == host_id
            ).all()
        if info:
            return info

    @staticmethod
    @log_exceptions(logger=app_loger)
    def read_info_about_lp_with_time(host_id, st_time, fin_time):
        with Session() as session:
            info = session.query(
                Hosts.name,
                Hosts.ip_add,
                LostPackets.number_of_packages,
                LostPackets.time_event
            ).join(
                LostPackets,
                Hosts.host_id == LostPackets.host_id
            ).filter(
                Hosts.host_id == host_id,
                LostPackets.time_event.between(st_time, fin_time)
            ).order_by(LostPackets.time_event).all()
        if info:
            return info
