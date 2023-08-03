from db.model import InfoAboutStatus, Session
from loger import app_loger
from datetime import datetime


class WorkWithHostStatus:

    @staticmethod
    def create(host_pk: int, status: str) -> None:
        with Session() as session:
            try:
                new_data = InfoAboutStatus(
                    host_id=host_pk,
                    status=status,
                    time_event=datetime.now())
                session.add(new_data)
                session.commit()
            except Exception as e:
                app_loger.critical(f'Невозможно записать в БД статус '
                                   f'{e} '
                                   f'{host_pk}')

    @staticmethod
    def read_all_data() -> list:
        with Session() as session:
            info_hosts = session.query(InfoAboutStatus).all()
            status_info = []
            if info_hosts:
                for info_host in info_hosts:
                    InfoAboutStatus(host_id=info_host.host_id,
                                    status=info_host.status,
                                    time_event=info_host.time_event
                                    )
                    status_info.append(InfoAboutStatus)
            return status_info

    @staticmethod
    def read_info_about_host(host_id: int) -> InfoAboutStatus:
        with Session() as session:
            info_host = session.query(InfoAboutStatus).\
                filter(InfoAboutStatus.host_id == host_id).first()
            if info_host:
                return info_host
