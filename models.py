from sqlalchemy import (Column, ForeignKey, Integer,
                        String)
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()
class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    entity = Column(String)
    entity_id = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="notification")