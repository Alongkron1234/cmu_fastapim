# from database import Base
# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.dialects.postgresql import UUID
# import uuid
# from sqlalchemy.orm import relationship

# class Profile(Base):
#     __tablename__ = "business_profile"
#     member_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
#     name = Column(String(250), nullable=False)
#     domain_name = Column(String(250), nullable=False)
#     detail = Column(String(250), nullable=False)
#     address = Column(String(250), nullable=False)
#     lat_long = Column(String(250), nullable=False)
#     business_type = Column(String(250), nullable=False)
#     ower_id = Column(String(250), nullable=False)

# class Business(Base):
#     __tablename__ = "business"
#     business_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
#     name = Column(String(250), nullable=False)
#     domain = Column(String(250), nullable=False)
#     business_type = Column(String(250), nullable=False)


# class Member(Base):
#     __tablename__ = "member"

#     business_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
#     member_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)


from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Business(Base):
    __tablename__ = "business"
    business_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String(250), nullable=False)
    domain = Column(String(250), nullable=False)
    business_type = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)

class Member(Base):
    __tablename__ = "member"

    business_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    member_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
