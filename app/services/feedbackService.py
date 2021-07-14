from sqlalchemy.orm import Session
from app.schema.requests.feedbackCreateRequest import FeedbackCreateRequest
from app.models.feedbackDetails import FeedbackDetails
from . import sendEmailService


def send_feedback(request: FeedbackCreateRequest,db: Session):
    subject = sendEmailService.feedback_email_subject(request.name,request.email)
    body = request.feedback
    sendEmailService.send_email("ssb.bits2016@outlook.com", subject, body)
    feedback = FeedbackDetails(name=request.name,email=request.email,feedback=request.feedback)
    db.add(feedback)
    db.commit()
    db.refresh(feedback)
    return {"detail": "Thank you for sharing your valuable feedback"}