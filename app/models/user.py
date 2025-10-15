from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import BaseModel


class User(BaseModel):
    __tablename__ = "users"
    
    # BASIC REQUIRED FIELDS
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    
    # OPTIONALS FIELDS CONFIG
    phone = Column(String(20), nullable=True)
    country = Column(String(100), nullable=True)
    city = Column(String(100), nullable=True)
    address = Column(Text, nullable=True)
    date_of_birth = Column(DateTime, nullable=True)
    
    # VERIFICATION AND STATUS
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
    
    # VERIFICATION EMAIL FIELDS
    verification_token = Column(String(255), nullable=True, index=True)
    verification_token_expires = Column(DateTime, nullable=True)
    
    # REST PASSWORD FIELDS
    reset_password_token = Column(String(255), nullable=True, index=True)
    reset_password_expires = Column(DateTime, nullable=True)
    
    # RELATIONSHIPS
    refresh_tokens = relationship("RefreshToken", back_populates="user", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<User(id={self.id}, email={self.email})>"


class RefreshToken(BaseModel):
    __tablename__ = "refresh_tokens"
    
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    token = Column(String(512), unique=True, nullable=False, index=True)
    expires_at = Column(DateTime, nullable=False)
    is_revoked = Column(Boolean, default=False)
    
    # RELATIONSHIPS
    user = relationship("User", back_populates="refresh_tokens")
    
    def __repr__(self):
        return f"<RefreshToken(id={self.id}, user_id={self.user_id})>"


class PasswordResetCode(BaseModel):
    __tablename__ = "password_reset_codes"
    
    email = Column(String(255), nullable=False, index=True)
    code = Column(String(6), nullable=False)  # Código de 6 dígitos
    is_used = Column(Boolean, default=False)
    expires_at = Column(DateTime, nullable=False)
    
    def __repr__(self):
        return f"<PasswordResetCode(id={self.id}, email={self.email})>"