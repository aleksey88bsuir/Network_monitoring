from sqlalchemy import create_engine, Column, ForeignKey, Integer, String,\
    DateTime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine('sqlite:///db/remote_hosts.db', echo=True)
# engine = create_engine('sqlite:///remote_hosts.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()


class Hosts(Base):
    __tablename__ = "hosts"

    host_id = Column(Integer, primary_key=True)
    ip_add = Column(String, unique=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    music = Column(String, default='None')
    descr = Column(String)

    statuses = relationship("InfoAboutStatus", cascade="all, delete-orphan",
                            backref="host")
    lost_packets = relationship("LostPackets", cascade="all, delete-orphan",
                                backref="host")

    def __repr__(self):
        return f'{self.host_id} {self.name} {self.ip_add} \n' \
               f'{self.music=} {self.descr=}'


class InfoAboutStatus(Base):
    __tablename__ = "info_about_status"

    status_id = Column(Integer, primary_key=True)
    host_id = Column(Integer, ForeignKey('hosts.host_id'))
    status = Column(String)
    time_event = Column(DateTime)


class LostPackets(Base):
    __tablename__ = "info_about_lost_packets"

    lost_id = Column(Integer, primary_key=True)
    host_id = Column(Integer, ForeignKey('hosts.host_id'))
    number_of_packages = Column(Integer)
    time_event = Column(DateTime)


Base.metadata.create_all(engine)
