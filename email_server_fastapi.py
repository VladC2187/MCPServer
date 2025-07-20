from fastapi import FastAPI
from pydantic import BaseModel
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="MCP Email Server", version="1.0.0")

class WelcomeRequest(BaseModel):
    name: str
    company: str

class ResetRequest(BaseModel):
    name: str
    reset_link: str

@app.post("/get_welcome_email")
def get_welcome_email(req: WelcomeRequest):
    """Generate a welcome email."""
    return {
        "email": f"""
Hi {req.name},

Welcome to {req.company}! We're thrilled to have you on board.

If you have any questions, feel free to reach out.

Best regards,
The {req.company} Team
"""
    }

@app.post("/get_password_reset_email")
def get_password_reset_email(req: ResetRequest):
    """Generate a password reset email."""
    return {
        "email": f"""
Hi {req.name},

We received a request to reset your password. Please use the following link:

{req.reset_link}

If you didn't request this, please ignore the email.

Best,
Support Team
"""
    }

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting FastAPI Email Server on http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
