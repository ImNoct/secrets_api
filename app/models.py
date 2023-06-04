from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from .database import Base


class Secret(Base):
    __tablename__ = "secrets"

    key = Column(String, primary_key=True, nullable=False)
    data = Column(String, nullable=False)
    # text = Column(String, nullable=False)
    # expire_at = Column(TIMESTAMP(timezone=True),
                        # nullable=False, server_default=text('now()'))