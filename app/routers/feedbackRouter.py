from uuid import UUID
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.data import database
from app.schema.requests.feedbackCreateRequest import FeedbackCreateRequest
from app.services import feedbackService

get_db = database.get_db

router = APIRouter(
    prefix="/feedback",
    tags=['Feedback']
)


@router.post('/', status_code=status.HTTP_200_OK)
def please_share_your_valuable_feedback(request: FeedbackCreateRequest, db: Session = Depends(get_db)):
    return feedbackService.send_feedback(request, db)