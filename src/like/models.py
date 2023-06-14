
from sqlalchemy import Table, Column, Integer, ForeignKey, MetaData

# from src.auth.models import user
# from src.video.models import video
from auth.models import User
from video.models import video

metadata = MetaData()
like = Table(
    "like",
    metadata,
    Column("video_id", Integer,  ForeignKey(video.c.id), default=1),
    Column("user_id", Integer, ForeignKey(User.id), default=1),
)