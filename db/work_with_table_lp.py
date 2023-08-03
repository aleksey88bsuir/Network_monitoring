from db.model import LostPackets, Session
from loger import app_loger
from datetime import datetime


class WorkWithLostPackets:

    @staticmethod
    def create(host_pk: int, amount_lost_packets: int) -> None:
        with Session() as session:
            try:
                new_data = LostPackets(
                    host_id=host_pk,
                    number_of_packages=amount_lost_packets,
                    time_event=datetime.now())
                session.add(new_data)
                session.commit()
            except Exception as e:
                app_loger.critical(f'Невозможно записать в БД количество '
                                   f'ошибок' f'{e} '
                                   f'{amount_lost_packets}',
                                   f'{type(amount_lost_packets)}')

    @staticmethod
    def read_all_data():
        with Session() as session:
            lp = session.query(LostPackets).all()
            lp_list = []
            if lp:
                for i in lp:
                    LostPackets(host_id=i.host_id,
                                number_of_packages=i.number_of_packages,
                                time_event=i.time_event
                                )
                    lp_list.append(LostPackets)
            return lp_list

    @staticmethod
    def read_info_about_host(host_id: int) -> LostPackets:
        with Session() as session:
            lp = session.query(LostPackets).\
                filter(LostPackets.host_id == host_id).first()
            if lp:
                return lp
